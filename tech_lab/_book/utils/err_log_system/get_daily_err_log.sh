LOG_PATH=''
cd $LOG_PATH
host_name=$(hostname)
rm $host_name"500_log"; grep -h -B 25 "500 GET" err_en_app.log* >> $host_name"500_log"
grep "500 GET" $host_name"500_log" > $host_name"pure_500"
rm $host_name"uncaught_log"; grep "Uncaught" err_en_app.log* >> $host_name"uncaught_log"
