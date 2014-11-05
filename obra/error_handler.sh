PROGNAME=$(basename  $0)
error_exit()
{
    timestamp="$(date +%Y%m%d-%H:%M:%S)"
    x_info=$(echo "Error_${PROGNAME}:Line${1:-"Ada"}_")
    zeta=$x_info$timestamp
    touch "$zeta"
    exit 1
}

cd labaa || error_exit $LINENO
