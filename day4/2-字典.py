# 作者: 大数据 浪哥
# 2025年07月11日10时51分02秒
# 1054074422@qq.com

# 字典是一种可变容器，它以键值对的形式存储数据。
# 字典的特点：
# 1. 字典是无序的，即键值对之间没有顺序关系。
# 2. 字典中的键必须是不可变对象，如字符串、数字、元组。
# 3. 字典中的值可以是任意对象。
# 4. 字典中的键值对是通过冒号分隔，键和值用逗号分隔。
# 5. 字典中的键值对用大括号{}包裹，键值对之间用逗号分隔。
# 6. 字典中的键值对可以动态添加、删除。
# 7. 字典中的键值对可以通过键来访问对应的值。
# 8. 字典中的键值对可以通过索引来访问对应的值。
# 9. 字典中的键值对可以通过items()方法来遍历。
# 10. 字典中的键值对可以通过keys()方法来获取所有的键，values()方法来获取所有的值。
#11. 字典是用hash表实现的，查找、插入、删除的时间复杂度都是O(1)。
#12. 红黑树是字典的底层实现。（java中HashMap底层实现是哈希表，TreeMap底层实现是红黑树） 、C++中std::map底层实现也是红黑树。

def use_dict_base():
    """
    字典的基本操作
    :return:
    """
    xiaoming_dict = {"name": "小明"}
    # 1. 取值
    print(xiaoming_dict["name"])
    #print(id(xiaoming_dict))
    print("-"*50)


    # 2. 增加/修改
    # 如果 key 不存在，会新增键值对
    xiaoming_dict["age"] = 18
    # 如果 key 存在，会修改已经存在的键值对
    print(xiaoming_dict)
    print("-"*50)
    xiaoming_dict["name"] = "小小明"
    print(xiaoming_dict)
    #print(id(xiaoming_dict))
    print("-"*50)


    # 3. 删除
    #方法一
    #print(xiaoming_dict.pop("name"))#移除指定键并返回对应的值。如果未找到该键，则返回默认值（如果已提供）；否则，抛出 KeyError
    # 在删除指定键值对的时候，如果指定的 key 不存在，程序会报错！
    #xiaoming_dict.pop("name123")

    #方法二
    del xiaoming_dict["name"]#无返回值
    print(xiaoming_dict)


    # 4. 统计键值对数量
    print(len(xiaoming_dict))


    # 5. 合并字典
    temp_dict = {"height": 1.75,
    "age": 20}
    # 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
    xiaoming_dict.update(temp_dict)
    print(xiaoming_dict)

    print("-"*50)
    # 6. 清空字典
    xiaoming_dict.clear()
    print(xiaoming_dict)
    print(id(xiaoming_dict))

def use_dict_iter():
    """
    字典遍历
    :return:
    """
    xiaoming_dict = {"name": "小明",
    "qq": "123456",
    "phone": "10086"}
    # 迭代遍历字典
    # 方法一：使用items()方法
    for k,v in xiaoming_dict.items():
        #print(f"键:{k}  值:{v}")
        print(k,v)

    print("-" * 50)
    # 方法二：使用keys()方法
    for k in xiaoming_dict.keys():
        print(k,xiaoming_dict[k])
    print("-" * 50)

    # 方法三：使用values()方法
    for v in xiaoming_dict.values():
        print(v)

    print("-" * 50)
    # 方法四：使用for循环遍历字典
    # 遍历字典时，只遍历键，不遍历值
    for k in xiaoming_dict:
        print(k,xiaoming_dict[k])
        #print("%s - %s" % (k, xiaoming_dict[k]))

def use_list_dict():
    """
    列表和字典的嵌套使用
    :return:
    """
    # 列表中存储字典
    xiaoming_list = [
        {"name": "小明", "age": 18},
        {"name": "小红", "age": 19},
        {"name": "小刚", "age": 20}
    ]
    # 遍历列表
    for item in xiaoming_list:
        print(item)

    print("-" * 50)
    # 字典中存储列表
    xiaoming_dict = {
        "students": xiaoming_list,
        "age": 25
    }
    # 遍历字典
    for k,v in xiaoming_dict.items():
        print(k,v)
        if k == "students":
            # 遍历列表
            for item in v:
                print(item)

def use_unpack_packet():
    """
    字典的拆包操作
    :return:
    """
    xiaoming_dict = {"name": "小明", "age": 18}
    # 1. 解包
    name, age = xiaoming_dict.values()
    print(name, age)

    k,v,w=(1,2,3)
    print(k,v,w)

    # 2. 打包
    new_dict = dict(name="小红", age=19)
    print(new_dict) # {'name': '小红', 'age': 19}

if __name__ == '__main__':
    #use_dict_iter()
    #use_list_dict()
    use_unpack_packet()