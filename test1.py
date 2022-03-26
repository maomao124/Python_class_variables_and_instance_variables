"""
 * Project name(项目名称)：Python类变量和实例变量
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 20:37
 * Version(版本): 1.0
 * Description(描述)：
 类体中、所有函数之外：此范围定义的变量，称为类属性或类变量；
类体中，所有函数内部：以“self.变量名”的方式定义的变量，称为实例属性或实例变量；
类体中，所有函数内部：以“变量名=变量值”的方式定义的变量，称为局部变量。
 """


# 类变量指的是在类中，但在各个类方法外定义的变量
class C1:
    a = 1
    b = 2

    def display(self):
        print(self.a, self.b)


if __name__ == '__main__':
    # 类变量的特点是，所有类的实例化对象都同时共享类变量，也就是说，类变量在所有实例化对象中是作为公用资源存在的
    c1 = C1()
    c2 = C1()
    print(c1)
    print(c2)
    print(c1.a)
    print(c1.b)
    print(C1.a)
    print(C1.b)
    C1.a = 3
    C1.b = 4
    print(C1.a)
    print(C1.b)
    print(c1.a)
    print(c1.b)
    c1.a = 5
    c2.b = 6
    print(c1.a)
    print(c1.b)
    print(c2.a)
    print(c2.b)
