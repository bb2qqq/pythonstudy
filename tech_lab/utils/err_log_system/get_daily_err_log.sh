source '/home/admin/local_env_config.py'
cd $CODE_PATH"logs/"
host_name=$(hostname)
rm $host_name"500_log"; grep -h -B 25 "500 GET" err_* >> $host_name"500_log"
grep "500 GET" $host_name"500_log" > $host_name"pure_500"
rm $host_name"uncaught_log"; grep "Uncaught" err_* >> $host_name"uncaught_log"
