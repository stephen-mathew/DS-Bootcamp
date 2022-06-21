### Stephen Mathew
### Python Basics Assignment 2
### 21-June-2022

**1.What are the two values of the Boolean data type? How do you write them?**

Ans: _`True` and `False`_

- - -

**2. What are the three different types of Boolean operators?**

Ans: _`and`,`or` and `not`_

- - -

**3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).**

Ans: 
| x     | y     | Result with `and` |
|-------|-------|-------------------|
| True  | True  | True              |
| True  | False | False             |
| False | True  | False             |
| False | False | False             |

| x     | y     | Result with `or` |
|-------|-------|------------------|
| True  | True  | True             |
| True  | False | True             |
| False | True  | True             |
| False | False | False            |

| x     | Result with `not` |
|-------|-------------------|
| True  | False             |
| False | True              |




- - -

**4. What are the values of the following expressions?**
> (5 > 4) and (3 == 5)
> not (5 > 4)
> (5 > 4) or (3 == 5)
> not ((5 > 4) or (3 == 5))
> (True and True) and (True == False)
> (not False) or (not True)

Ans: 
_False_
_False_
_True_
_False_
_False_
_True_

- - -

**5. What are the six comparison operators?**

Ans: _`==`,`!=`,`>`,`<`,`>=`,`<=`_

- - -

**6. How do you tell the difference between the equal to and assignment operators? Describe a condition and when you would use one.**

Ans: _The Assignment operator has a single `=` whereas the Equal to operator has 2 `=` symbols. The Assignment operator `==` is used when we need to assign a value to a variable whereas the Equal To `=` operator is used when we would like to do a comparison between 2 operands._

- - -

**7. Identify the three blocks in this code:**
> spam = 0
> if spam == 10:
> print('eggs')
> if spam > 5:
> print('bacon')
> else:
> print('ham')
> print('spam')
> print('spam')

Ans: _In the code, there is one `if` block looking for the condition `spam == 10`, another `if` block looking for the condition when `spam > 5` and a corresponding block when `spam <= 5`_

- - -

**8. Write code that prints `Hello` if `1` is stored in `spam`, prints `Howdy` if `2` is stored in `spam`, and prints `Greetings!` if anything else is stored in `spam`.**

Ans: 
> if spam == 1:
> &nbsp;&nbsp;&nbsp;print('Hello')
> elif spam == 2:
> &nbsp;&nbsp;&nbsp;print('Howdy')
> else:
> &nbsp;&nbsp;&nbsp;print('Greetings!')

- - -

**9.If your programme is stuck in an endless loop, what keys you’ll press?**

Ans: _I will use `Ctrl+C`. In a Jupyter notebook, the Kernel can be terminated or restarted._

- - -

**10. How can you tell the difference between `break` and `continue`?**

Ans: _`break` will break and exit out of the current loop's execution ignoring any subsequent statements in the current loop's iteration and ignoring any further iterations, whereas `continue` will only ignore any subsequent statement executions in the current loop's iteration and will start executing the next iteration of the same loop._

- - -

**11. In a for loop, what is the difference between `range(10)`, `range(0, 10)`, and `range(0, 10, 1)`?**

Ans: _`range(10)`, `range(0, 10)`, and `range(0, 10, 1) will iterate through all integers from 0 to 9 and produce the same behaviour._

- - -

**12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.**

Ans: 
> for i in range(1,11):
> &nbsp;&nbsp;&nbsp;print(i)

> i = 1
> while i <=10:
> &nbsp;&nbsp;&nbsp;print(i)
> &nbsp;&nbsp;&nbsp;i+=1

- - -

**13. If you had a function named `bacon()` inside a module named `spam`, how would you call it after importing `spam`?**

Ans: _from spam import bacon_

- - -
