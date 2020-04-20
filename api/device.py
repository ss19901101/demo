import json
from typing import Optional, Awaitable

from tornado import gen
from tornado.escape import json_decode, json_encode
from tornado.httpclient import AsyncHTTPClient, HTTPRequest

from base.http_client import post, get
from constant import DeviceStatus
from db import base_methd
from base.url_handler import route, RequestHandler
from model.device import Device
from model.interface import Interface


@route('/resmgr/dev')
class DeviceAPI(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    @gen.coroutine
    def get(self):
        result = yield base_methd.query('select * from device')
        result = json.dumps(result)
        self.write(result)

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
        self.finish('OK')
        data['id'] = device.id
        response = yield post(url='mock', body=json_encode(data))
        print(response.code)
        if response.code != 200:
            return
        for i in range(10):
            response = yield get(url='mock', params={'id': device.id})
            print('retry count %d', i)
            if str(response.body, encoding='utf-8') == 'ACTIVE':
                device.status = DeviceStatus.ACTIVE.value
                yield base_methd.update(device)
                break
            else:
                yield from gen.sleep(10)
