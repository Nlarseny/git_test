from time import sleep
import git
import time


iter = 0
while 1:
    iter += 1

    with open("test.txt", 'a') as the_file:
        first = str(iter) + "\n"
        the_file.write(first)

    

    time.sleep(20)