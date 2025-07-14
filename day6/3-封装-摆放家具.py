# 作者: 大数据 浪哥
# 2025年07月12日16时43分20秒
# 1054074422@qq.com

# 设计类时，优先设计被依赖的类，然后再设计依赖它的类。
class HouseItem:  # 家具类
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        """
        因为该函数是被其他类调用的，所以需要返回字符串，目的是显示打印信息
        :return:
        """
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:  # 房子类
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []

    def __str__(self):
        # Python 能够自动的将一对括号内部的代码连接在一起
        return ("户型：%s\n总面积：%.2f  [剩余：%.2f]\n家具：%s" % (
        self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item: HouseItem):  # 要想让 item 中提示 name，可以使用冒号策略：
        print("要添加 %s" % item)
        # 1. 判断家具面积是否大于剩余面积
        if item.area > self.free_area:
            print("%s 的面积太大，不能添加到房子中" % item.name)
            return
        # 2. 将家具的名称追加到名称列表中
        self.item_list.append(item.name)
        # 3. 计算剩余面积
        self.free_area -= item.area


# 1. 创建家具实例
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
print(bed)
print(chest)
print(table)
print("-" * 50)
# 2. 创建房子实例，并把家具添加到房子中
my_home = House("两室一厅", 60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
