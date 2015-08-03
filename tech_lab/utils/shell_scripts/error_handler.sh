PROGNAME=$(readlink -f "$0")
SCRIPT_ERR_LOG_PATH="/Users/zen1/git_test/script_err_log"


error_exit()
{
        timestamp="$(date +%Y%m%d-%H:%M:%S)"
            x_info=$(echo "Error_${PROGNAME}:Line_${1:-"null"}_")   # 没有传行号的话，行号是null
                zeta=$x_info$timestamp
                    echo "$zeta" >> $SCRIPT_ERR_LOG_PATH  # 此处可以将ceta的信息传入某个日志文件，而非创建一个空文件
                        exit 1
                    }
# Uncomment code below to see example effect
# cd Nostradamus || error_exit $LINENO
