# 学习笔记

## 变量赋值
* 当两个变量都同时指向同一个常数的时候，它们的id相等，由于数值较小的整数对象在内存中会
很频繁地使用，如果每次都向内存申请空间、请求释放，会严重影响 Python 的性能。好在
整数对象属于不可变对象，可以被共享而不会被修改导致问题，所以为小整数对象划定一个范围，
即小整数对象池，在Python运行时初始化并创建范围内的所有整数，这个范围内的整数对象是
被共享的，即一次创建，多次共享引用。
* 可变数据类型
  * list
  * dict
* 不可变数据类型
  * int
  * float
  * string
  * tuple
* 多次创建不可变类型的数据，可能会引起内存的问题，但是python的垃圾回收机制会自动回收
* 可变类型的值的变化并不会引起内存地址的变化，只是内存地址当中的内容发生变化

## 容器序列的深浅拷贝
* 序列
  * 容器序列 - list, tuple, collections.deque。能存放不同数据类型
  * 扁平序列 - str, bytes, bytearray, memoryview。存放相同类型的数据
* 非序列（映射）
  * dict

## 字典与扩展内置数据类型
* 字典内部用了散列函数 - hash， 线性查找时间
* dict的key必须是可以hash的, 比如list就不能作为key
* 使用collections扩展内置数据类型
  * collections.namedtuple
  * collections.Counter
  * collections.deque
  
## 函数
需要关注的四个点
* 函数的调用
  * 不带括号就是传递的对象
```python
def func2(): return 123
a = func2
a is <function func2 at 0x1042e4f80>
```
  * 带括号就是函数的执行
```python
def func2(): return 123
a = func2()
a is 123
```
```python
class Kls1():
    def __call__(self):
        return 123

inst1 = Kls1()
inst1()
123
```
* 函数的作用域(LEGB)
  * Local: 函数内
  * Enclosing: 外部嵌套函数
  * Global: 模块/文件
  * Builtin: Python 内置模块
* 函数的参数
  * `*args`
  * `**kwargs` - 关键字参数，在获取传递的参数时，`**kwargs`会优先获取，剩下的参数再
  交给`*args`
  * 偏函数
  * 高阶函数：函数的参数和返回值都是函数，很多高阶函数的功能都被lambda所代替
    * 常见的高阶函数：map, filter, apply
  * lambda（匿名函数）： 只是表达式，不是所有的函数都能封装进去。
    * 实现简单函数的时候可以使用lambda表达式代替
    * 使用高阶函数的时候一般使用lambda表达式
```python
k = lambda x:x+1
print(k(1))
```
* 函数的返回值
  * 函数是一个对象，所以可以作为某个函数的返回结果
* 取得编译后函数体的变量
  * func().__code__.co_varnames (local)
  * func().__code__.co_freevars (enclosing)
  * func().__closure__[0].cell_contents (enclosing value)

## 闭包
* 函数中的函数
* 定义态而非运行态，定义的时候就设置好了规则

## 装饰器
* target表示函数
* target() 表示函数执行
* new = func 体现"一切皆对象", 函数也可以被当作对象进行赋值
* PEP-318和PEP-3129
* 装饰器在模块导入的时候就自动运行
* 装饰器的堆叠
  * 注意装饰器堆叠的顺序不同，造成的结果也不同
* 内置装饰器
  * `functools.wraps` - 保持原有的函数名不变
  * `lru_cache`
* 类装饰器

## 对象协议
* 实现对象协议用的是魔术方法
* 对象协议有时候也叫鸭子类型
* 容器类型协议
  * __str__
  * __getitem__, __setitem__, __delitem__
  * __iter__
  * __call__
* 对象行为尽量模拟Python自带的数据类型名，如果原声数据类型解决不了，再自定义，但是
自己定义的类操作的时候也尽量遵循自带数据类型的行为和模式

## yield
* 函数中使用yield可以实现生成器
* 生成器可以让函数返回可迭代对象
* yield只是暂停函数，保持函数执行状态
* 迭代器终止时，会抛出StopIteration异常
* 生成器
  * iterables: 包含 __getitem__()或__iter__()方法的容器对象
  * iterator: 包含next()和__iter__()方法
  * generator: 包含yield语句的函数