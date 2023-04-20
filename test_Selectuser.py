import json
import pytest
import requests,json
from common.yamlUtil import yamlUtil


class TestSelectUser:
    # 类变量，先设置为空
    session = requests.session()

    # 登录  caseinfo是自定义参数名字，getToken.yml是指定取值文件
    @pytest.mark.parametrize('caseinfo',yamlUtil().read_testcase_ymal('getToken.yml'))
    def test_login(self,caseinfo):
        LoginUrl = caseinfo['request']['url']
        Loginparams = caseinfo['request']['data']
        Loginmethod = caseinfo['request']['method']
        res = TestSelectUser.session.request(Loginmethod, url=LoginUrl, params=Loginparams)
        # if res.cookies is not None:
        #     print("JSESSIONID=" + res.cookies.values()[0])
        # else:
        #     print("异常用例，登录失败")
        #只管写入数据到对应文件中
        yamlUtil().write_extract_ymal({"Cookie":"JSESSIONID="+res.cookies.values()[0], "X-Requested-With": "XMLHttpRequest"})

    def test_gettoken(self):
        TokenUrl = "http://www.hunanbdc.com.cn:7377/Devops-Bpmx-Affairs/devops/getToken"
        # 这里是登录成功之后返回的cookie，把他添加到获取token的请求头里面去,取得上个方法中写入的数据
        headers = yamlUtil().read_extract_ymal('Cookie')
        # headers = {
        #     "Cookie": "JSESSIONID=OWNjOWI3OTQtMDJlYi00MDY4LTliNjUtM2NmZmQwOWU2NWNk"
        # }
        GetToken = TestSelectUser.session.request("get", url=TokenUrl, headers=headers)
        print(GetToken.json()['message'])
        # 拿到josn键值对中 message 字段对应的数据
        end = yamlUtil().write_extract_ymal({'identitytoken':GetToken.json()['message']})


    @pytest.mark.parametrize("select",yamlUtil().read_testcase_ymal('getcondition.yml'))
    def test_senduser(self, select):
        value = yamlUtil().read_extract_ymal('identitytoken')

        SelectUrl = select['request']['url']
        SelectData = select['request']['data']
        selectmethod =select['request']['method']
        selectRes = TestSelectUser.session.request(selectmethod, url=SelectUrl, data=SelectData ,headers=value)
        print(selectRes.json())




