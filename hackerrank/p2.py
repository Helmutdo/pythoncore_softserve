#!/bin/python3
if __name__ == '__main__':

    n = int(input()) 
    lst = [i==i[::-1] for i in input().split()]
    
    print(any(lst))
        