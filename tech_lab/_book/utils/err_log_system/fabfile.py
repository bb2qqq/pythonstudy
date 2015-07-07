import datetime
from fabric.api import *

env.hosts=[]

ERROR_LOG_PATH = '/data/sites/backend_english/logs/'
LOCAL_ERROR_LOG_STORE_PATH = '/data/admin/superhero/error_log/'

def get_daily_error_log():
    local("scp admin@%s:%s*500_log %s" % (env.host, ERROR_LOG_PATH, LOCAL_ERROR_LOG_STORE_PATH))
    local("scp admin@%s:%s*pure_500 %s" % (env.host, ERROR_LOG_PATH, LOCAL_ERROR_LOG_STORE_PATH))
    local("scp admin@%s:%s*uncaught_log %s" % (env.host, ERROR_LOG_PATH, LOCAL_ERROR_LOG_STORE_PATH))
