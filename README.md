# MuBank
# >An embedded linux project based on raspberry pi 3b+
# Bank Embedded Linux Project Documentation

## Overview
This project implements a basic bank system using embedded Linux on a Raspberry Pi. It allows users to authenticate, check their balance, deposit, and withdraw money. It also sends transaction notifications to users via email.

## Files
1. **main.py**: This is the main script of the project. It sets up GPIO pins, initializes user data, creates a GUI, and provides functions for user interaction.
2. **emails.py**: This file contains the `Users` class, which manages user data and transactions. It also provides methods for withdrawing, depositing, updating balance, and updating transaction history.
3. **sendingEmails.py**: This file contains the `sendEmail` function, which sends transaction notifications to users via email using SMTP.
4. **Passwords.py**: this file contains password from Gmail please dont forgot to add your password [see the demo:](https://www.youtube.com/watch?v=g_j6ILT-X0k)
5. **userData.txt** this is the database for users and trancections
6. **Userdata.py**: this is file to only put users in userData.txt rather than typing them manually

## Hardware Requirements
- Raspberry Pi (any model with GPIO pins)
- LEDs (for visual feedback)
- Buzzer (for audio feedback)

## Software Requirements
- Raspbian OS or any Linux distribution for Raspberry Pi
- Python 3.x
- Required Python packages (RPi.GPIO, tkinter, PIL)

## Installation and Setup
1. Install Raspbian OS on your Raspberry Pi.
2. Install Python 3.x and required packages (`RPi.GPIO`, `PIL`, etc.).
3. Clone or download the project files to your Raspberry Pi.

## Usage
1. Connect the LEDs and buzzer to the GPIO pins of your Raspberry Pi according to the pin configuration in `main.py`.
2. Run the `main.py` script to start the bank system GUI.
3. Enter your username and password to authenticate.
4. Use the GUI to deposit, withdraw, and check balance.
5. Transaction notifications will be sent to your email.

## Project Structure
- **main.py**
  - Initializes GPIO pins.
  - Sets up the GUI using tkinter.
  - Provides functions for authentication, deposit, withdraw, and displaying user information.
  - Controls LEDs and buzzer for feedback.

- **emails.py**
  - Contains the `Users` class for managing user data.
  - Provides methods for withdrawing, depositing, updating balance, and updating transaction history.

- **sendingEmails.py**
  - Contains the `sendEmail` function for sending transaction notifications via email.

## Testing
- GUI testing done manually to ensure proper functionality and user experience.
  
## GPIO Pinout (Raspberry Pi 3+)
- `Getinfo_led_pin`: GPIO 20 (pin 38)
- `deposit_led_pin`: GPIO 21 (pin 40)
- `withdraw_led_pin`: GPIO 26 (pin 37)
- `login_led_pin`: GPIO 16 (pin 36)
- `Buzzer_pin`: GPIO 19 (pin 35)

This bank embedded Linux project provides a basic banking system that can be further expanded and customized. 
It demonstrates the use of GPIO pins for hardware interaction\
GUI development with tkinter, and email notification functionality in an embedded Linux environment.
