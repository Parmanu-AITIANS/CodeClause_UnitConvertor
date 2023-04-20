import time

def stopwatch():
    start_time = time.time()
    input('Press enter to stop')

    elapsed_time = time.time() - start_time
    mins, secs = divmod(elapsed_time, 60)
    timer = '{:02d}:{:02d}'.format(int(mins), int(secs))
    print(f'Time elapsed: {timer}')

stopwatch()
