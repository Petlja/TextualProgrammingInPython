# String as a collection and functions on collections

## String as a collection

We have used strings as the basic type so far, but strings can also be used as collections of individual characters. We can traverse string characters using a loop and retrieve individual characters using indices:

```{py-code} 14

s = 'text'
print(s[1], s[2])
for c in s:
    print(c)
```

## Functions on collections

There are many functions in Python that accept a collection as an argument. One of them is the *len* function, which we have already met. Some other commonly used functions that apply to collections are:

- *min*, a function that gives the smallest element of a collection
- *max*, a function that gives the largest element of a collection
- *sum*, a function that gives the sum of the elements of a collection

```{py-code} 15

print('Tuple:')
t = (2, 8, 4, 15, 3)
print('len(t) =', len(t))
print('min(t) =', min(t))
print('max(t) =', max(t))
print('sum(t) =', sum(t))

print('Range:')
r = range(1, 10, 2)
print('len(r) =', len(r))
print('min(r) =', min(r))
print('max(r) =', max(r))
print('sum(r) =', sum(r))

print('String:')
s = 'Python'
print('len(s) =', len(s))
print('min(s) =', min(s))
print('max(s) =', max(s))
# elements of s are not numbers, so uncommenting the next statement would cause an error
# print('sum(s) =', sum(s))
```

The values of the functions *len*, *sum*, *min*, *max* for the range can also be determined from the parameters of the range. Also, *min* and *max* are not commonly applied to a string (they return character with smallest and biggest code respectively). Here, we are just pointing out that all these functions accept various kinds of collections as their argument (including range and string).