### Where to buy a mac?
    http://www.appletuan.com

### Transfer your data from old mac to new mac
    Using Migration Assistant

### Install your needed softwares in softwares.md
    see infos in softwares.md

### Install Homebrew
    Official sites:
        http://brew.sh/

    update vim to vim74:
        brew install vim

    Change bashrc:
        vim='/usr/bin/vim'

    install python3:
        brew install python3

### Install GNU utilities on mac!
    brew install coreutils --with-default-names

> http://apple.stackexchange.com/questions/69223/how-to-replace-mac-os-x-utilities-with-gnu-core-utilities

### Install perl interactive shell
    perl -d -e 1                                # A quick interactive shell
    http://www.sukria.net/perlconsole.html      # Following INSTALL using sudo, install modules with cpan
    http://www.cpan.org/modules/INSTALL.html    # A perl module manager, choose sudo mode to install packages.
    Try Devel::REPL, another perl module.       # Using cpan in root mode.
    When met trouble with installing readline, saw below link(saved in evernote):
    https://coderwall.com/p/kk0hqw/perl-install-term-readline-gnu-on-osx

> Perhaps you should just install GNU-readline, and then use `perl -d -e 1` to use interactive perl shell.

### Install and config Virtual Box
    install an Ubuntu on virtualbox
    initial your git project in shared folder
    Do most of your job in this shared file.
    share the clipboard, net-card

### chrome config
    Stop stupid chrome helper eating memory and cpu:
        Preferences -> Show advanced settings -> Privacy -> Content Settings -> Plug-ins -> Click to play


# VIM CONFIG
### Vim clipboard config
*share clipboard with system*
    add "set clipboard=unnamed" to your vimrc

### Add vim dict

    Move the file `spanish` in current directory to /usr/share/dict/

    # get thesaurus dict
    http://www.gutenberg.org/dirs/etext02/mthes10.zip
    mv mthesaur.txt to /usr/share/dict

    Add these to vimrc:
    set dictionary+=/usr/share/dict/Spanish
    set thesaurus+=/usr/share/dict/mthesaur.txt

### Install ctags on OS X
    brew install ctags-exuberant

### Switch Esc and Cap in mac
    http://stackoverflow.com/questions/127591/using-caps-lock-as-esc-in-mac-os-x

### Install TagList on OS X
    http://www.vim.org/scripts/script.php?script_id=273

### Install python `if else` jump plugin
    http://www.vim.org/scripts/script.php?script_id=386


# ITERM CONFIG
*Download the latest super awesome nightly version of iterm2(with the most advancing features, like resize split size)*
   https://iterm2.com/nightly/latest

*Map alt + f/b key in iterm2*

    http://stackoverflow.com/questions/81272/is-there-any-way-in-the-os-x-terminal-to-move-the-cursor-word-by-word
    # The result looks like
    Option+b    Send ^[ B
    Option+f    Send ^[ f

*Enable system clipboard(lot of more convinient)*

    Iterm > Preference > General > Allow clipboard access to terminal apps √

*No shadow on inactive panes*

    Iterm > Preference > Appearance > Dim inactive split panes X

*solve iterm-vim select text problem*

    add set   mouse=nichr   to your .vimrc
    when you want selecting texts, press OPTION key and then drag your mouse on screen

*Change shortcut of split/tab motion*
    Preference -> Keys -> Global Shortcut Keys -> +
    map Control + Shift + h,j,k,l to Select Split Pane Left/Below/Above/Right
    map Option + h,l to select previous/next tab

*Hide title bar*
    Preference -> Appearance -> Panes/Screen
    Desactivate Show title bar option


# SYS CONFIG
### Regularly backup use timemachine
    EXEC YOUR TIMEMACHINE

### Config Color

    Calibrate screen color temparature:
        System Preference -> Color -> Calibrate (勾选 expert mode) 


    Solarized theme config Tutorial:
        http://www.vpsee.com/2013/09/use-the-solarized-color-theme-on-mac-os-x-terminal/    or  https://www.evernote.com/shard/s246/sh/d35f864a-3dc4-4d05-bbbd-c853031b2867/ae79fc7f7ccfd933adb64639305f5b91 

    Iterm:
        Preference -> Profiles -> Colors -> Load Presets    # Change color set to Solarize or something else
            Foreground color is the terminal font color
            Background is what it means

        Preference -> Profiles -> Window                    # Change Window Transparency

### Change time from number to clock

    click the time button -> View As Analog √

### Change cursor blink rate when editing

    defaults write -g NSTextInsertionPointBlinkPeriodOn -float 200 (200 is 200ms)
    Restore Default:
        defaults delete -g NSTextInsertionPointBlinkPeriodOn
