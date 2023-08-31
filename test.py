import time

timeout = time.time() + 20
# print(timeout)
# print(time.time())

five_second = time.time()

second = 0
while timeout >= time.time():
    if time.time() - five_second == 5:
        five_second = time.time()
        print(five_second)
