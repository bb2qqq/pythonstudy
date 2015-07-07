cd /data/admin/superhero/error_log
today=$(date +"%Y-%m-%d")
rm 500_log; cat *500_log >> 500_log
rm pure_500; cat *pure_500 >> pure_500
rm uncaught_log; cat *uncaught_log >> uncaught_log
/usr/local/bin/python2.7 error_log_filter.py | tee err_report
cat err_report >> all_day_report

mv 500_log /data/admin/superhero/error_log/reports/$today"500_log"
mv pure_500 /data/admin/superhero/error_log/reports/$today"pure_500"
mv uncaught_log /data/admin/superhero/error_log/reports/$today"uncaught_log"
mv err_report /data/admin/superhero/error_log/reports/$today"err_report"

rm *500_log
rm *pure_500
rm *uncaught_log
