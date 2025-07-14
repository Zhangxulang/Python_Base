# 作者: 大数据 浪哥
# 2025年07月14日03时05分49秒
# 1054074422@qq.com

# 单例模式（Singleton Pattern）是一种常用的软件设计模式。该模式的特点是某个类只能生成一个实例，该实例对于整个系统来说是单一的。当我们需要一个全局唯一的实例时，单例模式是最好的解决方案。
# 单例模式的优点：
# 1. 单例模式可以保证内存里只有一个实例，减少了内存的开销，尤其是频繁的创建和销毁实例。
# 2. 单例模式可以避免对资源的多重占用，保证了系统的稳定性。
# 3. 单例模式可以帮助我们全局控制某个类唯一的实例。
# #单例模式的实现：
# 我们可以通过多种方式实现单例模式，以下是两种常用的实现方式：
# 1. 饿汉模式（Eager Initialization）：在单例类被加载时，立即创建对象实例。这种方式在单例类被调用时，已经完成了实例化，所以这种方式的单例模式也被称为“懒汉模式”。
# 2. 懒汉模式（Lazy Initialization）：单例类在第一次被调用时，才创建对象实例。这种方式的单例模式也被称为“饿汉模式”。
# 下面以Python语言为例，来实现单例模式。
# 饿汉模式


# 通过重写 __new__ 方法来实现单例模式
class MusicPlayer(object):
    instance = None  # 用来保存单例类的实例

    # 1. 定义__new__方法，在对象实例化时，先判断是否存在实例，如果存在，则直接返回该实例，否则，创建实例并返回。
    def __new__(cls, *args, **kwargs):
        # 1. 创建对象时，new 方法会被自动调用
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        print("播放器初始化")
        self.name = name


if __name__ == '__main__':
    # 创建播放器对象
    player1 = MusicPlayer('七里香')
    player2 = MusicPlayer('红楼梦')
    print(id(player1))
    print(id(player2))
    print(player1.name)
    print(player2.name)
