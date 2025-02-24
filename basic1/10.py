'''
Number Expansion Calculator

Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
'''

print("enter a number")
n=int(input())
n1 = int("%s%s" %(n,n))
n2 = int("%s%s%s" %(n,n,n))

print(n+n1+n2)
