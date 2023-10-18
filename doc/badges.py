from pathlib import Path 
import xml.etree.ElementTree as ET
import json
import requests

current_dir = Path(__file__).parent.resolve()


def count_unfinished_strings(xml_file: Path):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Count the instances of <translation> elements with type="unfinished"
    count = sum(1 for element in root.iter("translation") if element.get("type") == "unfinished")

    return count


def count_all_strings(xml_file: Path):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Count the instances of <translation> elements 
    count = sum(1 for element in root.iter("translation"))

    return count


def generate_badge(name: Path, numerator: int, denominator: int) -> str:
    # Extract the countrycode from the name
    filename = name.stem  # Get the filename without the extension
    parts = filename.split('_')
    if len(parts) >= 2:
        countrycode = parts[1]
    else:
        raise ValueError("Invalid filename format")
    
    translated = numerator/denominator
    colour = 'red'
    
    if translated == 1.0:
        colour = 'green'
    elif translated >= 0.80:
        colour = 'yellow'

    # Construct the badge URL
    badge_url = f"https://img.shields.io/badge/{countrycode}-{numerator}/{denominator}-{colour}"
    return countrycode, badge_url


def process_files(directory: Path) -> dict:
    # Use glob to find all XML files in the directory
    ts_files = list(directory.glob("*.ts"))

    urls = {}

    for file in ts_files:
        den = count_all_strings(file)
        num = den - count_unfinished_strings(file)
        country, url = generate_badge(file, num, den)
        urls[country] = url

    return urls


def write_to_json(path: Path, data: dict):

    # Write file
    with open(path, 'w') as file:
        file.write(json.dumps(data))


def create_website_dir(path: Path):
    directory = path
    directory.mkdir(parents=True, exist_ok=True)


def download_image(url: str, destination: Path):
    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Open the file for binary writing
        with open(destination, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Image downloaded and saved to {destination}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    ts_dir = current_dir.parent
    url_dict = process_files(ts_dir)
    website_dir = current_dir.parent / 'docs'

    create_website_dir(website_dir)

    for country, url in url_dict.items():
        download_image(url, website_dir / f'{country}.svg')

    # write_to_json(website_dir / 'badges.json', url_list)

