# Branching statements

In programs with numbers we often need to compare two values, that is, to determine whether they are equal, whether one is smaller than the other, different from the other, and the like. Depending on the outcome of the comparison, the program may continue to execute in different ways.

Some of the symbols used for comparison are the same as in mathematics (for example `<` and `>`) and some are not. The following table gives the notation of all standard comparisons used in mathematics and in Python (and also in many other programming languages).

```{eval-rst}
.. table::
    :align: left
    :widths: 15, 15, 70

    ====================   ==================== ========================================
    Math                   Python               Meaning
    ====================   ==================== ========================================
    :math:`а < b`          a < b                a is less than b
    :math:`a \leq b`       a <= b               a is less than or equal to b
    :math:`a > b`          a > b                a is greater than b
    :math:`a \geq b`       a >= b               a is greater than or equal to b
    :math:`a = b`          a == b               a is equal to b
    :math:`a \neq b`       a != b               a is not equal to b
    ====================   ==================== ========================================
```

Notation $a<b$ can be understood as an expression whose value is true or false in each case. These values are written in Python as *True* and *False* and they are **logical constants**, that is, constants of the type `bool` which we call the logical type. Expressions whose value is true or false (logical type) are called **logical expressions**. All the expressions in the table above are logical expressions (we will see more logical expressions later).

## The if statement

The *if* statement is used to decide which of the two groups of statements to execute. In Python it is written as follows:

```{code}

if condition:
    statement_a1
    ...
    statement_ak
else:
    statement_b1
    ...
    statement_bm
```

```{infonote}

**Meaning (semantics) of the if statement:**

The statement written above means: if the condition is fulfilled, execute *statement_a1*, ... *statement_ak*, otherwise execute *statement_b1*, ... *statement_bm*.

**Writing rules (syntax) of the** if **statement**

- After the word ``if``, a logical expression is written and at the end of the line the character ``:`` (a colon) is required.
- In the following lines, indented for the same number of spaces (usually 4), the statements that should be executed if the logical expression evaluates to *True* are written. There may be one or more of these statements.
- After the commands that are executed if the condition is fulfilled, the word ``else`` is written and again the character ``:`` (colon). The word ``else`` is written at the same level of indentation as the word ``if``.
- In the following lines, indented for the same number of spaces, write the commands that are to be executed if the logical expression evaluates to *False*. There may be one or more of these statements as well.

The ``if`` statement is also called the *branching statement* because the program execution flow for this statement branches: the next statement to execute depends on the value of the logical expression in the condition. Groups of statements after the word *if* or *else* are therefore also called branches of the *if* statement.
```

In case the program does not need to do anything when the condition of the *if* statement is not fulfilled, that is, when we do not need *else* branch of the *if* statement, we can omit it:

```{code}

if condition:
    statement_a1
    ...
    statement_ak
```

We will use this short form of the *if* statement later.

### If statement - examples and tasks

```{questionnote}

**Example - who is younger:**

Peter and Mark want to play a game of pool. They agreed that the younger player plays first. Write a program that reads the age of Peter and Mark (that are not equal) and prints who will make the first move.
```

```{py-code} 1
:opt-in-ai:

peter = int(input("How old is Peter: "))
mark = int(input("How old is Mark: "))
if peter < mark:
    print('Peter plays first.')
else:
    print('Mark plays first.')
```

```{questionnote}

**Example - packing:**

The eggs on the farm are packed in 10-pack boxes and full boxes are sent to the store. Write a program that takes the number of eggs ready for packing and prints whether all the eggs can be packed and shipped to the store, or whether a few eggs will be left unpacked temporarily.
```

Here we need to check that the number of eggs is divisible by 10. For this reason, we use the operator `%`, which gives the remainder after division. If the remainder after dividing the number of eggs by 10 is equal to zero, all the eggs can be packed and sent.

```{py-code} 2
:opt-in-ai:

num_eggs = int(input("How many eggs: "))
if num_eggs % 10 == 0:
    print('All eggs can be sent.')
else:
    print('Some eggs will remain.')

```

```{questionnote}

**Task - Street side:**

Even house numbers are on the right side of the street and odd house numbers on the left. Write a program that takes a house number and prints which side of the street the number is on.

```

Here it is needed to examine if the given number is divisible by 2. The task is similar to the previous one - if the remainder of dividing the given house number by 2 is equal to zero, the number is on the right side of the street, otherwise it is on the left side.

```{py-code} 3
:opt-in-ai:

number = int(input("What is the house number: "))
# finish the program

```

```{questionnote}

**Task - cinema:**

You have 10 euros with you. Write a program that takes the movie ticket price and popcorn price, then prints out if you have enough money for both the ticket and popcorn.

```

```{py-code} 4
:opt-in-ai:

ticket_price = int(input("How much for the ticket: "))
popcorn_price = int(input("How much for the popcorn: "))
# finish the program

```