#!/usr/bin/env python3

from jsonrpcclient import request, parse, Ok
import requests

# CHANGE THIS URL IF REQUIRED
rpc_url = 'http://127.0.0.1:8000/soroban/rpc'


get_account_response = requests.post(rpc_url, json=request(
  'getAccount',
  params={
    "address": "GB3SSIX7JVRNFXKVBGXC4L66NPTSO3TU3UFJUWAWMMDVVOCXMIDXXRAI"
  }
))
print(f"getAccount: {get_account_response.json()}\n")

get_health_response = requests.post(rpc_url, json=request(
  'getHealth'
))
print(f"getHealth: {get_health_response.json()}\n")

get_latest_ledger_response = requests.post(rpc_url, json=request(
  'getLatestLedger'
))
print(f"getLatestLedger: {get_latest_ledger_response.json()}\n")

get_contract_data_response = requests.post(rpc_url, json=request(
  'getContractData',
  params={
    "contractId": "a6299ac13778b28e917b4af61d16074092b5a14e92c7e9351d825100e41877e7",
    "key": "AAAABQAAAAdDT1VOVEVSAA=="
  }
))
print(f"getContractData: {get_contract_data_response.json()}\n")

# send_transaction_response = requests.post(rpc_url, json=request(
#   'sendTransaction',
#   params={
#     "xdr.TransactionEnvelope": "AAAAAgAAAABndwzjYbYj4WubbspKSP2ugBwwmtTRSNYwrO3eu2TT9wAAAGQAEcpoAAAABgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAACgAAAAVoZWxsbwAAAAAAAAEAAAAHc29yb2JhbgAAAAAAAAAAAbtk0/cAAABA7S8ZDIj5I/NrZKIEtU9DDF/XNiUlKslxuCkQxUnpz++9+yZ2DdbrCI8yO+CP/BP+hKr5gxfBxJQMdDuAW5LHBw=="
#   }
# ))
# print(send_transaction_response.json())