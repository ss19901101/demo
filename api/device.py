from typing import Optional, Awaitable

from tornado import gen
from tornado.escape import json_decode, json_encode

from base.http_client import client_controller
from base.url_handler import route, RequestHandler
from huey_task.device_tasks import device_ok_callback
from model.device import Device
from model.interface import Interface
from rabbitmq import example_publisher


@route('/resmgr/dev')
class DeviceAPI(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    @gen.coroutine
    def get(self):
        message = {
            'id':self.get_argument(name='id')
        }
        example_publisher.publish_message(message)
        device_ok_callback(self.get_argument(name='id'))

    @gen.coroutine
    def post(self):
        device = Device()
        # 数据初始化及插入
        data = json_decode(self.request.body)
        for i in data:
            if i == 'interfaces':
                interfaces_list = []
                for item in data['interfaces']:
                    interface = Interface()
                    for k in item:
                        setattr(interface, k, item[k])
                    interfaces_list.append(interface)
                data[i] = interfaces_list
            setattr(device, i, data[i])
        yield device.save()
        for interface in device.interfaces:
            interface.device_id = device.id
            yield interface.save()
            print(interface.id)
        # 向Mock服务器请求数据
        data = json_decode(self.request.body)
        data['id'] = device.id
        response = yield client_controller.post(url='mock', body=json_encode(data))
        if response.code == 200:
            self.finish('OK')
