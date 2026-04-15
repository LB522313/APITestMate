class Assertor:
    @staticmethod
    def assert_response(response, expected_status, expected_json=None):
        """
        断言响应结果
        :param response: requests.Response 对象
        :param expected_status: 期望的状态码 (int)
        :param expected_json: 期望的 JSON 数据片段 (dict)，用于校验响应体中的部分字段
        :return: (bool, str) -> (是否通过, 错误信息)
        """
        errors = []

        # 1. 断言状态码
        if response.status_code != expected_status:
            errors.append(f"Status code mismatch: expected {expected_status}, got {response.status_code}")

        # 2. 断言 JSON 内容
        if expected_json:
            try:
                actual_json = response.json()
                for key, value in expected_json.items():
                    if key not in actual_json:
                        errors.append(f"Key '{key}' not found in response JSON")
                    elif actual_json[key] != value:
                        errors.append(f"Value mismatch for key '{key}': expected {value}, got {actual_json[key]}")
            except ValueError:
                errors.append("Response is not valid JSON, but expected_json was provided")

        if errors:
            return False, "; ".join(errors)
        return True, "Pass"
