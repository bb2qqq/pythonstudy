unix 是一个开放的系统。伯克利大学对unix进行了修改，制造了BSD( Berkeley Software Distribution ), 支持商业用途，许多商业公司使用了bsd进行修改，然后产生自己的系统。比如苹果的OSX.

而Linux是另一个类unix系统，试图与unix兼容, 要求完全开源。


`/`是根目录，所有的目录，文件和设备都在`/`下面

`/bin`下存有linux常用命令，以二进制文件的形式存在, bin是`binary`的缩写, [不同bin目录间的区别][1]

`/boot`目录用来存放Linux的内核

`/cdrom`目录用来挂载光驱文件系统, 你可以使用`mount /path/`命令来进行相关挂载操作(我不太理解手动mount的作用)

`/dev`目录下包含了所有linux系统使用的外部设备, `dev` 是`device`的缩写

`/etc`用来存放各类系统管理的配置文件, `etc`是`et cetera`的缩写，

`/home/`用来存放各位用户的数据，如你建立一个叫`Marquez`的用户，那么你的用户主目录就是`/home/Mario/`

`/lib`文件夹下存放有一些`.so`文件，这些文件的作用和windows下的`.dll`文件效果很像, 他们是各类程序，包括kernel程序在运行时需要调用的库, `lib`是`library`的缩写

`/lost+found`是用来存放机器意外关机或系统崩溃时的文件碎片的

`/mnt`目录用来存放挂载式储存设备的挂载目录，比如cdrom等目录，`mnt`是`mount`的缩写

`/media`目录被有些发行版用来挂载带usb接口的移动硬盘，比如U盘，移动硬盘等

`/opt`文件夹里存有你的增强性program，`opt`是`option`的缩写。

`/proc`文件夹里会存有各种系统信息，包括cpu信息，进程信息等, `proc`是`process`的缩写。

`/selinux` 用来存放selinux的相关文件，`selinux`是`secure linux`的意思，用于安全增强。此外，在`/etc/selinux/`存有该program的配置文件

`/srv`文件夹用来存放你建立网络服务时所提供的各类数据，如www服务读取的数据可以放在`/srv/www`中, `srv`是`serve`的缩写

`/tmp`用来存放程序运行时产生的临时文件, (据说里面产生的临时文件重启后会消失，待我实验一下), 实验结果: 重启后，虚拟机里的Ubuntu自己写的zen\_log消失, OSX x下/tmp里的zen\_log仍存在。

`/usr`文件夹用来存放不适合放在其他文件夹的额外的工具，是是linux系统中占用硬盘空间最大的目录，`Ubuntu`系统的游戏也放在此文件夹下  
用户可用的程序和数据都会放在此文件夹下

`/usr/share`文件夹会用来存放`shareble architecture-independent files`, 这里的shareble可以理解为能用在众多地方的program和文件,比如`vim`, `java`, `php`, `zsh`, `screen`, `doc`等, 此文件夹里存放的program最好是不需要被修改的。

`/usr/local`文件夹用来存放用户在本地自己安装的program, 它的文件夹结构和`/usr`很像，只不过`/usr/local`的`range`更窄一点。  
比如`vim`存放在`/usr/share`下，而`w3m`存放在`/usr/local/share`下, `openssl`和`perl`存放在`/usr/bin/`下，`git`存放在`/usr/local/bin`下  
或许我们可以这样理解，`/usr`下分作两个区域，`/usr/local`用来存放所有用户自行安装的和小范围应用的program及其data, 而`/usr/local`以外的区域主要用来存放预置的和全局性的program.  
同时`/usr/local/`和`/usr`的结构是一样的，就像在主`git`文件夹下再开了一个`sub-git directory`。

`/var`文件夹会存放一些经常变动的文件，如`/var/log`里会存有各类日志，`var`是`vary`的缩写

`/root`文件夹则是root用户的主目录

`/sbin`则是用来存放系统管理员的系统管理程序的目录。这个里面的命令，必须有root权限才能执行。


On a UNIX system( Linux also ), everything is a file; if something is not a file, it is a process.

A Linux system, just like UNIX, makes no difference between a file and a directory, since a directory is just a file containing names of other files.

Below is the file type chart of Linux:

Symbol    Meaning
-       Regular file
d       Directory
l       Link
c       Special file
s       Socket          ?
p       Named pipe      ?
b       Block device    ?


In a Unix-style file system, an index node, informally refered to as an inode, is a data structure used to represent a filesystem object, which can be one of various things including a file or a directory. Each inode stores the attributes and disk block location(s) of the filesystem object's data. Filesystem object attributes may include manipulation metadata (e.g. change, access, modify time), as well as owner and permission data (e.g. group-id, user-id, permissions)

An inode is identified by an integer number, often referred to as an i-number or inode number. On many types of file system implementations, the maximum number of inodes is fixed at file system creation, limiting the maximum number of files the file system can hold. A typical allocation heuristic for inodes in a file system is one percent of total size.

A Linux directory lists other filesystem objects by name, noramally identifying the listed object by referring to its inode. The directory contains an entry for itself, its parent, and each of its children.

A file in the file system is basically a link to an inode.  
A hard link then just creats another file with a link to the same underlying inode.  
When you delete a file it removes one link to the underlying inode. The inode is only deleted (or deletable/over-writable) when all links to the inode have been deleted.

A symbolic link(soft-link) is a link to another name in the file system. It can across filesystems, while hard-link can't.
