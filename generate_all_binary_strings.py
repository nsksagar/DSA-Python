def generate(n, curr, result):

    if len(curr) == n:
        result.append(curr)
        return 
    
    generate(n, curr + '0', result)

    if not curr or curr[-1] != '1':
        generate(n, curr + '1', result)


if __name__ == '__main__':

    

    n = int(input('Enter the input length n : '))

    result = [ ]

    curr = ''

    generate(n, curr, result)

    print(f'All binary strings of length {n}, are:{result}')