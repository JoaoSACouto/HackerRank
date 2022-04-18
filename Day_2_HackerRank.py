#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#
meal_cost = float(input().strip())
tip_percent = int(input().strip())
tax_percent = int(input().strip())
total_cost = float
tip_cost = float 
tax_cost = float


tip_cost = (meal_cost * tip_percent)/100
tax_cost = (meal_cost * tax_percent)/100
total_cost = tax_cost + tip_cost + meal_cost

print(round(total_cost))
