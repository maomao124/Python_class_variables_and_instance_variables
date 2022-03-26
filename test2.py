"""
 * Project name(项目名称)：Python类变量和实例变量
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 20:48
 * Version(版本): 1.0
 * Description(描述)： 实例变量
 实例变量指的是在任意类方法内部，以“self.变量名”的方式定义的变量，其特点是只作用于调用方法的对象。另外，实例变量只能通过对象名访问，无法通过类名访问。

 通过类对象可以访问类变量，但无法修改类变量的值。这是因为，通过类对象修改类变量的值，不是在给“类变量赋值”，而是定义新的实例变量
 类中，实例变量和类变量可以同名，但这种情况下使用类对象将无法调用类变量，它会首选实例变量，这也是不推荐“类变量使用对象名调用”的原因
 和类变量不同，通过某个对象修改实例变量的值，不会影响类的其它实例化对象，更不会影响同名的类变量
 """


class C:
    a = 0
    b = 0

    def __init__(self):
        self.a = 1
        self.b = 2

    def f1(self):
        self.c = 3


if __name__ == '__main__':
    c = C()
    print(c.a)
    print(c.b)
    # print(c.c)
    c.f1()
    print(c.c)

    c.a = 5
    c.b = 6
    print(c.a)
    print(c.b)
    print(C.a)
    print(C.b)
