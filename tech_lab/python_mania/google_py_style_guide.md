* Naming:

    module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name.

* Avoid global variables

* Use list comprehension for simple cases

code should fit in one line.  
multiple for loop is prohibited  
When things get complicated, uses loops instead.  


    Yes:
      result = []
      for x in range(10):
          for y in range(5):
              if x * y > 10:
                  result.append((x, y))

      for x in xrange(5):
          for y in xrange(5):
              if x != y:
                  for z in xrange(5):
                      if y != z:
                          yield (x, y, z)

      return ((x, complicated_transform(x))
              for x in long_generator_function(parameter)
              if x is not None)

      squares = [x * x for x in range(10)]

      eat(jelly_bean for jelly_bean in jelly_beans
          if jelly_bean.color == 'black')
    No:
      result = [(x, y) for x in range(10) for y in range(5) if x * y > 10]

      return ((x, y, z)
              for x in xrange(5)
              for y in xrange(5)
              if x != y
              for z in xrange(5)
              if y != z)


* Default Iterators and Operators


Pros:
The default iterators and operators are simple and efficient. They express the operation directly, without extra method calls. A function that uses default operators is generic. It can be used with any type that supports the operation.

Cons:
You can't tell the type of objects by reading the method names (e.g. has_key() means a dictionary). This is also an advantage.

    Yes:  for key in adict: ...
          if key not in adict: ...
          if obj in alist: ...
          for line in afile: ...

    No:   for key in adict.keys(): ...
          if not adict.has_key(key): ...
          for line in afile.readlines(): ...

* Lambda is Okay for one liners

* Conditional Expression is Okay for one liners

* Shebang LIne

Most .py files do not need to start with a #! line. Start the main file of a program with #!/usr/bin/python with an optional single digit 2 or 3 suffix per PEP-394.


* Explicitly close files and sockets when done with them.

The preferred way to manage files is using the "with" statement:

    with open("hello.txt") as hello_file:
        for line in hello_file:
            print line

For file-like objects that do not support the "with" statement, use contextlib.closing():

    import contextlib

    with contextlib.closing(urllib.urlopen("http://www.python.org/")) as front_page:
        for line in front_page:
            print line

