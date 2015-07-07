
### Pass arguments to fabric functions
    Q:
    How can I pass a parameter to a fabric task when calling "fab" from the command line? For example:

    def task(something=''):
        print "You said %s" % something


    $ fab task "hello"
    You said hello

    Done.
    Is it possible to do this without prompting with fabric.operations.prompt?

    A:
    Fabric uses the following syntax for passing arguments to tasks:

     fab task:'hello'
     fab task:something='hello'
     fab task:foo=99,bar=True
     fab task:foo,bar
