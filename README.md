# SummHeat-Waves-Mobile-Alert-System
Here's a sample `README.md` document for your "Heat Waves Mobile Alert System" project. You can customize it further as needed.

```markdown
# Heat Waves Mobile Alert System

## Overview
The Heat Waves Mobile Alert System is designed to monitor temperature data and send alerts via SMS when a heatwave is detected. The system analyzes historical temperature data, determines if a heatwave condition exists, and notifies users through Twilio SMS services.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Features
- Monitors historical temperature data from a CSV file.
- Detects heatwaves based on specified temperature thresholds and consecutive days.
- Sends SMS notifications to users when a heatwave is detected.

## Technologies Used
- Python 3.x
- Pandas
- Twilio API
- CSV for data storage

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Install the required packages:
   ```bash
   pip install pandas twilio
   ```

# Usage
1. Update the `historical_temperature_data.csv` file with your temperature data. Ensure it has a `temperature` column.
2. Configure your Twilio account by replacing `your_account_sid`, `your_auth_token`, and the `from_` number in the `send_sms` function.
3. Run the script:
   ```bash
   python heat_wave_detection.py
   ```

# How It Works
1. The script reads historical temperature data from a CSV file.
2. It analyzes the temperature data to detect heatwaves based on a defined threshold and the number of consecutive days above that threshold.
3. If a heatwave is detected, an SMS notification is sent to the specified phone number using the Twilio API.

# Sample CSV Format
Ensure your `historical_temperature_data.csv` file has the following structure:
```
date,temperature
2024-01-01,28
2024-01-02,31
2024-01-03,34
...
```

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Output
![Screenshot (65)](https://github.com/user-attachments/assets/a605b9fc-a8d1-43c8-989a-fa36e24faa0c)

