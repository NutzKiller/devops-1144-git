import time
import sys

def animated_text(text, delay=0.05):
    """Prints text with a typewriter animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def birthday_celebration():
    name = input("Enter your name: ").strip()
    age = int(input("Enter your age: "))
    
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

birthday_celebration()
