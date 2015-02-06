MY_HOST='127.0.0.1'
MY_PASSWD='goodpassword'

for x in 0
do
    k=$(( x + 1 ))
    today=$(date +"%Y-%m-%d 00:00" --date=$x' days ago')
    yesterday=$(date +"%Y-%m-%d 00:00" --date=$k' days ago')
    time_subfix=$(date +"%Y-%m-%d" --date=$k' days ago')
    for j in {0..99};do mysql -h$MY_HOST -uroot -p$MY_PASSWD genesis -e"select * from my_table_$j where
         order_time >= '$yesterday' and order_time <= '$today' " >> /my_path/table_prefix_\_$time_subfix;done

done
