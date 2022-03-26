"""
 * Project name(项目名称)：Python类变量和实例变量
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 20:58
 * Version(版本): 1.0
 * Description(描述)： 局部变量
除了实例变量，类方法中还可以定义局部变量。和前者不同，局部变量直接以“变量名=值”的方式进行定义
局部变量只能用于所在函数中，函数执行完成后，局部变量也会被销毁

 """


class C:
    def f1(self, a):
        """

        :param a:
        :return:
        """
        b = a * 2
        print("a=", a, "---", "b=", b)


if __name__ == '__main__':
    c = C()
    c.f1(4)
