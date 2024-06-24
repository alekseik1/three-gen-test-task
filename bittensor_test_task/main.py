from threading import Thread

import uvicorn

from bittensor_test_task.app import barista_app, client_app


def start_client_server():
    uvicorn.run(client_app, host="0.0.0.0", port=8000)


def start_barista_server():
    uvicorn.run(barista_app, host="0.0.0.0", port=8001)


if __name__ == "__main__":
    client_thread = Thread(target=start_client_server)
    barista_thread = Thread(target=start_barista_server)

    client_thread.start()
    barista_thread.start()

    client_thread.join()
    barista_thread.join()
