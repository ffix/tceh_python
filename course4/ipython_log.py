# IPython log file

get_ipython().run_line_magic('logstart', '')
def my_function():
    print('I am a function')


print(my_function)
print('Functions are objects', isinstance(my_function, object))
l = [0, 'str', True]
l
l.append(my_function)
l
l[-1]
l[-1]()
c = l[-1]
c()
def call_passed_function(incoming):
    print('Calling!')
    incoming()
    print('Called!')
    
call_passed_function(my_function)
def incr(x):
    return x+1
def call_passed_function(incoming, y):
    print('Calling!')
    incoming(y)
    print('Called!')
    
    
#call_passed_function(incr(1))
#call_passed_function(incr, 1)
# You can not call uncallable things:

try:
    d = 2
    d()  # but you can try
except TypeError as e:
    print('It is not a function', e)
    
f = 5
f()
print(callable(len), callable(45), callable(callable))
def return_min_function():
    return min
test = return_min_function()
min_value = test(4, 5, -9, 12)
print('Min values is', min_value)
sum(1, 3)
def custom_sum(x, y):
    return x + y
def curry(custom_sum, x):
    def new_custom_sum(y):
        custom_sum(x, y)
        
def curry(custom_sum, x):
    def new_custom_sum(y):
        custom_sum(x, y)
    return new_custom_sum
    
custom_sum(5, 6)
custom_sum(5, 8)
sum_5 = curry(custom_sum, 5)
sum_5
sum_5(7)
def curry(custom_sum, x):
    def new_custom_sum(y):
        return custom_sum(x, y)
    return new_custom_sum
    
sum_5 = curry(custom_sum, 5)
sum_5(7)
sum_6 = curry(custom_sum, 6)
sum_6
sum_6(9)
sum_5(9)
# new_sum(x, y) -> x+y
# new_5(y) -> 5 + y
def curry(incoming_fun, x):
    def n_fun(y):
        return incoming_fun(x, y)
    return n_fun

    
curry(new_sum, 10)
curry(custom_sum, 10)
curry(custom_sum, 11)
incr_10 = curry(custom_sum, 10)
incr_20 = curry(custom_sum, 20)
incr_10
incr_20
incr_10(1)
incr_20(1)
incr_10 == incr_20
x = 5
def foo():
    x = 7
    return x
x
foo()
def scoped_function(arg):
    value = arg * 10
    print(value)

scoped_function(2)
SOME_VAR = 'value'

def print_var():
    print(SOME_VAR)

print_var()
SOME_VAR = 'value'

def modify_var():
    SOME_VAR = SOME_VAR
    try:
        SOME_VAR += '_extra'
    except UnboundLocalError as e:
        print('Error', e)

modify_var()
print(SOME_VAR)


# BUT if you really want....
def modify_var():
    global SOME_VAR
    try:
        SOME_VAR += '_extra'  # Do not do this. REALLY, JUST DO NOT THIS!!!
    except UnboundLocalError as e:
        print('Error', e)

modify_var()
print(SOME_VAR)


# BUT if you really want....
def modify_var():
    global SOME_VAR
    try:
        SOME_VAR += '_extra'  # Do not do this. REALLY, JUST DO NOT THIS!!!
    except UnboundLocalError as e:
        print('Error', e)

modify_var()
print(SOME_VAR)
GLOBAL_LIST = []

def append_to_list(item):
    print('Adding', item)
    GLOBAL_LIST.append(item)
    
append_to_list(1)
append_to_list(2)
print(GLOBAL_LIST)
Z = 5


def bar(y):  # y - bounded
    x = 1      # x - bounded

    print(Z)   # Z - free

    def foo():
      print(x + y + Z)  # x, y, z - free here

    foo()
    
x = 5
def ll()"
Z = 5


def bar(y):  # y - bounded
    x = 1      # x - bounded

    print(Z)   # Z - free

    def foo():
      print(x + y + Z)  # x, y, z - free here

    foo()
    
Z = 5


def bar(y):  # y - bounded
    x = 1      # x - bounded

    print(Z)   # Z - free

    def foo():
      print(x + y + Z)  # x, y, z - free here

    foo()
    
x
bar()
bar(2)
Z = 5


def bar(y):  # y - bounded
    x = 1      # x - bounded

    print(Z)   # Z - free

    def foo():
      x = 9
      print(x + y + Z)  # x, y, z - free here

    val = foo()
    
def outer_function(value):
    def some_inner():
        print('Value was', value)
    return some_inner

v = outer_function('some')
print('it is a function', v, callable(v))
v()
def pretty_print(arg):
    def print_stars():
        print('-' * 8)
        print('*' * 8)

    print_stars()
    print(arg)
    print_stars()

pretty_print(12)
