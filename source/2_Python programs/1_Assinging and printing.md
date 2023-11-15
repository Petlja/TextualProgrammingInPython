# Assing a value to a variable and printing from  a program

Python programs consist of stetments. Let's look at some of the basic Python stetments we will use to write the first programs.

## Assigning a value to a variable

Variable is a named space in the memory of a computer, in which we can store values of any kind (number, text, logical value, or something else). Intermediate results are often placed in variables when calculating. When we run a Python shell, we can assign a value to a variable with one command, and then use the value of that variable in the following commands. For example:

```
>>> base = 6*8
>>> base
48
>>> base * 1.5
72.0
>>> base * 1.6
76.80000000000001
```

```{infonote}

**Value assignment statement**

The value assignment statement is written by writing the name of a variable, followed by the equals sign ``=``, and then the expression whose value we assign to the variable. We also consider integers and real numbers to be expressions (these are the simplest possible expressions).
```

```{infonote}

**Names of variables**

Variable names (as well as other names in programs we write) can consist of uppercase and lowercase letters, digits and underscore, but they cannot begin with a digit.

Python distinguishes between uppercase and lowercase letters. *N* and *n* are different names and if we use them both, they would represent two different variables.

The variable name can be as long as we need it.

When writing programs (or individual statements), we try to give the variables meaningful names so that the commands and programs are as clear as possible.
```

In Python, it is a common style that capital letters are not used (though allowed), and when a name is made up of more than one word, those words are separated by an uderscore, for example, *price_of_one_piece*. Numbers are used in names when it makes sense (which is not often).

# Variable names - check your understanding

Check your understanding of variable names by answering the next question. 

<!--
.. dragndrop:: console__basics_quiz_variable_names
    :feedback: Try again!
    :match_1: 2_date ||| invalid, starts with an illegal character
    :match_2: pet_no_2 ||| valid name
    :match_3: state_at_23:59 ||| invalid, contains an illegal character

    Match the proposed variable names with the answers.

-->

```{mchoice}
   :answer1: vArIaBlE
   :answer2: а1
   :answer3: 2D_graphics
   :answer4: _3D_graphics
   :answer5: pet-no-2
   :correct: 1,2,4

   Which of these can be the name of a variable?

```

## Print values from a program

In interactive work, it is enough to enter an expression to see its value, but we cannot use that in programs. To print something from a program, we use the *print()* function. For now, we will use only the simplest form of this function.

The expression whose value we want to print is put between brackets, for example:

```
>>> print(2 + 2)
4
>>>
```

With a single call of function *print()* we can print multiple values. Expressions whose values we want to print are listed between brackets and separated by commas, for example:

```
>>> a = 10
>>> b = 20
>>> circumference  = 2*a + 2*b
>>> area = a*b
>>> print(circumference, area)
60 200
>>>
```

```{infonote}

We have already encountered the functions in the chapters on Karel, we recognize them by the parentheses behind the name. Recall, we call the data that we specify between parentheses **parameters** or **arguments**. We'll talk more about functions soon.

```