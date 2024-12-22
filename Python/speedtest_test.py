import speedtest
import datetime
import time
import csv
import os

# Initialize Speedtest
st = speedtest.Speedtest()

# Function to perform speed test and log data to CSV
def speed_testing():
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Measuring internet speed at {today}...")

    # Measure download and upload speeds
    download = st.download() / 1_000_000  # Convert to Mbps
    upload = st.upload() / 1_000_000  # Convert to Mbps

    download_speed = f"{download:.2f}"
    upload_speed = f"{upload:.2f}"

    # Print speeds to the console
    print(f"Download Speed: {download_speed} Mbps")
    print(f"Upload Speed: {upload_speed} Mbps")

    # Log the results into a CSV file
    log_speed_to_csv(today, download_speed, upload_speed)

# Function to log the speed test results into a CSV file
def log_speed_to_csv(timestamp, download_speed, upload_speed):
    # Define CSV file path
    csv_file = "internet_speed.csv"

    # Check if the file exists
    file_exists = os.path.exists(csv_file)

    # Open the CSV file and write the data
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write header if the file does not exist
        if not file_exists:
            writer.writerow(["Timestamp", "Download Speed (Mbps)", "Upload Speed (Mbps)"])
        
        # Write the current speed data
        writer.writerow([timestamp, download_speed, upload_speed])

# Main script to run the speed test every 5 minutes


# Run the script
if __name__ == "__main__":
    speed_testing()
