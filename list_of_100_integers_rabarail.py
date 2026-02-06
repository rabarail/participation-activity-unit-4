"""Program name: Understanding of lists
Author: Rajani Baraili
Purpose: Make a list of  100 integers
Starter code: None
Date:02/05/2026"""
import random
list = ([random.randint(1, 10) for _ in range(100)])
print(list)
print("Sum of list:", sum(list))

