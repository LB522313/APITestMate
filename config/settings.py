import os

# 基础 URL，所有用例的请求都会拼接在这个 URL 后面
BASE_URL = "https://jsonplaceholder.typicode.com"


# 默认请求超时时间（秒）
TIMEOUT = 10

# 项目根目录
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 默认报告目录
DEFAULT_REPORT_DIR = os.path.join(PROJECT_ROOT, "reports")

# 默认用例文件路径
DEFAULT_CASE_FILE = os.path.join(PROJECT_ROOT, "cases", "demo.json")
