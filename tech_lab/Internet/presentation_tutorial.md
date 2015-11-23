### 什么是DOM?
DOM is abbreviation of `Document Object Model`.  
它用来描述HTML文件里的层级结构。  
在HTML文件中，我们把每一个尖括号包裹起来的tag叫做`element`.  
我们会用人类关系来描述elements间的相互关系：`parent, child, sibling, ancestor, descendant`.  
浏览器会解析DOM，以正确显示页面信息。  

### 什么是CSS?
CSS是用来表示HTML视觉呈现风格的文本。  
CSS styles由选择器(selector)和规则(rules)组成。  
选择器决定哪些元素将被渲染，而rules构成某一个选择器内渲染的具体内容。  

一个选择器的样例：
    h1  /* 选择所有h1标题 */
    p   /* 选择所有段落 */
    .caption    /* 选择含有class "caption"的元素 */
    #subnav     /* 选择 ID 为 "subnav"的元素 */

一个rules的样例：
    color: pink;
    background-color: yellow;
    margin: 10px;
    padding: 25px;

一个选择器和规则结合的样例：
    p {
        font-size: 12px;
        line-height: 14px;
        color: black;
    }

css文本可以直接嵌在HTML的head标签里，或者单独放在一个有.css后缀的文件里。再在head标签里引用，如：

    <head>
        <link rel="stylesheet" href="style.css">
    </head>

> d3 使用 CSS selector 来决定操作的目标对象

### 什么是SVG?
SVG的全称是`Scalable Vector Graphics`  
我们可以把这个理解为一种简单的标记语言。  
这种标记语言是用来描述一个图形的样子的。  
大部分的浏览器(除去一些IE早期版本）都支持HTML文件中直接嵌套的SVG渲染。  
以下是我用SVG画的一个圆的代码：

    <svg width='100', height='215'>
        <circle cx='30' cy='40' r='22'
        fill='red' stroke='blue' stroke-width='3'/>
    </svg>


### HTML中嵌套javascript
在里的html文件中，使用`script`标签后，你便能将javascript内容嵌套进去，直接在浏览器里执行！ javascript是活在浏览器里的语言！  

    <body>
        <script >
            while (1) {
                confirm("你关不掉这个的");
            }
        </script>
    </body>

或者你也可以在`<head>`元素里用引用的方式调用javascript脚本：

    <head>
        <script tpye='text/javascript' src="my_javascript.js"></script>
    </head>

> 在较先进的浏览器里，`type="text/javascript`通常可以省略
