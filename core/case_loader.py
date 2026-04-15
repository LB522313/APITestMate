import json
import os

class CaseLoader:
    @staticmethod
    def load_cases(file_path):
        """
        从 JSON 文件中加载测试用例
        :param file_path: 用例文件路径
        :return: 测试用例列表 (list of dict)
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Case file not found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                cases = json.load(f)
                if not isinstance(cases, list):
                    raise ValueError("JSON root must be an array of test cases.")
                return cases
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON format: {str(e)}")
