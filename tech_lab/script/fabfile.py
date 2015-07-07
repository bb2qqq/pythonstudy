# coding:utf-8
import datetime
from fabric.api import *
env.hosts=[
]

def add_ssh_key(ssh_key=None):
    target_key = ssh_key or raw_input('Please enter your ssh key:\n')
    key_comment = raw_input('Please type your comment for the ssh key:')

    default_path = '/home/admin/.ssh'
    change_path_hint = 'Type in CHANGE to change ssh path, other to continue: '
    print 'The default ssh-key path is', default_path

    change_path_choice = rawinput(change_path_hint)

    if change_path_choice == 'CHANGE':
        default_path = raw_input('Please enter new path of .ssh file:')

    with cd():
        sudo('echo " " >> authorized_keys')     # used for formatting purpose
        sudo('echo "# %s" >> authorized_keys' % key_comment)
        sudo('echo "%s" >> authorized_keys' % target_key)


def upload_config():
    """ 将当前用户指定路径下的bashrc和vimrc的内容append到目标机器的
        admin用户和root用户相应config下
    """
    default_path = '~/'
    change_path_hint = 'Type in CHANGE to change config path, other to continue: '
    print 'The default config path is', default_path

    change_path_choice = rawinput(change_path_hint)

    if change_path_choice == 'CHANGE':
        default_path = raw_input('Please enter new path of your config file:')

    local("scp %s.vimrc %s: ~/vimrc" % (env.host, default_path))
    local("scp %s.bashrc %s: ~/bashrc" % (env.host, default_path))
    sudo("cat ~/vimrc >> ~/.vimrc")
    sudo("cat ~/bashrc >> ~/.bashrc")
    sudo("cat ~/vimrc >> /root/.vimrc")
    sudo("cat ~/bashrc >> /root/.bashrc")
    sudo("rm ~/vimrc")
    sudo("rm ~/bashrc")


def update_bashrc(command=None):
    hint = 'Please type in the bash config item you wish to update:\n'
    command = command or raw_input(hint)
    """ 将指定配置插入到远程服务器admin和root用户下的.bashrc里 """
    run('''echo "alias cl='crontab -l'" >> ~/.bashrc''')
    sudo('''echo "alias cl='crontab -l'" >> /root/.bashrc''')

def update_vimrc(command=None):
    hint = 'Please type in the vim config item you wish to update:\n'
    command = command or raw_input(hint)
    """ 将指定配置插入到远程服务器admin和root用户下的.vimrc里 """
    run('echo "set mouse=nichr" >> ~/.vimrc')
    sudo('echo "set mouse=nichr" >> /root/.vimrc')
