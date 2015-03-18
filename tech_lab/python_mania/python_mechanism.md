
### Hash Object
hashlib.md5('target\_txt') will return a hash object with md5 algorithm.

Which stores its value as a 128-bit hash value (binary - data), and other attributes for manipulating this data.

Let's say `hash_sample` is a hash object with md5 algorithm.

Hash_sample.hexdigest() will transfer the binary into a 32 byte hex string.  
Two byte([0-9a-f]) for per 8 bit number(`max to 16*16`).  
(128/8) * 2 = 32

`hash_sample.digest()` will transfer the object's binary data into a 16 byte string:  
By default python tries to interpret the bytes as ascii using the \xhh escape to output the hex representation of any bytes not in the range of ascii.  
If there isn't such code in ascii, you'll saw unrecongnizable code on your screen when trying to print it out.  


> md5 will map the given text to a number between 0 to `2 ** 128`
