import inspect
import os

import requests

from utils.file import read_file_content

BASE_URL = "https://adventofcode.com"
YEAR = 2022


def check_for_input_file():
    path = os.path.dirname(inspect.stack()[1].filename)
    sep = os.sep
    if not os.path.exists(path + sep + "inputs" + sep + "input") and os.path.exists(".." + sep + "session"):
        print(" --- Downloading input file --- ")
        day = path.split(sep)[-1]
        day = int(day[3:])

        url = BASE_URL + "/" + str(YEAR) + "/day/" + str(day) + "/input"
        headers = {'User-Agent': 'https://github.com/Aeilko/Advent-of-Code-' + str(YEAR)}
        cookies = {"session": read_file_content(".." + sep + "session")}

        response = requests.get(url, headers=headers, cookies=cookies)
        if not response:
            print("Error on request, status code " + str(response.status_code))
        else:
            file = open("inputs/input", "wb")
            file.write(response.content)
            file.close()
            print("Input downloaded successfully")
        print()
