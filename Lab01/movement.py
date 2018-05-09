#!/usr/bin/env python3
from ev3dev.ev3 import *
from helper import LargeMotorPair
import time

btn = Button()

cs = ColorSensor()

cs.mode = 'COL-REFLECT'

ml = LargeMotor('outB')
mr = LargeMotor('outC')
m = LargeMotorPair(OUTPUT_B, OUTPUT_C)

ts = TouchSensor(); assert ts.connected, "Connect a touch sensor to any port"


while not btn.any():

    if ts.value():
        m.reset()
        m.run_to_rel_pos(speed_sp=400, position_sp=(-2*360))
        time.sleep(1)
        m.wait_until_not_moving()
        mr.run_to_rel_pos(speed_sp=400, position_sp=1*360)
        time.sleep(0.5)
        mr.stop(stop_action='brake')
        m.run_to_rel_pos(speed_sp=400, position_sp=2*360)
        time.sleep(1)
        m.wait_until_not_moving()
        ml.run_to_rel_pos(speed_sp=400, position_sp=4 * 360)
        time.sleep(1)
        ml.stop(stop_action='brake')
        while cs.value() > 30:
            ml.run_forever(speed_sp=400)
            mr.run_forever(speed_sp=400)

    if cs.value() < 30:
        ml.run_forever(speed_sp=450)
        mr.stop(stop_action='brake')
    else:
        ml.stop(stop_action='brake')
        mr.run_forever(speed_sp=450)

ml.stop(stop_action ='brake')
mr.stop(stop_action = 'brake')