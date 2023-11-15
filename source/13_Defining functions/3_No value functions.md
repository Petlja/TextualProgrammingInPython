# Functions that do not return value

Functions that do not return value just do some work and we use them as commands. Such were, for example, the *back()* or *take_at_neighboring_square()* functions, which we wrote in a section dedicated to managing Karel. let's look at an example of such function in a program with a text interface.

```{questionnote}

**Example - transportation:**

It takes 55, 35, 40 and 20 minutes respectively to members of a family of four to arrive home from where they are, provided that they start going home before 4 p.m. Otherwise they need 15 minutes more.

Write a program that loads the departure time in hours and minutes for each family member and lists the time of arrival home.
```

The *process_family_member* function performs all the necessary actions for one family member: it loads the departure time, than based on departure time it extends the duration of the trip if necessary, then calculates and prints the time of arrival home. In the main program, this function is just called for each family member.

```{py-code} 6

def process_family_member(which_one, travel_duration):
    prompt = 'Enter the hour and minute of departure of the ' + which_one + ' member'
    s_hour, s_min = input(prompt).split()
    departure_hour, departure_minute = int(s_hour), int(s_min)
    if departure_hour >= 16:
        travel_duration += 15
    arrival_total_minutes = departure_hour * 60 + departure_minute + travel_duration
    arrival_hour = arrival_total_minutes // 60
    arrival_minute = arrival_total_minutes % 60
    print('The', which_one, "member arrived home at", arrival_hour, "hours and", arrival_minute, "minutes.")

process_family_member("first", 55)
process_family_member("second", 35)
process_family_member("third", 40)
process_family_member("fourth", 20)

```

Finally, let's mention some of the benefits of writing functions that, because of the shortness of our examples and tasks, could not come to the fore:

- Functions in long programs are often used to decompose the main part of a program and make it shorter and easier to understand. Our programs are not so long that it would be necessary to decompose them, but they show how it could be done with longer programs.
- Functions can help us avoid repeating the same or similar code in programs. Repeating the code should be avoided as such code is harder to maintain - every change should be made in multiple places, which is tedious and subject to errors and omissions.
- When we write functions, we enable others to use parts of our code more easily. The functions we write can be extracted into a separate module, which other people can easily include in their programs.
- For very large programs, forming functions allows the program to be split into multiple files instead of one huge and incomprehensible file.
