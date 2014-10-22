PROGNAME=$(basename $0)
error_exit()
{
    x_info=$(echo "Error_${PROGNAME}:Line${1:-"Sweet Error"}")
    touch $x_info
    exit 1
}

cd labaa || error_exit $LINENO
