# 判断  (python的代码块靠缩进来区分)
# age=int(input("请输入你的年龄："))
# if age>60:
#   print("你应该退休了")
# elif age>30:
#   print("家庭责任很重呀")
# elif age>20:
#   print("是时候规划未来了")
# else:
#   print("要好好读书将来才能有更多的选择")

# while循环
# a=1
# while a<10:
#   print("哈哈哈哈")
#   a+=1

  # """
  # 练习：
  # 录入十个学生的成绩
  # 这十个人分别是，鲁班，后裔，马可波罗，鬼谷子，关羽，张飞，赵云，公孙离，貂蝉，大桥
  # 并且名字和成绩要对应上
  # 而且大于60的和小于60的要分开存放
  # """

# studentList=["鲁班","后裔","马可波罗","鬼谷子","关羽","张飞","赵云","公孙离","貂蝉","大乔"]
# highChengJi={}
# lowChengJi={}
# a=0
# while a<len(studentList):
#   chengji=int(input("请输入"+studentList[a]+"的成绩："))
#   if chengji>=60:
#     highChengJi[studentList[a]]=chengji
#   else:
#     lowChengJi[studentList[a]]=chengji
#   a+=1
# print("大于60的成绩为:",highChengJi)
# print("小于60的成绩为:",lowChengJi)


"""
for循环
"""
#  遍历
# a=["鲁班","后裔","马可波罗","鬼谷子","关羽","张飞","赵云","公孙离","貂蝉","大乔"]
# for i in a:
#   print(i)

  # """
  # 练习1：打印九九乘法表
  # """
# for i in range(1,10):
#   # range函数可以创建一个整数列表，遵循左闭右开，range(start, stop, step)，一般用在for循环中
#   for j in range(1,i+1):
#     print(i,"x",j,"=",i*j,end=" ")
#   print()
# ###########################


  # 练习2
  # 通过print打印，模拟一个红绿灯的功能，红灯30次，绿灯35次，黄灯3次
# while True:
#   for i in range(30,0,-1):
#     print("红灯还有",i,"秒结束")
#   for i in range(35,0,-1):
#     print("绿灯还有",i,"秒结束")
#   for i in range(3,0,-1):
#     print("黄灯还有",i,"秒结束")
# ######################################

# 练习3
# 使用代码，实现一个注册的功能
# 用户输入账号和密码，要求账号长度为5-8位，密码6-12位，并且账号必须小写开头
# 存储到字典中{}

username=input("请输入账号：")
password=input ("请输入密码：")
print("**********************")
if len(username)>=5 and len(username)<=8:
  if username[0] in "qwertyuiopasdfghjklzxcvbnm":
    if len(password)>=8 and len(password)<=12:
      print("注册成功！",{username:password})
    else:
      print("密码必须8-12位！")
  else:
    print("账号的首字母必须是小写！")
else:
  print("账号的长度不符合规范，请输入5-8位的账号") 