
from huey_task.db_sync.device import Device
from huey_task.huey_config import huey
from huey_task.db_sync import sa


@huey.task()
def device_ok_callback(id):
    device = sa.query(Device).get(id)
    with sa.begin():
        device.id = id
        device.status = 1
    print('device %s is under control', id)

    return 'ok'
