print(input("Name a title for your routine "))
waketime=input("What time did you wake up at?")
print("I woke up at "+waketime)
school=input("Did you go to school today?(Yes or No)")
if school=="Yes":

    print("I went to school today")
else:
    print("I did not go to school today")
playstudy=input("Did you play, study or both?")
if playstudy=="play":
    print("I played today")
elif playstudy=="study":
    print("I studied")
else:
    print("I played and studied")
studytime=int(input("How much do you study in a week?(In hours)"))
print("I studied for",studytime,"hours this week")
