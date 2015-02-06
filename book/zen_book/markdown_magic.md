### ON STACKOVERFLOW ###

* To produce the real key effection
    
      <kbd> KEY </kbd>


### BASIC ###

Indentation for each label is 2 space.
Indentation for code is 4 space.
If you want show code under a first-level label, You`ll need indent 6 spaces, which is code identation + label indetation. And on second-level label, you`ll need indent 1 code identation(4 spaces) and 2 label indention

Beaware that the affecfive scope of a label lasts for one blankline, and the border of the scope is the last line of the Label group.  If you write 2 blank lines, the current label scope will finish, and a new scope will be genarated.


Belowing is an example.

The code:

      * Label0              \#  Independent Label


    * Label1                \#  First_level Label

          code1             \#  belong to Label1

      * Label2              \#  sub label of Label1
        
            code2           \#  belong to Label2

        * Label3            \#  sub label of Label2

        code4               \#  belongs to Label3, so need more indentation to get code visual effect.

      * Label4              \# sub label of Label1

The effect:

  * Label0              


* Label1                

      code1             

  * Label2              

        code2           

    * Label3            

    code4              

  * Label4              



    Code from git book
    I don`t know how many spaces I have!
