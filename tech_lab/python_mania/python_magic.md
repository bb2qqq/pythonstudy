
### Arithmatic operation ###

* convert a string coded in base-n system into decimal number

      int(str, base_n)
      e.g: int('0xAE', 16)

## DATA STRUCTURE ##


#### SET OPERATION ####

    UNION               s | t           #  all elements in s and t, except duplicate
    INTERSECTION        s & t           #  elements that are in s and t
    DIFERENCE           s - t           #  element in s but not in t
    SYMMETRIC_DIFFER    s ^ t           #  equal to (s - t) | (t - s), means that element in t or s that are not appeared in both set



* if List_A exists, iter over List_A, otherwise iter over List_B

        for i in List_A or List_B:
            print i

* Formate Year/Month/Day without 0 padding

        import datetime
        "{dt.year}{dt.month}{dt.day}".format(dt=datetime.datetime.now())

* delete one item from a dict

        my_dict.pop(key, default_value)

>   This will delete the key-value pair if key in my_dict, otherwise defualt_value will be returned, so you won't get an error when key isn't in my_dict

