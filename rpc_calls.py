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

get_events_response = requests.post(rpc_url, json=request(
    'getEvents',
    params={
        "startLedger": "100",
        "endLedger": "1000",
        "filters": {
            "type": "contract",
            "contractIds": [
                "a6299ac13778b28e917b4af61d16074092b5a14e92c7e9351d825100e41877e7",
                "4018b6f8f2d50449d001920362be249d2bdf768d5a6da6ce73146a994d8747c7"
            ]
        }
    }
))
print(f"getEvents: {get_events_response.json()}\n")

get_network_response = requests.post(rpc_url, json=request(
    'getNetwork'
))
print(f"getHealth: {get_network_response.json()}\n")

get_tx_status_response = requests.post(rpc_url, json=request(
    'getTransactionStatus',
    params={
        "hash": "9975a8f097fe3e6a3c6048a5c91631202b8f4f2b5f6edb2f81655631aeb3ef51"
    }
))
print(f"getTransactionStatus: {get_tx_status_response.json()}\n")

request_airdrop_response = requests.post(rpc_url, json=request(
    'requestAirdrop',
    params={
        "account": "GD3LWOYS4I6P2VF43MH2E627O5LMIJWCSGNIP3Y7SNWU52FGJT4ZI7VP"
    }
))
print(f"requestAirdrop: {request_airdrop_response.json()}")

send_transaction_response = requests.post(rpc_url, json=request(
  'sendTransaction',
  params={
    "xdr": {
        "TransactionEnvelope": "AAAAAgAAAABndwzjYbYj4WubbspKSP2ugBwwmtTRSNYwrO3eu2TT9wAAAGQAEcpoAAAABgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAACgAAAAVoZWxsbwAAAAAAAAEAAAAHc29yb2JhbgAAAAAAAAAAAbtk0/cAAABA7S8ZDIj5I/NrZKIEtU9DDF/XNiUlKslxuCkQxUnpz++9+yZ2DdbrCI8yO+CP/BP+hKr5gxfBxJQMdDuAW5LHBw=="
    }
  }
))
print(f"sendTransaction: {send_transaction_response.json()}\n")

simulate_transaction_response = requests.post(rpc_url, json=request(
  'simulateTransaction',
  params={
    "xdr": {
        "TransactionEnvelope": "AAAAAgAAAABndwzjYbYj4WubbspKSP2ugBwwmtTRSNYwrO3eu2TT9wAAAGQAEcpoAAAABgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAACgAAAAVoZWxsbwAAAAAAAAEAAAAHc29yb2JhbgAAAAAAAAAAAbtk0/cAAABA7S8ZDIj5I/NrZKIEtU9DDF/XNiUlKslxuCkQxUnpz++9+yZ2DdbrCI8yO+CP/BP+hKr5gxfBxJQMdDuAW5LHBw=="
    }
  }
))
print(f"simulateTransaction: {simulate_transaction_response.json()}\n")