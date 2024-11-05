#section 1

'''
def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n - 1)




if __name__ == '__main__':
    print(find_sum(5))
    '''
#section 2

#0,1,1,2,3,5,8,13,21,34


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    print(fib(5))