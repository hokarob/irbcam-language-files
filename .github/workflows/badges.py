from pathlib import Path 
from xml.etree import ElementTree
from typing import Tuple

import requests

current_dir = Path(__file__).parent.resolve()


def count_strings(xml_file: Path) -> Tuple[int, int]:
    """Find number of translation strings and how many are missing a translation

    :param: xml_file: Path to XML file (.ts file)
    :return: Total number of strings and unfinished strings
    """

    tree = ElementTree.parse(xml_file)
    root = tree.getroot()
    
    # Strings with type "unfinished". These are not translated
    unfinished = 0
    
    # Vanished strings are no longer used in IRBCAM. The string has been removed from the source code
    vanished = 0
    
    # Obsolete is assigned when the translation of the deleted message had been validated.
    obsolete = 0

    # Total number of strings
    strings = 0

    # Strings with empty source. e.g. tr(""). These are disregarded
    nosource = 0

    # Find all messages
    for context in root.iter('context'):
        # Find name of context (QML or cpp file)
        context_name = context.find('name').text
        # print(f'Looking for strings in {context_name}')

        # Loop through messages
        for message in context.iter('message'):
            # Verify that the message has a source
            source = message.find('source')
            if source is None:
                raise ValueError
            if source.text is None:
                nosource += 1
                continue


            # Attempt to extract translation value
            translation = message.find('translation')
            if translation is None:
                raise ValueError(f'Did not find translation tag for message: "{source.text}"')
            
            # Skip if the message has vanished
            if translation.get('type') == 'vanished':
                vanished += 1
                continue

            # Skip if the message is obsolete
            if translation.get('type') == 'obsolete':
                obsolete += 1
                continue


            # Increment number of strings
            strings += 1

            # Count if the message is unfinished
            if translation.get('type') == 'unfinished':
                # print(f'Unfinished string in {context_name}. Source text: "{source.text}"')
                location = message.find('location')
                if location is None:
                    continue
                unfinished += 1
                continue

    # print(f'Total: {strings}\nUnfinished: {unfinished}\nVanished: {vanished}\nObsolete: {obsolete}')

    return strings, unfinished


def generate_badge(name: Path, numerator: int, denominator: int) -> Tuple[str, str]:
    """Generate url to badge in SVG format

    :param name: Path to .ts-file
    :param numerator: Numerator in fraction
    :param denominator: Denominator in fraction
    :return: Country code and URL to shields.io
    """
    # Extract the countrycode from the name
    filename = name.stem  # Get the filename without the extension
    parts = filename.split('_')
    if len(parts) >= 2:
        countrycode = parts[1]
    else:
        raise ValueError("Invalid filename format")
    
    translated_ratio = numerator / denominator
    
    # Set badge colour
    if numerator == denominator:
        colour = 'green'
    elif translated_ratio >= 0.80:
        colour = 'yellow'
    else:
        colour = 'red'

    # Construct the badge URL
    badge_url = f"https://img.shields.io/badge/{countrycode}-{numerator}/{denominator}-{colour}"
    return countrycode, badge_url


def process_files(directory: Path) -> dict:
    """Process .ts (XML format) files.

    :param directory: Directory with .ts files
    :return: dictionary where each key is a country code, and it's respective value is URL to the badge
    """
    # Use glob to find all XML files in the directory
    ts_files = list(directory.glob("*.ts"))

    urls = {}

    for file in ts_files:
        den, unfinished = count_strings(file)
        # num = count_unfinished_strings(file)
        num = den - unfinished
        country, url = generate_badge(file, num, den)
        urls[country] = url

    return urls


def create_website_dir(path: Path) -> None:
    """Create a directory

    :param path: Path to create a directory at
    """
    directory = path
    directory.mkdir(parents=True, exist_ok=True)


def download_image(url: str, destination: Path) -> None:
    """Download SVG file

    :param url: URL to download from
    :param destination: Destination to store image at
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Open the file for binary writing
        with open(destination, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Badge downloaded and saved to {destination}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    # Set directories
    ts_dir = current_dir.parent.parent
    website_dir = current_dir.parent.parent / 'docs'
    
    # Create directory for GitHub pages
    create_website_dir(website_dir)
    
    # Generate URL to badges
    url_dict = process_files(ts_dir)

    # Download badges
    for country, url in url_dict.items():
        download_image(url, website_dir / f'{country}.svg')
