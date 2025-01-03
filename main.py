import time

def countdown_timer(seconds):
    # Print the countdown starting message
    print(f"Starting countdown from {seconds}...")
    
    # loop through the seconds, counting down
    while seconds > 0:
        print(f"{seconds} seconds remaining...")
        time.sleep(1)
        seconds -= 1
        
    # When the countdown is over, print a message
    print("0 seconds remaining...")
    time.sleep(.9)
    print("Time is up")
    
# ASk the user how many seconds for the coutntdown
user_input = input("Enter the number of seconds for the countdown: ")

# Convert the input to an integer
try:
    countdown_seconds = int(user_input)
    countdown_timer(countdown_seconds)
    
except ValueError:
    print("Please enter a valid number.")
    
    
    
