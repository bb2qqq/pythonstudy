# 根据实际情况调整的fabric脚本路径
$SCRIPT_PATH="/data/admin/temp/manage_scripts/fabric/"
# 根据实际情况调整的错误日志存放目录
$ERR_LOG_PATH='/data/admin/superhero/error_log/'

cd $SCRIPT_PATH
/usr/local/bin/fab get_daily_error_log


cd $ERR_LOG_PATH
today=$(date +"%Y-%m-%d")
rm 500_log; cat *500_log >> 500_log
rm pure_500; cat *pure_500 >> pure_500
rm uncaught_log; cat *uncaught_log >> uncaught_log
/usr/local/bin/python2.7 error_log_filter.py | tee err_report
cat err_report >> all_day_report

mv 500_log $ERR_LOG_PATH"reports/"$today"500_log"
mv pure_500 $ERR_LOG_PATH"reports/"$today"pure_500"
mv uncaught_log $ERR_LOG_PATH"reports/"$today"uncaught_log"
mv err_report $ERR_LOG_PATH"reports/"$today"err_report"

rm *500_log
rm *pure_500
rm *uncaught_log
