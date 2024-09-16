import requests
import time
from datetime import datetime, timedelta

# Dirección de la tesorería de Bitcoin de El Salvador
address = "32ixEdVJWo3kmvJGMTZq5jAQVZZeuwnqzo"

# Función para obtener el balance on-chain
def get_on_chain_balance(address):
    try:
        url = f"https://mempool.space/api/address/{address}"
        response = requests.get(url)
        data = response.json()
        return data['chain_stats']['funded_txo_sum'] - data['chain_stats']['spent_txo_sum']
    except Exception as e:
        print(f"Error al obtener el balance on-chain: {e}")
        return None

# Función para obtener el balance en el mempool
def get_mempool_balance(address):
    try:
        url = f"https://mempool.space/api/address/{address}"
        response = requests.get(url)
        data = response.json()
        return data['mempool_stats']['funded_txo_sum'] - data['mempool_stats']['spent_txo_sum']
    except Exception as e:
        print(f"Error al obtener el balance mempool: {e}")
        return None

# Función para obtener la variación del balance en un periodo dado
def get_balance_variation(address, days):
    try:
        end_time = int(time.time())  # Timestamp actual
        start_time = end_time - days * 24 * 60 * 60  # Timestamp del inicio del periodo (30 o 7 días)
        url = f"https://mempool.space/api/address/{address}/txs/chain"
        response = requests.get(url)
        transactions = response.json()

        balance_start = 0
        
        # Calcular el balance al inicio del periodo (hace X días)
        for tx in transactions:
            if tx['status']['block_time'] <= start_time:
                balance_start += sum(output['value'] for output in tx['vout'] if output['scriptpubkey_address'] == address)
                balance_start -= sum(input['prevout']['value'] for input in tx['vin'] if input['prevout']['scriptpubkey_address'] == address)

        return balance_start
    except Exception as e:
        print(f"Error al obtener la variación de balance: {e}")
        return None

# Obtener los balances y variaciones
on_chain_balance = get_on_chain_balance(address)
mempool_balance = get_mempool_balance(address)
balance_start_30_days = get_balance_variation(address, 30)
balance_start_7_days = get_balance_variation(address, 7)

# Imprimir los resultados
print(f"Dirección de la tesorería de Bitcoin de El Salvador: 32ixEdVJWo3kmvJGMTZq5jAQVZZeuwnqzo ")

if on_chain_balance is not None:
    print(f"On-chain Balance: {on_chain_balance} SATS")

if mempool_balance is not None:
    print(f"Mempool Balance: {mempool_balance} SATS")

if balance_start_30_days is not None and on_chain_balance is not None:
    balance_variation_30_days = on_chain_balance - balance_start_30_days
    print(f"Balance variation in 30 days: {balance_variation_30_days} SATS")

if balance_start_7_days is not None and on_chain_balance is not None:
    balance_variation_7_days = on_chain_balance - balance_start_7_days
    print(f"Balance variation in 7 days: {balance_variation_7_days} SATS")
