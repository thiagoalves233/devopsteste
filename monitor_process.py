import psutil
import time
import sys

def monitor_process(process_identifier):
    process = None

    # Verifica se o argumento é um ID de processo ou nome
    try:
        process_id = int(process_identifier)
        process = psutil.Process(process_id)
    except ValueError:
        # Se não for um ID, tenta encontrar o processo pelo nome
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == process_identifier:
                process = psutil.Process(proc.info['pid'])
                break

    if process is None:
        print(f"Processo '{process_identifier}' não encontrado.")
        return

    print(f"Monitorando processo: {process.name()} (PID: {process.pid})")
    
    try:
        while True:
            cpu_usage = process.cpu_percent(interval=1)
            memory_info = process.memory_info()
            memory_usage = memory_info.rss / (1024 * 1024)  # Convertendo para MB

            print(f"Uso de CPU: {cpu_usage}% | Uso de Memória: {memory_usage:.2f} MB")
            time.sleep(4)  # Espera 4 segundos (1 segundo para cpu_percent)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        print("O processo não está mais disponível.")
    except KeyboardInterrupt:
        print("\nMonitoramento interrompido.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python monitor_process.py <nome_ou_id_do_processo>")
        sys.exit(1)

    process_identifier = sys.argv[1]
    monitor_process(process_identifier)
