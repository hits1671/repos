'''
File Extension Extractor

Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java

'''

print("enter filename with extension")
filename = input()
print(filename.split(".")[1])

