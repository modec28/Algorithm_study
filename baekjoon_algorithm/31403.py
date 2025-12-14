from typing import Union

def sum(a: Union[int, str], b:Union[int, str], with_string: bool= True):
    if not with_string:
        a, b = int(a), int(b)
    return a + b

def subtract(a: Union[int, str], b:Union[int, str], with_string: bool= True):
    return int(a) - int(b) 
    

A = input()
B = input()
C = input()
print(subtract(sum(A, B, with_string=False), C, with_string=False))
print(subtract(sum(A, B), C))