# coding:utf-8
import datetime
from fabric.api import *
env.hosts=[
]

@runs_once
def change_path(name, default_path):
    print 'The default %s path is %s' %  (name, default_path)
    change_path_hint = 'Type in your specified path here, or default path will be used: ' 
    change_path_choice = raw_input(change_path_hint)

    if not change_path_choice:
        return default_path
    else:
        return change_path_choice

def add_ssh_key(ssh_key=None, key_comment=None):
    target_key = ssh_key or raw_input('Please enter your ssh key:\n')
    key_comment = key_comment or raw_input('Please type your comment for the ssh key:')

    default_path = change_path('ssh_key', default_path='/home/admin/.ssh')
    with cd():
        sudo('echo " " >> authorized_keys')     # used for formatting purpose
        sudo('echo "# %s" >> authorized_keys' % key_comment)
        sudo('echo "%s" >> authorized_keys' % target_key)

def replace_config(vim_sig, bash_sig):
    """ 将当前用户指定路径下的bashrc和vimrc的内容替换目标服务器上
        admin用户和root用户的相关配置
    """
    default_path = change_path('config', default_path='~/')

    if vim_sig:
        local("scp %s.vimrc admin@%s:~/vimrc" % (default_path, env.host))
        sudo("cp /home/admin/.vimrc /home/admin/vimrc_backup")
        sudo("cp /home/admin/vimrc /home/admin/.vimrc")
        sudo("cp /root/.vimrc /root/vimrc_backup")
        sudo("cp  /home/admin/vimrc /root/.vimrc")
        sudo("rm /home/admin/vimrc")

    if bash_sig:
        local("scp %s.bashrc admin@%s:~/bashrc" % (default_path, env.host))
        sudo("cp /home/admin/.bashrc /home/admin/bashrc_backup")
        sudo("cp /home/admin/bashrc /home/admin/.bashrc")
        sudo("cp /root/.bashrc /root/bashrc_backup")
        sudo("cp  /home/admin/bashrc /root/.bashrc")
        sudo("rm /home/admin/bashrc")


def upload_config(vim_sig=True, bash_sig=True):
    """ 将当前用户指定路径下的bashrc和vimrc的内容append到目标机器的
        admin用户和root用户相应config下
    """
    default_path = change_path('config', default_path='~/')

    if vim_sig:
        local("scp %s.vimrc admin@%s:~/vimrc" % (default_path, env.host))
        sudo("cat /home/admin/vimrc >> /home/admin/.vimrc")
        sudo("cat /home/admin/vimrc >> /root/.vimrc")
        sudo("rm /home/admin/vimrc")

    if bash_sig:
        local("scp %s.bashrc admin@%s:~/bashrc" % (default_path, env.host))
        sudo("cat /home/admin/bashrc >> /home/admin/.bashrc")
        sudo("cat /home/admin/bashrc >> /root/.bashrc")
        sudo("rm /home/admin/bashrc")


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
