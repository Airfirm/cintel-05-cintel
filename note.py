from collections import deque

# Create an empty deque
empty_deque = deque()
print(empty_deque) 

# Create a deque by passing in a list with values
temp_deque_F = deque( [46, 48, 37, 44, 45] )
print(temp_deque_F)  

# Create a deque by passing in a list variable
temp_list_C = [3, 4, 6, 4, 3, 2]
temp_deque_C = deque( temp_list_C )
print(temp_deque_C )

# append elements to the end (right)
temp_deque_F.append(50)
temp_deque_F.append(52)
temp_deque_F.append(54)
temp_deque_F.append(51)
print(temp_deque_F)

# append elements to the front (left)
temp_deque_F.appendleft(60)
temp_deque_F.appendleft(62)
temp_deque_F.appendleft(64)
temp_deque_F.appendleft(61)
print(temp_deque_F)
print(len(temp_deque_F))

# remove elements from the right (end) it's default, value(61)
temp_deque_F.pop() 
print(temp_deque_F)
print(len(temp_deque_F))

# remove elements from the left (front) value(51)
temp_deque_F.popleft() 
print(temp_deque_F)
print(len(temp_deque_F))

# get the length
print(len(temp_deque_F))

# clear the deque
temp_deque_F.clear()  
print(temp_deque_F)

from collections import deque

# Initialize deque with a max length of 3 to store last 3 stock prices
msft_prices = deque(maxlen=3)

# Clear the deque (we might call this at the start of a new day)
msft_prices.clear()

# Simulate updating the stock price with new values
msft_prices.append(310.35)
print("MSFT stock prices:", list(msft_prices))

msft_prices.append(312.31)
print("MSFT stock prices:", list(msft_prices))

msft_prices.append(315.25)
print("MSFT stock prices:", list(msft_prices))

msft_prices.append(317.41)
print("MSFT stock prices:", list(msft_prices))

msft_prices.append(319.51)
print("MSFT stock prices:", list(msft_prices))

msft_prices.append(321.42)
print("MSFT stock prices:", list(msft_prices))

from collections import deque
import random

# Create a deque with max length 20
recent_temps = deque(maxlen=20)

# Step 1: Fill deque with 20 initial temperature readings
print("Initial 20 temperature readings:")
for i in range(20):
    temp = random.randint(65, 85)
    recent_temps.append(temp)
    print(f"Reading {i+1}: {temp}")

print("-" * 60)

# Step 2: Continue adding new readings and calculating moving average
for i in range(10):  # Simulate 10 more new readings
    new_temp = random.randint(65, 85)
    recent_temps.append(new_temp)

    # Calculate moving average of the most recent 20 readings
    moving_avg = sum(recent_temps) / len(recent_temps)

    print(f"New Reading {i+21}: {new_temp}")
    print(f"Last 20 temperatures: {list(recent_temps)}")
    print(f"Moving Average (last 20): {moving_avg:.2f}")
    print("-" * 60)

from collections import deque

# Predefined list of temperature readings (simulate data stream)
temperature_stream = [72, 68, 75, 70, 81, 69, 74, 76, 73, 78, 77, 66, 84, 71, 80, 79, 67, 83, 65, 85]

# Create deque to hold the last N readings
N = 10
recent_temps = deque(maxlen=N)

# Step 1: Add the first N readings and print them
print(f"Initial {N} temperature readings:")
for i in range(N):
    temp = temperature_stream[i]
    recent_temps.append(temp)
    print(f"Reading {i+1}: {temp}")

print("-" * 60)

# Step 2: Continue adding new readings and compute moving average
for i in range(N, len(temperature_stream)):
    new_temp = temperature_stream[i]
    recent_temps.append(new_temp)

    moving_avg = sum(recent_temps) / len(recent_temps)

    print(f"New Reading {i+1}: {new_temp}")
    print(f"Last {N} temperatures: {list(recent_temps)}")
    print(f"Moving Average (last {N}): {moving_avg:.2f}")
    print("-" * 60)
