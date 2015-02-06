import datetime
from fabric.api import *
from fabric.contrib.console import confirm
env.hosts=['admin@203.90.236.146', 'qwe', 'qweq', 'qweqwe']


def zen_test():
    for i in env.hosts:
        local("echo 'BB' >> fabfab")
#    run('touch test_fab_aplha')
#    run('echo "ABF" >> test_fab')

def deploy():
    code_dir = '~/git_zen'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone user@vcshost:/path/to/repo/.git %s" % code_dir)
    with cd(code_dir):
        run('git log')
        run('touch app.wsgi')


def zen():
    run("echo 'Zen is great'")



def test():
    with settings(warn_only=True):
        result = local('./manage.py test my_app', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def prepare_deploy():
    local("./manage.py test my_app")
    local("git add -p && git commit")
    local("git push")
