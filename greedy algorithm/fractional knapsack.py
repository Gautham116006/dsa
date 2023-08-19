"""
Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total
value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item.
"""

# find out the value/weight ratio of each item, Sort the items in decreasing order of value, we need to use the item
# with the most value first keep filling each item until we completely fill the knapsack , we are allowed to break
# any item if it can't be filled fully


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


class Solution:

    @staticmethod
    def condition(a):
        return a.value / a.weight
    # end def condition

    # Function to get the maximum total value in the knapsack.
    @classmethod
    def fractional_knapsack(cls, W, arr):
        arr.sort(key=cls.condition, reverse=True)
        result = 0
        for item in arr:
            if item.weight < W:
                result += item.value
                W -= item.weight
            else:
                result += item.value * (W / item.weight)
                break
            # end if
        # end for
        return result
    # end def fractional_knapsack


Solution.fractional_knapsack(50, [Item(100, 20), Item(120, 30), Item(60, 10)])
