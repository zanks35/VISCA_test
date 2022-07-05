import os
import time

import pytest

if __name__ == '__main__':


    pytest.main(['-vs','--alluredir', './temp','./testcase/visca_test.py::Test_visca::test_power'])
    time.sleep(3)#生成临时报告的时间
    os.system('allure generate ./temp -o ./allure-report --clean')#生成正式报告