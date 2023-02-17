def var_print():
    number = 42
    string = "42"
    string2 = "quarante-deux"
    floater = 42.0
    boolean = True
    a_list = [42]
    a_dict = {42: 42}
    a_tuple = (42,)
    a_set = set()
    hat = "has a type"
    print(number, hat, type(number))
    print(string, hat, type(string))
    print(string2, hat, type(string2))
    print(floater, hat, type(floater))
    print(boolean, hat, type(boolean))
    print(a_list, hat, type(a_list))
    print(a_dict, hat, type(a_dict))
    print(a_tuple, hat, type(a_tuple))
    print(a_set, hat, type(a_set))


if __name__ == '__main__':
    var_print()