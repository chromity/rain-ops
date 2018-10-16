from django.shortcuts import render
from bot.models import SensorData
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(18, GPIO.IN)

import serial 
import string
import logging


def index(request):
    data = SensorData.objects.order_by('date_time')
    return render(request, 'data/index.html', {'data': data})

def load(request):
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600)
    
        noise_ave = 0
        for i in range(0,60):
            serial_line = str(ser.readline())

            s = serial_line.split("\\")
            noise = s[0]
            noise = noise[2:]

            noise_ave = noise_ave + int(noise)

        water_lvl = 0
        if GPIO.input(14) == 0:
            water_lvl = 1
        if GPIO.input(18) == 0:
            water_lvl = 2
        if GPIO.input(15) == 0:
            water_lvl = 3

        rain_audio_level = noise_ave / 60

        is_raining = None
        if GPIO.input(2) == 1:
            is_raining = False
        else: 
            is_raining = True

        data = SensorData()
        data.water_level = water_lvl
        data.rain_audio_level = rain_audio_level
        data.is_raining = is_raining
        data.save()

        GPIO.cleanup()
        
        return HttpResponse(200)
    except:
        return HttpResponse(500)

