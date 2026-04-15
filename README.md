# APITestMate

一个简单轻量的 Python 接口自动化测试工具。

## 功能特点
- 从 JSON 文件加载测试用例
- 支持 GET 和 POST 请求
- 断言响应状态码和 JSON 响应体字段
- 使用 Jinja2 生成 HTML 测试报告
- 可配置的基础 URL 和超时时间

## 项目结构
```
APITestMate/
├── config/
│   ├── __init__.py
│   └── settings.py      # 配置文件，包含基础 URL 等
├── core/
│   ├── __init__.py
│   ├── http_client.py   # HTTP 请求处理
│   ├── case_loader.py   # 加载 JSON 测试用例
│   ├── assertor.py      # 断言处理
│   └── reporter.py      # 生成 HTML 报告
├── cases/
│   └── demo.json        # 示例测试用例
├── reports/             # 生成的报告会保存在这里
├── main.py              # 程序入口
├── requirements.txt     # Python 依赖
└── README.md
```

## 安装步骤
1. 确保已安装 Python 3.7+
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法
在项目根目录下运行以下命令：

```bash
python main.py -c cases/demo.json
```

### 命令行参数
- `-c`, `--cases`: 测试用例 JSON 文件路径（默认：`cases/demo.json`）
- `-r`, `--report-dir`: HTML 报告保存目录（默认：`reports`）

## 测试用例示例
查看 `cases/demo.json` 了解 GET 和 POST 请求的断言示例。
