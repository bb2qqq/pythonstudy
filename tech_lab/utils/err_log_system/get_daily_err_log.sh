source '/home/admin/local_env_config.py'
cd $CODE_PATH"logs/"

host_name=$(hostname)"_"$(hostid)"_"

today=$(date +"%Y-%m-%d")
yesterday=$(date +"%Y-%m-%d" --date='1 days ago')

rm $host_name"500_log";
rm $host_name"uncaught_log";

find -newermt $yesterday ! -newermt $today -name "err*log*" -exec  grep -h -B 25 "500 GET" {} >> $host_name"500_log" \;
find -newermt $yesterday ! -newermt $today -name "err*log*" -exec  grep "Uncaught" {} >> $host_name"uncaught_log" \;

grep "500 GET" $host_name"500_log" > $host_name"pure_500"
