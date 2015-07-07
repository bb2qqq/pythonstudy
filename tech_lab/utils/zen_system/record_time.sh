LOG_FILE="/users/zen1/git_test/log/cmge_log"
record_time()
{
    CUR_TIME=`DATE +%y%M%D-%h:%m:%s`
    echo $CUR_TIME"_"$1 >> $LOG_FILE
}

record_time loveme
