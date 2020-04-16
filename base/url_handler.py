from functools import wraps


class URLHandler:
    def __init__(self):
        self.urls = list()

    def __call__(self, url, method='GET', *args, **kwargs):
        def register(cls):
            self.urls.append((url, cls))
            return cls
        return register


handler = URLHandler()  # 创建路由表对象
