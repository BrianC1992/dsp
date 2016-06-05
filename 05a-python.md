# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are sequences of items.  A list is an ordered, changeable sequence of the same kinds of items. They can be dealt with individually.  A tuple is a sequence of different types of items that cannot be changed. They are dealt with as a unit. Tuples are used as keys in dictionaries because they cannot be changed.  This is so a key can be mapped to a specific value in the dictionary.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets and lists are sequences of items.  Sets, however, are unordered and do not contain duplicate items.   Lists are ordered and can have duplicates.  
An example of a list is:  
```
squares = [1, 4, 9, 16, 25]  
```  
An example of a set is:  
```  
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}  
```  
Sets are faster when you are trying to see if an object is in a set.  This is because sets use hash functions to map to the set. Hash tables are automatically resized so that the speed is constant no matter the size of the set.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> A lambda function is a function that takes a number of arguments and returns the value of a single expression.  
An example of using a lambda function is:  
```
tups = [
    (1, 3, -2),
    (3, 2, 1),
    (-1, 0, 4),
    (0, -1, 3),
    (-2, 6, -5)
]  
sorted(tups, key=lambda tup: tup[1])  
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> A list comprehension is a construct that allows a list to be transformed from another list.  
An example of a list comprehension is below:  
```  
doubled_odds = [n * 2 for n in numbers if n % 2 == 1]  
```  
The equivalent statement with map and filter is below:  
```  
doubled_odds = map(lambda n: n * 2, filter(lambda n: n % 2 == 1, numbers))  
```  
The capabilities seem to be about the same.  However, list comprehensions are somewhat more readable.  

A set comprehension is similar to a list comprehension except you are working on a set.  
An example would be:  
```  
a = {x for x in 'abracadabra' if x not in 'abc'}  
```  
Dictionary comprehensions work the same way as list comprehensions.  
Example:  
```  
{x: x**2 for x in (2, 4, 6)}  
```  

 


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





