# Test task
Original link to this repo: https://github.com/alekseik1/three-gen-test-task

## How to run

```bash
docker-compose up --build
```

Then go to `examples/` folder - there you'll find requests examples.

```bash
curl -X POST http://localhost:8080/order/
```

This will hang - it's okay.

In another shell:
```bash
curl -X GET http://localhost:8080/start/
```

It will return `order_id` after some time.
Run then:
```bash
curl -X POST -d '{"order_id": "e3e70682-c209-4cac-a29f-6fbed82c07cd"}' -H "Content-Type: application/json" http://localhost:8080/finish/
```

This uuid is reproducible.
