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
    """

    :param obj: object
    :return obj: object

    this method is a simple orm method for saving a object to the database
    and returns the object with an auto-generated id
    """
    fields = []
    params = []
    args = []
    for attr in dir(obj):
        if attr in obj.attribute_map:
            arg_temp = getattr(obj, attr)
            if (not isinstance(arg_temp, list) or not isinstance(arg_temp, object)) \
                    and arg_temp is not None:
                fields.append(attr)
                params.append('%s')
                args.append(arg_temp)
    sql = 'insert into %s (%s) values (%s)' % (
        obj.__class__.__name__.lower(), ','.join(fields), ','.join(params))
    cursor = yield execute_sql(sql, args)
    obj_id = cursor.lastrowid
    return obj_id


@gen.coroutine
def execute_sql(sql, args):
    cursor = yield POOL.execute(sql, args)
    return cursor


@gen.coroutine
def soft_delete(obj):
    sql = 'update %s set deleted=1 where id = %s' % (
        obj.__class__.__name__.lower(), obj.id
    )
    yield POOL.execute(sql)


@gen.coroutine
def update(obj):
    fields = []
    args = []
    for attr in dir(obj):
        if attr in obj.attribute_map:
            arg_temp = getattr(obj, attr)
            if (not isinstance(arg_temp, list) or not isinstance(arg_temp, object)) \
                    and arg_temp is not None and attr is not 'id':
                attr = str(attr) + '= %s'
                fields.append(attr)
                args.append(arg_temp)
    sql = 'update %s set %s where id = %s' % (
        obj.__class__.__name__.lower(), ','.join(fields), obj.id)
    yield POOL.execute(sql, args)
