#!/bin/bash

#this is the GPIO pin connected to the lead on switch labeled OUT
GPIOpin1=23

#this is the GPIO pin connected to the lead on switch labeled IN
GPIOpin2=24

echo "$GPIOpin1" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio$GPIOpin1/direction
echo "$GPIOpin2" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio$GPIOpin2/direction
echo "1" > /sys/class/gpio/gpio$GPIOpin2/value
while [ 1 = 1 ]; do
power=$(cat /sys/class/gpio/gpio$GPIOpin1/value)
if [ $power = 1 ]; then
sleep 1
power=$(cat /sys/class/gpio/gpio$GPIOpin1/value)
else
sleep 1
if [[ $UID != 0 ]]; then
    echo "0" > /sys/class/gpio/gpio$GPIOpin2/value
    echo "Sending kill signal to PiPUB..."
    sleep 1
    echo "1" > /sys/class/gpio/gpio$GPIOpin2/value
    echo "Raspberry Pi shutting down..."
    sleep 1
    sudo poweroff
else
    echo "0" > /sys/class/gpio/gpio$GPIOpin2/value
    echo "Sending kill signal to PiPUB..."
    sleep 1
    echo "1" > /sys/class/gpio/gpio$GPIOpin2/value
    echo "Openelec shutting down..."
    sleep 1
    poweroff
fi
fi
done
