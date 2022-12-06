#!/usr/bin/env python3

from stellar_sdk import xdr, soroban_types
from stellar_sdk import Keypair, TransactionBuilder, Network
from stellar_sdk.soroban import SorobanServer
from stellar_sdk.soroban_types import InvokerSignature, BigInt, Int64

# Prints `AAAABQAAAAdDT1VOVEVSAA==` for use in the `getContractData` method
counter_key = soroban_types.Symbol("COUNTER")._to_xdr_sc_val().to_xdr()
print(counter_key)

# Prints `4` which was the current state of the contract at time of writing
response_xdr = 'AAAAAQAAAAQ='
response_value = xdr.sc_val.SCVal.from_xdr(response_xdr).u32.uint32
print(response_value)

# Prints `` for use in `getContractData` to retrieve WASM byte-code
# contract_data_key = xdr.sc_contract_code.SCContractCode(xdr.sc_contract_code_type.SCContractCodeType(1)).to_xdr()
# print(contract_data_key)
# contract_data_le_key = xdr.sc_object.SCObject(xdr.sc_contract_code.SCContractCode.to_xdr())
# print(contract_data_le_key)

# te_xdr = xdr.transaction_envelope.TransactionEnvelope.from_xdr('AAAAAgAAAABndwzjYbYj4WubbspKSP2ugBwwmtTRSNYwrO3eu2TT9wAAAGQAEcpoAAAABgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAACgAAAAVoZWxsbwAAAAAAAAEAAAAHc29yb2JhbgAAAAAAAAAAAbtk0/cAAABA7S8ZDIj5I/NrZKIEtU9DDF/XNiUlKslxuCkQxUnpz++9+yZ2DdbrCI8yO+CP/BP+hKr5gxfBxJQMdDuAW5LHBw==')
# print(te_xdr.to_xdr_bytes())

# Prints `` for use in the `getLedgerEntry` method
counter_ledger_key = xdr.ledger_key_contract_data.LedgerKeyContractData(
    contract_id=xdr.hash.Hash(bytes.fromhex('a6299ac13778b28e917b4af61d16074092b5a14e92c7e9351d825100e41877e7')),
    key=soroban_types.Symbol("COUNTER")._to_xdr_sc_val()
).to_xdr()
print(counter_ledger_key)

event_topic = soroban_types.Symbol("transfer")._to_xdr_sc_val().to_xdr()
print(event_topic)

kp = Keypair.from_secret('SDAT54W7Q7WZO6PI5VXD5MTYR64WCEYAVVFM2SPRIJDJQWC3EKLDUPCJ')
soroban_server = SorobanServer('http://127.0.0.1:8000/soroban/rpc')
source = soroban_server.load_account(kp.public_key)
contract_id = '71c670db8b9d9dd3fa17d83bd98e4a9814f926121972774bd419fa402fe01dc7'
tx = (
    TransactionBuilder(source, Network.FUTURENET_NETWORK_PASSPHRASE)
    .set_timeout(300)
    .append_invoke_contract_function_op(
        contract_id=contract_id,
        method="import",  # or 'export'
        parameters=[
            InvokerSignature(),  # Invoker
            BigInt(0),  # Nonce
            Int64(1_000 * 10**7)  # amount, 1,000 tokens
        ],
        source=kp.public_key,
    )
    .build()
)
print(tx.to_xdr())