### Official tutorial link
http://doc.scrapy.org/en/latest/intro/tutorial.html

### XPath Expressions

* `/html/head/title`: selects the `<title>` element, inside the `<head>` element of an HTML document
* `/html/head/title/text()`: selects the text inside the aforementioned `<title>` element
* `//td`: selects all the `<td>` elements
* `//div[@class="mine"]`: selects all `div` elements which contain an attribute `class="mine"`

> The last `//div[@class="mine"]` selector will be using quite frequently in practice. So type them 10 times for a practice.

Practice:

    //div[@class="mine"]
    //div[@class='footer']
    //div[@class='well login-reg-box']
    //div[@class='clearfix']
    //div[@class='zg-wrap clearfix']
    //div[@class='zm-noti7-frame']
    //div[@class="zg-wrap"]
    //div[@class="top"]
    //div[@class="items"]
    //div[@class="fkm"]


### Selector methods

* `xpath()`: returns nodes selected by xpath expression
* `css()`: returns nodes selected by css expression
* `extract()`: returns a unicode string with the selected data
* `re()`: returns a list of unicode strings extracted by applying regular expression.
