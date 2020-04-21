from huey.contrib.djhuey import RedisHuey

huey = RedisHuey(
    name='huey_demo',
    host='127.0.0.1',
    port='6379',
    db=10,
    result_store=False,
)