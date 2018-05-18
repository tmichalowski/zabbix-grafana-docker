#!/usr/bin/python
import requests
import os
import simplejson as json
#[ provide credential variables etc ]

grafana_host='192.168.74.146'
grafana_port='3000'


#grafana_url = os.path.join('http://', '%s:%u' % (grafana_host, grafana_port))
grafana_url = 'http://127.0.0.1:3000/api'
session = requests.Session()
login_post = session.post(
   os.path.join(grafana_url, 'login'),
   data=json.dumps({
      'user': 'admin',
      'email': '',
      'password': 'admin' }),
   headers={'content-type': 'application/json'})

# Get list of datasources
datasources_get = session.get(os.path.join(grafana_url, 'api', 'datasources'))
datasources = datasources_get.json()

# Add new datasource
datasources_put = session.put(
   os.path.join(grafana_url, 'api', 'datasources'),
   data=json.dumps({
      'access': 'direct',
      'name': 'Zabbix',
      'password': 'zabbix',
      'type': 'Zabbix',
      'url': 'http://zabbix-web-nginx-pgsql/api_jsonrpc.php',
      'user': 'Admin'}),
      headers={'content-type': 'application/json'})
