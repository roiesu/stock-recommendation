import time
from src.core.data_collection import run

INTERVAL_SECONDS = 300

def loop():
    print("Starting scheduler loop...")
    while True:
        try:
            run()
        except Exception as e:
            print(f"Error during scheduler loop: {e}")
        time.sleep(INTERVAL_SECONDS)

# Exists for dubgging, runs dierctly
if __name__ == "__main__":
    loop()
