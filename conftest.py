import pytest
from common.yamlUtil import yamlUtil

#作用域大全 package包 session一次请求 function函数 class类 moudle模块  以大方向来判定
@pytest.fixture(scope='function')
def conn_database():
    print("连接数据库")
    yield "12321"
    print("关闭数据库")
#autouse 自动执行
@pytest.fixture(scope='session',autouse=True)
def clear_yml():
    yamlUtil().dele_extract_ymal()