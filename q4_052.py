#!/usr/bin/env python3

import sys

mean = 0
median = 0
mode = 0

def average(n):
   return sum(n) / len(n)

def middle(n):
   if len(n) % 2 == 0:
      return n[int(len(n) / 2)] + n[int(len(n) / 2 - 1)] / 2
   else:
      return n[int(len(n) / 2)]

def most(n):
   return max(len(n), key=n.count)

def main():
   nums = sorted([float(n.strip('\n'))])
   mean = average(nums)
   median = middle(nums)
   mode = most(nums)
   print('Mean: {:.1f}'.format(mean))
   print('Median: {:.1f}'.format(median))

if __name__ == '__main__':
   main()
