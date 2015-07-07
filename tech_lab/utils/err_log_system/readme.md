get_daily_err_log.sh:  用crontab部署在app server上，用于生成初步过滤后的错误日志文件
process_error_log.sh:  进行日志的二次过滤，整理归档
fabfile.py:  执行具体的拉取任务，将app server上的日志拉到管理机指定目录下
error_log_filter.py:  日志二次过滤中的组件脚本, 规则需要依据http请求的规则进行动态调整
