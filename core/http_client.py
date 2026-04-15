import requests
from config.settings import BASE_URL, TIMEOUT

class HttpClient:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = BASE_URL
        self.timeout = TIMEOUT

    def send_request(self, method, url, params=None, json_data=None, headers=None):
        """
        发送 HTTP 请求
        :param method: GET, POST 等
        :param url: 接口路径，会与 base_url 拼接
        :param params: URL 参数 (dict)
        :param json_data: JSON 请求体 (dict)
        :param headers: 请求头 (dict)
        :return: requests.Response 对象
        """
        full_url = f"{self.base_url}{url}"
        
        # 默认设置 Content-Type 为 application/json
        if headers is None:
            headers = {}
        if 'Content-Type' not in headers and json_data:
            headers['Content-Type'] = 'application/json'

        try:
            response = self.session.request(
                method=method.upper(),
                url=full_url,
                params=params,
                json=json_data,
                headers=headers,
                timeout=self.timeout
            )
            return response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {str(e)}")
