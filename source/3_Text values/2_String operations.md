# String operations

## Joining strings

Strings can be joined together with a **string concatenation** operation. This operation is denoted by the sign `+`, just like the operation of summation, so in programming concatenation is often informally called string addition.

```{py-code} 8
:opt-in-ai:

s = 'continu' + 'ation'
print(s)
```

Sometimes, we may have an integer or a real number written in a string, so it is important to understand that the sign `+` refers to addition when talking about numbers, and when strings are involved it refers to the concatenation of strings. For example, in the following program, the first *a + b* is the addition of numbers, and the second is the addition of strings. Accordingly, the printed results also differ (try it out).

```{py-code} 9
:opt-in-ai:

a = 14.2
b = 1
print(a + b)

a = '14.2'
b = '1'
print(a + b)
```

It is likely that occasionally you may be confused by the result when executing a program. The result may be different than expected for many reasons, and one possibility is that you unintentionally added up strings instead of numbers.

The `+` character can stand between two numeric expressions or between two strings, but not between a string and a number (in any order). Such combinations result in a *TypeError* (try it).

```{py-code} 10
:opt-in-ai:

print('2' + 2)
```

## String multiplication

Strings can also be multiplied. This means that it is allowed to multiply a string by an integer (either from left or right), and the result is a new string, which is obtained by repeating a given string a given number of times.

In the following example we underline the numbers with a line, and that line is obtained as a result of multiplying the string '-' by 12.

```{py-code} 11
:opt-in-ai:

a = 1.23958
b = 5467251.707256
c = 384.150576
total = a + b + c
print(format(a, '12.2f'))
print(format(b, '12.2f'))
print(format(c, '12.2f'))
print(12 * '-')
print(format(total, '12.2f'))

```