source '/home/admin/local_env_config.py'
cd $CODE_PATH"logs/"

host_name=$(hostname)"_"$(hostid)"_"


yesterday=$(date +"%Y-%m-%d" --date='1 days ago')
tomorrow=$(date +"%Y-%m-%d" --date='next day')

rm $host_name"500_log";
rm $host_name"uncaught_log";

find -newermt $yesterday ! -newermt $tomorrow -name "err*log*" -exec  grep -h -B 25 "500 GET" {} >> $host_name"500_log" \;
find -newermt $yesterday ! -newermt $tomorrow -name "err*log*" -exec  grep "Uncaught" {} >> $host_name"uncaught_log" \;

grep "500 GET" $host_name"500_log" > $host_name"pure_500"
