# Quiz

```{questionnote}

**Example - when to depart**

Ronnie should arrive at destination no later than 5:00 pm. Depending on the way of travel he chooses, Ronnie may need 55, 70, 85, or 95 minutes. Write a program that prints for each way of travel when Ronnie needs to leave at the latest to arrive on time.

```

A program that solves this task could look like this:

```{py-code} 4

arrival = 17*60
for travel_duration in (55, 70, 85, 95):
    leaving = arrival - travel_duration
    leaving_hours = leaving // 60
    leaving_minutes = leaving % 60
    print("If the travel lasts", travel_duration, "minutes, Ronnie should leave at", leaving_hours, "hours and", leaving_minutes, "minutes.")



```

```{questionnote}

**Task - trip duration**

George intends to start a 600-kilometer car trip at 9 a.m. and is interested in arriving time if he was traveling at an average speed of 90, 100, 120 or 130 kilometers per hour. Finish the program to list the time of arrival at the destination for each of the aforementioned average speeds.
```

```{py-code} 5

path_length = 600 # Km
leaving = 9       # h
for a in ():  # fix
    trip_duration = path_length / speed # h
    arrival = leaving + trip_duration    # h
    arrival_hours = int(arrival)
    arrival_minutes = round((arrival - arrival_hours) * 60)
    print("At", speed, "km / h the arrival time is at", arrival_hours, "hours and", arrival_minutes, "minutes.")
```

% commented out
%
% path_length = 600
% leaving = 9
% for speed in (90, 100, 120, 130):
%     trip_duration = path_length / speed
%     arrival = leaving + trip_duration
%     arrival_hours = int(arrival)
%     arrival_minutes = round((arrival - arrival_hours) * 60)
%     print("At", speed, "km / h the arrival time is at", arrival_hours, "hours and", arrival_minutes, "minutes.")

```{questionnote}

**Task - final grade**

The sum of 5 Katie's grades so far is 23. Katie expects another grade from the final task. Finish the program below so that for each possible final grade (1, 2, 3, 4, or 5) it prints what the average grade would be in that case.
```

```{py-code} 6

sum_grades_so_far = 23
num_grades_so_far = 5
for # complete the statement
    average_grade = 0 # fix
    print("With the final grade", final_grade, "average grade would be", average_grade)


```

```{questionnote}

**Task - allowance**

Little Theo makes a plan for spending his pocket money over a 14-day vacation. Write a program that, for an average daily spend of 5, 10, or 20 euro, lists how much money in total Theo would need in each case.

```

```{py-code} 7

num_days = 14
# finish the program
```
