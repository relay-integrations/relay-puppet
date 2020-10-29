#!/usr/bin/env python

import logging
import time
from urllib.parse import urljoin

import requests
from relay_sdk import Interface, Dynamic as D

relay = Interface()

relay_api_url = relay.get(D.connection.relayAPIURL)
relay_api_token = relay.get(D.connection.token)

data = {
    'environment': relay.get(D.environment),
    'scope': relay.get(D.scope),
    'noop': relay.get(D.noop),
    'debug': relay.get(D.debug),
    'trace': relay.get(D.trace),
    'evaltrace': relay.get(D.evaltrace),
}

headers = {'Authorization': f'Bearer {relay_api_url}'}

r = requests.post(
    urljoin(relay_api_url, '_puppet/runs'),
    json=data,
    headers=headers,
)
r.raise_for_status()

run = r.json

relay.outputs.set('id', run['id'])

logging.info('Waiting for Puppet run {} to start...'.format(run['id']))

while run['status'] == 'pending':
    time.sleep(5)

    r = requests.get(urljoin(relay_api_url, '_puppet/runs/{}'.format(run['id'])), headers=headers)
    r.raise_for_status()

    run = r.json

logging.info('Run dispatched to Puppet server successfully!')

if run.get('job_id'):
    relay.outputs.set('jobID', run['job_id'])

    logging.info('The Puppet Enterprise console may have more information for the job: {}'.format(run['job_id']))
