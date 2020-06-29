import json
import jsonpath
import requests


def test_add_students():
    url = "http://thetestingworldapi.com/api/Students/171"

    reponse = requests.get(url)

    print(reponse.text)