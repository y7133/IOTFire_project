from mq import *
import sys, time


print("Press CTRL+C to abort.")
    
mq = MQ1();
while True:
    perc = mq.MQPercentage()
    sys.stdout.write("\r")
    sys.stdout.write("\033[K")
    sys.stdout.write("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm, LNG: %g ppm" % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"], perc["GAS_LNG"]))
    sys.stdout.write(" Flame:%d"%perc["FLAME"])
    sys.stdout.flush()
    time.sleep(0.1)


print("\nAbort by user")