def add(a, b):
    return a + b

def main():
    expr = input('Enter expression.\n').strip()
    a_str, op, b_str = expr.split()

    try:
        a, b = float(a_str), float(b_str)
    except ValueError:
        print('Error: You must enter numbers.')
        return
    
    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    elif op == '/':
        result = div(a, b)
    else:
        result = 'Unsupported operator. Only one of: + - * /'
    
    print(result)

if __name__ == "__main__":
    main()