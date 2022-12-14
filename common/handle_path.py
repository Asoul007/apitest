"""
====================================
@Author:Asoul
@Email:blink_wang@163.com
@FileName:handle_path.py
@DateTime:2022/9/5 9:43
@Code Description:
====================================
"""
import os

# 项目的根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试用例的目录路径
CASE_DIR = os.path.join(BASE_DIR,"test_case")

# 测试报告的目录路径
REPORT_DIR = os.path.join(BASE_DIR,"reports")

# 日志目录的项目路径
LOG_DIR = os.path.join(BASE_DIR,"logs")

# 用例数据的项目路径
DATA_DIR = os.path.join(BASE_DIR,"data")

# 配置文件目录的路径
CONF_DIR = os.path.join(BASE_DIR,"config")

