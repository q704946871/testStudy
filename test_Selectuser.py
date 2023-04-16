
import requests
import pytest
class TestSelectUser:
    #类变量，先设置为空

    identitytoken = ""
    headers = ""
    cookie = ""
    def test_GetSessoion(self):
        session = requests.session()
        return session
    #登录
    def test_Login(self):
        LoginUrl= "http://www.hunanbdc.com.cn:7377/Devops-Bpmx-Affairs/estate/login/validBack"
        Loginparams= {
            "account": "TGl1SmlhSGFv",
            "password": "RGFuZ2VyITE5OTYwNjAxMQ==",
            "isVerify": "true",
            "callbackURL": "",
            "clientSystemId": ""
        }
        res= self.test_GetSessoion().request("post", url=LoginUrl, params=Loginparams)
        TestSelectUser.cookie = res.cookies.values()
        print(TestSelectUser.cookie)
    def test_GetToken(self):
        # 第一步，先拿到登录时候获取到的token，用于后续查询
        TokenUrl = "http://www.hunanbdc.com.cn:7377/Devops-Bpmx-Affairs/devops/getToken"
        # lists = Login.res.cookies.items()
        # 这里是登录成功之后返回的cookie，把他添加到获取token的请求头里面去
        headers ={
            "JSESSIONID" : TestSelectUser.cookie
        }
        print(headers)
        GetToken= self.test_GetSessoion().request("get",url=TokenUrl,cookies = "JSESSIONID=NTI2ZmU5NmUtZDAwMi00MzIzLTlkYzctNTMxODZjNDQwNTYw")
        print("上一行是错误的地方")
        # json()['message'] 拿到josn键值对中 message 字段对应的数据
        TestSelectUser.identitytoken = GetToken.json()['message']
    #根据拿到的token去查数据
    def test_SendUser(self):
        SelectUrl = "http://222.240.168.20:90/devops/rest/root/query/ptsysuser_ext/listdata"
        SelectData = {
            "SYSTEM_ID_": 1,
            "ACCOUNT_": "",
            "USER_TYPE_": "",
            "DISTRICT_CODE_": "",
            "FULLNAME_": "刘家豪",
            "UKEY_ID_": "",
            "USER_FROM_": 1,
            "pageSize": 10,
            "pageNo": 1,
            "identitytoken": TestSelectUser.identitytoken
        }
        selectRes = self.test_GetSessoion().request("post",url=SelectUrl, data=SelectData)
        rs = re.search("state",selectRes.json())['state']
        print(rs)

    # def test_UploadFile(self):
    #     url = "http://www.hunanbdc.com.cn:7377/Devops-Bpmx-Affairs/system/file/fileUpload"
    #     data = {
    #         #  r   不转义
    #        # "file": open(r"C:\Users\Administrator\Pictures\Screenshots\屏幕截图.png","rb")
    #     }
    #     rep  = requests.post(url=url,files=data,headers=TestSelectUser.headers)
    #     print(rep.json())

if __name__ == '__main__':
    pytest.main(['-vs'])