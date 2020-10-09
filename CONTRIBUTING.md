# Programming Language
Programming Language is not limited, you can use any types of languages you want. But we do recommend you to use lanaguages
that can be easily understood, such as python, java and so on.

# Libaray
We recommend you to write the algorithms by youself without importing any libraries.

# File name
The file name must be meaningful and self explanatory.

# Explanation
For each algorithm, there should be a block comment on top of the codes that explains everything about it. Some necessary
sections are:
- `Problem`: Describes what kinds of problems can this algorithm solve
- `Ideas`: Briefly explain what is your idea(or the author's idea if you are copying from elsewhere)
- `Time Complexcity` Time complexcity of this algorithm, and explain what are the variables in the Big Oh formula

Some optional sections are:
- `Restriction`: The restriction of this algorithm
- `Extra Space`: Extra space that this algorithm requires
- `Addition`: Additional notes that should be noticed

And you can add more sections if you want. An example (linear search):
```python
'''
Problem:
We have a list s={s1, s2, s3, ..., sn}, we want to
find the index of an element si(1 <= i <= n). If si
appears multiple times, just return the first index
it appears. If there is no such element, return -1.

Ideas:
Simple linear search, from index 0 to index n. Compare
each element with the target using ==, if they are equal,
return the index and end the method. Otherwise, return -1
at the end of the method.

Time Complexcity:
O(n), where n is the len of the given list
'''
```

# Commit
Commits must be meaningful and self explanatory.
