#! /usr/bin/env python
import requests
import json

def add(filename,title,host,user,pswd,cert=None,version=None,dependencies=None):
    url = host + "/rest/templates/add"
    
    with open(filename, 'r') as f: 
        xsd_data = f.read()
    
    data=dict()
    data['content'] = [xsd_data]
    data['filename'] = [filename]
    data['title'] = [title]
    if version: data['templateVersion'] = [version]
    if dependencies: data['dependencies[]'] = dependencies
    
    r = requests.post(url, data=data, auth=(user, pswd), verify=cert)
    
    if int(r.status_code)==201:
        return int(r.status_code)
    else:
        return r.json()

# API method appears to be broken
def select(host,user,pswd,cert=None,ID=None,filename=None,title=None,version=None,templateVersion=None,Hash=None):
    url = host + "/rest/templates/select"
    params = dict()
    if ID: params['id']=ID
    if filename: params['filename']=filename
    if title: params['title']=title
    if version: params['version']=version
    if templateVersion: params['templateVersion']=templateVersion
    if Hash: params['hash']=Hash
    r = requests.get(url, params=params, auth=(user, pswd), verify=cert)
    return r.json()

def delete(ID,host,user,pswd,cert=None,next=None):
    url = host + "/rest/templates/delete"
    params = dict()
    params['id']=ID
    if next: params['next']=next
    r = requests.delete(url, params=params, auth=(user, pswd), verify=cert)
    if int(r.status_code)==204:
        return "Successful deletion of: "+ID
    else:
        return r.json()

def restore(ID,host,user,pswd,cert=None):
    url = host + "/rest/templates/restore"
    params = dict()
    params['id']=ID
    r = requests.get(url, params=params, auth=(user, pswd), verify=cert)
    return r.json()

def select_all(host,user,pswd,cert=None):
    url = host + "/rest/templates/select/all"
    r = requests.get(url, auth=(user, pswd), verify=cert)
    return r.json()

def versions_select_all(host,user,pswd,cert=None):
    url = host + "/rest/templates/versions/select/all"
    r = requests.get(url, auth=(user, pswd), verify=cert)
    return r.json()

def current_id(host,user,pswd,cert=None,filename=None,title=None):
    templates = select_all(host,user,pswd,cert)
    versions = versions_select_all(host,user,pswd,cert)
    
    name_matches = list()
    for t in templates:
        if title == t['title']: name_matches.append(t['id'])
        if title == t['filename']: name_matches.append(t['id'])
        
    current_versions = list()
    for v in versions:
        current_versions.append(v['current'])
    
    current_list = list(set(name_matches).intersection(current_versions))
    if len(current_list) == 1:
        return current_list[0]
    else:
        print "Error: Multiple current templates found by that name!"

def select_current(host,user,pswd,cert=None):
    templates = select_all(host,user,pswd,cert)
    versions = versions_select_all(host,user,pswd,cert)
    
    name_matches = list()
    for t in templates:
        name_matches.append(t['id'])
        
    current_versions = list()
    for v in versions:
        current_versions.append(v['current'])
        
    current_list = list(set(name_matches).intersection(current_versions))
    
    current_templates = list()
    for t in templates:
        if t['id'] in current_list:
            current_templates.append(t)
    
    return current_templates