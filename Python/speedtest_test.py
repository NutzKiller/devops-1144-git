import speedtest
import datetime

st = speedtest.Speedtest()
today = datetime.datetime.now().strftime("[%d/%m/%Y/%H:%M:%S]")

def speed_testing():
  print("Measuring download speed...")
  download = st.download()
  print(f"Download speed: {download / 1_000_000:.2f} Mbps") 

  print("Measuring upload speed...")
  upload = st.upload()
  print(f"Upload speed: {upload / 1_000_000:.2f} Mbps")

print(today)
speed_testing()