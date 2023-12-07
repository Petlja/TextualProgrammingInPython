# Text, numbers and conversions

## Reading text

The programs we have learned to write so far contain all the information needed and always work the same way. When we need a program to do the same thing with different data, we would have to modify the program itself. This method may be quite appropriate when changes to the data are small and infrequent.

Another way to get our program to handle more diverse tasks is to enable data entry. Inserting data into a program during its execution is done using the *input()* function. This function works by waiting for the program user to type something (and press the *Enter* key) and then returning the typed text as a result.

When you run this program, to see how it works, type something and press *Enter*. Try the same program in the *IDLE* environment or on the *repl.it* site.

```{py-code} 1
:opt-in-ai:
 
s = input()
print("You wrote", s)
```

The program works as described, but this program behavior can be confusing. If someone were to run a program like this in the *IDLE* environment without knowing that the program was expecting data, it might look like their computer was locked because nothing was happening, and in fact the program was just waiting for input from the keyboard.

To help the user understand what is expected of them, we can also use the form of the *input* function with a single text argument, which will be printed as a guide to the user. For example:

```{py-code} 2
:opt-in-ai:

s = input("Write something: ")
print("You wrote", s)
```

Whether we choose one or the other form of the *input* function, depends on the purpose of the program. When writing a program in which other people will enter data, we use a form with an argument, serving as an instruction. When we write a program only for personal short-term (maybe even one-time) use, then we have no need for instructions and can use a form without arguments.

Also, be aware that for some of the environments in which the program is running, we can arrange our program so  that the data is being read from another location where we've prepared it in advance, instead of reading the data from the keyboard. In such cases there is no waiting for the data to be entered, it is loaded automatically and there is no need to print the instruction. Therefore, in such cases we would also use the *input* function without arguments.

## Reading numbers

We have seen that the *input()* function returns a string (text typed by a user). This means that if we need data of another type, we need to change the type of data returned by the *input()* function from string to the desired type. Changing the data type is also called **conversion**. For example, if we want an integer, then we need to convert the resulting text to an integer. Here's how to do it in Python:

```{py-code} 3
:opt-in-ai:

s = input("Enter a whole number: ")
n = int(s)
print(n+n)
```

The `int()` function converts a text value to an integer value. Thus, with the command `n = int(s)` we place an integer value in the variable *n*, which is why the + sign in the program represents the addition of integers. Summation is added to the program as proof that *n* is indeed an integer value (the result shows that the values are added up as numbers).

Since the *input* function returns a string, we can also pass its result directly to the *int* function. That way we avoid using the *s* variable and get a slightly shorter program that does the same thing:

```{py-code} 4
:opt-in-ai:

n = int(input("Enter a whole number: "))
print(n+n)
```

______________________________________________________________________

For a real number, *int* should just be replaced with *float*, because the `float()` function converts a text value to a real number. For example, if we want to load a real number and print twice that number, the program may look like this:

```{py-code} 5
:opt-in-ai:

s = input("Enter a real number: ")
a = float(s)
print(2*a)
```

or

```{py-code} 6
:opt-in-ai:

a = float(input("Enter a real number: "))
print(2*a)

```

Check out what happens in these two examples when you enter something else rather than a number.

## About conversions

We have seen that when a string contains an integer or a real number, that string can be converted to an integer or real type using the *int()* or *float()* functions. On the other side, integers and real numbers can always be converted to a string. The *str()* function is used to convert to a string.

```{py-code} 7
:opt-in-ai:

a = 1
a_str = str(a)
print(a_str + a_str)

b = 2.1
b_str = str(b)
print(b_str + b_str)
```

The conversion of an integer value to a real one is done automatically when needed, although we can also do this explicitly by calling the *float* function.

```{py-code} 8
:opt-in-ai:

print(float(1))
```

Conversely, when we need to convert a real number to an integer, that conversion does not happen automatically (for a reason) and needs to be set in the program by calling the *int()* function. When converting a real number to an integer, any decimals of the real number are discarded, which means that rounding is always **towards zero**. In other words, when the value of the real number *x* is not an integer, *int(x)* is closer to zero than *x*.

```{py-code} 9
:opt-in-ai:

print(float(1))

print(int(1.68))
print(int(-1.68))
```
