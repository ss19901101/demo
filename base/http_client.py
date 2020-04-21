from tornado.httpclient import AsyncHTTPClient, HTTPRequest



class HTTPClient:
    def __init__(self, base_prefix):
        """

        :type base_prefix: str
        """
        self._base_prefix = None
        if base_prefix is not None:
            self._base_prefix = base_prefix

    @property
    def base_prefix(self):
        return self._base_prefix

    @base_prefix.setter
    def base_prefix(self, base_prefix):
        self._base_prefix = base_prefix

    def get(self, url='', params=None):
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
        return self.http(url=url)

    def post(self, url='', body=''):
        """

        :param url:
        :param body:
        :return: HTTPResponse
        """
        return self.http(url=url, method='POST', body=body)

    async def http(self, url='', method='GET', body=None):
        """

        :param url:
        :param method:
        :param body:
        :return: HTTPResponse
        """
        http_client = AsyncHTTPClient()
        request = HTTPRequest(url=self._base_prefix + url, method=method, body=body)
        return await http_client.fetch(request)


client_controller = HTTPClient('http://localhost:8081/')
client_api = HTTPClient('http://localhost:8080/')
