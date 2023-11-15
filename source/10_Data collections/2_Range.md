# Range

Range is another type of collection. Unlike tuple, the elements of this collection are always integers.

Range can be defined in several ways.

## Range with one argument

The simplest form of specifying a range is *range(n)*, where *n* is a positive integer. The *range(n)* range contains integers from 0 to *n*, not including *n*. For example, *range(5)* contains values 0, 1, 2, 3, 4.

```{py-code} 7

for i in range(5):
    print(i)
```

We see that in the *for* statement, we can use range in the same way as the tuple. In fact, any collection may be in place of the tuple or range.

Since the *range(n)* range contains a total of *n* values, this range is often used when a command only needs to be repeated *n* times in the same way:

```{py-code} 8

for i in range(5):
    print("Hello!")
```

The *print* function was executed for each value *i* of sequence 0, 1, 2, 3, 4, but in this example, those values are not used in the loop body. Thus, we achieved that the *print* function was executed 5 times in exactly the same way, that is, it was repeated 5 times.

Another common use of this type of range is to get through all the elements of a tuple. In such case, the loop variable serves as an index. This way of going through the values of the tuple is suitable when besides these tuple values in the loop we also need their sequence numbers (this way of going through the collection is more common in other programming languages than Python).

```{py-code} 9

colors = ["Red", "Green", "Blue", "Yellow", "Magenta"]
n = len(colors)
for i in range(n):
    print('Color #', i, 'is', colors[i])

```

## Range with two arguments

When we need a sequence of consecutive integers that does not start at zero, we set the range as *range(a, b)*, where *a* and *b* are integers such that $a<b$. Then the sequence is made up of integers from *a* to *b*, not including *b*. For example, the range *range(1, 6)* gives the sequence of numbers 1, 2, 3, 4, 5:

```{py-code} 10

for i in range(1, 6):
    print(i)
```

## Range with three arguments

The third form of specifying a range has three arguments:

```{py-code} 11

for i in range(2, 12, 2):
    print(i)
```

The range values given by *range(a, b, c)* go from *a* to *b* (not including *b*) with the step *c*, i.e. values change by *c*. Step *c* can also be negative:

```{py-code} 12

for i in range(12, 2, -2):
    print(i)

```

We can convert a range into a tuple (the opposite is not possible, nor is it ever needed):

```{py-code} 13

a = tuple(range(2, 12, 2))
print(len(a))
```