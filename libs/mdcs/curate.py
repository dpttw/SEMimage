#! /usr/bin/env python
import requests
import json
from templates import current_id

def curate(file_name,file_title,template_id,host,user,pswd,cert=None,content=None):
    if content is None:
        with open(file_name, 'r') as f: 
            content = f.read()
    data=dict()
    data['content']=[content]
    data['schema']=[template_id]
    data['title']=[file_title]
    
    url = host +  "/rest/curate"
    r = requests.post(url, data=data, auth=(user, pswd), verify=cert)
    if int(r.status_code)==201:
        return "created"  #int(r.status_code)
    else:
        return r.json()

def curate_as(file_name,file_title,host,user,pswd,cert=None,filename=None,template_title=None,content=None):
    template_id = current_id(host,user,pswd,cert=cert,filename=filename,title=template_title)
    return curate(file_name,file_title,template_id,host,user,pswd,cert=cert,content=content)
