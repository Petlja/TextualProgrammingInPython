# Working interactively with Python

Start your Python shell. The `>>>` characters you see represent a prompt. This way the Python interpreter tells us that it is ready to receive the command.

When working interactively, Python interpreter can also be used as a calculator - type an expression and get its value:

```
>>> 3 + 2
5
>>> 3.25 + 2.25
5.5
>>> 3 - 2
1
>>> 4 * 2
8
>>> 4 / 2
2.0
```

The following symbols are used for basic calculating operations in Python (as in most programming languages):

- addition: `+`
- subtraction: `-`
- multiplication: `*`
- division: `/`

In addition to these basic and most commonly used ones, we sometimes need a few other operations, which are used less frequently. Those are:

- integer division (taking the whole part of the quotient): `//`, for example the value of the expression $7 // 2$ is $3$.
- remainder of a division: `%`, for example the value of the expression $7 \% 2$ is $1$.
- the power operator: `**`, for example the value of the expression $2 ** 4$ is $2^4 = 16$.

```
>>> 7 // 2
3
>>> 7 % 2
1
>>> 2 ** 4
16
```

Computers distinguish between integers and real numbers, write them differently in their memory, and do computations with them in different ways. So in programming, value 2.0 is not quite the same as 2, although the values are mathematically equal (the sign `==` is used to compare the two values).

```
>>> 2.0 == 2
True
>>> type(2.0)
<class 'float'>
>>> type(2)
<class 'int'>
```

What we see in the example above means that the first number is real and the second is an integer (the word *float* denotes real numbers, and *int* denotes integers).

In this regard, note that in Python, the result of the ordinary division `/` is always a real number, even when the operands are integers and are divisible (there is no remainder). When we want the result of the division between two integers to be an integer, we should use the integer division operator `//`.

```
>>> 6/2
3.0
>>> 6//2
3
```

% commented out
%
% Using Python's built-in functions, we can convert a real number to an integer, and an integer to a real number.
%
% .. code::
%
%     >>> float(3)
%     3.0
%     >>> int(3.0)
%     3
%     >>> int(6/2)
%     3

For the other operations specified, the result is an integer when both operands (the numbers to which the operation applies) are integers, and real if at least one operand is real.

```python
>>> 3 + 2
5
>>> 3.0 + 2
5.0
>>> 3 + 2.0
5.0
>>> 2.0 ** 4
16.0
```

The rules for calculating expression values are the same as in mathematics:

- The power is computed before the other operations. If there are multiple sequencing power operations, they are performed from right to left.
- Multiplication, division and remainder operations are applied before addition and subtraction. When there are more in a row, they are executed from left to right.
- When we need a different order of computation, we use parentheses (the part in parentheses is calculated first).

```
>>> (5-3) * (2+2)
8
>>>
```

We end our work in the Python shell by typing the command `quit()`.

```
>>> quit()
```

## Calculating - check your understanding

Make sure you understand the rules of calculating in Python by answering the following questions.

```{mchoice}
:answer1: 15
:answer2: 30
:answer3: 50
:answer4: 125
:correct: 2

What is the value of the expression ``5 + 5 * 5``?
```

```{mchoice}
:answer1: 3
:answer2: 0
:answer3: 5
:answer4: 6
:correct: 3

   What is the value of the expression ``4 + 11 % 5``?
```

```{mchoice}
:answer1: 60
:answer2: 100000000
:answer3: 1000000
:answer4: 300
:correct: 2


   What is the value of the expression ``10 ** 2 ** 3``?
```

```{mchoice}
:answer1: 1.666666
:answer2: 1
:answer3: 11.666666
:answer4: 12
:correct: 4

   What is the value of the expression ``15 - 10 // 3``?
```

```{mchoice}
:answer1: 5.0
:answer2: 5
:answer3: 1.0
:answer4: 1
:correct: 1


   What is the value of the expression ``15 / (5 - 2)``?
```
