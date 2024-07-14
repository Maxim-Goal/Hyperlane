import random
import requests
import time
import csv

from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account.signers.local import LocalAccount
from fake_useragent import UserAgent

from Configurations import (abi_merkly_eth_bridge, contracts_address_merkly_eth_bridge, network_info, network_rpc,
                            contracts_address_zeroway_refuel, abi_zeroway_refuel)
from Key_proxy import key_proxy


class Client:

    def __init__(self, rpc: str,
                 private_key: str | None = None,
                 seed: str | None = None,
                 proxys: str | None = None,
                 check_proxy: bool = True,
                 ):

        self.headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'user-agent': UserAgent().chrome
        }
        self.rpc = rpc
        self.proxys = proxys

        if self.proxys:
            if 'http' not in self.proxys:
                self.proxys = f'http://{self.proxys}'

            if check_proxy:
                your_ip = requests.get(
                    'http://eth0.me/', proxies={'http': self.proxys}, timeout=10
                ).text.rstrip()
                if your_ip not in proxys:
                    print(f"Proxy doesn't work! Your IP is {your_ip}.")

        self.w3 = Web3(provider=Web3.HTTPProvider(endpoint_uri=self.rpc, request_kwargs={'proxies': {'http': self.proxys},
                                                                                         'headers': self.headers}))


        if private_key:
            self.account = self.w3.eth.account.from_key(private_key=private_key)
        elif seed:
            self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
            self.w3.eth.account.enable_unaudited_hdwallet_features()
            web3_account: LocalAccount = self.w3.eth.account.from_mnemonic(seed)

            private_key = web3_account._private_key.hex()
            self.account = self.w3.eth.account.from_key(private_key=private_key)
        else:
            self.account = None

    def auto_add_params(self, tx_type: int,
                        to_address: str,
                        data: str,
                        value: int | float | None = None,
                        chain_id: int | None = None,
                        nonce: int | None = None,
                        gas_price: int | None = None,
                        from_address: str | None = None,
                        ):
        tx_params = {'to': to_address, 'data': data}
        if chain_id is None:
            tx_params['chainId'] = self.w3.eth.chain_id
        else:
            tx_params['chainId'] = chain_id

        if nonce is None:
            tx_params['nonce'] = self.w3.eth.get_transaction_count(self.account.address)
        else:
            tx_params['nonce'] = nonce

        if from_address is None:
            tx_params['from'] = self.account.address
        else:
            tx_params['from'] = from_address

        if gas_price is None:
            if tx_type == 2:
                tx_params['maxPriorityFeePerGas'] = self.w3.eth.max_priority_fee
                tx_params['maxFeePerGas'] = self.w3.eth.gas_price + self.w3.eth.max_priority_fee
            else:
                tx_params['gasPrice'] = self.w3.eth.gas_price

        if value is not None:
            tx_params['value'] = value

        tx_params['gas'] = self.w3.eth.estimate_gas(tx_params)

        return tx_params


for i in range(len(key_proxy)):

    # Начало настроек
    networks = ["optimism", "arbitrum", "base", "linea"] # Доступные сети: "optimism", "arbitrum", "base", "linea", "scroll"
    protocols = ('zeroway', 'merkly') # Доступные протоколы: 'zeroway' - refuel(отправка ETH), 'merkly' - отправка ETH
    amount = random.uniform(0.3, 0.5) # Какой % будет переводиться от баланса. Пример 0.3(30%) до 0.5(50%)
    waiting_time = random.randint(1000, 2000) # Рандомное время ожидания между транзакциями в секундах от и до
    # Конец настроек

    key_proxy_work_lst = key_proxy
    key_proxy_work = random.choice(key_proxy_work_lst)
    key = key_proxy_work[0]
    proxy = key_proxy_work[1]
    key_proxy_work_lst.remove(key_proxy_work)

    address_balance = 0
    while address_balance < 0.002:
        network = random.choice(networks)
        connect_network = Client(rpc=network_rpc[network], private_key=key, proxys=proxy)
        address_balance = connect_network.w3.eth.get_balance(connect_network.account.address)
        address_balance = connect_network.w3.from_wei(address_balance, 'ether')

    amount = int(connect_network.w3.eth.get_balance(connect_network.account.address) * amount)

    networks.remove(network)
    destination_network = random.choice(networks)
    protocol = random.choice(protocols)

    if protocol == 'merkly':
        merkly_eth_bridge_contract = connect_network.w3.eth.contract(
            connect_network.w3.to_checksum_address(contracts_address_merkly_eth_bridge[network]),
            abi=abi_merkly_eth_bridge)

        fee = merkly_eth_bridge_contract.functions.quoteBridge(
            _destination=network_info[destination_network]['chains_id'],
            amount=amount).call()

        data = merkly_eth_bridge_contract.encodeABI(
            "bridgeETH",
            args=(network_info[destination_network]['chains_id'], amount)
        )

        tx = connect_network.auto_add_params(2, contracts_address_merkly_eth_bridge[network], data, value=amount + fee)

        signed_tx = connect_network.account.sign_transaction(tx)
        tx_hash = connect_network.w3.eth.send_raw_transaction(signed_tx.rawTransaction)

        print(f"Отправлено {connect_network.w3.from_wei(amount, 'ether')} ETH через {str(protocol).capitalize()}"
              f" из {str(network).capitalize()} в"
              f" {str(destination_network).capitalize()}."
              f"\nТранзакция отправлена с хэшем: {tx_hash.hex()}")
    else:
        if connect_network.w3.from_wei(amount, 'ether') < 0.0005:
            amount = connect_network.w3.to_wei(0.0005, 'ether')
        elif connect_network.w3.from_wei(amount, 'ether') > 0.005:
            amount = connect_network.w3.to_wei(0.005, 'ether')

        zeroway_refuel_contract = connect_network.w3.eth.contract(
            connect_network.w3.to_checksum_address(contracts_address_zeroway_refuel[network]),
            abi=abi_zeroway_refuel
        )

        fee = zeroway_refuel_contract.functions.calculateRefuelFee(connect_network.account.address, amount,
                                                                   network_info[destination_network]['chains_id']).call()

        data = zeroway_refuel_contract.encodeABI(
            "refuel",
            args=(connect_network.account.address, amount, network_info[destination_network]['chains_id'])
        )

        tx = connect_network.auto_add_params(2, contracts_address_zeroway_refuel[network], data, value=amount + fee)

        signed_tx = connect_network.account.sign_transaction(tx)
        tx_hash = connect_network.w3.eth.send_raw_transaction(signed_tx.rawTransaction)

        print(f"Отправлено {connect_network.w3.from_wei(amount, 'ether')} ETH через {str(protocol).capitalize()}"
              f" из {str(network).capitalize()} в"
              f" {str(destination_network).capitalize()}."
              f"\nТранзакция отправлена с хэшем: {tx_hash.hex()}")

    log_lst = [time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time())),
               connect_network.account.address,
               round(connect_network.w3.from_wei(amount, 'ether'), 5),
               str(protocol).capitalize(),
               str(network).capitalize(),
               str(destination_network).capitalize(),
               tx_hash.hex()]

    with open('log.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(log_lst)
    time.sleep(waiting_time)

