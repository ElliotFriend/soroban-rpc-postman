#!/usr/bin/env python3

from stellar_sdk import xdr, soroban_types

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

te_xdr = xdr.transaction_envelope.TransactionEnvelope.from_xdr('AAAAAgAAAABndwzjYbYj4WubbspKSP2ugBwwmtTRSNYwrO3eu2TT9wAAAGQAEcpoAAAABgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAACgAAAAVoZWxsbwAAAAAAAAEAAAAHc29yb2JhbgAAAAAAAAAAAbtk0/cAAABA7S8ZDIj5I/NrZKIEtU9DDF/XNiUlKslxuCkQxUnpz++9+yZ2DdbrCI8yO+CP/BP+hKr5gxfBxJQMdDuAW5LHBw==')
print(te_xdr.to_xdr_bytes())