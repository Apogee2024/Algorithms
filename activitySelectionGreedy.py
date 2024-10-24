activities = ["Play Golf", "Paint", "Cook", "Sleep", "Jog", "Write Code", "Eat"]

startTimes = [1, 3, 1, 3, 4, 6, 8]

endTimes = [3, 4, 4, 6, 6, 9, 9]

#Approach 1:  We can arrange the activities in the order of start times and pick one after another such that none overlaps.
# #But would this give the maximum number of non overlapping activities? No, we should arrange based on end times!

#Approach 2: Arrange the activities in the order of the end times and pick the ones that end first followed by the
# next possible non-overlapping activity that ends first and so on.

def activitySelection(activities, startTimes,endTimes ):
    # define an array for our result
    result = []
    endTime = 0

    for _ in range(len(activities)):
        actStart = startTimes[_]
        actEnd = endTimes[_]
        # if it start after the end time, then we can add it
        if actStart >= endTime:
            result.append(_)
            endTime = actEnd
    schedule = []
    for _ in range(len(result)):
        schedule.append([activities[result[_]],startTimes[result[_]],endTimes[result[_]]])
    return schedule


print(activitySelection(activities,startTimes,endTimes))




