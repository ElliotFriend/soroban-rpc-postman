# soroban-rpc-postman <!-- omit in toc -->

Here lies RPC requests made from postman to a Soroban-RPC endpoint

[![Run in Postman][pm-button]][pm-collection]

## Table of Contents <!-- omit in toc -->

- [What's the Point Here?](#whats-the-point-here)
- [Relevant Documentation](#relevant-documentation)
- [The Postman Collection](#the-postman-collection)
- [The Requests](#the-requests)
  - [`getAccount`](#getaccount)
  - [`getHealth`](#gethealth)
  - [`getLatestLedger` (WIP)](#getlatestledger-wip)
  - [`getContractData`](#getcontractdata)
  - [`getEvents` (WIP)](#getevents-wip)
  - [`getNetwork` (WIP)](#getnetwork-wip)
  - [`getTransactionStatus`](#gettransactionstatus)
  - [`requestAirdrop` (WIP)](#requestairdrop-wip)
  - [`sendTransaction`](#sendtransaction)
  - [`simulateTransaction`](#simulatetransaction)

## What's the Point Here?

Here's what you'll find in this repository:

- A collection of the (current) JSON RPC requests that can be made against a
  Soroban-RPC endpoint
- Information on how to format the requests to a Soroban-RPC endpoint
- A collection of Postman requests that will get you going toward making those
  RPC requests
- A place to get started writing scripts and apps in Python and JavaScript
  (because those are the main languages I use.)

## Relevant Documentation

Here is some of the resources I've used in creating this collection.

- [Soroban RPC Design Document][design-doc]
  - This is the best source I've found so far. It's not _intended_ as a
    finalized document, but more as a communal brainstorm/roadmap.
- [Paul's OpenRPC Spec][paul-spec] (out-of-date I believe)
- [Smephite's amazing guide to all things types][smephite-guide]
- [JSON-RPC 2.0 Specification][jsonrpc-spec]
- The [jsonrpcclient][python-jsonrpcclient] Python library makes it quite easy
  to generate and parse requests like these.
- There is also a [json-rpc-2.0][node-json-rpc] npm package, although I'm no
  good with JavaScript.

## The Postman Collection

You can get to a running (I think) version of the collection right in your
browser by clicking the button below.

[![Run in Postman][pm-button]][pm-collection]

Alternatively, the `Soroban-RPC Requests.postman-collection.json` file has the
same requests in a format you could import directly into your own instance of
Postman.

## The Requests

The basic structure of a JSON-RPC request looks something like this:

```json5
{
    "jsonrpc": "2.0", // Specifies the JSON-RPC protocol version to use. Must be exactly "2.0"
    "id": 8675309, // An identifier for the client. I'm not entirely sure if this is required by Soroban-RPC
    "method": "<method-name>", // The name of the method to be invoked
    "params": {
        // A structured value that holds the parameter(s) being used during the invocation
        "<key>": "<value>"
    }
}
```

With that out of the way, here's how we use the (currently) existing methods for
Soroban-RPC endpoints.

With the first method, `getAccount` request, I will also provide a python and
javascript snippet for making the request to the endpoint. I trust you'll be
able to extrapolate how to request different methods when necessary. (I will
attempt to keep a working, more-complete, and up-to-date `rpc_calls.py` file in
this repository, as well.)

### `getAccount`

When invoking `getAccount`, you must supply the account's public key as the
`address` parameter.

The response is intended to be a _minimal_ set of account information, and will
include the account ID, sequence number, and balances (not yet?).

#### `getAccount` Request <!-- omit in toc -->

Request body:

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "method": "getAccount",
    "params": {
        "address": "GBTXODHDMG3CHYLLTNXMUSSI7WXIAHBQTLKNCSGWGCWO3XV3MTJ7PNZA"
    }
}
```

#### `getAccount` Response <!-- omit in toc -->

Response body:

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "result": {
        "id": "GBTXODHDMG3CHYLLTNXMUSSI7WXIAHBQTLKNCSGWGCWO3XV3MTJ7PNZA",
        "sequence": "3435501390397448"
    }
}
```

### `getHealth`

When invoking `getHealth`, you are checking on the general well-being of the
node. No parameters are required, nor are they accepted.

#### `getHealth` Request <!-- omit in toc -->

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "method": "getHealth"
}
```

#### `getHealth` Response <!-- omit in toc -->

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "result": {
        "status": "healthy"
    }
}
```

### `getLatestLedger` (WIP)

When invoking `getLatestLedger`, you will find out the current latest known
ledger of this node. This is a subset of ledger info available through Horizon.

#### `getLatestLedger` Request <!-- omit in toc -->

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "method": "getLatestLedger"
}
```

#### `getLatestLedger` Response <!-- omit in toc -->

```json5
"work-in-progress"
```

According to the [design-doc], it should return something like this (someday?):

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "result": {
        "id": "<hash>", // hash of the latest ledger
        "protocolVersion": "<number>",
        "sequence": "<number>"
    }
}
```

### `getContractData`

> **WARNING**: `getContractData` WILL SOON BE DEPRECATED IN FAVOR OR
> [`getLedgerEntry`][getLedgerEntry]

Invoking `getContractData` is useful for reading the current value of
`CONTRACT_DATA` ledger entries directly through RPC. This allows you to directly
inspect the _current state_ of a contract.

#### `getContractData` Request <!-- omit in toc -->

The tricky part for this method is getting a useable value for the `key`
parameter. The contract below is a deployed copy of the [`increment`
example][increment-contract] from the Soroban documentation examples. As such,
the `key` we need to provide is an xdr-encoded  `ScVal` of the symbol `COUNTER`.

This can be achieved using the `soroban` branch of the python `stellar_sdk`. A
starter script is suppllied in `sc_val.py`

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "method": "getContractData",
    "params": {
        "contractId": "a6299ac13778b28e917b4af61d16074092b5a14e92c7e9351d825100e41877e7",
        "key": "AAAABQAAAAdDT1VOVEVSAA=="
    }
}
```

This method can also be used to retrieve WASM byte-code that is stored on the
ledger. This requires us to supply a `key` of the `ContractCode` SCVal ledger
entry. Here's what the request would look like:

```json5
"something"
```

#### `getContractData` Response <!-- omit in toc -->

For the first request above (the "COUNTER" data entry). The returned `xdr` can
be decoded as in `sc_val.py`:

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "result": {
        "xdr": "AAAAAQAAAAQ=",
        "lastModifiedLedgerSeq": "1166180",
        "latestLedger": "1166323"
    }
}
```

The response with the WASM byte-code looks like this:

```json5
"something
```

### `getEvents` (WIP)

The `getEvents` method can be used for a client to retrieve a filtered list of
events that are emitted by a specified ledger range.

#### `getEvents` Request <!-- omit in toc -->

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "method": "getEvents",
    "params": {
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
}
```

#### `getEvents` Response <!-- omit in toc -->

```json5
"work-in-progress"
```

### `getNetwork` (WIP)

The `getNetwork` method returns general information about the currently
configured network.

#### `getNetwork` Request <!-- omit in toc -->

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "method": "getNetwork"
}
```

#### `getNetwork` Response <!-- omit in toc -->

```json5
"work-in-progress"
```

### `getTransactionStatus`

You can use `getTransactionStatus` to find out if a sent transaction has been
successful, failed, etc. You will also get a `results` response with anything
that was returned by the transaction. In the example below, the transaction was
deploying the `increment` contract, and the `results` contains the bytes of the
contract ID.

#### `getTransactionStatus` Request <!-- omit in toc -->

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "method": "getTransactionStatus",
    "params": {
        "hash": "9975a8f097fe3e6a3c6048a5c91631202b8f4f2b5f6edb2f81655631aeb3ef51"
    }
}
```

#### `getTransactionStatus` Response <!-- omit in toc -->

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "result": {
        "id": "9975a8f097fe3e6a3c6048a5c91631202b8f4f2b5f6edb2f81655631aeb3ef51",
        "status": "success",
        "results": [
            {
                "xdr": "AAAABAAAAAEAAAAEAAAAIKYpmsE3eLKOkXtK9h0WB0CStaFOksfpNR2CUQDkGHfn"
            }
        ]
    }
}
```

### `requestAirdrop` (WIP)

The `requestAirdrop` is a friendbot interface. A request can be made (outside of
the public network) to give lumens to a particular account.

#### `requestAirdrop` Request <!-- omit in toc -->

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "method": "requestAirdrop",
    "params": {
        "account": "GD3LWOYS4I6P2VF43MH2E627O5LMIJWCSGNIP3Y7SNWU52FGJT4ZI7VP"
    }
}
```

#### `requestAirdrop` Response <!-- omit in toc -->

```json5
"work-in-progress"
```

### `sendTransaction`

The `sendTransaction` allows you to submit a real stellar transaction. You don't
get a status in return, you are expected to use `getTransactionStatus` to find
out if it was successful or not, and to get any return from the invocation.

#### `sendTransaction` Request <!-- omit in toc -->

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "method": "sendTransaction",
    "params": {
        "xdr": {
            "TransactionEnvelope": "AAAAAgAAAABndwzjYbYj4WubbspKSP2ugBwwmtTRSNYwrO3eu2TT9wAAAGQAEcpoAAAABgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAACgAAAAVoZWxsbwAAAAAAAAEAAAAHc29yb2JhbgAAAAAAAAAAAbtk0/cAAABA7S8ZDIj5I/NrZKIEtU9DDF/XNiUlKslxuCkQxUnpz++9+yZ2DdbrCI8yO+CP/BP+hKr5gxfBxJQMdDuAW5LHBw=="
        }
    }
}
```

#### `sendTransaction` Response <!-- omit in toc -->

```json5
"something"
```

### `simulateTransaction`

The `simulateTransaction` method is intended to submit a trial invocation of a
smart contract to get back return values, ledger footprint, expected costs, etc.
I don't seem to be able to make this work. That might be because I'm trying to
use a "classic" stellar transaction?

#### `simulateTransaction` Request <!-- omit in toc -->

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "method": "simulateTransaction",
    "params": {
        "xdr.TransactionEnvelope": "AAAAAgAAAABndwzjYbYj4WubbspKSP2ugBwwmtTRSNYwrO3eu2TT9wAAAGQAEcpoAAAABgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAACgAAAAVoZWxsbwAAAAAAAAEAAAAHc29yb2JhbgAAAAAAAAAAAbtk0/cAAABA7S8ZDIj5I/NrZKIEtU9DDF/XNiUlKslxuCkQxUnpz++9+yZ2DdbrCI8yO+CP/BP+hKr5gxfBxJQMdDuAW5LHBw=="
    }
}
```

#### `simulateTransaction` Response <!-- omit in toc -->

```json5
"work-in-progress"
```

[design-doc]: <https://docs.google.com/document/d/1TZUDgo_3zPz7TiPMMHVW_mtogjLyPL0plvzGMsxSz6A/edit#heading=h.ohr0vgpzoi7r>
[paul-spec]: <https://github.com/paulbellamy/soroban-docs/blob/soroban-rpc/soroban-rpc/openrpc.yaml>
[smephite-guide]: <https://gist.github.com/Smephite/09b40e842ef454effe4693e0d18246d7>
[jsonrpc-spec]: <https://www.jsonrpc.org/specification>
[pm-button]: <https://run.pstmn.io/button.svg>
[pm-collection]: <https://app.getpostman.com/run-collection/5352332-9ccf291a-944a-4037-8655-1d6c35d20cf8?action=collection%2Ffork&collection-url=entityId%3D5352332-9ccf291a-944a-4037-8655-1d6c35d20cf8%26entityType%3Dcollection%26workspaceId%3D0450a14f-82ac-4faf-8045-b7bcf89928b5>
[python-jsonrpcclient]: <https://www.jsonrpcclient.com/en/4.0.1/index.html>
[node-json-rpc]: <https://www.npmjs.com/package/json-rpc-2.0>
[getLedgerEntry]: <https://github.com/stellar/soroban-tools/pull/274>
[increment-contract]: <https://soroban.stellar.org/docs/examples/storing-data>
