# 作者: 大数据 浪哥
# 2025年08月10日14时12分55秒
# 1054074422@qq.com

# 不可变数据类型：int、float、bool、str、tuple、frozenset
# 可变数据类型：list、dict、set

# 不可变数据类型：
# int、float、bool、str、tuple、frozenset
# 这些数据类型的值一旦创建，其值就不能改变。

# 可变数据类型：
# list、dict、set
# 这些数据类型的值可以改变，可以增删改查。

# 以下是不可变数据类型示例：
def test_immutable_data_type():
    # int
    a = 10
    b = a
    a = 20
    print(b)  # 仍然 10

    # float
    a = 3.14
    b = a
    a = 2.71
    print(b)  # 仍然 3.14

    # bool
    a = True
    b = a
    a = False
    print(b)  # 仍然 True

    # str
    a = "hello"
    b = a
    a = "world"
    print(b)  # 仍然 "hello"

    # tuple
    a = (1, 2, 3)
    a = 10
    b = a
    a = 20
    print(b)  # 仍然 10


def test_mutable_data_type():  # 原地修改会影响所有引用
    L = [1, 2]
    M = L
    L.append(3)
    print(M)  # [1, 2, 3] —— M 和 L 指向同一个对象

    t = (1, [2, 3])
    t[1].append(4)
    print(t)  # (1, [2, 3, 4]) —— tuple 的容器结构不可变，但内部的 list 是可变的

    d = {}
    d[(1, 2)] = "ok"  # works
    try:
        d[[1, 2]] = "no"  # TypeError: unhashable type: 'list'
    except TypeError as e:
        print("error:", e)

    b = b'abc'  # bytes, 不可变  ，b'abc'前面的b表示是bytes类型，后面跟的'abc'是字符串
    ba = bytearray(b'abc')  # bytearray, 可变
    ba[0] = ord('z')  # 修改字节
    print(ba)  # bytearray(b'zbc')

    mv_readonly = memoryview(b'abc')  # 底层不可写（bytes），通常可哈希
    mv_writable = memoryview(bytearray(b'abc'))  # 底层可写，不可哈希
    import hashlib
    print(hash(mv_readonly))
    try:
        print(hash(mv_writable))
    except Exception as e:
        print("writable memoryview not hashable:", e)


def add(x, lst=[]):
    lst.append(x)
    return lst


# 正确写法：
def add_fixed(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst


# 深拷贝和浅拷贝：
def test_copy():
    import copy
    orig = [[1]]  #支持嵌套列表
    sh = copy.copy(orig)
    deep = copy.deepcopy(orig)
    orig[0].append(2)
    print("orig:", orig)  # [[1, 2]]
    print("sh:", sh)  # [[1, 2]]  —— 浅拷贝共享内部列表
    print("deep:", deep)  # [[1]]     —— 深拷贝独立，新对象


if __name__ == '__main__':
    # test_immutable_data_type()
    # test_mutable_data_type()
    # print(add(1))  # [1]
    # print(add(2))  # [1, 2] —— 非预期，lst 被共享
    # print(add_fixed(1,[]))
    # print(add_fixed(2,[1,3,5]))
    test_copy()
