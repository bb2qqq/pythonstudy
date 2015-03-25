# Where to buy a mac?
    http://www.appletuan.com

# Install perl interactive shell
    perl -d -e 1                                # A quick interactive shell
    http://www.sukria.net/perlconsole.html      # Following INSTALL using sudo, install modules with cpan
    http://www.cpan.org/modules/INSTALL.html    # A perl module manager, choose sudo mode to install packages.
    Try Devel::REPL, another perl module.       # Using cpan in root mode.
    When met trouble with installing readline, saw below link(saved in evernote):
    https://coderwall.com/p/kk0hqw/perl-install-term-readline-gnu-on-osx

> Perhaps you should just install GNU-readline, and then use `perl -d -e 1` to use interactive perl shell.

# Install Picture Documentation tool

    https://www.yinxiang.com/skitch/

# Install Mou
    http://25.io/mou

# chrome config
    Stop stupid chrome helper eating memory and cpu:
        Preferences -> Show advanced settings -> Privacy -> Content Settings -> Plug-ins -> Click to play


# Install GNU utilities on mac!
    brew install coreutils --with-default-names

> http://apple.stackexchange.com/questions/69223/how-to-replace-mac-os-x-utilities-with-gnu-core-utilities

# Install ulysses-iii
    search "ulysses" in your bookmark manager

# Install Calibre to convert epub
    http://www.calibre-ebook.com/download_osxf


# Homebrew

    Official sites:
        http://brew.sh/

    update vim to vim74:
        brew install vim

    Change bashrc: 
        vim='/usr/bin/vim'

    install python3:
        brew install python3

# Virtual Box
    install an Ubuntu on virtualbox
    initial your git project in shared folder
    Do most of your job in this shared file.
    share the clipboard, net-card

# VIM
*share clipboard with system*

    add "set clipboard=unnamed" to your vimrc

# Iterm config.

*Map alt + f/b key in iterm2*

    http://stackoverflow.com/questions/81272/is-there-any-way-in-the-os-x-terminal-to-move-the-cursor-word-by-word

*Enable system clipboard(lot of more convinient)*

    Iterm > Preference > General > Allow clipboard access to terminal apps √

*No shadow on inactive panes*

    Iterm > Preference > Appearance > Dim inactive split panes X


*solve iterm-vim select text problem*

    add set   mouse=nichr   to your .vimrc
    when you want selecting texts, press OPTION key and then drag your mouse on screen

# install ctags on OS X
    brew install ctags-exuberant

# Switch Esc and Cap in mac
    http://stackoverflow.com/questions/127591/using-caps-lock-as-esc-in-mac-os-x


# install TagList on OS X
    http://www.vim.org/scripts/script.php?script_id=273

# install python `if else` jump plugin
    http://www.vim.org/scripts/script.php?script_id=386


# install Xmind on OS X
    http://www.xmind.net/download/mac/

# Regularly backup use timemachine
    EXEC YOUR TIMEMACHINE    

# Config Color

    Calibrate screen color temparature:
        System Preference -> Color -> Calibrate (勾选 expert mode) 


    Solarized theme config Tutorial:
        http://www.vpsee.com/2013/09/use-the-solarized-color-theme-on-mac-os-x-terminal/    or  https://www.evernote.com/shard/s246/sh/d35f864a-3dc4-4d05-bbbd-c853031b2867/ae79fc7f7ccfd933adb64639305f5b91 

    Iterm:
        Preference -> Profiles -> Colors -> Load Presets    # Change color set to Solarize or something else
            Foreground color is the terminal font color
            Background is what it means

        Preference -> Profiles -> Window                    # Change Window Transparency

# Adobe Reader 

    install abode reader:
        http://get.adobe.com/reader/

    color set:
        Preferences -> Accessibility -> Document Colors Options -> Replace Document Colors -> ( Background: light-grey, Font: deep dark brown, like black )

    enable scrolling:
        View -> Page Display -> Enable Scrolling

    memorize last view page:
        Preferences -> Documents  -> Restore last view setting when reopening documents √

# Change time from number to clock

    click the time button -> View As Analog √

# Change cursor blink rate when editing

    defaults write -g NSTextInsertionPointBlinkPeriodOn -float 200 (200 is 200ms)
    Restore Default:
        defaults delete -g NSTextInsertionPointBlinkPeriodOn

