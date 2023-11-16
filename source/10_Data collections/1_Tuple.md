# Tuple
 
In the previous lesson, we used a tuple to perform some commands (computing and printing) over each value from the tuple using the *for* loop.

Tuples are also a type of data in Python, such as numbers, strings, or logical values. The types *int* (integer), *float* (real number), *str* (string) and *bool* (logical value) are **basic types**. The difference between tuples and basic types is that the value of a tuple consists of multiple values of a simpler type.

Each value that consists of multiple values of a simpler type will be called a **collection**. The data the collection consists of are called **collection elements**.

The only collections we have seen so far are tuples, which we will now get to know in more detail. We will see some more types of collections very soon.

## Packing and unpacking tuples

We can fit the whole tuple into a variable, as we do with values of a simpler type. In the following example, the *temperatures* variable contains the entire tuple as its value.

```{py-code} 1

temperatures = (25, 24, 25, 23, 25, 25)
for t in temperatures:
    print(t)
```

This kind of value assignment (as in the first line of the program) is known as tuple packing. The reverse assignment is also possible: when we know how many elements are there in a tuple, we can assign the tuple elements to the corresponding number of variables:

```{py-code} 2

full_name = ("Arthur", "Conan", "Doyle")
first_name, middle_name, last_name = full_name
print(first_name)
print(middle_name)
print(last_name)
```

Statements like `first_name, middle_name, last_name = full name` are called tuple unpacking.

The same effect is achieved by a related statement

```
first_name, middle_name, last_name = "Arthur", "Conan", "Doyle"
```

Tuples do not appear in this statement, which is called multiple value assignment.

## Tuple elements and indices

We can also get the elements of a tuple by writing the name of the tuple, and behind it in square brackets the sequence number of the element we want. It should be noted here that counting the elements of any collection starts from zero. For example:

```{py-code} 3

basic_colors = ("Red", "Green", "Blue")
print(basic_colors[0])
print(basic_colors[1])
print(basic_colors[2])
```

The sequence number of an element is also called the **index** of the element. if the tuple has *n* elements, we can use the numbers 0, 1, 2, ... *n-1* as indices. In the example above, *n* = 3, so indices 0, 1, and 2 are allowed. Trying to use an index outside these bounds causes an error (try it).

## Tuple length

The number of elements of a tuple can be obtained by using the *len* function.

```{py-code} 4

basic_colors = ("Red", "Green", "Blue")
n = len(basic_colors)
print(n)
```

or shorter:

```{py-code} 5

print(len(("Red", "Green", "Blue")))
```

Note the double brackets (one for function and the other for tuple).

Through these examples we have seen that tuple elements can be numbers or strings. In fact, the tuple elements can be of any type, basic or complex.

For example, it is possible to create a tuple of tuples:

```{py-code} 6

t = ((11, 12, 13), (21, 22, 23))
print(len(t))

```

% commented out
%
% t2 = ((1, 2, 3), ) # last comma matters
% print(len(t2))

Tuple *t* contains two simpler tuples, therefore the number of its elements is 2.

In Python, the elements of a tuple can be of different types, and we will see such examples latter.