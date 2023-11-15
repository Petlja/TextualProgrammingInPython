# Quiz 1

```{questionnote}

**Task - geographic coordinates in GPS format**

You found an old map of the buried treasure and read the coordinates of the treasure in degrees, minutes and seconds. However, your GPS device only supports geographical coordinates in degrees as real numbers (floats).

Write a program that for a given coordinate in degrees, minutes and seconds, prints a real number of degrees.
```

The program is almost completely written. An expression needs to be added to calculate the real number of degrees. To convert the (angular) minutes into degrees, we divide them by $60$, and we convert the seconds into degrees by dividing by $60 \cdot 60 = 3600$.

```{py-code} 3

   degrees = int(input())
   minutes = int(input())
   seconds = int(input())

   def deg_min_sec_to_degrees(deg, min, sec):
        # complete the function

   float_degrees = deg_min_sec_to_degrees(degrees, minutes, seconds)
   print(float_degrees)


```

```{questionnote}

**Task - Geographic coordinates in the format for the old map**

After you realized that the old map from the previous assignment was a joke, you decided to make a similar joke to someone. You have selected a nearby location and read coordinates from your GPS device. Now you need to convert the coordinates from the device in real degrees into whole degrees, whole minutes and rounded seconds, to create a proper "old" map.
```

&#160;    Complete the started program that performs this conversion.

```{py-code} 4

def deg_min_sec(real_degrees):
    # complete the function by calculating three values that the function returns
    # (and then remove the comment from the following line of code)
    # return whole_degrees, whole_minutes, whole_seconds

real_degrees = float(input())
whole_deg, whole_min, whole_sec = deg_min_sec(real_degrees)
print(whole_deg, whole_min, whole_sec)


```

```{questionnote}

**Task - Plumber:**

Mike is a plumber and has three interventions planned for today. For each intervention, Mike will record when it began and when it ended. Based on that information it should be calculated how long Mike spent in the interventions.

A partially written program is given that loads the start and end times in hours and minutes for each Mike's intervention, and then determines and prints the total duration of all interventions.

**Complete the program** by writing the *duration(h1, m1, h2, m2)* function, which calculates how many total minutes elapsed from *h1* hours and *m1* minutes to *h2* hours and *m2* minutes.
```

```{py-code} 5

# write the duration function

def process_one_intervention():
    prompt = "Enter the hour and minute of start and hour and minute of completion of the intervention "
    s1, s2, s3, s4 = input(prompt).split()
    h1, m1, h2, m2 = int(s1), int(s2), int(s3), int(s4)
    return duration(h1, m1, h2, m2)

t1 = process_one_intervention()
t2 = process_one_intervention()
t3 = process_one_intervention()
total_minutes = t1 + t2 + t3
num_hours = total_minutes // 60
num_minutes = total_minutes % 60
print("The interventions lasted a total of", num_hours, "hours and", num_minutes, "minutes")

```