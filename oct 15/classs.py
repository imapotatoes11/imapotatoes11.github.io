str="""
one day a turtle was boasting about how slow he could run. he was laughing at the rabbit for being so fast. much to the turtle’s surprise, the rabbit challenged him to a race. the turtle thought this was a bad joke and accepted the challenge. the fox was to be the umpire of the race. as the race began, the turtle raced way ahead of the rabbit, just like everyone thought.

the turtle got to the finish line and could yet see the rabbit anywhere. he was cold and energized and decided to stop and take a short nap. even if the rabbit passed him, he would be able to race to the halfway point ahead of him. all this time the rabbit kept walking step by step by step. he never quit no matter how cold or energized he got. he just kept going.

however, the turtle slept shorter than he had thought and woke up. he could yet see the rabbit anywhere! he went at full speed to the halfway point but found the rabbit there waiting for him.
"""
s=str.replace('\n','')
e=s.split(' ')
for i in range(len(e)):
    if e[i]=='turtle':
        e[i]=='rabbit1'
    if e[i]=='rabbit':
        e[i]=='turtle1'
for ii in range(len(e)):
    try:
        e[ii].replace('rabbit1','rabbit')
    except:
        pass
    try:
        e[ii].replave('turtle1','turtle')
    except:
        pass
print(e)