PROGNAME=$(basename  $0)

error_exit()
{
        timestamp="$(date +%Y%m%d-%H:%M:%S)"
            x_info=$(echo "Error_${PROGNAME}:Line_${1:-"null"}_")   # 没有传行号的话，行号是null
                zeta=$x_info$timestamp
                    touch "$zeta"  # 此处可以将ceta的信息传入某个日志文件，而非创建一个空文件
                        exit 1
                    }
# Uncomment code below to see example effect
# cd Nostradamus || error_exit $LINENO
