def subtract(x, y, output='return'):
    result = x - y
    if output == 'print':
        print(result)
    elif output == 'return':
        return result
    else:
        raise ValueError("Invalid output option. Choose 'print' or 'return'. Please read the SM Docs for more info.")

def add(x, y, output='return'):
    result = x + y
    if output == 'print':
        print(result)
    elif output == 'return':
        return result
    else:
        raise ValueError("Invalid output option. Choose 'print' or 'return'. Please read the SM Docs for more info.")

def multiply(x, y, output='return'):
    result = x * y
    if output == 'print':
        print(result)
    elif output == 'return':
        return result
    else:
        raise ValueError("Invalid output option. Choose 'print' or 'return'. Please read the SM Docs for more info.")

def divide(x, y, output='return'):
    result = x / y
    if output == 'print':
        print(result)
    elif output == 'return':
        return result
    else:
        raise ValueError("Invalid output option. Choose 'print' or 'return'. Please read the SM Docs for more info.")