# ++++++++++++++++ Exponential Backoff ++++++++++++++++

import time

waitTime = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print('Attempts', attempts + 1, 'wait-Time', waitTime)
    time.sleep(waitTime)
    waitTime *= 2
    attempts += 1

