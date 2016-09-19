import json
import requests
import mdcs 

def dxmls(SURL,USER,PSWD,schtitle):

        url = SURL + "/rest/templates/select/all"
        allSchemas = json.loads(requests.get(url, auth=(USER, PSWD)).text)

        schemaId = []
        for i in range(len(allSchemas)):
                if allSchemas[i]['title'] == schtitle:  
                        schemaId.append(str(allSchemas[i]['id']))

        url = SURL + "/rest/explore/query-by-example"
        
        query = {"schema":schemaId[0]}
        req_data = {"query":json.dumps(query)}
        print req_data,type(req_data)
        qres = json.loads(requests.post(url,req_data,auth=(USER, PSWD)).text)
        print len(qres)

        for i in range(len(qres)):
                file_id = qres[i]['_id']
                print mdcs.explore.delete(file_id,SURL,USER,PSWD,'cert')
        

        return None
