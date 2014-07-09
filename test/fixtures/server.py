from __future__ import print_function
import signal
import sys
import time


def handler(signum, frame):
    print("Killed!")
    sys.stdout.flush()
    raise SystemExit

signal.signal(signal.SIGQUIT, handler)
signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

if __name__ == '__main__':
    while True:
        print("Still here")
        sys.stdout.flush()
        time.sleep(1)
