from datetime import datetime
from math import remainder


def countdown():
    print("========countdown timer==========")
    goal = input("Enter your Goal: ")
    deadline_input= input("Input your deadline date and time  (YYYY-MM-DD HH:MM:SSS): ")
    
    try:
        deadline = datetime.strptime(deadline_input, "%Y-%m-%d %H:%M:%S")
        now = datetime.now()
        if deadline < now: 
            print("The deadline has already passed.")
            return
        time_left = deadline - now
    
        days =time_left.days
        hours, remainder =  divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"\nGoal: {goal}")
        print(f"Deadline: {deadline}")
        print(f"Time left: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS")
if __name__ == "__main__":
    countdown()
