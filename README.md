# Real-Time Password Strength Checker

## Overview

This Python application provides a real-time password strength checking tool using Tkinter for the GUI. It evaluates passwords based on length, character types (uppercase, lowercase, digits, special characters), commonality, and entropy.

## Features

- **Password Strength Evaluation**: Checks passwords against criteria for weak, moderate, strong, very strong, and insane strength levels.
- **Real-Time Feedback**: Dynamically updates password strength as you type.
- **Common Password Detection**: Alerts if the password is too common based on a predefined list.
- **Entropy Measurement**: Calculates the password's entropy to gauge randomness.
- **Toggle Password Visibility**: Option to show or hide the entered password.
- **Asynchronous Common Password Loading**: Uses threading to load a large list of common passwords in the background, ensuring smooth application responsiveness.

## Requirements

- Python 3.x
- Tkinter (typically included with Python installations)

## Usage

1. **Installation**: Clone the repository and ensure Python 3.x is installed.
   
2. **Dependencies**: Install required dependencies using `pip`:
   ```bash
   pip install tkinter
   ```

3. **Execution**: Run the application using Python:
   ```bash
   git clone https://github.com/your-username/password-strength-checker.git
   cd password-strength-checker
   python password_strength_checker.py
   ```

4. **Interacting with the Application**:
   - Enter a password in the input field.
   - Password strength is evaluated in real-time and displayed.
   - Use checkboxes and buttons to interact with additional features.

## License

MIT License

Copyright (c) [2024] [harshgharsandiya]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
