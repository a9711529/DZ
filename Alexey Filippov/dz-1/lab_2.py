#coding: utf-8

import math
import random

f = open('nums.txt', 'w')

for i in range(0,5):
    f.write(str(random.randrange(1,50))+'\n')
f.close()

f = open('nums.txt')
nums = f.readlines()
su = int(nums[0]) + int(nums[1])
po = pow(int(nums[2]), int(nums[3]))
sq = math.sqrt(po)
ma = max(su, sq)
co = math.cos(int(nums[4]))
print('sum of first two nums: ' + str(su))
print('sqrt from pow: ' + str(sq))
print('max: ' + str(ma))
print('cos from last num: ' + str(co))




