import cv2 as cv
import numpy as np
from time import sleep
from hcsr04 import HCSR04
from girace import GiraceSensor
from motor_DC import dc_motor
from SensorChuva import RainSensor
from SensorLuminosidade import LuminositySensor
from SensorUltrassonico import UltrassonicSensor

def main():
    girace = GiraceSensor()
    rainSensor = RainSensor()
    lumiSensor = LuminositySensor()
    ultraSensor = UltrassonicSensor()

    ultraSensor.init()
    lumiSensor.loopreading()
    rainSensor.loopreading()
    girace.acceleration()
    dc_motor.duty_cycle()

if __name__ == "__main__":
    main()