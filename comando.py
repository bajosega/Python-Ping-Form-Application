import time
import statistics
import matplotlib.pyplot as plt
from ping3 import ping, verbose_ping

def ping_ip(ip, duration):
    timestamps = []
    rtt_times = []
    
    start_time = time.time()
    end_time = start_time + duration
    
    while time.time() < end_time:
        timestamp = time.time() - start_time
        rtt = ping(ip)
        
        if rtt is not None:
            timestamps.append(timestamp)
            rtt_times.append(rtt)
        
        time.sleep(1)  # Esperar 1 segundo antes de cada ping
        
    return timestamps, rtt_times

def plot_statistics(timestamps, rtt_times):
    fig, ax = plt.subplots()
    ax.plot(timestamps, rtt_times)
    ax.set(xlabel='Tiempo (s)', ylabel='RTT (ms)', title='Estadísticas de Ping')
    ax.grid()
    plt.show()

if __name__ == '__main__':
    ip_address = 'jb'  # Reemplaza con la dirección IP a la que deseas hacer ping
    duration = 60  # Duración del período de tiempo en segundos
    
    timestamps, rtt_times = ping_ip(ip_address, duration)
    plot_statistics(timestamps, rtt_times)
