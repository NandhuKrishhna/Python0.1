def sum_all(*args):
    return sum(args)
print(sum_all(1,2,3))  # 6

def print_info(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
print_info(name="Alice", age=25)

name = "Nandhu";
print(name.split())