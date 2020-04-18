from __future__ import print_function

from tornado_mysql import pools
from tornado_mysql.cursors import DictCursor

pools.DEBUG = True

POOL = pools.Pool(
    dict(host='127.0.0.1', port=3306, user='root', passwd='19901101',
         db='demo', cursorclass=DictCursor),
    max_idle_connections=2,
    max_recycle_sec=3,
    max_open_connections=5,
)
