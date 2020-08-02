"""
 print("你好")
 a=input("请输入：")
 print("input输入的内容是：",a)



a=input("请输入a：")
b=input("请输入b：")
print(len(a+b))
"""


# 元组
# a=(1,2,3,4,"你好","傻逼",True,False)
# print(a[4])


# # 切片  (遵循左闭右开，开始和结尾可省略不写)
# print(a[:4])
# print(a[4:6])
# print(a[6:])

# # index 查找某个值的下标  (只能操作一维元组)
# print(a.index("傻逼"))
# # count 统计某个值的数量  (只能操作一维元组)
# print(a.count("你好"))

# 二维元组
# b=(a,"你好","傻逼")
# print(b[0][3])


"""
 ***数组***
"""
# 元组与数组的区别：元组写好的值是不能修改的，数组可以修改
# a=[1,2,3,4,"你好","傻逼",True,False]
# a.append("append") #往数组中追加数据
# a.insert(0,"insert")  #往数组中指定的位置插入数据
# print(a)
# pop  相当于剪切的作用
#  b=a.pop(2)
#  print(a)
# print(b)

# extend  合并数组
c=["你好","我不好"]
# a.extend(c)
# print(a)
# clear()  清空数组
# remove()  删除某个值
# b=a.remove("傻逼")
# print(b)
# print(a)

"""
python的语法
所有的方法都是小括号结尾。比如，print()
元组、数组、字典的取值，都是用中括号取值，如a[2]
元组、数组、字典的定义，分别是(),[],{}
"""

"""
字典的特点
1、字典中的值没有顺序
2、字典中的结构必须是键值对的结构
"""
a={"name":"张三",0:"你好","age":18}
# 取值
print(a["name"])
# 新增
a["height"]="178cm"
print(a)
# 修改
a["name"]="王八"
print(a)




