#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#
import bisect
def minimumLoss(price):
    ans=float('inf')
    stack=[price[0]]
    for num in price[1:]:
        if num<stack[0]:
            ans=min(ans,stack[0]-num)
            stack.insert(0,num)
        else:
            index=bisect.bisect(stack,num)
            if index<len(stack):
                ans=min(ans,stack[index]-num)
            stack.insert(index,num)
    return ans

price=[20,7,8,2,5]
ans=minimumLoss(price)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
