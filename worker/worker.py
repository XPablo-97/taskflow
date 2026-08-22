import time
import requests

API_URL = "http://localhost:8000"
POLL_INTERVAL_SECONDS = 5


def fetch_pending_tasks():
    response = requests.get(f"{API_URL}/tasks")
    response.raise_for_status()
    tasks = response.json()
    return [t for t in tasks if t["status"] == "pending"]


def process_task(task):
    print(f"Procesando tarea {task['id']} ({task['title']})...")
    time.sleep(2)  # simula trabajo real (ej: generar un informe)
    response = requests.post(f"{API_URL}/tasks/{task['id']}/complete")
    response.raise_for_status()
    print(f"Tarea {task['id']} marcada como 'done'")


def main():
    print("Worker iniciado. Buscando tareas pendientes cada "
          f"{POLL_INTERVAL_SECONDS} segundos...")
    while True:
        pending = fetch_pending_tasks()
        if not pending:
            print("No hay tareas pendientes.")
        for task in pending:
            process_task(task)
        time.sleep(POLL_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
