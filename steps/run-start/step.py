#!/usr/bin/env python

import logging
import time
from urllib.parse import urljoin

import requests
from relay_sdk import Interface, Dynamic as D

relay = Interface()

relay_api_url = relay.get(D.connection.relayAPIURL)
relay_api_token = relay.get(D.connection.token)

def get_or_default(path, default=None):
    try:
        return relay.get(path)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 422:
            return default
        raise

data = {
    'environment': relay.get(D.environment),
    'scope': relay.get(D.scope),
    'noop': get_or_default(D.noop, False),
    'debug': get_or_default(D.debug, False),
    'trace': get_or_default(D.trace, False),
    'evaltrace': get_or_default(D.evaltrace, False),
}

headers = {'Authorization': f'Bearer {relay_api_token}'}

r = requests.post(
    urljoin(relay_api_url, '_puppet/runs'),
    json=data,
    headers=headers,
)
r.raise_for_status()

run = r.json()

relay.outputs.set('id', run['id'])

logging.info('Waiting for Puppet run {} to start...'.format(run['id']))

while run['state']['status'] == 'pending':
    time.sleep(5)

    r = requests.get(urljoin(relay_api_url, '_puppet/runs/{}'.format(run['id'])), headers=headers)
    r.raise_for_status()

    run = r.json()

logging.info('Run dispatched to Puppet server successfully!')

if run['state'].get('job_id'):
    relay.outputs.set('jobID', run['state']['job_id'])

    logging.info('The Puppet Enterprise console may have more information for the job: {}'.format(run['state']['job_id']))
