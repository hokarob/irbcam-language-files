from pathlib import Path 
import xml.etree.ElementTree as ET
import requests

current_dir = Path(__file__).parent.resolve()


def count_unfinished_strings(xml_file: Path) -> int:
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Count the instances of <translation> elements with type="unfinished"
    count = sum(1 for element in root.iter("translation") if element.get("type") == "unfinished")

    return count


def count_all_strings(xml_file: Path) -> int:
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    count = 0
    # Count the instances of <translation> elements 
    # count = sum(1 for element in root.iter("translation") if element.get("type") != "vanished")
    for element in root.iter("translation"):
        # Check if the "type" attribute exists and is not "vanished"
        if "type" not in element.attrib:
            count += 1
        elif element.attrib["type"] == "unfinished":
            count += 1
        elif element.attrib["type"] == "vanished" or element.attrib["type"] == "obsolete":
            print('Skippng vanished or obsolete string')
        else:
            raise ValueError(element)

    return count


def generate_badge(name: Path, numerator: int, denominator: int) -> str:
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
    # Use glob to find all XML files in the directory
    ts_files = list(directory.glob("*.ts"))

    urls = {}

    for file in ts_files:
        den = count_all_strings(file)
        # num = count_unfinished_strings(file)
        num = den - count_unfinished_strings(file)
        country, url = generate_badge(file, num, den)
        urls[country] = url

    return urls


def create_website_dir(path: Path) -> None:
    directory = path
    directory.mkdir(parents=True, exist_ok=True)


def download_image(url: str, destination: Path) -> None:
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
