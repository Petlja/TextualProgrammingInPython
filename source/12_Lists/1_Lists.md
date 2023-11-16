# Lists

So far, we have mentioned tuples and ranges as types of collections, and we have seen that the string can also be used as a collection. Another very important and often used type of collections are lists.

## Lists vs. tuples

Lists, as well as tuples, can be specified by enumerating the elements, except that the list elements are written between square brackets:

```{py-code} 1

for x in [2, 5, 8, 3]:
    print(x)
```

The lists are in many ways similar to tuples. All of the features of the tuples mentioned in the collections chapter apply to lists as well:

- A list can also be placed in a variable and vice versa - list elements can be assigned to an appropriate number of variables (in other words, a list can be packed and unpacked)
- list elements can be accessed using the list name and the sequence number (index) of the element written in square brackets
- list length is obtained by the function *len*

```{py-code} 2

names = ["Tom", "Polly", "Filip", "Mary"]
t, p, f, m = names
print("p =", p)
print("names[0] =", names[0])
print("len(names) =", len(names))
```

The lists also have some features that set them apart from the tuples. For example, lists can be extended using the *append* function:

```{py-code} 3

a = []
a.append(3)
a.append(7)
a.append(2)

for x in a:
    print(x)
```

Also, list elements can change their values and can be deleted from the list:

```{py-code} 4

a = [3, 7, 2]
print("Initial list:")
for x in a:
    print(x)

a[0] = 5
print("Changed list:")
for x in a:
    print(x)

del a[1]
print("Shorter list:")
for x in a:
    print(x)
```

Such operations with tuples are not possible. Once made, the tuple remains as it is. A tuple cannot be modified - it cannot change its length or the values of individual elements. A variable containing a tuple can only get a whole new tuple as a value, however by doing so, the previous tuple was not modified but ceased to exist. That is why tuples are said to be immutable.

Tuples can be used for collections of data that we do not intend to modify while executing a program (although we can change them manually before executing a program). By using tuples, we ensure that the data will not change accidentally, and program will work slightly more efficiently with the tuple than it would do with the list.

Tuple *t* can be converted to a list *a* during the program execution, and vice versa: `a = list(t)` or `t = tuple(a)`, but such conversions are seldom needed and are better avoided (if they are often applied to large collections, conversions like this can slow the program significantly).

## Building a list

As we have already seen, we can gradually build lists in a program. For example, if we are given a tuple of numbers from which we want to copy those that are greater than zero (and perform some extra task with these numbers latter), we can do this:

```{py-code} 5

numbers  = (2, 5, -2, 1, -3, 4, -7, 3)
positive_numbers = []
for x in numbers:
    if x > 0:
        positive_numbers.append(x)

for x in positive_numbers:
    print(x)
```

At the beginning we have an empty list, and then in the loop we use the *append* function to add to the list the elements we want.

## Loading a list

In the same way, we can load data into a list:

```{py-code} 6

a = []
n = int(input("How many elements to load: "))
for i in range(n):
    x = float(input("Please enter an element: "))
    a.append(x)

print("The elements of the list are:")
for x in a:
    print(x)

```

Another way to load a list is to first form a list of required length and then assign the loaded values directly to the list elements in the loop.

```{py-code} 7

n = int(input("How many elements to load: "))
a = [0] * n
for i in range(n):
    a[i] = float(input("Please enter an element: "))

print("The elements of the list are:")
for x in a:
    print(x)
```

We used the statement `a = [0] * n` to form a list of *n* elements. The operation `[0] * n` is called list multiplication. The result of the list multiplication is concatenation of *n* repetitions of the given list. For example, \[0\] * 5 is the list \[0, 0, 0, 0, 0\], and \[2, 7\] * 3 is the list \[2, 7, 2, 7, 2, 7\].

If the user enters all the elements of the list in one line separated by spaces, we write the program like this:

```{py-code} 8

a_str = input("Enter all the elements: ")
a = []
for s in a_str.split():
    a.append(float(s))

print("The elements of the list are:")
for x in a:
    print(x)
```

We used the *split()* function to parse the entered text into shorter strings containing individual numbers.

```{infonote}

*split()* **function**:

The *split()* function parameter is a character or text that we want to use as a separator. If a separator is not specified, a space ``' '`` is assumed as default.

`"1234 56".split() -> ["1234", "56"]`

`"1234,56".split(',') -> ["1234", "56"]`

The result of the *split()* function is a string list. The number of shorter strings we get as a result depends on the number and layout of the separator characters in the starting string. For example, if the text contains only one separator somewhere in the middle, we will get two shorter strings. Each new appearance of the separator character can produce one string more in the resulting list (if it really separates some part of the starting string from the rest of the text).

`"1;23;456;7".split(';') -> ["1", "23", "456", "7"]`

`" 1  234    56 7 ".split() -> ["1", "234", "56", "7"]`

```