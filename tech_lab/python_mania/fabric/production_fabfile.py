import datetime
from fabric.api import *
env.hosts=[ 'host1',
            'host2',
            ]

yesterday = datetime.datetime.now().date() - datetime.timedelta(days=1)

DATE_STAMP = "{dt.year}{dt.month}{dt.day}".format(dt=yesterday)
LOG_PATH = "/my/log_path/"
TEMP_PATH = '/home/admin/temp/action_log/'
LOCAL_STORE_PATH = '/home/admin/temp/action_log/'
JAN_STAMP = '20151'
DEC_STAMP = '201412'

index_pool = range(100, 200)
used_pool = []


def get_history_action_log():
    global index_pool, used_pool

    for index in index_pool:
        if index not in used_pool:
            server_fix = str(index)
            used_pool.append(index)
            break

    sudo("mkdir -p %s" % TEMP_PATH)
    with cd(LOG_PATH):
        sudo("zip %s.zip  *%s* *%s*" %(server_fix, JAN_STAMP, DEC_STAMP))
        sudo("cp %s.zip %s" %(server_fix, TEMP_PATH ))
    local("scp %s:%s* %s" % (env.host, TEMP_PATH, LOCAL_STORE_PATH))

    with cd(TEMP_PATH):
        sudo("rm -f %s.zip" % server_fix)
