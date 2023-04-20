import os

import pytest

if __name__ == '__main__':
    pytest.main()
    #allure generate 生成allure报告，./temp 生成数据的json路径 ./report文件输出的目录  --clean 清除上一次数据
   # os.system('allure generate ./temp -o ./report --clean')
