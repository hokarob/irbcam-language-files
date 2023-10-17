from pathlib import Path 
import xml.etree.ElementTree as ET
import json

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


def process_files(directory: Path):
    # Use glob to find all XML files in the directory
    ts_files = list(directory.glob("*.ts"))

    urls = {}

    for file in ts_files:
        num = count_unfinished_strings(file)
        den = count_all_strings(file)
        country, url = generate_badge(file, num, den)
        urls[country] = url

    return urls


def write_to_json(path: Path, data: dict):

    # Create dir
    directory = path.parent
    directory.mkdir(parents=True, exist_ok=True)

    # Write file
    with open(path, 'w') as file:
        file.write(json.dumps(data))



if __name__ == '__main__':
    ts_dir = current_dir.parent
    url_list = process_files(ts_dir)

    write_to_json(current_dir.parent / 'public/badges.json', url_list)

