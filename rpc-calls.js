const { JSONRPCClient } = require("json-rpc-2.0");
const fetch = require("node-fetch2");
(async () => {

  // CHANGE THIS URL IF REQUIRED
  const RPC_URL = 'http://127.0.0.1:8000/soroban/rpc'

  const client = new JSONRPCClient((jsonRPCRequest) =>
    fetch(RPC_URL, {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify(jsonRPCRequest),
    }).then((response) => {
      if (response.status === 200) {
        return response
          .json()
          .then((jsonRPCResponse) => client.receive(jsonRPCResponse));
      } else if (jsonRPCRequest.id !== undefined) {
        return Promise.reject(new Error(response.statusText));
      }
    })
  )

  client
    .request("getAccount", { "address": "GB3SSIX7JVRNFXKVBGXC4L66NPTSO3TU3UFJUWAWMMDVVOCXMIDXXRAI" })
    .then((result) => console.log(result))
})();