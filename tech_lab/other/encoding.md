##### What does x mean in "0xA1"? ######

`0x` is a special character that tells human the number after it are written in hexadecimal, so `0xA1` stands for `273` in decimal


### What's the difference between bit and byte? ###


One bit is a 0 or 1.  
And 1 byte equals to 8 bit.  
In IP adresses, when can represent our ip in both bit and byte.  
Like 192.168.0.1 is byte version.  
Meanwhile 11000000  10101000  00000000  00000001 is the bit version.  
As you can see, the number range a byte(8 bit) can represent is 0-255  
ASCII is short for "American Standard Code for Information Interchange", There are 256 symbols in this standard(each with length of 1 byte, thus 8 bit), perfectlly mapping the different status one byte can represent.  
Basically all the keys you can find on your keyboard(U.S.A standard keyboard) are in ASCII.  

> There are some other special keys in ASCII which are not on the keyboard, such as swith-line, you can view it [here][1]

ASCII perfectly represents the English alphabet, but what if we want to type Chinese? There are thousands of characters!  
So people from those countries who have their own special characters starts to build thier own coding format.  
Like Chinese people invent GB2312 which rules that all symbol with index\_number equal or under 127 are as the same in `ASCII`.  
But 2 symbols with index greater than 127 are special symbols,  
such as 7000 common simple Chinese Characters, Roma and Greek symbols, mathmatic symbols, Japanese symbols.  
These special characters are called `全角字符` in `GB2312`, and those characters with index less than 127 are called `半角字符`.  
But this isn't enough to include all the Chinese characters, so they changed the rule:  
As the first char in a two-char set is greater than 127, we consider this two-char set a `全角字符`,  
no matter the second char is greater than 127 or not. Through this modification.  
They enlarged the library to more than 20000 chinese symbols(including newly added Traditional Chinese symbol).  
This encode-system is called `GBK`  
But later, they found there are minority nations, so they extended it another time.  
This time they made a `1byte, 2byte, 4byte` char system. Which include all Chinese symbols and minority nations symbols of course.  
It's called `GB 18030`, nice, huh.  
But people in Taiwan also got their chinese symbol system `Big-5`, its encode methodology is totally different with these `GB` guys.  
So if you wanna display software programmed by Taiwanese, you'd better got `Big-5` on your computer.  
What if we also need to display `Thai`, `Indians`, `Arabian`?  
Is there a magic stuff can help me display all characters on earth?  
Yes, there is. It's called `Unicode`.  
The conception of unicode is simple: Map all the characters on earth to an interger.  
The decided to use two byte to represent them first, that is called UCS2(Universal Character set)  
Which will enable theoretically 65536 characters. And later they found that not enough.  
So UCS4(4 bytes) comes out, which enable theoretically 4294967296 different characters.  
But actually, they didn't dumbly match each index-num with a chracter, they sorted characters with some kind of methodology.  
So the total avail Unicode character number for now is 1111998, and 109384 used. For more informations, click [here][2]  
Though these guys make some bit special as sort head. It's still quite enough for human symbols.  
Considering basic ASCII symbols like `a, b, c` requires only 1 byte. Convert them to 2 byte in Unicode is wasting space.  
So, an intermediate encode-system comes out, it's called UTF(Unicode Transformation Format).  
The most popular UTF for now is utf-8. It transformes unicode to 1 to 4 bytes according to the index value of Unicode.  



[1]: http://localhost:4000/code_sources/ascii_special_symbol.html
[2]: http://stackoverflow.com/questions/5924105/how-many-characters-can-be-mapped-with-unicode

Add this content to the html file of link [1]:
\a 响铃(BEL) 007
\b 退格(BS) 008
\f 换页(FF) 012
\n 换行(LF) 010
\r 回车(CR) 013
\t 水平制表(HT) 009
\v 垂直制表(VT) 011
\\ 反斜杠 092
\? 问号字符 063
\' 单引号字符 039
\" 双引号字符 034
\0 空字符(NULL) 000
\ddd 任意字符 三位八进制
\xhh 任意字符 二位十六进制
