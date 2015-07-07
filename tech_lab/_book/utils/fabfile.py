# coding:utf-8
import datetime
from fabric.api import *
env.hosts=[
"admin@23.91.98.172",    # 英文版测试服
"admin@119.81.219.36",   # 英文版iOS提审服
"admin@124.205.35.139",  # 土耳其测试服
"admin@119.81.219.40",   # 英文管理服
"admin@45.113.70.165",   # 美国版测试服
"admin@45.113.71.125",   # 美国iOS提审服
"admin@203.90.236.146",  # 台湾管理服
"admin@85.195.78.225",   # 土耳其iOS提审服
]

@runs_once
def change_path(name, default_path):
    change_path_hint = 'Type in CHANGE to change %s path, other to continue: ' % name
    print 'The default %s path is %s' %  (name, default_path)

    change_path_choice = raw_input(change_path_hint)

    if change_path_choice in ['c', 'C', 'CHANGE', 'change', 'Change']:
        default_path = raw_input('Please enter new path of %s:' % name)

    return default_path

def add_ssh_key(ssh_key=None):
    target_key = ssh_key or raw_input('Please enter your ssh key:\n')
    key_comment = raw_input('Please type your comment for the ssh key:')

    default_path = change_path('ssh_key', default_path='/home/admin/.ssh')
    with cd():
        sudo('echo " " >> authorized_keys')     # used for formatting purpose
        sudo('echo "# %s" >> authorized_keys' % key_comment)
        sudo('echo "%s" >> authorized_keys' % target_key)

def replace_config():
    """ 将当前用户指定路径下的bashrc和vimrc的内容替换目标服务器上
        admin用户和root用户的相关配置
    """
    default_path = change_path('config', default_path='~/')

    local("scp %s.vimrc admin@%s:~/vimrc" % (default_path, env.host))
    local("scp %s.bashrc admin@%s:~/bashrc" % (default_path, env.host))
    sudo("cp /home/admin/vimrc /home/admin/.vimrc")
    sudo("cp /home/admin/bashrc /home/admin/.bashrc")
    sudo("cp  /home/admin/vimrc /root/.vimrc")
    sudo("cp  /home/admin/bashrc /root/.bashrc")
    sudo("rm /home/admin/vimrc")
    sudo("rm /home/admin/bashrc")

def upload_config():
    """ 将当前用户指定路径下的bashrc和vimrc的内容append到目标机器的
        admin用户和root用户相应config下
    """
    default_path = change_path('config', default_path='~/')

    local("scp %s.vimrc admin@%s:~/vimrc" % (default_path, env.host))
    local("scp %s.bashrc admin@%s:~/bashrc" % (default_path, env.host))
    sudo("cat /home/admin/vimrc >> /home/admin/.vimrc")
    sudo("cat /home/admin/bashrc >> /home/admin/.bashrc")
    sudo("cat /home/admin/vimrc >> /root/.vimrc")
    sudo("cat /home/admin/bashrc >> /root/.bashrc")
    sudo("rm /home/admin/vimrc")
    sudo("rm /home/admin/bashrc")

def replace_config():
    """ 将当前用户指定路径下的bashrc和vimrc的内容append到目标机器的
        admin用户和root用户相应config下
    """
    default_path = change_path('config', default_path='~/')

    local("scp %s.vimrc admin@%s:~/vimrc" % (default_path, env.host))
    sudo("cp /home/admin/vimrc /home/admin/.vimrc")
    sudo("cp /home/admin/vimrc /root/.vimrc")
    sudo("rm /home/admin/vimrc")


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

