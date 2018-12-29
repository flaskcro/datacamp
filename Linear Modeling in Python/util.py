import inspect

def get_source(function_name):
    lines = inspect.getsource(function_name)
    print(lines)