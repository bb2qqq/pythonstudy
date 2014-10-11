I_used_goods_elevator = False
goods_elevator = 1

def use_elevator(elevator_number):
    if elevator_number == 1:
        I_used_goods_elevator = False
    else:
        I_used_goods_elevator = True

while not I_used_goods_elevator:
    use_elevator(goods_elevator)
