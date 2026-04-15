# APITestMate

<div align="center">
  <p><strong>一个基于 Python 的轻量级接口自动化测试工具</strong></p>
  <p>
    <a href="https://github.com/LB522313/APITestMate"><img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Version"></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.7+-green.svg" alt="Python"></a>
    <a href="https://github.com/LB522313/APITestMate/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-orange.svg" alt="License"></a>
  </p>
</div>

---

## 📖 项目简介

**APITestMate** 是一个简单易用的接口自动化测试工具，专为快速验证 API 功能而设计。它支持从 JSON 文件读取测试用例，自动发送 GET/POST 请求，并对响应状态码和 JSON 字段进行断言。测试完成后，工具会自动生成美观的 HTML 测试报告，方便查看和分析测试结果。

此外，APITestMate 还支持 Docker 容器化运行，让你无需配置本地环境即可一键启动测试，极大地提升了部署和使用的便捷性。

## ✨ 功能特性

- ✅ **支持多种请求方法**：目前支持 GET 和 POST 请求，易于扩展其他 HTTP 方法。
- 📄 **JSON 用例管理**：使用简洁的 JSON 格式编写测试用例，易于阅读和维护。
- 🔍 **智能断言机制**：支持断言响应状态码（`expected_status`）和响应体中的 JSON 字段值（`expected_json`）。
- 📊 **HTML 测试报告**：基于 Jinja2 模板自动生成包含详细数据和统计信息的 HTML 报告。
- ⚙️ **灵活的命令行参数**：通过 `-c` 指定用例路径，`-r` 指定报告输出目录。
- 🐳 **Docker 容器化支持**：提供 Dockerfile，支持一键构建镜像并运行，实现环境隔离。
- 🏗️ **模块化架构设计**：代码结构清晰，分为 `core`（核心逻辑）、`config`（配置）等模块，便于二次开发和功能扩展。

## 📂 项目结构

```
APITestMate/
├── config/
│   ├── __init__.py
│   └── settings.py          # 全局配置（BASE_URL, TIMEOUT 等）
├── core/
│   ├── __init__.py
│   ├── http_client.py       # HTTP 请求客户端封装
│   ├── case_loader.py       # JSON 测试用例加载器
│   ├── assertor.py          # 响应断言处理器
│   └── reporter.py          # HTML 报告生成器
├── cases/
│   └── demo.json            # 示例测试用例文件
├── reports/                 # 自动生成的 HTML 报告存放目录
├── main.py                  # 程序主入口
├── requirements.txt         # Python 依赖列表
├── Dockerfile               # Docker 镜像构建文件
└── README.md                # 项目说明文档
```

## 🚀 快速开始

### 方式一：本地运行

1. **克隆项目**
   ```bash
   git clone https://github.com/LB522313/APITestMate.git
   cd APITestMate
   ```

2. **安装依赖**
   确保你的系统已安装 Python 3.7+，然后运行：
   ```bash
   pip install -r requirements.txt
   ```

3. **运行测试**
   ```bash
   python main.py -c cases/demo.json
   ```

4. **查看报告**
   测试结束后，在 `reports/` 目录下找到以时间戳命名的 `.html` 文件，用浏览器打开即可查看。

### 方式二：Docker 运行

如果你不想配置本地 Python 环境，可以使用 Docker 一键运行：

1. **构建镜像**
   ```bash
   docker build -t apitestmate .
   ```

2. **运行容器**
   ```bash
   # 挂载当前目录的 reports 文件夹，以便在宿主机查看报告
   docker run -v $(pwd)/reports:/app/reports apitestmate python main.py -c cases/demo.json
   ```

## 📝 编写测试用例

测试用例采用 JSON 数组格式。以下是一个典型的用例示例：

```json
{
  "case_id": "TC001",
  "case_name": "获取用户信息",
  "method": "GET",
  "url": "/users/1",
  "params": {},
  "json_data": null,
  "expected_status": 200,
  "expected_json": {
    "id": 1,
    "name": "Leanne Graham"
  }
}
```

### 字段说明

| 字段名 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| `case_id` | String | ✅ | 用例唯一标识符 |
| `case_name` | String | ✅ | 用例名称，用于报告展示 |
| `method` | String | ✅ | 请求方法，如 `GET`, `POST` |
| `url` | String | ✅ | 接口路径，会与 `settings.py` 中的 `BASE_URL` 拼接 |
| `params` | Object | ❌ | URL 查询参数（Query Params） |
| `json_data` | Object | ❌ | 请求体数据（JSON Body），通常用于 POST 请求 |
| `expected_status` | Integer | ✅ | 期望的 HTTP 状态码 |
| `expected_json` | Object | ❌ | 期望的响应 JSON 片段，用于校验关键字段 |

## ⚙️ 配置说明

你可以在 [`config/settings.py`](config/settings.py) 中修改全局配置：

- **`BASE_URL`**: 接口的基础地址。例如，如果你的测试环境是 `http://api.test.com`，请在此处修改。
- **`TIMEOUT`**: 请求超时时间（秒）。如果网络较慢，可以适当调大该值。

## 📊 测试报告说明

测试完成后，工具会在 `reports/` 目录下生成 HTML 报告。报告包含以下内容：

- **概览统计**：总用例数、通过数、失败数及通过率。
- **详细结果表**：展示每个用例的 ID、名称、请求方法、URL、状态码、耗时以及断言结果。
- **错误详情**：如果用例失败，会明确显示具体的错误原因（如状态码不匹配或字段值不一致）。

## 💡 高级用法

### 自定义命令行参数

你可以灵活指定不同的用例文件和报告目录：

```bash
# 指定特定的用例文件
python main.py -c cases/login_tests.json

# 指定报告输出到 custom_reports 目录
python main.py -c cases/demo.json -r custom_reports
```

### 扩展 HTTP 方法

目前的 `HttpClient` 已经支持所有 `requests` 库支持的方法。你只需在 JSON 用例中将 `method` 字段改为 `PUT`, `DELETE` 等即可直接使用。

## 🐳 Docker 镜像说明

项目根目录包含 `Dockerfile`，它基于官方 Python 镜像构建，预装了所有依赖。使用 Docker 运行可以确保在不同机器上获得完全一致的运行环境，非常适合集成到 CI/CD 流程中。

## 🔮 后续计划

- [ ] 支持更多的断言类型（如正则表达式匹配、响应时间断言）。
- [ ] 增加对 Excel (`.xlsx`) 格式用例的支持。
- [ ] 实现用例之间的依赖管理和数据传递（关联）。
- [ ] 增加并发执行功能，提升大规模测试的效率。

## 🤝 贡献指南

欢迎任何形式的贡献！如果你有好的想法或发现了 Bug，请提交 Issue 或 Pull Request。

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 📄 许可证

本项目采用 MIT 许可证。详情请参阅 [`LICENSE`](LICENSE) 文件。

## 📬 联系作者

如果你有任何问题或建议，欢迎通过以下方式联系：

- **GitHub**: [@LB522313](https://github.com/LB522313)
- **项目地址**: [https://github.com/LB522313/APITestMate](https://github.com/LB522313/APITestMate)

---

<p align="center">Made with ❤️ by LB522313</p>
