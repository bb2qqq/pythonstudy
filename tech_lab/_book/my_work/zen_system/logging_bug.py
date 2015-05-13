import datetime
import traceback

def logging_bug():
    """ Recording bug raise time and reason """
    traceback_info = repr(traceback.format_exc())
    # formatting traceback info
    tb_info_list = traceback_info.split('\\n')
    now = str(datetime.datetime.now())

    with open('debug_log', 'a') as debug_log:
        debug_log = open('debug_log', 'a')
        debug_log.write('\n%s\n' % now)
        for line in tb_info_list:
            line = line.replace("\\'", "'")
            debug_log.write('%s\n' % line)

# Example
if __name__ == '__main__':
    try:
        fuck
    except:
        logging_bug()
