# current_time = datetime.datetime.now()
# timestamp = current_time.strftime("%d.%m.%Y")

# with open("names.txt", 'r') as file:
#   for line in file:
#         parts = line.split(',')
#  # entries = file.readlines()

#   if len(parts) >= 4:
#     birthdate_str = parts[-1].strip()

#     try:
#         birthdate = datetime.datetime.strptime(birthdate_str, "%d.%m.%Y")

#         if birthdate.day == today_day and birthdate.month == today_month:
#            name = parts[0].strip()
#            print(f"Today is {name}'s Birthday!")

#     except ValueError:
#        continue
# with open("names.txt", 'w') as filename:
#   for entry in entries:
#     current_time = datetime.datetime.now().strftime("%d.%m.%Y")
#     filename.write(f'[{current_time}] {entry.strip()} \n')


# today = datetime.datetime.now()
# today_day = today.day
# today_month = today.month
# birthday_found = False

# today_formatted = f"{today_day:02d}.{today_month:02d}"

# with open("names.txt", 'r') as file:
#     for line in file:
#         parts = line.split(',')
        
#         if len(parts) == 4:
#             birthdate_str = parts[-1].strip()
#             print(f"Checking birthday string: {birthdate_str}")
            
#             try:
#                 birthdate_parts = birthdate_str.split(".")
#                 birthdate_day = int(birthdate_parts[0])
#                 birthdate_month = int(birthdate_parts[1])
#                 birthdate_formatted = f"{birthdate_day:02d}.{birthdate_month:02d}"

#                 print(f"Formatted birthdate: {birthdate_formatted}")
#                 print(f"Today's date: {today_formatted}")

#                 if birthdate_formatted == today_formatted:
#                     name = parts[0].strip() 
#                     print(f"Today is {name}'s Birthday!")
#                     birthday_found = True
#             except ValueError:
#                 print(f"Could not parse date for line: {line.strip()}")
#                 continue

# # If no birthdays were found, print a message
# if not birthday_found:
#     print("No birthdays today.")

import datetime

today = datetime.datetime.now()
today_day = today.day
today_month = today.month
birthday_found = False

today_formatted = f"{today_day:02d}.{today_month:02d}"

with open("names.txt", 'r') as file:
    for line in file:
        parts = line.split(',')
        
        if len(parts) == 4:
            birthdate_str = parts[-1].strip()
            
            try:
                birthdate_parts = birthdate_str.split(".")
                birthdate_day = int(birthdate_parts[0])
                birthdate_month = int(birthdate_parts[1])
                birthdate_formatted = f"{birthdate_day:02d}.{birthdate_month:02d}"

                if birthdate_formatted == today_formatted:
                    name = parts[0].strip() 
                    print(f"Today is {name}'s Birthday!")
                    print(f'Happy birthday {name}')
                    birthday_found = True
            except ValueError:
                continue

# If no birthdays were found, print a message
if not birthday_found:
    print("No birthdays today.")
