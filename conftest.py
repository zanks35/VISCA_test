# 读取数据方法
import pytest


def read_yaml():
    return ['chenglong','zengzidan','cai']
@pytest.fixture(scope="function",autouse=False,params=read_yaml(),ids=['c','z','cai'],name='db')

def exe_database_sql(request):

    print("之前执行sql查询")
    # print(request.param)
    yield request.param
    # time.sleep(10)
    print("000之后执行000")

@pytest.fixture(scope="session",autouse=False,name='all')
def all_exe(request):
    print("之前执行sql查询")
    # print(request.param)
    yield request.param
    # time.sleep(10)
    print("000之后执行000")