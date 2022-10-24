# simple function
    # def function():
        # do something

    # def function(something):
        # do this with something


def some_func():
    result = 3 * 2
    return result

#some_func()
#print(some_func())

def format_name(f_name, l_name):
    format_f_name = f_name.title()
    format_l_name = l_name.title()

    return format_f_name + " " + format_l_name

print(format_name("leonardo", "CESAR"))


# multiple return values
def format_name2(f_name, l_name):
    if f_name == "":
        return None
    format_f_name = f_name.title()
    format_l_name = l_name.title()

    return format_f_name, format_l_name

print(format_name2("", "CESAR"))