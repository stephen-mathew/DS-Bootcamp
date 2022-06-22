# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def test1():
    print("this is the first time I am using pycharm")

def fibo(n):
	l=[]
	a, b = 0, 1
	l.append(a)
	l.append(b)
	for i in range(n):
		a, b = b, a+b
		l.append(b)
	return l

print(fibo(10))



