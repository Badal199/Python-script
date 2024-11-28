import time
from datetime import datetime

# Result pattern
RESULT_PATTERN = ["SMALL", "BIG", "SMALL", "BIG", "SMALL", "SMALL", "BIG", "SMALL", "BIG", "BIG", "SMALL", "BIG", "SMALL", "SMALL"]

# Function to simulate an advanced server loading animation
def loading_server():
    print("\033[1;34m" + "CONNECTING TO BN LAST KING HACKER SERVER..." + "\033[0m")
    for i in range(1, 101, 20):
        time.sleep(0.5)
        print(f"\033[1;36mLOADING... {i}%\033[0m")
    time.sleep(0.5)
    print("\033[1;32mSERVER CONNECTED SUCCESSFULLY.\033[0m")
    time.sleep(0.5)
    print("\033[1;35mACCESSING RESULTS...\033[0m")
    time.sleep(1)

# Function to display the redesigned table box
def display_result_table(period, result):
    print("\033[1;33m" + "+" + "-" * 38 + "+\033[0m")  # Yellow table top border
    print(f"\033[1;33m| Period Number:\033[0m \033[1;32m{period:<24}\033[1;33m|\033[0m")  # Green text for period
    print("\033[1;33m+" + "-" * 38 + "+\033[0m")  # Yellow middle border
    print(f"\033[1;33m| Result:        \033[0m \033[1;32m{result:<24}\033[1;33m|\033[0m")  # Green text for result
    print("\033[1;33m+" + "-" * 38 + "+\033[0m")  # Yellow table bottom border

# Function to generate period number based on UTC
def generate_period():
    now = datetime.utcnow()
    total_minutes = now.hour * 60 + now.minute
    period_number = int(now.strftime("%Y%m%d")) * 100000 + 10001 + total_minutes
    return period_number

# Main function to run the script
def main():
    print("\033[1;31m" + "=" * 50 + "\033[0m")  # Red header
    print("\033[1;31m BN LAST KING PREDICTION SYSTEM - HACKER STYLE\033[0m")
    print("\033[1;31m" + "=" * 50 + "\033[0m\n")  # Red footer
    
    current_period = generate_period()
    index = 0

    while True:
        loading_server()  # Show loading animation
        
        # Generate the next period and result
        new_period = generate_period()
        if new_period != current_period:  # Show result only when period changes
            result = RESULT_PATTERN[index % len(RESULT_PATTERN)]  # Cycle through the pattern
            display_result_table(new_period, result)  # Display result in a table
            index += 1
            current_period = new_period

        time.sleep(1)  # Check every second for period change

if __name__ == "__main__":
    main()