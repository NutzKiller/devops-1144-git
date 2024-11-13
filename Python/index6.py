import datetime
import os

# # Open the file in append mode, or create it if it doesn't exist
# with open("journal.txt", "a") as file:
#     while True:
#         # Prompt the user for a journal entry
#         entry = input("Enter a journal entry (or type 'exit' to stop): ")
        
#         # Exit the loop if the user types 'exit'
#         if entry.lower() == 'exit':
#             break
        
#         # Get the current date and time
#         current_time = datetime.datetime.now()
        
#         # Format the timestamp
#         timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
#         # Write the entry to the file with the timestamp
#         file.write(f"[{timestamp}] {entry}\n")

# print("Journal entries have been logged.")

# #2
# print("\nDisplaying all journal entries:")
# with open("journal.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# #3  3. Append More Entries:
#    - Reopen journal.txt in append mode.
#    - Prompt the user to add more journal entries.
#    - For each new entry, log it with the current date and time at the end of the file

# current_time = datetime.datetime.now()
# timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

# with open("journal.txt", "a") as file:
#   new_input = input("Add more journal entries: ")
#   file.write(f"[{timestamp}] {new_input}\n")
#   print("Your entry has been logged.")


# #4 Count Entries and Words:
#    - Open journal.txt in read mode again.
#    - Count and display the total number of entries and words in the file.
def add_journal_entry():
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
with open("journal.txt", "a") as file:
    new_input = input("Enter a journal entry (or type 'done' to finish): ")
while new_input.lower() != 'done':
    file.write(f"[{timestamp}] {new_input}\n")
    new_input = input("Enter a journal entry (or type 'done' to finish): ")
print("Your entries have been logged.")

def count_entries_and_words():
    try:
        with open("journal.txt", "r") as file:
          entries = file.readlines()
        
        total_entries = len(entries)

        total_words = len(entries)
        print("Counting entries and words:")
        print(f"Total Entries: {total_entries}")
        print(f"Total Words: {total_words}")  

    except FileNotFoundError:
        print("Error: journal.txt does not exist.")

def main():
    # Add journal entries
  add_journal_entry()

    # Ask the user if they want to add more entries
  additional = input("Would you like to add more journal entries? (yes/no): ")
  while additional.lower() == 'yes':
        # If yes, allow the user to add more entries
        with open("journal.txt", "a") as file:
            new_entry = input("Enter additional text: ")
            current_time = datetime.datetime.now()
            timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] {new_entry}\n")
        additional = input("Would you like to add more journal entries? (yes/no): ")
    
    # Count and display entries and words
  count_entries_and_words()

# Run the program
main()