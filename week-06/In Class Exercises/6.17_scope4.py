# Cris Ramirez
# demonstrates enclosed scope

def outer_func():
    x = 'YearUp'
    def inner_func():
        print(x)
    inner_func()
outer_func()