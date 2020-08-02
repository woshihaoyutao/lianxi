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
studentList=["鲁班","后裔","马可波罗","鬼谷子","关羽","张飞","赵云","公孙离","貂蝉","大乔"]
highChengJi={}
lowChengJi={}
a=0
while a<len(studentList):
  chengji=int(input("请输入"+studentList[a]+"的成绩："))
  if chengji>=60:
    highChengJi[studentList[a]]=chengji
  else:
    lowChengJi[studentList[a]]=chengji
  a+=1
print("大于60的成绩为:",highChengJi)
print("小于60的成绩为:",lowChengJi)


