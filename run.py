import os
import time

import pytest

if __name__ == '__main__':

    # pytest.main(['-vs','./testcase/visca_test.py::Test_visca::test_Color_Temperature'])
    pytest.main(['-vs','./testcase/visca_test.py'])
    time.sleep(3)#生成临时报告的时间
    os.system('allure generate ./allure-results -o ./allure-report --clean')#生成正式报告