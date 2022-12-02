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

## Relevant Documentation

Here is some of the resources I've used in creating this collection.

- [Soroban RPC Design Document][design-doc]
  - This is the best source I've found so far. It's not *intended* as a
    finalized document, but more as a communal brainstorm/roadmap.
- [Paul's OpenRPC Spec][paul-spec] (out-of-date I believe)
- [Smephite's amazing guide to all things types][smephite-guide]
- [JSON-RPC 2.0 Specification][jsonrpc-spec]

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

### `getAccount`

When invoking `getAccount`, you must supply the account's public key as the
`address` parameter.

The response is intended to be a *minimal* set of account information, and will
include the account ID, sequence number, and balances (not yet?).

#### `getAccount` Request <!-- omit in toc -->

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "method": "getAccount",
    "params": {
        "address": "GB3SSIX7JVRNFXKVBGXC4L66NPTSO3TU3UFJUWAWMMDVVOCXMIDXXRAI"
    }
}
```

#### `getAccount` Response <!-- omit in toc -->

```json5
{
    "jsonrpc": "2.0",
    "id": 8675309,
    "result": {
        "id": "GB3SSIX7JVRNFXKVBGXC4L66NPTSO3TU3UFJUWAWMMDVVOCXMIDXXRAI",
        "sequence": "3435501390397448"
    }
}
```

### `getHealth`

#### `getHealth` Request <!-- omit in toc -->

```json5
"something"
```

#### `getHealth` Response <!-- omit in toc -->

```json5
"something"
```

### `getLatestLedger` (WIP)

#### `getLatestLedger` Request <!-- omit in toc -->

```json5
"something"
```

#### `getLatestLedger` Response <!-- omit in toc -->

```json5
"something"
```

### `getContractData`

#### `getContractData` Request <!-- omit in toc -->

```json5
"something"
```

#### `getContractData` Response <!-- omit in toc -->

```json5
"something"
```

### `getEvents` (WIP)

#### `getEvents` Request <!-- omit in toc -->

```json5
"something"
```

#### `getEvents` Response <!-- omit in toc -->

```json5
"something"
```

### `getNetwork` (WIP)

#### `getNetwork` Request <!-- omit in toc -->

```json5
"something"
```

#### `getNetwork` Response <!-- omit in toc -->

```json5
"something"
```

### `getTransactionStatus`

#### `getTransactionStatus` Request <!-- omit in toc -->

```json5
"something"
```

#### `getTransactionStatus` Response <!-- omit in toc -->

```json5
"something"
```

### `requestAirdrop` (WIP)

#### `requestAirdrop` Request <!-- omit in toc -->

```json5
"something"
```

#### `requestAirdrop` Response <!-- omit in toc -->

```json5
"something"
```

### `sendTransaction`

#### `sendTransaction` Request <!-- omit in toc -->

```json5
"something"
```

#### `sendTransaction` Response <!-- omit in toc -->

```json5
"something"
```

### `simulateTransaction`

#### `simulateTransaction` Request <!-- omit in toc -->

```json5
"something"
```

#### `simulateTransaction` Response <!-- omit in toc -->

```json5
"something"
```

[design-doc]: <https://docs.google.com/document/d/1TZUDgo_3zPz7TiPMMHVW_mtogjLyPL0plvzGMsxSz6A/edit#heading=h.ohr0vgpzoi7r>
[paul-spec]: <https://github.com/paulbellamy/soroban-docs/blob/soroban-rpc/soroban-rpc/openrpc.yaml>
[smephite-guide]: <https://gist.github.com/Smephite/09b40e842ef454effe4693e0d18246d7>
[jsonrpc-spec]: <https://www.jsonrpc.org/specification>
[pm-button]: <https://run.pstmn.io/button.svg>
[pm-collection]: <https://app.getpostman.com/run-collection/5352332-9ccf291a-944a-4037-8655-1d6c35d20cf8?action=collection%2Ffork&collection-url=entityId%3D5352332-9ccf291a-944a-4037-8655-1d6c35d20cf8%26entityType%3Dcollection%26workspaceId%3D0450a14f-82ac-4faf-8045-b7bcf89928b5>
