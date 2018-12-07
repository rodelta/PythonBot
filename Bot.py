from time import sleep

import Sea


# *** Main ***
def main():
    print 'Bot start'
    print 'Bot end'
def checkDependencies():
    from sys import modules

    depends = ['cv2', 'numpy', 'win32api', 'win32con', 'win32gui', 'win32ui']
    missing = [dep for dep in depends if dep not in modules]
    if missing:
        print 'Error, dependencies not found: {}'.format(', '.join(missing))
        print 'Exiting program'
        raise SystemExit

if __name__ == '__main__':
    main()

# Profiling:
# T = cv.getTickCount()
# print (T - cv.getTickCount()) / cv.getTickFrequency()
#
# start_time = time.time()
# print("Sail -- %s seconds ---" % (time.time() - start_time))
