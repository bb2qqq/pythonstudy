PROGNAME=$(basename  $0)
datestamp="$(date +%Y%m%d --date='yesterday')"

error_exit()
{
        timestamp="$(date +%Y%m%d-%H:%M:%S)"
            x_info=$(echo "Error_${PROGNAME}:Line${1:-"Ada"}_")
                zeta=$x_info$timestamp
                    touch "$zeta"
                        exit 1
                    }

cd Nostradamus || error_exit $LINENO
