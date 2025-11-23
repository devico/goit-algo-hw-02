from queue import Queue, Empty
from itertools import count

# Створити чергу заявок
queue = Queue()
_id_counter = count(1)


def generate_request():
    """Створити нову заявку та додати її до черги."""
    ticket = {"id": next(_id_counter)}
    queue.put(ticket)
    print(f"[NEW]   Додано заявку #{ticket['id']}")


def process_request():
    try:
        ticket = queue.get_nowait()
    except Empty:
        print("[INFO]  Черга пуста")
        return

    print(f"[PROC]  Обробка заявки #{ticket['id']}")


def main():
    print("Сервісний центр запущено. Натисніть Ctrl+C для виходу.\n")
    try:
        while True:
            generate_request()

            process_request()
    except KeyboardInterrupt:
        print("\nЗавершення роботи...")


if __name__ == "__main__":
    main()
