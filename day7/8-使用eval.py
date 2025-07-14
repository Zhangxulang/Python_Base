# 作者: 大数据 浪哥
# 2025年07月15日03时17分44秒
# 1054074422@qq.com

#eval专门处理配置文件
def eval_demo():
    # 基本的数学计算
    print(eval("1 + 1"))  # 2
    # 字符串重复
    print(eval("'*' * 10"))  #    '**********'
    # 将字符串转换成列表
    print(type(eval("[1, 2, 3, 4, 5]")))  # list
    # 将字符串转换成字典
    print(type(eval("{'name': 'xiaoming', 'age': 18}")))  # dict


def read_config_file():
    with open('confg', 'r+', encoding='utf-8') as f:
        content = f.read()
        print(content)
        print(type(content))
        # 这里使用eval函数处理配置文件
        print('-'*50)
        my_dict = eval(content)
        print(my_dict)
        print(type(my_dict))
        # 这里可以对my_dict进行操作
        # 保存修改后的配置文件
        f.close()



def get_server_config(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        config = eval(f.read())
        f.close()

    ip = config["server_ip"]
    port = config["server_port"]
    print(f"服务器 IP：{ip}")
    print(f"服务器端口：{port}")

if __name__ == '__main__':
    #eval_demo()
    #read_config_file()
     get_server_config('confg')

