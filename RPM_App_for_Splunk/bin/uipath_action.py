#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib import request
from wsgiref import validate
import requests
import sys
import os
import json
import logging
import logging.handlers

#the below logging configuration is used for script debugging API calls made to UiPath
def setup_logger(level):
    logger = logging.getLogger('uipath_action_logger')
    logger.propagate = False
    logger.setLevel(level)
    file_handler = logging.handlers.RotatingFileHandler(os.environ['SPLUNK_HOME'] + '/var/log/splunk/uipath_action.log', maxBytes=2500000000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


logger = setup_logger(logging.INFO)

def get_access_token(client_id, user_key, tenant_name):
    request_url = 'https://account.uipath.com/oauth/token'
    data = {'grant_type': 'refresh_token', 'client_id': client_id,
            'refresh_token': user_key}
    headers = {'Content-Type': 'application/json',
               'X-UIPATH-TenantName': tenant_name}
    logger.warning("batman " + str(data))
    response = requests.post(url=request_url, headers=headers,
                             data=json.dumps(data))
    data = response.json()
    code = response.status_code
    logger.warning("batman2 " + str(code) + " " + str(data))
    access_token = data['access_token']
    return access_token


def start_job(access_token, tenant_name, auth, release_key):
    request_url2 = 'https://cloud.uipath.com/splunzabrpaa/DefaultTenant/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs'
    data = {"startInfo": {"ReleaseKey": release_key, "Strategy": "All",
        "RobotIds": [], "NoOfRobots": 0}}
    headers2 = {'Content-Type': 'application/json', 'X-UIPATH-TenantName': tenant_name, 'Authorization': auth}
    logger.warning("catwomen " + str(headers2) + str(data))
    response = requests.post(url=request_url2, headers=headers2, data=data)
    data = response.json()
    code = response.status_code
    logger.warning("catwomen2 " + str(code) + " " + str(data))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--execute':
        payload = json.loads(sys.stdin.read())
        logger.info(payload)
        config = payload.get('configuration')
        tenant_name = config.get('tenant_name')
        client_id = config.get('client_id')
        user_key = config.get('user_key')
        event_result = payload.get('result')
        release_key = event_result.get('StartInfo.ReleaseKey') 
        access_token = get_access_token(client_id, user_key, tenant_name)
        auth = 'Bearer ' + access_token
        job = start_job(access_token, tenant_name, auth, release_key)


if __name__ == '__main__':
    main()

