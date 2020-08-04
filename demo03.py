"""
python类的讲解
通过class命名，首字母必须大写
"""
class Women():
  def __init__(self,name,age,sex,height,weight):
    self.name=name
    self.age=age
    self.sex=sex
    self.height=height
    self.weight=weight

  def makechild(self):
    print("生宝宝")
  def cookie(self):
    print("做饭")
  def work(self,work):
    print("我的工作是："+work)

zhangsan=Women("wangwu","19","女","168cm","45kg")
zhangsan.work("挖掘机")
print(zhangsan.height)

print("**********************")
"""
继承
"""
class Student(Women):
  pass
zhaosi=Student("李留","18","男","183cm","68kg")
print(zhaosi.weight)
zhaosi.work("街溜子")
