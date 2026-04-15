# APITestMate - 轻量级接口自动化测试工具

APITestMate 是一个基于 Python 的接口自动化测试小工具，支持读取 JSON 用例文件，自动发送 HTTP 请求，断言响应状态码和 JSON 字段，并生成精美的 HTML 测试报告。同时提供 Docker 镜像，实现一键运行，无需安装 Python 环境。

## ✨ 功能特性

- ✅ 支持 **GET / POST** 请求（可轻松扩展 PUT / DELETE）
- ✅ 用例管理：**JSON 格式** 用例文件，结构清晰
- ✅ 断言功能：**状态码断言** + **JSON 字段断言**（支持嵌套字段，如 `user.name`）
- ✅ **自动生成 HTML 测试报告**（带时间戳，包含统计图表和详细失败信息）
- ✅ **命令行参数**：灵活指定用例文件 (`-c`) 和报告输出目录 (`-r`)
- ✅ **Docker 容器化**：一键运行，环境隔离，开箱即用
- ✅ 模块化设计：请求客户端、用例加载器、断言库、报告生成器分离，易于扩展

## 📁 项目结构
APITestMate/
├── core/ # 核心模块
│ ├── http_client.py # 发送 HTTP 请求（GET / POST）
│ ├── case_loader.py # 加载 JSON 用例文件
│ ├── assertor.py # 断言逻辑（状态码、JSON字段）
│ └── reporter.py # 生成 HTML 报告（基于 Jinja2）
├── config/
│ └── settings.py # 全局配置（BASE_URL, TIMEOUT）
├── cases/ # 存放测试用例 JSON 文件
│ └── demo.json # 示例用例（JSONPlaceholder）
├── reports/ # 测试报告输出目录（自动创建）
├── main.py # 程序入口
├── requirements.txt # Python 依赖
├── Dockerfile # Docker 镜像构建文件
└── README.md

text

## 🚀 快速开始

### 方式一：本地运行（需要 Python 3.8+）

1. 克隆项目
   ```bash
   git clone https://github.com/LB522313/APITestMate.git
   cd APITestMate
安装依赖

bash
pip install -r requirements.txt
运行测试（使用示例用例）

bash
python main.py -c cases/demo.json
查看报告
打开 reports/ 目录下最新生成的 report_时间戳.html 文件。

方式二：Docker 运行（无需本地 Python 环境）
构建镜像

bash
docker build -t apitestmate .
运行测试并挂载报告目录

bash
docker run --rm -v "$(pwd)/reports:/app/reports" apitestmate -c cases/demo.json
查看报告
同样在本地 reports/ 文件夹中找到 HTML 报告。

📝 编写测试用例
在 cases/ 目录下创建 .json 文件，格式如下：

json
[
    {
        "name": "获取用户信息",
        "method": "GET",
        "url": "/users/1",
        "expected_status": 200,
        "expected_json": {"id": 1, "name": "Leanne Graham"}
    },
    {
        "name": "创建新文章",
        "method": "POST",
        "url": "/posts",
        "request_body": {
            "title": "foo",
            "body": "bar",
            "userId": 1
        },
        "expected_status": 201,
        "expected_json": {"title": "foo"}
    }
]
字段说明
字段	类型	必填	说明
name	string	是	用例名称（显示在报告中）
method	string	是	请求方法（GET / POST）
url	string	是	接口路径（与 BASE_URL 拼接）
request_body	object	否	POST 请求的 JSON Body
expected_status	int	是	期望的 HTTP 状态码
expected_json	object	否	期望响应中包含的 JSON 字段（支持点号嵌套，如 user.name）
⚙️ 配置
修改 config/settings.py 可以调整全局参数：

python
BASE_URL = "https://jsonplaceholder.typicode.com"   # 被测接口基础地址
TIMEOUT = 10                                        # 请求超时时间（秒）
📊 测试报告
执行完成后，会在 reports/ 目录生成类似 report_20250415_143022.html 的报告文件。报告包含：

执行时间戳

总计用例数、通过数、失败数

每条用例的名称、状态（PASS/FAIL）、错误信息

你可以运行一次测试后，用浏览器打开报告截图，然后替换下面的占位图片。

https://via.placeholder.com/800x400?text=HTML+Report+Screenshot

🔧 高级用法
命令行参数
bash
python main.py -c <用例文件路径> [-r <报告输出目录>]
-c / --case：必需，指定 JSON 用例文件。

-r / --report-dir：可选，指定报告输出目录（默认为 reports）。

示例：

bash
python main.py -c cases/my_test.json -r my_reports
扩展更多 HTTP 方法
你可以在 core/http_client.py 中轻松添加 put、delete 等方法，并在 main.py 中增加对应的分支即可。

🐳 Docker 镜像
基础镜像：python:3.9-slim

镜像大小：约 200MB

运行入口：python main.py

你可以自行构建，也可以将镜像推送到 Docker Hub（可选）。

🗺️ 后续计划
支持 Excel 用例文件（数据驱动）

支持变量传递（如登录 token 关联）

集成 Pytest + Allure（更强大的测试框架和报告）

并发执行用例，提升效率

🤝 贡献
欢迎提交 Issue 和 Pull Request，共同完善这个项目。

📄 许可证
MIT License

📬 联系
作者：刘斌（LB522313）
GitHub：LB522313
项目地址：https://github.com/LB522313/APITestMate