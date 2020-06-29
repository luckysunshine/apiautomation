import json
import jsonpath
import requests


def test_add_students():

    token_url = "http://thetestingworldapi.com/Token"
    data = {"grant_type": "password", "username": "admin", "password": "adminpass"}
    token_res = requests.post(token_url, data)
    token_value = jsonpath.jsonpath(token_res.json(), 'access_token')
    auth = {"authorization": 'Bearer ' + token_value[0]}
    url = "http://thetestingworldapi.com/api/Students/171"

    reponse = requests.get(url, headers=auth)

    print(reponse.text)