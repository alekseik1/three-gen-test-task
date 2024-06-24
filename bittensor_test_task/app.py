import random
from queue import Queue
from time import sleep
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

client_app = FastAPI()
barista_app = FastAPI()

order_queue = Queue()
finished_orders = set()


class Order(BaseModel):
    order_id: UUID


# To handle the delusional DDoSer
client_ip_counts = {}

MAX_REQUESTS_PER_IP = 100


@client_app.middleware("http")
async def limit_ip_requests(request, call_next):
    client_ip = request.client.host
    if client_ip not in client_ip_counts:
        client_ip_counts[client_ip] = 0
    client_ip_counts[client_ip] += 1

    if client_ip_counts[client_ip] > MAX_REQUESTS_PER_IP:
        raise HTTPException(status_code=429, detail="Too many requests")

    response = await call_next(request)
    return response


@client_app.post("/order/")
async def make_order():
    order = Order(order_id=uuid4())
    order_queue.put(order)
    while order.order_id not in finished_orders:
        sleep(1)
    finished_orders.remove(order.order_id)
    return {"status": "Your americano is ready!"}


@barista_app.get("/start/")
async def start():
    if order_queue.empty():
        raise HTTPException(status_code=404, detail="No orders available")
    order = order_queue.get()
    sleep(random.randint(30, 60))
    return {"client_id": order.order_id}


@barista_app.post("/finish/")
async def finish(order: Order):
    finished_orders.add(order.order_id)
    return {"status": "Order completed"}
