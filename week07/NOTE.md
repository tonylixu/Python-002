# 学习笔记

## 类和对象
* Python经典类(2.2)以及新式类(3.x)
* 类的两大成员: 属性和方法
* 属性
  * 类属性在内存中只有一份 (节省内存)
  * 对象属性在每个对象都保存一份
  * `class Human(object)` 在2.2以上可以写作 `class Human`
* Add class attribute
  * `Human.newattr = 1`
  * `Human.__dict__`
* Default type can't add new property
  * `setattr(list, 'newattr', 'value'`)
  * TypeError

### 方法
* 普通方法: `def get_something(self)`
* 类方法: `@classmathod def class_method(cls)`
* 静态方法 由类调用，无参数 `@staticmethod`
* 三种方法在内存中都属于类
* `__init__`是初始化函数
* `__new__`才是构造函数
