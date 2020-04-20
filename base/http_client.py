from tornado.httpclient import AsyncHTTPClient, HTTPRequest

BASE_PREFIX = 'http://localhost:8081/'


def get(url='', params=None):
    """

    :type url: str
    :type params: object
    """
    if params is None:
        params = {}
    query_str = '?'
    for key in params:
        query_str += key + '=' + str(params[key]) + '&'
    url = url + query_str[0:-1]
    return http(url=url)


def post(url='', body=''):
    """

    :param url:
    :param body:
    :return: HTTPResponse
    """
    return http(url=url, method='POST', body=body)


async def http(url='', method='GET', body=None):
    """

    :param url:
    :param method:
    :param body:
    :return: HTTPResponse
    """
    http_client = AsyncHTTPClient()
    request = HTTPRequest(url=BASE_PREFIX + url, method=method, body=body)
    return await http_client.fetch(request)
