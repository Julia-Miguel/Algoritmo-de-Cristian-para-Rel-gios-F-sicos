import ntplib
from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

def get_ntp_time():
    """Obtém o horário atualizado via NTP."""
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')
        return response.tx_time
    except Exception as e:
        print(f"Erro ao obter NTP: {e}")
        return time.time()  # Fallback para horário local

@app.route('/time', methods=['GET'])
def get_time():
    """Retorna o horário NTP com atraso simulado."""
    time.sleep(random.uniform(0.1, 0.5))  # Simula atraso de rede
    current_time = get_ntp_time()
    print(f"Servidor retornando horário: {current_time:.2f}")
    return jsonify({'time': current_time})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)