#1) Write a class for N-dimensional vector. Implement operations for addition, subtraction, dot and cross product, unit vector in the same direction
#2) Write a function - Given two sorted lists, create a merged sorted list

def hanoi(n, source, helper, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        print ("A", source, helper, target)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
            print ("B", source, helper, target)
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)
        print ("C", source, helper, target)
        
source = [3,2,1]
target = []
helper = []
hanoi(len(source),source,helper,target)

print source, helper, target
