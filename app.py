from requests.exceptions import RequestException
from consts import CONFIG_PATH
import requests
import json
import sys


def retrieve_url():
    try:
        with open(CONFIG_PATH, "r") as file:
            url = json.load(file)["url"]
            return url
    except OSError:
        print("Could not read file: " + CONFIG_PATH)
        sys.exit()
    except KeyError:
        print("Key url not found within the json file")
        sys.exit()


def insert_response(url, parsed_content):
    data = {"url": url, "content": parsed_content}
    try:
        with open(CONFIG_PATH, "w") as file:
            file.write(json.dumps(data, indent=4))
    except OSError:
        print("Could not write to file: " + CONFIG_PATH)
        sys.exit()


def main():
    url = retrieve_url()
    try:
        parsed_content = requests.get(url).content[:15]
    except RequestException:
        print("Failed retrieving response from url: " + str(url))
        sys.exit()

    insert_response(url, str(parsed_content))


if __name__ == '__main__':
    main()
