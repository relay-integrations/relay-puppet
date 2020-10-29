#!/usr/bin/env python

import logging
import time
from urllib.parse import urljoin

import requests
from relay_sdk import Interface, Dynamic as D

relay = Interface()

relay_api_url = relay.get(D.connection.relayAPIURL)
relay_api_token = relay.get(D.connection.token)

run_id = relay.get(D.id)

headers = {'Authorization': f'Bearer {relay_api_url}'}

while True:
    r = requests.get(urljoin(relay_api_url, f'_puppet/runs/{run_id}'), headers=headers)
    r.raise_for_status()

    run = r.json
    if run['status'] != 'complete':
        # XXX: FIXME: We need to take into account next_update_before to handle
        # this properly.
        logging.info('Run is not yet complete (currently {}), waiting...'.format(run['status']))

        time.sleep(5)
        continue

    if run.get('job_id'):
        relay.outputs.set('jobID', run['job_id'])

    if run.get('outcome'):
        relay.outputs.set('outcome', run['outcome'])

    logging.info('Run complete with outcome {}'.format(run.get('outcome', '(unknown)')))

    break
