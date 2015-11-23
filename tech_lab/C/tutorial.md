### 疑问
C语言如何写一个(只接受一个参数，但这个参数可以为int或char)的函数？  
没有pointer的struct，内存里的数据如何删除掉。  


### Point Lexicon
`type *ptr`  
    "a pointer of type named ptr"

`*ptr`
    "the value of whatever ptr is pointed at"

`*(ptr + i)`
    "the value of (whatever ptr is pointed at plus i)"

`&thing`
    "the address of thing"

`type *ptr = &thing`
    "a pointer of type named ptr set to the address of thing"

`ptr++`
    "increment where ptr points"

### Memory Leakage
In C, if you allocate a memory, and there is no pointers pointed to it.  
Then this memory is forgot, we can also call this `memory leakage`.  
Actually, if you just assign things memories but forgot to recollect the memory after the task.  
Then the usable memory space will be decreased. After accumulations by time and iterations. Your program will crash because of lack of memory.  

### Void type
In C, if a function returns nothing, we specified it with a `void` type

### NULL
In C, NULL is a `unset or invalid pointer`, you often use it to determing if a pointer is valid.  
Like `if (my_pointer != NULL) { do_something()}`

### Get address of variable
In C, you directly operate on memory addresses, thus you can print them out, too.  
Remember, what consists basis of computer? Binary! Thus memory address is actually a number!  
We print it with `%p` escaper, and add a `&` symbol before the variable, so explicity tell the compiler we want print the address.  
`&` is the `symbol of get the address`

    \\ CODE
    #include <stdio.h>

    int main(int argc, char *argv[]) {
        int a = 5;
        char *str_array[] = {"LWW", "TCM", "BGG"};
        printf("%p\n", &a);
        printf("%p\n", &str_array);
        return 0;
    };

    \\ RESULT
    0x7fff5113b93c
    0x7fff5113b950

### Arrays or Pointers?
Pointers is something that refers to a particular area of memory，  
You should only use it in these 4 conditions:

1. Ask the OS for a chunk of memory to work with, which includes `struct`.
2. Passing large blocks of memory(like large structs) to functions.
3. Taking the address of a function so to use it as a dynamic callback.
4. Complex Scanning of chunks of memory, such as converting bytes off a socket into data structure, or parsing files.

For nearly everything else when you see others using pointers, they should use arrays.  
In early years, using pointers can boost speed, but nowadays, arrays and pointers have the same speed.  
So no need to optimize on this.  
So, you shall always use array as you can. Pointers optimization is kind of ultimate resolution.  



### Scopes
In C, inside every single round of for loop, it got an isolated scope.  
Take a look of the code below:

    #include <stdio.h>

    int main(int argc, char *argv[])
    {
        char letter = 'a';
        int i = 0;

        for (i=0; i<3; i++) {
            char letter = argv[1][i];
            printf("%c\n", letter);
        };
        printf("%c\n", letter);
        return 0;
    }

    make ex
    ./ex bus

    b
    u
    s
    a

You can see that the `letter` variable inside the `for loop` won't affect the `outside letter variable`.  
And it changes every round.  



### bitwise OR/AND & Logical OR/AND

1. Bitwise operator will excuted all the comparison no matter what,  
meanwhile Logic operator will stop execute when the condition can't be True.

Take an example:
    if x() & y() { //do something }
    if x() && y() { //do something }

The when `x()` evaluates to `false`, the first bitwise operator will continue to run `y()`,  
but the second logical operator statement won't run `y()`, it just stops.  

2. Bitwise operator is faster than logic operator, even if they are in the same speed, it costs less system resource.

3. it seems in C, bitwise operator only works as you expected on int `1` and `0`,  
if you add other types in comparison, it may acts out of your imagination.  
For example. `i^j^k` will be evaluates to true both for `char i='a'; int j=0; int k=0;` and `char i='a'; int j = 1; int k=0;`.

### Tips

Using `for loops` in favour of `while loops`, because `for loop` are harder to break.


### Data types
`int`:  Int, escaped with `%d`
`float`:    Single Float, escaped with `%f`
`double`:   Double Float, escaped with `%f`
`char`:     Character, wrapped in `''`, escaped with `%c`
`char str_name[]`:  Char Array(String), should add `\0` at the end, escaped with `%s`
`char *str_name`:   String, wrapped in `""`, without adding `\0`
`char *var_name[]`: Arrays of strings
`const`:    Made a specified var a constant, make its value unmodifiable(read-only).


### For loop

    for (INITIALIZER, TEST, INCREMENT) {
        CODE
    }

INITIALIZER only run once at the beginning.  
If the current for loop VAR past the TEST, CODE run.  
After CODE ran, INCREMENT works, incresase the VAR in the for loop.  
Watch again if VAR past the TEST, if yes, continue LOOP, if not, STOP.



### Handy Tools
Error check
    http://valgrind.org/downloads/


### Details about `make`
* Make assmue there's a file called `Makefile` in current directory and run it.  
Basically you can add any shell command in the Make file. Below is an example:

    Z="zen_on_the_moon"

    fun:
        touch $Z
        now=$(shell date)
        echo "file created on"$(now) >> $Z

> In make file, you use `$(variable_name)` to get variable, and `$(bash command)` to get command execute result.

* add an `all:` item in `Makefile`, then you can use mere `make` command to to activate what's inside `all:` item.

* You can make several item(lists) at once, such as:

    make program_1 program_2


### complile a program

1. Using `make` to make an executeable file with the same name as c code file

    # assuming you have my_program.c file already
    make my_program

2. Using `cc` (clang compiler) to specify source file and target file.

    cc my_program.c -o arbitary_name_for_executable_file


### Prinf Formatters
[Tutorial](http://www.codingunit.com/printf-format-specifiers-format-conversions-and-formatted-output)

Formatters:

    \n  new_line
    \t  tab
    \r  carriage return
    \b  backspace
    \v  vertical tab
    \f  new page
