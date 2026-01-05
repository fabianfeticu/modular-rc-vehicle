# modular-rc-vehicle
This project is a custom-built RC vehicle designed from scratch, combining embedded systems, wireless communication, and desktop software. A PC-based GUI communicates through a Raspberry Pi Pico and long-range NRF24L01 modules to an Arduino Mega onboard the car, which controls motors, steering, sensors, and a programmable 5×5 LED matrix built using shift registers. The chassis and mechanisms are currently built using simple materials due to lack of access to a 3D printer, with plans to redesign mounts, enclosures, and structural parts using 3D-printed components. The project focuses on modular design, hardware-software integration, and iterative engineering under real constraints.


The project is modular and more features will be added on the go (future features I'd like to add include: Temperature and other useful sensors, ultrasonic sensors, a display for displaying messages)

# Modular RC Car with Wireless Control and LED Matrix

This project is a custom-built RC vehicle designed from scratch using modular electronics and software.

## Overview
The system consists of:
- A PC-based GUI for control and visualization
- A Raspberry Pi Pico acting as the communication bridge
- NRF24L01+PA+LNA modules for wireless transmission
- An Arduino Mega onboard the vehicle handling motors, steering, sensors, and LED output

## Current Progress (~15%)
- ✔ Physical chassis using a sandwich-style structure(using two plastic "plates"),(no 3D printer)
- ✔ Steering system using a servo
- ✔ Dual motor setup with temporary mechanical mounting
- ✔ 5x5 LED matrix using three 8-bit shift registers
- ✔ LED matrix control library with symbols and patterns
- ✔ Initial GUI for motor control and LED output

## In Progress
- Wireless communication protocol
- Motor driver module (waiting for MOSFETs and relays)
- GUI pattern animation and custom LED pattern upload
- Improved mechanical design (planned 3D-printed parts)

## Why This Project
This project combines:
- Embedded systems (Arduino, Pico)
- Wireless communication
- Desktop software development
- Mechanical design under constraints
- Custom hardware abstraction libraries

## Planned Improvements
- Fully modular electronics stack
- 3D-printed mounts and enclosures
- Better steering geometry
- Expandable sensor system
