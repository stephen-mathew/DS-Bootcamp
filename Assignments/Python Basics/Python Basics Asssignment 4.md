### Stephen Mathew
### Python Basics Assignment 4
### 22-June-2022

**Q1. What exactly is `[]`?**

Ans: _`[]` is an empty list, or a list with 0 elements._ 

- - - 

**Q2. In a list of values stored in a variable called `spam`, how would you assign the value `'hello'` as the third value? _(Assume [2, 4, 6, 8, 10] are in `spam`.)_**

Ans: _This can be done using `spam.insert(2,'hello')`_ 

- - - 

**Q3. What is the value of `spam[int(int('3' * 2) / 11)]`?**

Ans: _8 (assuming `'hello'` is not inserted)_ 

- - - 

**Q4. What is the value of spam[-1]?**

Ans: _10_ 

- - - 

**Q5. What is the value of spam[:2]?**

Ans: _[2,4]_ 

- - - 

**_Let's pretend `bacon` has the list `[3.14, 'cat', 11, 'cat', True]` for the next three questions._**

**Q6. What is the value of `bacon.index('cat')`?**

Ans: _1_ 

- - - 

**Q7. How does `bacon.append(99)` change the look of the list value in `bacon`?**

Ans: _It becomes `[3.14, 'cat', 11, 'cat', True, 99]`_ 

- - - 

**Q8. How does `bacon.remove('cat')` change the look of the list in `bacon`?**

Ans: _It becomes `[3.14,  11, 'cat', True, 99]`_ 

- - - 

**Q9. What are the list concatenation and list replication operators?**

Ans: _Concatenation can be done using the `+` operator and replication can be done using the `*` operator._ 

- - - 

**Q10. What is difference between the list methods `append()` and `insert()`?**

Ans: _`append()` adds the element to the end of the list, whereas `insert()` adds the element at the specified index_ 

- - - 

**Q11. What are the two methods for removing items from a list?**

Ans: _`pop()` and `remove()`_ 

- - - 

**Q12. Describe how list values and string values are identical.**

Ans: _A string is a list of characters. Most list operations will apply to strings too._ 

- - - 

**Q13. What's the difference between tuples and lists?**

Ans: _Tuples are immutable whereas lists are mutable._ 

- - - 

**Q14. How do you type a tuple value that only contains the integer `42`?**

Ans: _`(42)`_ 

- - - 

**Q15. How do you get a list value's tuple form? How do you get a tuple value's list form?**

Ans: _`tuple(<list>)` can be used to get the list's tuple form. Similarly, `list(<tuple>)` can be used to get the tuple's list form._ 

- - - 

**Q16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?**

Ans: _The variable contains the reference to the list object._ 

- - - 

**Q17. How do you distinguish between `copy.copy()` and `copy.deepcopy()`?**

Ans: _The assignment operator `=` does not create a new object but only assigns the reference of the object to a new variable. In the case of `copy.copy()`, a new object is created. This new object, would store the references of the original object's nested objects. In the case of `copy.deepcopy()` also a new object is created. Additionally, copies of the nested objects of the original object are also created recursively._ 

- - - 


