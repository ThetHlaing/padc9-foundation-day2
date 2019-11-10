##Create a split string decorator and apply to say hi function

def uppercase_decorator(function):
    print("in the uppercase decorator function")
    def wrapper():
        print("in the uppercase decorator wrapper function")
        result = function()
        
        make_uppercase = result.upper()
        print('Making uppercase')
        
        return make_uppercase

    return wrapper


def split_string_decorator(function):
    print("in the split string decorator")
    def wrapper():
        print("in the split string wrapper")
        func = function()

        splitted_string = func.split()
        print("Spliting the string")

        return splitted_string
    
    return wrapper


# @split_string_decorator
@uppercase_decorator
def say_hi():
    print("in the target function")
    return "hello there, mg mg"

print(say_hi())