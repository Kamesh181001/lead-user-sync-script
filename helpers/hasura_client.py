import os
import requests

# Staging
HASURA_GRAPHQL_ENDPOINT = 'https://hasura-staging.lidolearning.com/v1/graphql'
HASURA_ADMIN_SECRET = 'lidolearning-test'

# Prod
# HASURA_GRAPHQL_ENDPOINT = 'https://hasuraapi.lidolearning.com/v1/graphql'
# HASURA_ADMIN_SECRET = '10xbetter'


def run_query(query, variables):
    print(query, variables)
    body = {
        'query': query,
        'variables': variables
    }
    response = _make_post_call(body)
    print('query response: ', response)
    if response.get('data') is not None:
        return response.get('data')
    raise RuntimeError('query failed: ' + str(response))


def _make_post_call(body):
    url = HASURA_GRAPHQL_ENDPOINT
    headers = {
        'Content-type': 'application/json',
        'x-hasura-admin-secret': HASURA_ADMIN_SECRET
    }
    response = requests.post(url, json=body, headers=headers, timeout=10)
    return response.json()
