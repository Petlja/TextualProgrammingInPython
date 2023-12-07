# Printing text and numbers

In addition to integers and real numbers, one of the basic types of data in programming is text. The text data is called a **string**. In addition to letters, they can contain all other characters used in the text: punctuation, parentheses, numbers, mathematical operators, various special characters such as `%`, `$`, `^`. `&` etc.

Text values are written between quotation marks. We call the text under quotation marks a **text constant** or a **literal**. Single `'...'` and double `"..."` quotes can be used interchangeably in Python (it is only important that quotes are of the same type at the beginning and end of the string). For example:

```
s1 = 'One text'
s2 = "Another text"
```

We will use the word string for the textual data type, as well as for any expression whose value is that type. The most important examples of string expressions are text constants (literals) and variables that contain text.

## Printing text

The strings are printed in the same way as the numeric data. The string we want to print is simply specified as a *print()* function argument.

```{py-code} 1
:opt-in-ai:

print("Hello world!")
```

When the *print()* function has multiple arguments, these arguments can be of different types:

```{py-code} 2
:opt-in-ai:

print('2+2 =', 2+2)
```

When we use multiple arguments, we write them separated by commas (as with any function). The values of all the arguments specified will be printed in the same order, and will be separated by one space.

## More about printing numbers

Sometimes the printed result looks illegible:

```{py-code} 3
:opt-in-ai:

print(5/3)
```

Most often we don't need all these digits. Real numbers can look more readable if we use the *format* function. With this function (among other things) we can specify how many digits after the decimal point we want to display:

```{py-code} 4
:opt-in-ai:

x = 5/3
s = format(x, '.2f')
print(s)
```

To specify the number of decimal places to display, we called the *format* function like this: the first argument of the function is the value we print, and the second argument is the description of the printing format. In this description, the part '.2' means that we want two decimal places, and the part 'f', abbreviated from *float*, means that we give a description for a real number (the type of real numbers is called *float*). The function returns a string in which the number *x* is written as specified.

Note that this formatted printing does not change the value of the variable *x*.

We've broken the example down into steps to make it clearer, though it could also be written in one line of code. For example, to print with 4 decimal places:

```{py-code} 5
:opt-in-ai:

print(format(5/3, '.4f'))
```

______________________________________________________________________

When displaying multiple real numbers one below the other, we can make them more readable by aligning the decimal points. For example, this way of printing is not easily comprehensible:

```{py-code} 6
:opt-in-ai:

print(-1.23)
print(7251.7)
print(84.15)
```

To get a more readable look, we can use the *format* function like this:

```{py-code} 7
:opt-in-ai:

print(format(-1.23, '8.2f'))
print(format(7251.7, '8.2f'))
print(format(84.15, '8.2f'))
```

In the description '8.2f' the number 8 means that the textual version of the given number should be left-padded with spaces (if needed) to take up total of 8 places. These 8 places include the digits, the decimal point, possible sign of the number and spaces in front of the number.

Other parts of the description ('.2f') have the same meaning as before.

The *format* function has many other features, but we will not use them here.

