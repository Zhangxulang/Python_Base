# 作者: 大数据 浪哥
# 2025年07月14日02时16分01秒
# 1054074422@qq.com

class Tool(object):
    # 使用赋值语句，定义类属性，记录创建工具对象的总数，类似于类的全局变量
    count = 0

    def __init__(self, name):
        self.name = name
        # 针对类属性做一个计数+1
        Tool.count += 1

    @classmethod  # 类方法内部，可以直接使用 cls 访问 类属性 或者 调用类方法
    def show_tool_count(cls):
        """
        当你不使用对象属性，只使用类属性时，可以用类方法来实现。
        类方法的第一个参数永远是 cls，代表当前类。
        类方法可以访问和修改类属性。
        :return:
        """
        print(cls.count)

    @staticmethod  #静态方法
    def help():
        """
        静态方法不需要访问类属性或实例属性，可以直接调用。
        静态方法可以访问和修改全局变量。
        :return:
        """
        print("帮助信息:这是一个工具类，可以用来实例化各种工具对象。")


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")
# 知道使用 Tool 类到底创建了多少个对象?
print("现在创建了 %d 个工具" % Tool.count)
# 调用类方法
Tool.show_tool_count()
# 调用静态方法
Tool.help()
