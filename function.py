def greet(name):
    message = f"Hello, {name}"
    return message

def append_to_list(item , list=[]):
    list.append(item)
    return list



def sum_number(*args):
    print(args[1])


def print_info(**kwargs):
    print(kwargs)


square = lambda x : print(x)
square("Nandhu Krishna");
