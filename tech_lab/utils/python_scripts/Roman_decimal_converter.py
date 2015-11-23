# coding: utf-8

roman_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roman_char_rank = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
int_roman_map = {1: ('I', 'V', 'X'), 10: ('X', 'L', 'C'), 100: ('C', 'D', 'M'), 1000: ('M', '?', '?')}



def roman_to_int(s):
    """ 输入罗马字符，返回相应十进制数字 """
    index = 0
    total_value = 0
    while index < len(s):
        current_char = s[index]
        current_char_value = roman_int_map[current_char]

        if index + 1 == len(s):     # 指针移到最后一个字符
            total_value += current_char_value
            break

        next_char = s[index + 1]
        next_char_value = roman_int_map[next_char]

        if roman_char_rank.index(current_char) >= roman_char_rank.index(next_char):
            total_value += current_char_value
            index += 1
        else:
            total_value += ( next_char_value - current_char_value)
            index += 2

    return total_value

# 要解决10进制到罗马数字的转换。首先我们要把10进制各个位上的值都求出来

def int_to_roman(number, allow_minus=True):
    """ 输入int, 返回对应的罗马字符。
        默认开启减法表达，allow_minus=False关闭减法表达。该功能尚未完成（TODO)
        只支持1万以内的数字转换。
    """
    if not type(number) == int or not 1 <= number <= 9999:
        print "只支持1至9999间的整数转换。"
        return

    # 将1905转成[1000, 900, 0, 5]这样的列表
    expression = str(number)
    expr_length = len(expression)
    base = 10
    value_list = []

    for index, digit in enumerate(expression):
        digit_rank = abs(index - expr_length)
        digit_value = int(digit) * (base**(digit_rank-1))
        value_list.append(digit_value)

    # 将形式如同[1000, 900, 0, 5]的列表转成罗马数字
    roman_expression = ''
    for decimal_value in value_list:
        first_digit = int(str(decimal_value)[0])
        # 罗马数字里没有0的表示
        if first_digit == 0:
            continue

        digit_numbers = decimal_value/first_digit
        unit_1_char, unit_5_char, unit_10_char = int_roman_map[digit_numbers]
        if digit_numbers == 1000:
            agent_expr = unit_1_char * first_digit
        else:
            if first_digit == 4:
                agent_expr = unit_1_char + unit_5_char
            elif first_digit == 9:
                agent_expr = unit_1_char + unit_10_char
            elif first_digit < 5:
                agent_expr = unit_1_char * first_digit
            else:
                first_digit -= 5
                agent_expr = unit_5_char + unit_1_char * first_digit

        roman_expression += agent_expr

    return roman_expression

def test_conversion():
    for i in range(1, 10000):
        if i != roman_to_int(int_to_roman(i)):
            print i, "TEST FAILED!"
            break
    else:
        print "TEST PASSED"
