import requests
class TestSelectUser:
    session = requests.session()

    def test_Login(self):
        LoginUrl = "http://222.240.168.20:90/devops/rest/bpmx/auth/login"
        Loginparams = {
            "account": "cGVuZ3hpb25n",
            "password": "U1RiZGMyMDIwLg==",
            "identifyCode": "",
            "isSlideCheck": "",
            "loginMethod": "0"
        }
        res = TestSelectUser.session.request("post", url=LoginUrl, params=Loginparams)
        a =bytes.decode(res.content)
        list(a)
        print(a)

        return TestSelectUser
