def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        temp = []
        for i in items:
            temp_key = i.get(args[0], "None")
            if temp_key != "None":
                temp.append(temp_key)
        return temp
    else:
        k = []
        for i in items:
            temp = {}
            for j in args:
                temp_key = i.get(j, "None")
                if temp_key != "None":
                    temp.update({j: temp_key})
            k.append(temp)
        print(*k, sep = ", ")