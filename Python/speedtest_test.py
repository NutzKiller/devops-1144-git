# import speedtest
# import datetime

# st = speedtest.Speedtest()
# today = datetime.datetime.now().strftime("[%d/%m/%Y/%H:%M:%S]")

# def speed_testing():
#   print("Measuring download speed...")
#   download = st.download()
#   print(f"Download speed: {download / 1_000_000:.2f} Mbps") 

#   print("Measuring upload speed...")
#   upload = st.upload()
#   print(f"Upload speed: {upload / 1_000_000:.2f} Mbps")

# # print(today)
# # speed_testing()

# with open("speed_log.txt", "a") as file:
#   file.write(f"{today} {speed_testing()}\n")



import speedtest
import datetime
import time
import schedule

st = speedtest.Speedtest()

def speed_testing():
    today = datetime.datetime.now().strftime("[%d/%m/%Y/%H:%M:%S]")
    print("Measuring download speed...")
    download = st.download()
    download_speed = f"Download speed: {download / 1_000_000:.2f} Mbps"
    print(download_speed)

    print("Measuring upload speed...")
    upload = st.upload()
    upload_speed = f"Upload speed: {upload / 1_000_000:.2f} Mbps"
    print(upload_speed)

    # Return speeds as a string
    # return f"{download_speed}\n{upload_speed}"

# Save the output to speed_log.txt
    with open("speed_log.txt", "a") as file:
     file.write(f"{today}\n{download_speed}\n{upload_speed}\n")

schedule.every().sunday.at("09:15").do(speed_testing)
schedule.every().monday.at("09:15").do(speed_testing)
schedule.every().tuesday.at("09:15").do(speed_testing) 
schedule.every().wednesday.at("09:15").do(speed_testing)



while True: 
    schedule.run_pending()
    time.sleep(1)