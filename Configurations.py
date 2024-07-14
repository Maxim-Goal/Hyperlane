import json

network_info = {
    "optimism": {'chains_id': 10, 'tx_type': 2},
    "arbitrum": {'chains_id': 42161, 'tx_type': 2},
    "base": {'chains_id': 8453, 'tx_type': 2},
    "linea": {'chains_id': 59144, 'tx_type': 2},
    "scroll": {'chains_id': 534352, 'tx_type': 2},
    "blast": {'chains_id': 81457, 'tx_type': 2},
}

network_rpc = {
    "optimism": "https://endpoints.omniatech.io/v1/op/mainnet/public",
    "arbitrum": "https://arb1.arbitrum.io/rpc",
    "base": "https://mainnet.base.org",
    "linea": "https://linea.decubate.com",
    "scroll": "https://mainnet-rpc.scroll.io/",
}

# Merkly
contracts_address_merkly_eth_bridge = {
    "optimism": "0xc110e7faa95680c79937ccaca3d1cab7902be25e",
    "arbitrum": "0x233888F5Dc1d3C0360b559aBc029675290DAFa70",
    "base": "0x0cb0354E9C51960a7875724343dfC37B93d32609",
    "linea": "0x8F2161c83F46B46628cb591358dE4a89A63eEABf",
    "scroll": "0xc0faBF14f8ad908b2dCE4C8aA2e7c1a6bD069957",
}

abi_merkly_eth_bridge = json.loads('''[
  {
    "type": "function",
    "name": "quoteBridge",
    "constant": true,
    "stateMutability": "view",
    "payable": false,
    "inputs": [
      {
        "type": "uint32",
        "name": "_destination"
      },
      {
        "type": "uint256",
        "name": "amount"
      }
    ],
    "outputs": [
      {
        "type": "uint256",
        "name": "fee"
      }
    ]
  },
  {
    "type": "function",
    "name": "bridgeETH",
    "constant": false,
    "stateMutability": "payable",
    "payable": true,
    "inputs": [
      {
        "type": "uint32",
        "name": "_destination"
      },
      {
        "type": "uint256",
        "name": "amount"
      }
    ],
    "outputs": [
      {
        "type": "bytes32",
        "name": "messageId"
      }
    ]
  },
  {
    "type": "function",
    "name": "bridgeWETH",
    "constant": false,
    "stateMutability": "payable",
    "payable": true,
    "inputs": [
      {
        "type": "uint32",
        "name": "_destination"
      },
      {
        "type": "uint256",
        "name": "amount"
      }
    ],
    "outputs": [
      {
        "type": "bytes32",
        "name": "messageId"
      }
    ]
  }
]''')

# ZeroWay
contracts_address_zeroway_refuel = {
    "optimism": '0x73F9228039b5c2CE4DCfFA32A8712A48283EDE9b',
    "arbitrum": '0x73F9228039b5c2CE4DCfFA32A8712A48283EDE9b',
    "base": '0x73F9228039b5c2CE4DCfFA32A8712A48283EDE9b',
    "linea": '0x73F9228039b5c2CE4DCfFA32A8712A48283EDE9b',
    "scroll": '0x73F9228039b5c2CE4DCfFA32A8712A48283EDE9b',
}

abi_zeroway_refuel = json.loads('''[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"InvalidInitialization","type":"error"},{"inputs":[],"name":"NotInitializing","type":"error"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"OwnableInvalidOwner","type":"error"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"OwnableUnauthorizedAccount","type":"error"},{"inputs":[],"name":"ReentrancyGuardReentrantCall","type":"error"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"DepositETH","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"DepositFallbackETH","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"target","type":"address"},{"indexed":true,"internalType":"uint32","name":"destinationDomain","type":"uint32"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"address","name":"mailbox","type":"address"},{"indexed":false,"internalType":"bool","name":"success","type":"bool"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"Handle","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint64","name":"version","type":"uint64"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"target","type":"address"},{"indexed":true,"internalType":"uint32","name":"destinationDomain","type":"uint32"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"hyperlaneFee","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"serviceFee","type":"uint256"},{"indexed":false,"internalType":"bytes32","name":"messageId","type":"bytes32"}],"name":"Refuel","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"newMailbox","type":"address"}],"name":"SetMailbox","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"components":[{"internalType":"uint256","name":"minRefuelAmount","type":"uint256"},{"internalType":"uint256","name":"maxRefuelAmount","type":"uint256"},{"internalType":"uint256","name":"fixedFee","type":"uint256"},{"internalType":"uint256","name":"basicMultiplier","type":"uint256"},{"internalType":"bool","name":"boundsEnabled","type":"bool"},{"internalType":"uint256","name":"minLiquidityBound","type":"uint256"},{"internalType":"uint256","name":"maxLiquidityBound","type":"uint256"},{"internalType":"uint256","name":"minPercentFeeBound","type":"uint256"},{"internalType":"uint256","name":"maxPercentFeeBound","type":"uint256"},{"internalType":"uint256","name":"emergencyLiquidityMinimum","type":"uint256"}],"indexed":false,"internalType":"struct ZeroWayGasRefuelV1.RefuelSettings","name":"newRefuelSettings","type":"tuple"}],"name":"SetRefuelSettings","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"target","type":"address"},{"indexed":false,"internalType":"uint256","name":"currentLiquidity","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TrySendRefuelFailed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"target","type":"address"},{"indexed":false,"internalType":"uint256","name":"currentLiquidity","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TrySendRefuelSuccess","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"target","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"WithdrawDebt","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"WithdrawETH","type":"event"},{"inputs":[{"internalType":"address","name":"target_","type":"address"},{"internalType":"uint256","name":"amount_","type":"uint256"},{"internalType":"uint32","name":"destinationDomain_","type":"uint32"}],"name":"calculateHyperlaneFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"target_","type":"address"},{"internalType":"uint256","name":"amount_","type":"uint256"},{"internalType":"uint32","name":"destinationDomain_","type":"uint32"}],"name":"calculateRefuelFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"target_","type":"address"},{"internalType":"uint256","name":"amount_","type":"uint256"},{"internalType":"uint32","name":"destinationDomain_","type":"uint32"}],"name":"calculateServiceFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"depositETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"getFeeMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint32","name":"origin_","type":"uint32"},{"internalType":"bytes32","name":"sender_","type":"bytes32"},{"internalType":"bytes","name":"data_","type":"bytes"}],"name":"handle","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"hyperlaneClient","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"initialOwner_","type":"address"},{"internalType":"address","name":"mailboxAddr_","type":"address"},{"components":[{"internalType":"uint256","name":"minRefuelAmount","type":"uint256"},{"internalType":"uint256","name":"maxRefuelAmount","type":"uint256"},{"internalType":"uint256","name":"fixedFee","type":"uint256"},{"internalType":"uint256","name":"basicMultiplier","type":"uint256"},{"internalType":"bool","name":"boundsEnabled","type":"bool"},{"internalType":"uint256","name":"minLiquidityBound","type":"uint256"},{"internalType":"uint256","name":"maxLiquidityBound","type":"uint256"},{"internalType":"uint256","name":"minPercentFeeBound","type":"uint256"},{"internalType":"uint256","name":"maxPercentFeeBound","type":"uint256"},{"internalType":"uint256","name":"emergencyLiquidityMinimum","type":"uint256"}],"internalType":"struct ZeroWayGasRefuelV1.RefuelSettings","name":"refuelSettings_","type":"tuple"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"mailboxAddr","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"target_","type":"address"},{"internalType":"uint256","name":"amount_","type":"uint256"},{"internalType":"uint32","name":"destinationDomain_","type":"uint32"}],"name":"refuel","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"refuelSettings","outputs":[{"internalType":"uint256","name":"minRefuelAmount","type":"uint256"},{"internalType":"uint256","name":"maxRefuelAmount","type":"uint256"},{"internalType":"uint256","name":"fixedFee","type":"uint256"},{"internalType":"uint256","name":"basicMultiplier","type":"uint256"},{"internalType":"bool","name":"boundsEnabled","type":"bool"},{"internalType":"uint256","name":"minLiquidityBound","type":"uint256"},{"internalType":"uint256","name":"maxLiquidityBound","type":"uint256"},{"internalType":"uint256","name":"minPercentFeeBound","type":"uint256"},{"internalType":"uint256","name":"maxPercentFeeBound","type":"uint256"},{"internalType":"uint256","name":"emergencyLiquidityMinimum","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newMailbox_","type":"address"}],"name":"setMailbox","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"minRefuelAmount","type":"uint256"},{"internalType":"uint256","name":"maxRefuelAmount","type":"uint256"},{"internalType":"uint256","name":"fixedFee","type":"uint256"},{"internalType":"uint256","name":"basicMultiplier","type":"uint256"},{"internalType":"bool","name":"boundsEnabled","type":"bool"},{"internalType":"uint256","name":"minLiquidityBound","type":"uint256"},{"internalType":"uint256","name":"maxLiquidityBound","type":"uint256"},{"internalType":"uint256","name":"minPercentFeeBound","type":"uint256"},{"internalType":"uint256","name":"maxPercentFeeBound","type":"uint256"},{"internalType":"uint256","name":"emergencyLiquidityMinimum","type":"uint256"}],"internalType":"struct ZeroWayGasRefuelV1.RefuelSettings","name":"newRefuelSettings","type":"tuple"}],"name":"setRefuelSettings","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"userDebt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to_","type":"address"}],"name":"withdrawDebt","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to_","type":"address"},{"internalType":"uint256","name":"amount_","type":"uint256"}],"name":"withdrawETH","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]''')