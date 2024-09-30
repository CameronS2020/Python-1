#nested list practice.

#tracking blood sugar by day and by meal

"""
total = 0
average = 0
times_of_day = ["Breakfast", "Lunch", "Dinner", "Bedtime"]

blood_sugar_levels = []
for time in times_of_day:
    level = input(f"Enter your blood sugar level for {time}: ")
    blood_sugar_levels.append([time, level])

#print(blood_sugar_levels)
for i in range(len(times_of_day)):
    time = times_of_day[i][0]
    level = blood_sugar_levels[i][1]
    total += int(level)
    print(f"at {time} your blood sugar level was: {level}")
print(blood_sugar_levels)

average = total / 4
print(f"your average blood sugar today was: {average:.0f}")
"""

"""
Assignment
Define Time Slots:
Create a list named time_slots with different times of the day, such as "Morning", "Midday", "Afternoon", "Evening".

User Input for Heart Rate:
Use a loop to iterate over each time slot. For each time slot, use the input() function to ask the user to enter their heart rate (in beats per minute). Convert this input to an integer.

Storing Heart Rate Data:
Create an empty list named heart_rates. For each time slot, append a sublist to heart_rates that contains the time slot and the corresponding heart rate.

Calculate Average Heart Rate:
Initialize a variable to keep track of the total heart rate. Use a loop to add up the heart rate recorded at each time slot. Calculate and print the average heart rate at the end.
"""
#making total and average defined, before letting them be calculated later
total = 0

average = 0

#lets the input know to ask for different, preset times.
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

heart_rate = []

for time in time_slots:
    bpm = input(f"Enter your heart rate for the {time}:  ")
    heart_rate.append([time, bpm])

for i in range(4):
    # time = time_slots[i][0]
    #[i][1] not [i][i] stigmatism got me confused.
    bpm = heart_rate[i][1]
    total += int(bpm)
    print(f"at {time} your heart rate was: {bpm}")
print(heart_rate)

average = total / 4
print(f"Your average heart rate today was: {average:.0f}")
#Thank you for your help, it literally worked the second you walked away without me changing anything else.