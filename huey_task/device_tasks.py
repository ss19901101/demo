from huey_task.huey_config import huey


@huey.task()
def device_ok_callback(id, name):
    print('device % s is under control, now id is %s', name, id)
    return 'ok'
