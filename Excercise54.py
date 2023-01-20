"""--------------------------------------------------------------------------------
Exercise 5.4.
What is the output of the following program? Draw a stack diagram that shows the
state of the program when it prints the result.

    def recurse(n, s):
        if n == 0:
            print(s)
        else:
            recurse(n-1, n+s)

    recurse(3, 0)

1.  What would happen if you called this function like this:
    recurse(-1, 0) ?

2.  Write a docstring that explains everything someone would need to know in
    order to use this function (and nothing else).
-------------------------------------------------------------------------------------"""

"""
The output of the program is s+{n+(n-1)+(n-2)+ ....... +1}

For example:
if s=0 and n = 3; 0+(3+2+1) = 6 will be printed.
if s=2 and n = 3; 2+(3+2+1) = 8 will be printed.


Stack Diagram:

__main__ :
    None

recurse:
    n ---> 3
    s ---> 0
    
recurse:
    n ---> 2
    s ---> 3

recurse:
    n ---> 1
    s ---> 5

recurse:
    n ---> 0
    s ---> 6

"""

# Answer1:
"""
recurse(-1, 0) will be infinite recursion.

"""

# Answer2
def recurse(n, s):
    '''Recursive function for getting the value of n and s
        and printing s+{n+(n-1)+(n-2)+ ....... +1}

    n -> positive integer;
    s -> integer.
    '''
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)


