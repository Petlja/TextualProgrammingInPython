
# Writing functions that return value

The following rules apply to writing functions in Python:

```{infonote}

**Function writing rules:**

- The function definition begins with the word ``def``, followed by the function name, then a list of arguments in parentheses, and the ``:`` character (colon) at the end of the line.
- Any properly written name may appear as a *function_name* (the rules are the same as for variable names).
- An empty list (nothing) may appear as *argument_list* if the function does not use arguments, or one or more comma-separated arguments.
- Any Python statements may appear in the function body (*statement_1*, ... *statement_k*). These commands are written indented with respect to the row containing the function name and arguments.
```

Functions may or may not return some value. So far we have had the opportunity to see both types of functions. For example, the functions by which Karel (the robot) moves forward, turns around, picks up and leaves balls are all functions that do not return any value. On the other hand, mathematical functions like *abs* or *round*, as well as functions to check if Karel has balls with him, whether there are any balls on the square, or whether Karel can go forward are functions that do return a value.

In order for a function to return a value, it is necessary to specify the `return` statement at least once in the body of the function. The `return` statement consists of the word *return*, folowed by an expression whose value the function is to return.

```{code} 

    def square(x):
        return x * x

    print(square(3))
```

The *return* statement can appear in multiple places in a function (usually with different values), and must be specified at the end of the function body. The *abs* function, if it had not been embedded, could have been defined as follows:

```{code} 

def abs(x):
    if x > 0:
        return x
    else:
        return -x
```

A function can return more than one value. One such function is the built-in *divmod* function, which returns two numbers - the result of integer division and the reminder. We use the *divmod* function as we do with functions that return a single value, we only place the returned values in multiple variables:

```{py-code} 1

quotient, reminder = divmod(813, 10)
print('The quotient is', quotient, 'and the remainder', reminder)

```

When we write functions that return multiple values, it is sufficient to specify comma-separated values after the word *return*. If we were to define the built-in *divmod* function ourselves, we could write it like this:

```{code} 
def divmod(a, b):
    return a // b, a % b
```

## Example

```{questionnote}

**Example - painting:**

To paint :math:`1m^{2}` of walls requires about :math:`0.5kg` of paint. Write a function that accepts the following 4 arguments:

- the length of the room
- the width of the room
- the height of the room
- length that is not to be painted (total width of doors, windows, closets, etc.)

The function should return the amount of paint (in kilograms) required to paint the walls and ceilings.

After the function, write a program that loads the data for 5 different rooms, and then using the written function calculates and prints the total amount of paint needed to paint all five rooms.
```

```{py-code} 2


def paint_needed(a, b, h, not_to_paint):
    coverage = 0.5 # how many kilograms per square meter
    ceiling = a*b
    walls = h * (2*a + 2*b - not_to_paint)
    area_to_paint  = ceiling + walls
    return area_to_paint * coverage

total_paint_needed = 0
for i in range(5):
    s = input('Enter the length, width and height of the room, and the non-painting length').split()
    total_paint_needed += paint_needed(float(s[0]), float(s[1]), float(s[2]), float(s[3]))

print("A total of", total_paint_needed, "kilograms of paint is required")

```