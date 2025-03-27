import time
import requests
import random
import sys

SERVER_URL = 'http://server:5000/time'

def get_server_time(max_retries=3):
    """Obtém o horário do servidor e calcula o RTT com retentativas."""
    for attempt in range(max_retries):
        try:
            start_time = time.time()
            response = requests.get(SERVER_URL, timeout=5)
            end_time = time.time()
            server_time = response.json()['time']
            rtt = end_time - start_time
            estimated_time = server_time + (rtt / 2)  # Ajuste pelo RTT
            return estimated_time, rtt
        except requests.RequestException as e:
            print(f"Tentativa {attempt + 1}/{max_retries} falhou: {e}")
            time.sleep(2)  # Espera antes de tentar novamente
    print("Falha ao sincronizar após várias tentativas. Usando horário local.")
    return time.time(), 0

def adjust_clock(current_time, target_time):
    """Ajusta o relógio local gradualmente em passos de 0.1s."""
    step = 0.1
    while abs(current_time - target_time) > step:
        if current_time < target_time:
            current_time += step
        else:
            current_time -= step
        print(f"Ajustando relógio para: {current_time:.2f}")
        time.sleep(0.1)  # Simula ajuste gradual
    return target_time

if __name__ == '__main__':
    # Offset inicial configurável via argumento ou aleatório
    if len(sys.argv) > 1:
        offset = float(sys.argv[1])
    else:
        offset = random.uniform(-10, 10)
    
    local_time = time.time() + offset
    print(f"Horário local inicial: {local_time:.2f} (offset: {offset:.2f}s)")
    
    while True:
        print(f"\nHorário local antes da sincronização: {local_time:.2f}")
        estimated_time, rtt = get_server_time()
        print(f"RTT: {rtt:.2f}s, Hora estimada do servidor: {estimated_time:.2f}")
        local_time = adjust_clock(local_time, estimated_time)
        print(f"Horário local após sincronização: {local_time:.2f}")
        time.sleep(10)  # Sincroniza a cada 10 segundos