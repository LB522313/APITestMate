import os
import time
from jinja2 import Template
from config.settings import DEFAULT_REPORT_DIR

class Reporter:
    def __init__(self, report_dir=None):
        self.report_dir = report_dir or DEFAULT_REPORT_DIR
        os.makedirs(self.report_dir, exist_ok=True)
        self.results = []

    def add_result(self, case_id, case_name, method, url, status_code, duration, success, error_msg=""):
        self.results.append({
            "case_id": case_id,
            "case_name": case_name,
            "method": method,
            "url": url,
            "status_code": status_code,
            "duration": duration,
            "success": success,
            "error_msg": error_msg
        })

    def generate_html_report(self):
        """
        生成 HTML 测试报告
        :return: 报告文件的绝对路径
        """
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        report_filename = f"report_{timestamp}.html"
        report_path = os.path.join(self.report_dir, report_filename)

        total = len(self.results)
        passed = sum(1 for r in self.results if r['success'])
        failed = total - passed
        pass_rate = (passed / total * 100) if total > 0 else 0

        template_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>APITestMate Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        .summary { background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
        .summary p { margin: 5px 0; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .pass { color: green; font-weight: bold; }
        .fail { color: red; font-weight: bold; }
        .error-msg { color: #d9534f; font-size: 0.9em; }
    </style>
</head>
<body>
    <h1>APITestMate Test Report</h1>
    <div class="summary">
        <p><strong>Total Cases:</strong> {{ total }}</p>
        <p><strong>Passed:</strong> <span class="pass">{{ passed }}</span></p>
        <p><strong>Failed:</strong> <span class="fail">{{ failed }}</span></p>
        <p><strong>Pass Rate:</strong> {{ "%.2f"|format(pass_rate) }}%</p>
    </div>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Method</th>
                <th>URL</th>
                <th>Status Code</th>
                <th>Duration (s)</th>
                <th>Result</th>
                <th>Error Message</th>
            </tr>
        </thead>
        <tbody>
            {% for result in results %}
            <tr>
                <td>{{ result.case_id }}</td>
                <td>{{ result.case_name }}</td>
                <td>{{ result.method }}</td>
                <td>{{ result.url }}</td>
                <td>{{ result.status_code }}</td>
                <td>{{ "%.3f"|format(result.duration) }}</td>
                <td class="{{ 'pass' if result.success else 'fail' }}">{{ 'PASS' if result.success else 'FAIL' }}</td>
                <td class="error-msg">{{ result.error_msg if not result.success else '' }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
        """
        
        template = Template(template_str)
        html_content = template.render(
            total=total,
            passed=passed,
            failed=failed,
            pass_rate=pass_rate,
            results=self.results
        )

        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return report_path
