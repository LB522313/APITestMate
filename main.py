import argparse
import time
import sys
import os

# 将项目根目录添加到系统路径，确保可以导入 config 和 core
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config.settings import DEFAULT_CASE_FILE, DEFAULT_REPORT_DIR
from core.case_loader import CaseLoader
from core.http_client import HttpClient
from core.assertor import Assertor
from core.reporter import Reporter

def run_tests(case_file, report_dir):
    print(f"--- APITestMate Started ---")
    print(f"Loading cases from: {case_file}")
    
    # 1. 加载用例
    try:
        cases = CaseLoader.load_cases(case_file)
    except Exception as e:
        print(f"Error loading cases: {e}")
        return

    print(f"Found {len(cases)} test cases.")
    
    # 2. 初始化组件
    client = HttpClient()
    reporter = Reporter(report_dir=report_dir)
    
    # 3. 执行用例
    for case in cases:
        case_id = case.get("case_id", "UNKNOWN")
        case_name = case.get("case_name", "Unnamed Case")
        method = case.get("method", "GET")
        url = case.get("url", "/")
        params = case.get("params")
        json_data = case.get("json_data")
        expected_status = case.get("expected_status", 200)
        expected_json = case.get("expected_json")

        print(f"Running [{case_id}] {case_name}...", end=" ")
        
        start_time = time.time()
        try:
            # 发送请求
            response = client.send_request(method, url, params=params, json_data=json_data)
            duration = time.time() - start_time
            
            # 断言
            success, error_msg = Assertor.assert_response(response, expected_status, expected_json)
            
            # 记录结果
            reporter.add_result(
                case_id=case_id,
                case_name=case_name,
                method=method,
                url=url,
                status_code=response.status_code,
                duration=duration,
                success=success,
                error_msg=error_msg
            )
            
            if success:
                print("PASS")
            else:
                print(f"FAIL - {error_msg}")
                
        except Exception as e:
            duration = time.time() - start_time
            error_msg = str(e)
            print(f"ERROR - {error_msg}")
            reporter.add_result(
                case_id=case_id,
                case_name=case_name,
                method=method,
                url=url,
                status_code=0,
                duration=duration,
                success=False,
                error_msg=error_msg
            )

    # 4. 生成报告
    report_path = reporter.generate_html_report()
    print(f"\n--- APITestMate Finished ---")
    print(f"Report generated: {report_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="APITestMate - Simple API Automation Tool")
    parser.add_argument("-c", "--cases", type=str, default=DEFAULT_CASE_FILE, help="Path to the test case JSON file")
    parser.add_argument("-r", "--report-dir", type=str, default=DEFAULT_REPORT_DIR, help="Directory to save the HTML report")
    
    args = parser.parse_args()
    
    run_tests(args.cases, args.report_dir)
