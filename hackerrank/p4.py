#!/bin/python3
if __name__ == '__main__':
    #n = int(input())
    #arr = map(int, input().split())
    n = 5
    arr = [2, 3, 6, 6, 5]
    # arr_sorted = list(reversed(sorted(arr)))
    
    # i = max(arr_sorted)

    # for numero in arr_sorted:
    #     if numero < i:
    #         print(numero)
    #         break


    arr_sorted = [ i for i in reversed(sorted(arr)) if i < max(arr) ]
    
    print(arr_sorted[0])