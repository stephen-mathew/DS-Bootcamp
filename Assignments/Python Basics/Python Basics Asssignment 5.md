### Stephen Mathew
### Python Basics Assignment 5
### 22-June-2022

**Q1. What does an empty dictionary's code look like?**

Ans: _{}_ 

- - - 

**Q2. What is the value of a dictionary value with the key `'foo'` and the value `42`?**

Ans: 
> dic = {'foo':42}
> dic['foo'] 

- - - 

**Q3. What is the most significant distinction between a dictionary and a list?**

Ans: _The index in a dictionary is user-defined whereas the index in a list are integers starting from 0_ 

- - - 

**Q4. What happens if you try to access `spam['foo']` if `spam` is `{'bar': 100}`?**

Ans: _A `KeyError` would be thrown_ 

- - - 

**Q5. If a dictionary is stored in `spam`, what is the difference between the expressions `'cat' in spam` and `'cat' in spam.keys()`?**

Ans: _It is the same._ 

- - - 

**Q6. If a dictionary is stored in `spam`, what is the difference between the expressions `'cat' in spam` and `'cat' in spam.values()`?**

Ans: _`'cat' in spam` looks for the key `cat` among all the keys of the dictionary `spam` whereas `'cat' in spam.values()` looks for the value `cat` among all the values of the dictionary `spam`_ 

- - - 

**Q7. What is a shortcut for the following code?**
> if 'color' not in spam:
> &nbsp;&nbsp;&nbsp;spam['color'] = 'black'


Ans: _`spam['color']=spam.get('color','black')`_ 

- - - 

**Q8. How do you "pretty print" dictionary values using which module and function?**

Ans: _Using the `pprint` module and the `pprint` function._ 

- - - 
