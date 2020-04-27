from tornado.escape import json_encode

from base.http_client import client_api

from tornado import gen, ioloop


async def main():
    concurrency = 10
    data = {'esn': 'abc', "device_name": "abc", "device_type": 1, "status": 3, "interfaces": [
        {
            "interface_type": 1,
            "ip": "192.168.0.1"
        },
        {
            "interface_type": 1,
            "ip": "192.168.0.2"
        }]}

    async def worker():
        response = await client_api.post(url='resmgr/dev', body=json_encode(data))
        print(response.code)

    # Start workers, then wait for the work queue to be empty.
    workers = gen.multi([worker() for _ in range(concurrency)])

    # Signal all the workers to exit.
    await workers


if __name__ == "__main__":
    print(__name__)
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(main)
    ioloop.IOLoop.instance().start()


