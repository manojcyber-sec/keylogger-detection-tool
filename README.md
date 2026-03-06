# Keylogger Detection Tool

A simple cybersecurity tool that monitors running processes and detects potential keylogger activity.

## Features

- Real-time process monitoring
- Suspicious keyword detection
- Trusted process whitelist
- Logging of suspicious activity
- Web dashboard for monitoring

## Technologies Used

- Python
- Flask
- psutil
- threading

## Project Structure

keylogger-detection-tool
│
├── dashboard
│   └── app.py
│
├── src
│   └── process_scanner.py
│
├── logs
│
├── requirements.txt
└── README.md

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the dashboard:

python dashboard/app.py

Open browser:

http://127.0.0.1:5000
