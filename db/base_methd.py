from tornado import gen

from db import POOL


@gen.coroutine
def query(query_str):
    print(123)
    cur = yield POOL.execute(query_str)
    temp_list = []
    for item in cur:
        temp_list.append(item)
    return temp_list


@gen.coroutine
def add(obj):
    fields = []
    params = []
    args = []
    for attr in dir(obj):
        if attr in obj.attribute_map:
            arg_temp = getattr(obj, attr)
            if (not isinstance(arg_temp, list) \
                    or not isinstance(arg_temp, object)) \
                    and arg_temp is not None:
                fields.append(attr)
                params.append('%s')
                args.append(arg_temp)
    sql = 'insert into %s (%s) values (%s)' % (
        obj.__class__.__name__.lower(), ','.join(fields), ','.join(params))
    print(sql)
    print(args)
    temp = yield POOL.execute(sql, args)
    return temp

def delete(str):
    pass


def update(str):
    pass
