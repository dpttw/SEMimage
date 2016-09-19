#! /usr/bin/env python
import requests
import json

def upload(name,host,user,pswd,cert=None):
    url = host + "/rest/blob"
    files = {'blob':open(name, 'rb')}
    r = requests.post(url, files=files, auth=(user, pswd), verify=cert)
    if int(r.status_code)==201:
        response = r.json()
        return url+"?id="+response['handle'].split('id=')[1]
    else:
        return r.json()