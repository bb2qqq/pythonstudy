### undefined
`undefined` is a global object, you can't change its value on global scope(value always equal to undefined).  
But in local scope, it's not a reserved code, thus you can treat it as normal variable in local scope.  

A function returns nothing, it return an undefined object.  
If you trying to access a non-exists attribute of an object, you got undefined, too.  
A variable defined without assigning value, is undefined object.  
If a function, method or statement returns such a variable, it returns undefined object.  


### Run script interactively
First run `node`, then use `.load ./script.js` to load particular script

### Function & Class

在javascript里，function有两种写法  
[点击这儿观看关于这两种写法不同之处的讨论](http://stackoverflow.com/questions/336859/var-functionname-function-vs-function-functionname)


    # 在脚本运行时运行
    var my_func = function(parameters) {};

    # 在脚本解析时运行
    function MyFunc(parameters) {};

因为第二种方式是在脚本解析时运行，所以你没办法在global层用if语句来控制它的定义。
虽然目前我没发现它的应用价值，不过我们可以把第二类function嵌套在第一类function里，
这样我发现，在解析时，F2并不会被定义:
(在阅读如下代码时，最好开一个vim窗口，将代码贴在里面，以供参照）

    // CODE

    signal = true

    if (signal) {
        var F1 = function() {
            function F2(p) {
                 console.log(p);
                 this.func = F2;
            };
            F2();
            this.func2 = F2;
        };
    };


    // TEST AREA


    // F2 wasn't defined in parse-time

    > F1
    [Function]
    > F2
    ReferenceError: F2 is not defined
    > F1.F2
    undefined
    > F1.func
    undefined
    > F1.func2
    undefined

    // After F1 run, F2 still not defined in global scope
    // but two this arguments works both on global scope
    // And besides, we saw that `Function` can't be target of `this` statement

    > F1()
    undefined
    undefined
    > F1.F2
    undefined
    > F2
    ReferenceError: F2 is not defined
    > func
    [Function: F2]
    > func2
    [Function: F2]

    // Calling F1 inside an obj didn't assign F2 to obj's `func` attribute.
    // Instead F2 was assigned to global attribute `func` again.
    // It seems that F2 was called inside F1's scope, since he didn't find an obj,
    // so it went straight to global scope?

    > func = null
    null
    > func2 = null
    null
    > obj = {}
    {}
    > obj.f = F1
    [Function]
    > obj.f()
    undefined
    undefined
    > obj.func
    undefined
    > obj.func2
    [Function: F2]
    > func
    [Function: F2]
    > func2
    null


### this
JS里，有一个很有意思的关键词：this  
它最基本的用法是用于指代任何call它的object，谁call它，它就指谁。  
有点像python的self，但是在全局scope里也能用this.  
在全局scope里，this.D等于locals()['D']  



### Scopes
在javascript里，for循环下并没有单独的scope，而是和当前逻辑层级共用同一个scope空间。


    # Example 1
    D = {1:2}
    var i = 111

    for (var i in D) {
        console.log(i);
    }
    console.log(i)

    1
    1


    # Example 2
    D = {1:2}
    var i = 111

    var f = function() {
        for (var i in D) {
            console.log(i);
        }
    }
    f()
    console.log(i)

    1
    111


## Data Types
在javascript里，我猜想，dict是更基础的类，array是因为继承了它的特性，所以type是object  
所以javascript里的array既有array空间，也有一个dict空间，  
对dict空间进行赋值操作不会改变array空间的length.  
它们在大部分时间保持相互独立，但是当你使用L['1'] = "aaa"的时候，它们会交叉。  
也就是说javascript把L['1']和L[1]看做是等效的。  

此外，javascript还支持给此前不存在的array index赋值。赋值完后，列表长度变为该index值+1  
然后列表里的其他位置，如果此前未被赋值的话，会被`undefined`填充，或者说，你用L[index]调用它们得到`undefined`.  

在使用literal表达初始化字典时，字典的key不用加字符符号，javascript会自动转换  
在之后的赋值和取值中，如果key是字符型的数字，那么你取key对应的value时，key输入数字或字符是等效的。  
但如果key是字符的话，则一定需要输入字符，忘记字符符号如`""`或`''`会导致报错。

    # Example 1

    L = []
    L['key'] = 'value'
    L.key
    'value'
    L.length
    0

    # Example 2
    L = []
    L[1] = 1
    L.length
    2
    L['5'] = 5
    L.length
    6
    L
    [ , 1, , , , 5 ]

    # Example 3
    > D = { name: 'Z', 1: 1}
    { '1': 1, name: 'Z' }
    > D[1]
    1
    > D['1']
    1
    > D[name]
    ReferenceError: name is not defined
    > D['name']
    'Z'
    > D[1.555] = 2
    2
    > D
    { '1': 1,
      name: 'Z',
      '1.555': 2 }
    > D.name
    'Z'
    > D.1.555
    ...

[Comparison of array and dict methods](/Users/zen1/zen/pythonstudy/tech_lab/javascript/pictures/array_and_dict_methods.jpg)

> 在javascript里，你去取

### Loop over arrays
使用 `for (i in my_array) {console.log(i)}`，你得到的是列表里各个item的序号，而不是值。  

    > for (i in ['a', 'b']) {console.log(i);};
    0
    1

但是在新的`ECMA Script  6`(这是什么？）标准里，我们可以使用新的语法，`for (i of my_array) {}`.  
这个feature在Firefox 13+, Chrome 37+的浏览器里被支持，node0.12.0(非stable)也支持这一特性。  

    > for (i of ['a', 'b']) {console.log(i);};
    a
    b


### Official Doc Sites
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference


### Reverse Boolvalue of a var
    var a = "Hey"
    a
    'Hey'
    a = !a
    a
    false
    a = !a
    a
    true


### Logic Operators
    &&  AND
    ||  OR
    !   NOT


### Relative Comparison

`===` 表示严格相等，而`==`表示相对相等

    1 === true
    false

    1 == true
    true

    [1] == true
    true

    [2] == true
    false

    [true] == true
    false

    [0] == false
    true

    [false] == false
    false

    [null] == false
    false

    "S" == true
    false

    "" == false
    true

    0 == false
    true

    [] == false
    true

    null == false
    false

    var D = {}
    D == false
    false

> 在不同类型数值之间的相对比较时(字符/数字 和 其他类型），javascript会先将其他类型进行转化，而其他类型的默认转换函数基本都是（目前我未发现特殊例子）toString.  
> 所以将上面例子里奇怪的结果之间的其他类型toString的结果代入，再看感觉就对了。  
> 更多解释：http://stackoverflow.com/questions/25531424/why-is-null-true-in-javascript


### Var or not?

如果你使用var，表示在当前scope下声明变量。  
如果不用var的话，javascript会从当前scope层层向上搜索，直到找到一个已定义的同名变量或是到达global层，然后将该scope下的原变量替换。  
试看一例：

    # DEFINE
    t = 1   // global
    var f = function(){
        t=2
        console.log(t)
    }

    # CALL
    f()
    2
    t
    2


    # DEFINE
    t = 1
    var f2 = function(){
        var t = 2
        t = 3
        console.log(t)
    }

    # CALL
    f2()
    3
    t
    1
