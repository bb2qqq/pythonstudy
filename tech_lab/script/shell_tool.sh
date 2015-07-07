# 过滤supervisor产生的python日志中的500 错误信息
awk '/Uncaught/{a=1} /500 GET/{a=1} /200 GET/{a=0} a' log_file > error_log
