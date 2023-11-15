# Starting a program and program errors

## Running programs in browser

To help you get started, we used the **ActiveCode**  component of the [Runestone Interactive](http://runestoneinteractive.org/) project and enabled you to run Python programs in the web pages of this course. For example, below are the statements we previously entered interactively, but this time written as a program. You can start the program by clicking the "Run" button.

```{py-code} 1

a = 10
b = 20
circumference  = 2*a + 2*b
area = a*b
print(circumference, area)
```

## Running programs from the IDLE environment

It is recommended that you, in addition to writing programs on these web pages, run programs at least occasionally in the *IDLE* environment. Getting used to the *IDLE* environment is important for you to become more independent in programming.

When you run *IDLE* on your computer, open the integrated text editor (File / New File menu) and type in the previous (or any other) program.

When you finish the program, save it (menu File / Save) and then run it (menu Run / Run Module).

```{image} ../../_images/Console/console_run_from_idle.png
:align: center
:width: 350px
```

You will see the result in the interactive shell window.

## Running programs from an online environment

Another way to run your Python program is to use one of the online programming environments. One such environment is <https://repl.it/>.

```{image} ../../_images/Console/console_repl.it_start.png
:align: center
:width: 500px
```

Click on the `+ new repl` button, select the Python language and click `Create repl`. Your web browser will open a page where you can type a program and run it.

```{image} ../../_images/Console/console_repl.it_run.png
:align: center
:width: 500px
```

## Program errors

Sometimes, you may not type a statement in the program exactly as required by the Python rules. In such case, the Python interpreter cannot understand the statement and you receive an error message. Each runtime environment reports an error in a slightly different way, but each of them tells in which line of the program the error occurred and what type of error it is.

The occurrence of errors (also known as bugs) should not worry you as it is a common thing and happens to experienced developers as well. Look at the message carefully, make sure you understand what is wrong, then correct it and run the program again. Understanding error messages is an integral part of programming and can be practiced like many other skills.

To help you understand the error messages you will be getting (and to become less anxious about errors), we recommend that you now try to deliberately make some small mistakes that might anyway happen to you when writing a program.

When you make a few intentional errors, you will gain some experience how error messages look like and it will be easier for you to understand the same messages latter, when they occur unintentionally.

You can try some errors here:

```{py-code} 2

# add statement(s)

```

We have also prepared a few programs with intentionally made mistakes, which we then explain. Programs are short to make errors more noticeable, but in longer programs, debugging is almost the same. Since the error message contains the program line number in which the error occured, in longer programs you just need to first find the program line mentioned and look at that (and possibly the previous) line.

Run each of the following programs, then see the error message and explanation.

```{py-code} 3

prit(2+2)
```

The message says that it is an error of type *NameError*. This means that some of the names in the specified line are unknown to the Python interpreter (name is not defined). Note that the name of the *print* function is not spelled correctly (and the function *prit* does not exist). By inserting the letter *n* the error is corrected and the program works.

```{py-code} 4

result = 2 + 2
print(resultt)
```

The error is of the same type, only this time it refers to the name *resultt*. By removing the superfluous letter *t*, the program becomes correct.

```{py-code} 5

a = 3
b = 2
print(a b)
```

The error is of type *SyntaxError*, which means that Python statement construction rules are not followed. In this case, a comma between *a* and *b* is missing.

```{py-code} 6

a = 3
b = 2
print a, b
```

Another syntax error. Again, the rules of statement construction were not followed, and this time the brackets are missing.

```{py-code} 7

a = 3
b = 0
print(a / b)
```

The error is of type *ZeroDivisionError*. This error is different from the previous ones, because the statement was written correctly and was successfully interpreted. However, the execution of this command resulted in zero division, which is not a permitted operation. The program should be written in such a way that it does not attempt a zero division. The correction in this case depends on what we want our program to do in this situation. One possibility is to check that the divisor is not zero before dividing.

______________________________________________________________________

Make sure you understand these three types of error by answering the question.

<!--
```{eval-rst}
.. dragndrop:: console__program_quiz_errors
    :feedback: Try again!
    :match_1: SyntaxError|||print(3*(2+2)
    :match_2: NameError|||а=3</br>print(a / b)
    :match_3: ZeroDivisionError|||b=3//6</br>print(3 // b)

    Match the error type with the program.
```
-->