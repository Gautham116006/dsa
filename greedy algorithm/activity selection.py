"""
Given N activities with their start and finish day given in array start[ ] and end[ ].
Select the maximum number of activities that can be performed by a single person, assuming that a person can only work
on a single activity at a given day.
Note : Duration of the activity includes both starting and ending day
"""


# sort the end dates
# re-arrange the start dates too
# once sorted look for number of non overlapping sets

def condition(arr):
    return arr[1], arr[0]
# end def condition


def activity_selection(start, end):
    activities = list([s, e] for s, e in zip(start, end))
    activities.sort(key=condition)

    curr_activity = activities[0]
    result = 1
    for activity in activities[1:]:
        if activity[0] <= curr_activity[1]:
            continue
        else:
            result += 1
            curr_activity = activity
        # end if
    # end for

    return result
# end def activity_selection


print(activity_selection([7, 6, 2, 7, 3], [10, 6, 10, 9, 5]))
