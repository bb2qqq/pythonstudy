
* if List_A exists, iter over List_A, otherwise iter over List_B

        for i in List_A or List_B:
            print i

* Formate Year/Month/Day without 0 padding

        import datetime
        "{dt.year}{dt.month}{dt.day}".format(dt=datetime.datetime.now())

* delete one item from a dict

        my_dict.pop(key, default_value)

>   This will delete the key-value pair if key in my_dict, otherwise defualt_value will be returned, so you won't get an error when key isn't in my_dict
