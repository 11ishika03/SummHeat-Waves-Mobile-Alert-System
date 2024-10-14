#ISHIKA KHANDELWAL

import pandas as pd
from twilio.rest import Client

def detect_heatwaves(data, threshold=30, consecutive_days=3):
    data['heatwave'] = False
    count = 0

    for i in range(len(data)):
        if 'temperature' in data.columns:
            if data['temperature'][i] > threshold:
                count += 1
            else:
                count = 0

            if count >= consecutive_days:
                data['heatwave'][i] = True
        else:
            print("Column 'temperature' does not exist in the DataFrame.")
            return data

    return data

def send_sms(to, message):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_='+1234567890',
        to=to
    )

    print(f"Message sent to {to}: {message.sid}")

# Update the path to the CSV file
data_path = r'E:\AICTE Internship\Summer Heat Waves Mobile Alert System\historical_temperature_data.csv'

# Load historical temperature data from the updated CSV file path
data = pd.read_csv(data_path)

# Print the DataFrame to check columns and data
print(data.head())  # Display the first few rows of the DataFrame
print("Columns in DataFrame:", data.columns.tolist())  # List the columns

# Strip any leading/trailing spaces from column names
data.columns = data.columns.str.strip()

# Apply heatwave detection
data = detect_heatwaves(data)

# Check for heatwaves and send notifications
for index, row in data.iterrows():
    if row['heatwave']:
        send_sms('+19876543210', f"Heatwave detected on {row['date']} with temperature {row['temperature']}°C.")
