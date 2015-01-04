:%g/pattern/d                          # find line contains pattern in this file and delete that line

:%s/\(.*\)-\(.*\)-/\2-\1-/g            # 找到用 - 符号分隔的两段内容，并把它们的顺序交换
