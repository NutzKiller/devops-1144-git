import datetime
import time
import sys

# Function for animated text
def animated_text(text, delay=0.05):
    """Prints text with a typewriter animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Function for the birthday celebration
def birthday_celebration(name, age):
    """Celebrates the birthday with the given name and age."""
    print("\n🎉🎈🎂 WELCOME TO THE BIRTHDAY CELEBRATION! 🎂🎈🎉\n")
    time.sleep(1)

    animated_text(f"HAPPY BIRTHDAY, {name.upper()}! 🎊🎉\n")
    time.sleep(1)

    animated_text(f"Wow, {age} years of awesomeness! You’re truly one of a kind, {name}.")
    animated_text("Today is all about YOU, so let’s make it unforgettable! 🥳✨\n")
    time.sleep(1)

    if age < 18:
        animated_text("Enjoy the sweetest years of your life! 🍭🍬 Stay curious and keep dreaming big!")
    elif 18 <= age < 30:
        animated_text("Welcome to the golden years of adventure and growth. 🌟 Keep shining bright!")
    elif 30 <= age < 50:
        animated_text("Life’s just getting started—cheers to wisdom, success, and more cake! 🎂🍷")
    else:
        animated_text("A toast to you, aging like fine wine—better and more refined every year! 🍷🎉")
    print()

    animated_text("🎵🎤 Time for some music and celebration! 🥳🎶")
    time.sleep(0.5)
    for _ in range(3):
        animated_text("🎈🎉 🎂 HURRAY! 🎂 🎉🎈", delay=0.1)

    animated_text("\nLet’s countdown to another fantastic year!\n")
    for i in range(5, 0, -1):
        animated_text(f"{i}... 🎈", delay=0.5)
    animated_text("✨🎊 HAPPY BIRTHDAY!!! 🎊✨")

    animated_text(f"\n{name}, here’s to more laughter, love, and memories ahead. Have the BEST day ever! 🎂🎉🎁\n")
    print("-" * 40)

# Main script to find birthdays and trigger celebration
def check_birthdays():
    today = datetime.datetime.now()
    today_day = today.day
    today_month = today.month
    current_year = today.year
    birthday_found = False

    today_formatted = f"{today_day:02d}.{today_month:02d}"

    with open("names.txt", 'r') as file:
        for line in file:
            parts = line.split(',')
            
            if len(parts) == 4:
                name = parts[0].strip()
                birthdate_str = parts[-1].strip()
                
                try:
                    birthdate_parts = birthdate_str.split(".")
                    birthdate_day = int(birthdate_parts[0])
                    birthdate_month = int(birthdate_parts[1])
                    birthdate_year = int(birthdate_parts[2])
                    birthdate_formatted = f"{birthdate_day:02d}.{birthdate_month:02d}"

                    if birthdate_formatted == today_formatted:
                        # Calculate age
                        age = current_year - birthdate_year
                        if today_month < birthdate_month or (today_month == birthdate_month and today_day < birthdate_day):
                            age -= 1  # Adjust for birthdays later in the year

                        print(f"Today is {name}'s Birthday!")
                        print(f'Happy birthday {name}')
                        birthday_found = True

                        # Trigger the celebration script
                        birthday_celebration(name, age)
                except ValueError:
                    continue

    # If no birthdays were found, print a message
    if not birthday_found:
        print("No birthdays today.")

# Check birthdays once every day at a specific time (e.g., 09:15)
def run_daily_check():
    while True:
        now = datetime.datetime.now()

        # Run the check only if it's 09:15 AM today
        if now.hour == 9 and now.minute == 15:
            check_birthdays()
            break  # Stop the script after the check is completed

        # Wait for 60 seconds before checking again
        time.sleep(60)

# Run the birthday check every day at 09:15
run_daily_check()
