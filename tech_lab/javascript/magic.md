### Check object type

you use `typeof my_var == "var_type"` to check if a var is your specified type.  
Or `typeof my_var` to get its type string. Below is all possible results:

    undefined   "undefined"
    null    "object"
    函数    "function"
    布尔值    "boolean"
    数值    "number"
    字符串  "string"
    Symbol  "symbol"
    其他    "object"
    宿主对象（如浏览器）    Implementation-dependent

> 注意 `typeof NaN` 是 "number"，列表，字典和它们的嵌套都是"object"
