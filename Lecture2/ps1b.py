###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    
    n = len(egg_weights) + 1
    m = target_weight + 1
    tableMemo = [[0 for j in xrange(m)] for i in xrange(n)]

    for i in xrange(1, n):
        for j in xrange(1, m):
            tableMemo[i][j] = tableMemo[i - 1][j]
            if(j >= egg_weights[i - 1] and tableMemo[i][j - 1] + egg_weights[i-1] <= j):
                tableMemo[i][j] = max(tableMemo[i][j], tableMemo[i][j - 1] + egg_weights[i-1])

    print tableMemo
    return tableMemo[len(egg_weights)][target_weight]


def dp_make_weight2(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    
    # def sumWeight(dictmemo):
    #     total = 0
    #     for i in dictmemo.keys():
    #         total += i * dictmemo[i]
    #     return total
    # if(target_weight == 0):
    #     return sumWeight(memo)
    # elif target_weight < 0:
    #     return -1
    # else:
    #     result = 0
    #     nextItem = max(egg_weights)
    #     #Explore left branch
    #     withVal = dp_make_weight2(egg_weights,
    #                         target_weight - nextItem, memo)
    #     withVal
    #     #Explore right branch
    #     withoutVal = fastMaxVal(egg_weights, target_weight, memo)
    #     #Choose better branch
    #     if withVal > withoutVal:
    #         result = (withVal + nextItem)
    #     else:
    #         result = (withoutVal)
    #     memo[nextItem] = result
    # return result

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()