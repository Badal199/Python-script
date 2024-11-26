import time
import random
from itertools import cycle
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Predefined pattern for results
result_pattern = [
    "BIG", "BIG", "BIG", "SMALL", "SMALL", "BIG", "SMALL", "SMALL", "BIG", "SMALL",
    "BIG", "SMALL", "SMALL", "BIG", "SMALL", "BIG", "SMALL", "SMALL", "BIG", "SMALL",
    "SMALL", "SMALL", "BIG", "BIG", "SMALL", "SMALL", "SMALL", "BIG", "SMALL", "SMALL",
    "BIG", "SMALL", "SMALL", "SMALL", "BIG", "BIG", "SMALL", "SMALL", "SMALL", "BIG"
]

# Cyclic iterator for results
results_iterator = cycle(result_pattern)

# ASCII Art Headers
def hacker_header():
    print(Style.BRIGHT + Fore.GREEN + "=" * 60)
    print(Fore.LIGHTCYAN_EX + "        🚀 BN LAST KING HACKER SYSTEM 🚀")
    print(Fore.GREEN + "       [ ONLINE PREDICTING TOOL - V1.0 ]")
    print(Fore.YELLOW + "       POWERED BY: HACK SUPPORT SYSTEM")
    print(Style.BRIGHT + Fore.GREEN + "=" * 60)

# Function to simulate fetching the period number from Java code
def get_period_number_from_java():
    current_time = time.time()
    total_seconds = int(current_time)
    remaining_seconds = 30 - (total_seconds % 30)
    total_minutes = total_seconds // 60
    period_number = total_minutes * 2 + (1 if (total_seconds % 60) >= 30 else 0)
    return period_number, remaining_seconds

# Loading animation
def loading_animation():
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "[LOADING RESULT...]", end="")
    for _ in range(10):
        print(Fore.GREEN + ".", end="", flush=True)
        time.sleep(0.2)
    print("\n" + Fore.LIGHTCYAN_EX + "[RESULT LOADED SUCCESSFULLY]")

# Display results with hacker-style design
def display_results():
    hacker_header()
    last_period_number = None

    while True:
        # Get current period number and remaining seconds
        period_number, remaining_seconds = get_period_number_from_java()

        # Check if the period number has changed
        if period_number != last_period_number:
            # Loading animation
            loading_animation()

            # Fetch the next result from the pattern
            next_result = next(results_iterator)

            # Display the result in hacker style
            print(Fore.GREEN + Style.BRIGHT + f"🌐 Online System: [ACTIVE]")
            print(Fore.LIGHTMAGENTA_EX + f"🛠️ Server Status: [RUNNING]")
            print(Fore.YELLOW + f"Period Number: {Fore.LIGHTCYAN_EX}{period_number}")
            if next_result == "BIG":
                print(Fore.LIGHTGREEN_EX + f"💻 HACKED RESULT: {next_result} ♥️")
            else:
                print(Fore.LIGHTRED_EX + f"💻 HACKED RESULT: {next_result} 💚")
            print(Fore.LIGHTCYAN_EX + "🔐 Hack Tool Status: [ENCRYPTED]")
            print(Fore.MAGENTA + "-" * 60)
            last_period_number = period_number

        # Display the countdown timer
        print(
            Fore.CYAN + Style.BRIGHT +
            f"⌛ Remaining Time: {Fore.YELLOW}{remaining_seconds} seconds",
            end="\r"
        )
        time.sleep(1)

# Main function
if __name__ == "__main__":
    display_results()