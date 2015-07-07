import re
from dateutils import parser

time_pattern = re.compile(r'[.*?+0800]')
http_pattern = re.compile(r'GET.*HTTP/[0-9.]*" [0-9]*'
current_file = open('my_nginx_log', 'r')

for line in current_file:
    log_time_str = time_pattern.match(line).group()
    log_datetime = parser.parse(log_time_str, fuzzy=True)
    http_str = http_pattern.match(line).group()
    http_str_list = http_str.split(' ')
    method, content, protocol_version, return_status = http_str_list
