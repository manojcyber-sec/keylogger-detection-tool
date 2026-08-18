# Keylogger Detection Tool

A Python-based cybersecurity tool that monitors running processes and identifies potentially suspicious keylogger-related activity.

## Overview

Keyloggers are malicious programs that can capture user keystrokes and expose sensitive information.

This project demonstrates a defensive approach to detecting potential keylogger activity by monitoring running processes, checking suspicious indicators, and recording detected activity for further analysis.

## Features

- Real-time process monitoring
- Suspicious process and keyword detection
- Trusted process whitelist
- Suspicious activity logging
- Web dashboard for monitoring
- Lightweight Python-based detection

## Detection Approach

The tool continuously monitors running processes and checks them against predefined suspicious indicators.

When potentially suspicious activity is detected:

1. The process is identified.
2. Suspicious indicators are checked.
3. Trusted processes are filtered using a whitelist.
4. Suspicious activity is logged.
5. The dashboard can be used to review detected activity.

## Technologies Used

- Python
- Flask
- psutil
- Threading

## Project Structure

```text
keylogger-detection-tool/
├── dashboard/
│   └── app.py
├── src/
│   └── process_scanner.py
├── logs/
├── requirements.txt
└── README.md
