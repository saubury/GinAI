import config
import RPi.GPIO as GPIO
import time
import threading
import itertools


def pump_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for this_gpio in config.pump_gpio:
        print(f'Setting GPIO.setup({this_gpio}, GPIO.OUT)' )
        GPIO.setup(this_gpio, GPIO.OUT)

    GPIO.setwarnings(True)

def pump_thread_runner(gpio_pump_name, run_seconds):
    print (f'START gpio_pump_name {gpio_pump_name} run_seconds {run_seconds}')
    # time.sleep(pumpPreWaitTime)
    GPIO.output(gpio_pump_name, GPIO.HIGH)
    time.sleep(run_seconds)
    GPIO.output(gpio_pump_name, GPIO.LOW)
    print (f'STOP gpio_pump_name {gpio_pump_name} run_seconds {run_seconds}')

def pump_thread_start(gpio_pump_name, run_seconds):
    thread = threading.Thread(target=pump_thread_runner, args=(gpio_pump_name, run_seconds))
    thread.start()

def do_drink(pump_instructions_ml):
    pump_setup()
    pumpruntime = lambda x: x / config.ML_per_second
    pump_instructions_sec = list(map(pumpruntime,pump_instructions_ml))

    # Iterate over multiple lists with zip
    for (this_gpio, this_runtime) in zip(config.pump_gpio, pump_instructions_sec):
        pump_thread_start(this_gpio, this_runtime)

    return (max(pump_instructions_sec))

if __name__ == '__main__':
    pump_instructions_ml = [50,50,50,50]
    do_drink(pump_instructions_ml)

