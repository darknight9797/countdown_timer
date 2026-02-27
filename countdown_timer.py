import time

total_seconds = int(input("Enter time in seconds: "))

while total_seconds > 0:
    mins = total_seconds // 60
    secs = total_seconds % 60
    print(f"{mins:02d}:{secs:02d}")
    time.sleep(1)   #wait one second
    total_seconds -= 1
    
print("Time's up!")