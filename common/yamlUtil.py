import os
import yaml

class   yamlUtil:
    #读取extract文件中的数据
    def read_extract_ymal(self,key):
        #with open 打开某文件
        # os.getcwd()+'./extract.yml'
        # 获得根目录下的某文件
        # mode ='r'读取文件
        # encoding 文件格式
        # as f 作为文件流
        with open(os.getcwd()+'/extract.yml',mode='r',encoding='UTF-8') as f:
            #yaml.load 加载文件
            #stream 文件流名称 loader 加载方式 ymal.FullLoader 加载所有
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    # 写入extract文件中的数据
    def write_extract_ymal(self,data):
        # with open 打开某文件
        # os.getcwd()+'./extract.yml'
        # 获得根目录下的某文件
        # mode ='r/w/a'读取文件 写入文件 追加文件
        # encoding 文件格式
        # as f 作为文件流
        with open(os.getcwd() + '/extract.yml', mode='w', encoding='UTF-8') as f:
            # yaml.load 读取和加载文件
            # stream 文件流名称 loader 加载方式 ymal.FullLoader 加载所有
            #传入数据   allow_unicode  允许使用unicode编码
            yaml.dump(data=data,stream=f,allow_unicode=True)
    # 删除extract文件中的数据
    def dele_extract_ymal(self):
        with open(os.getcwd() + '/extract.yml', mode='a', encoding='UTF-8') as f:
            f.truncate()


    def read_testcase_ymal(self,yaml_name):
        #with open 打开某文件
        # os.getcwd()+'./extract.yml'
        # 获得根目录下的某文件
        # mode ='r'读取文件
        # encoding 文件格式
        # as f 作为文件流
        with open(os.getcwd()+'\\'+yaml_name,mode='r',encoding='UTF-8') as f:
            #yaml.load 加载文件
            #stream 文件流名称 loader 加载方式 ymal.FullLoader 加载所有
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value
