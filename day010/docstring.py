# multiple return values
from unittest.result import failfast


def format_name2(f_name, l_name):
    '''
    Take a first and last name and format it to return 
    the title case version of the name
    '''
    if len(f_name) < 1:
        return None
    format_f_name = f_name.title()
    format_l_name = l_name.title()

    return format_f_name, format_l_name

print(format_name2("", "CESAR"))

# ctrl + /: add "#" for multiple lines