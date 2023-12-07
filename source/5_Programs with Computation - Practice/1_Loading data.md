# Tasks without loading data

So far, we have learned how to load numbers in programs, how to perform computational operations on them, and how to print results. We can now put this into practice with a few simple math tasks.



## Example

```{questionnote}

**Example - Celebration**

Jessica and Oscar are organizing a celebration. The rented space accommodates 100 people, Jessica has so far invited 43, and Oscar 28.

Write a program that calculates and prints how much more space is available.
```

The problem can be solved as follows:

```{py-code} 1
:opt-in-ai:

print(100-43-28)
```

or like this:

```{py-code} 2
:opt-in-ai:

total_places = 100
called_by_jessica = 43
called_by_oscar = 28
places_left = total_places - called_by_jessica - called_by_oscar
print(places_left)

```

```{infonote}

While this may seem unnecessary here, the solution with variables is worth practicing. Programs that use variables can do much more than those without variables. For example, if we load values into a program, variables are necessary. Also, more complex calculations would be very incomprehensible if they could not be broken down into simpler steps, and for intermediate values we again need variables.

We mentioned earlier that we should try to give meaningful names to the variables. It doesn't matter to the computer (it works equally well with any names), but when we calculate something that matters to us, using variables with meaningful names will help us understand that program after a long time. Also, such a program will be easier to understand by other people who read it.

```

## Practice tasks

```{questionnote}

**Task - spending all the money**

How many items worth 76 euros can be bought for 500 euros? How much money will remain if the largest possible number of items is bought?

```

The shorter (and less clear) version of the solution is

```{py-code} 3
:opt-in-ai:

print(500 // 76, 500 % 76)

```

Write a clearer solution using variables.

```{py-code} 4
:opt-in-ai:

# insert your code here

```

```{questionnote}

**Task - Date**

If today is the 15th of the month and the month is 31 days long, how many days are there until the 11th of the next month (at the same time of day)?
```

Your job is to write a solution in which the starting and calculated values are assigned to variables. By clicking on the "short solution" button you can see a short solution as a hint.
<!--     print(11+31-15)
-->

```{py-code} 5
:opt-in-ai:

    # insert your code here

```

```{questionnote}

**Task - purchase of 3 articles**

Ben has 20 euros and wants to buy 3 bicycle lamps for 1.58 euros each. How much money will he have left?
```

Write a program that uses variables for the starting and calculated values.

```{py-code} 6
:opt-in-ai:
 
# insert your code here

```