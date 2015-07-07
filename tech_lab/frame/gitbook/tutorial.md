Manual-Page
    http://help.gitbook.com/

### init local server with specified ports
    gitbook server -p xxxx .

### view help info of particular command
    gitbook -h gitbook command


## Plugin wits

### gtoc
    gtoc (RECOMMENDED! easy to use, table of content pluing, 5 Star)
    https://github.com/boycgit/gitbook-plugin-gtoc

    Usage:
        make or edit the file `book.json` on your target book directory
        add `{ "plugins": ["gtoc"] }` to it.
        run `gitbook install`

    Advance Usage:
        (There is a tuned gtoc.css in the same directory of this file,
         you can use it to replace the gtoc.css file in your new project)


        1. CHANGE BUTTON POSITION
            In /node_modules/gitbook-plugin-gtoc/book/gtoc.css
            Line 145 .gtoc-menu-min {} decide the buttons of switch and go top.
            you can change the `right:` property to the px numbers you prefer,
            then the position of buttons will be changed.

        2. CHANGE INDEX TABLE WIDTH
            If your titles or tags for contnet are too long,
            the default width is unable to display them all.
            Then you can edit /node_modules/gitbook-plugin-gtoc/book/gtoc.css
            In Line 44, `.gitbook-table-of-contents {`, there is a `width` attr,
            change it to the px numbers you prefer.(STANDARD VALUE = button px - 20)
            Be aware, if you did this, you may also need to do Advance Usage 1 and 3,
            in order to get an acceptable display effect.

        3. CHANGE INDEX TABLE MINIMIZATION INDENT VALUE
            If you have changed your table width, the default minimization indent value
            can't fold your table back completely after you extended them.
            There are three groups of json values contains keyword `state-min` in
            /node_modules/gitbook-plugin-gtoc/book/gtoc.css
            Respectively on line 30, 79, and 165
            You should change their px value equal to your button px value(In Usage 1).
            And be aware, your table width should be "button px - 20".

        4. CHANGE BUTTON SIZE
            If you want to make your button larger or smaller, go to:
            /node_modules/gitbook-plugin-gtoc/book/gtoc.css
            in line 179, there is a json data `.git-menu-min a{`, you can set your preferable
            px numbers in `width` and `height` attrs to adjust the button size.
            After doing this, you may also need do Usage 5 to change the hint-word size.

        5. CHANGE THE BUTTON HINT-WORD SIZE
            In /node_modules/gitbook-plugin-gtoc/book/gtoc.css, Line 198,
            there is a json data named `.gtoc-menu-min .word{`, change the px numbers
            in it equal to what you set in Usage 4.
            But be aware, the font won't change as the block size enlarged.
            You shall find a way to change it by yourself if you wish to do that.

