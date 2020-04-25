#!/usr/bin/env python3

import requests
import json


def request_code(token):
    payload = {'token': token}
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data'
    r = requests.get(url, params=payload)
    
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        print('GET BODY:', r.json())
        exit()

    data = r.json()
    with open('answer.json', 'w') as f:
        json.dump(data, f)

    return {'text': data['cifrado'], 'rotations': data['numero_casas']}
    
    
def update_answer(decoded, cryptographic_summary):
    jsonFile = open('answer.json', 'r')
    data = json.load(jsonFile)
    jsonFile.close()

    data['decifrado'] = decoded
    data['resumo_criptografico'] = cryptographic_summary

    jsonFile = open('answer.json', 'w+')
    jsonFile.write(json.dumps(data))
    jsonFile.close


def post_answer(token):
    payload = {'token': token}
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution'
    answer = {'answer': open('answer.json', 'rb')}
    r = requests.post(url, params=payload, files=answer)

    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        print('POST BODY:', r.json())
        exit()

    print('OK: ', r.json())