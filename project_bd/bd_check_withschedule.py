import datetime

# Function for the birthday celebration with a personalized message
def birthday_celebration(name, age):
    """Generates a personalized and age-appropriate birthday blessing for the given name and age."""
    if age < 18:
        blessing = [
            f"🎉🎂 Happy Birthday, {name}! 🎂🎉",
            "May you always stay curious, full of energy, and chase your dreams with joy! 🍭🍬",
            "The world is full of endless possibilities, so go out there and make your mark! 🌟",
            "Stay young at heart and keep having fun—today is YOUR day! 🎈🎉"
        ]
    elif 18 <= age < 30:
        blessing = [
            f"🎉🎉 Happy Birthday, {name}! 🎉🎉",
            "Welcome to the prime years of adventure and growth! 🌟",
            "May this year bring you new opportunities, excitement, and the courage to chase your dreams! 💼",
            "Remember, life’s a journey—enjoy the ride and embrace every new chapter! ✨🎂"
        ]
    elif 30 <= age < 50:
        blessing = [
            f"🎉🎉 Happy Birthday, {name}! 🎉🎉",
            "These are the years of wisdom, success, and accomplishment! 🏆",
            "May your path continue to be full of love, laughter, and lasting achievements! 💼",
            "Here’s to another year of incredible milestones, both personal and professional. Cheers to you! 🥂"
        ]
    else:
        blessing = [
            f"🎉🎉 Happy Birthday, {name}! 🎉🎉",
            "Here’s to a life filled with unforgettable memories and timeless wisdom! 🌟",
            "May you continue to age like fine wine—more refined, stronger, and wiser every year! 🍷",
            "Enjoy the incredible richness of life, love, and joy with every passing year! 💖"
        ]
    
    return blessing

# Function to check for birthdays and return the birthday message
def check_birthdays():
    """Checks for today's birthdays and returns a list of celebratory messages."""
    today = datetime.datetime.now()
    today_day = today.day
    today_month = today.month
    current_year = today.year

    today_formatted = f"{today_day:02d}.{today_month:02d}"
    birthdays_today = []

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
                            age -= 1  # Adjust for late birthdays

                        # Get the personalized blessing
                        message = birthday_celebration(name, age)

                        # Append the birthday info as a dictionary
                        birthdays_today.append({
                            "name": name,
                            "age": age,
                            "messages": message
                        })

                except ValueError:
                    continue

    return birthdays_today
