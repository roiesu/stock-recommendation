import time
from src.core.data_collection import run
from src.utilities.constants import INTERVAL_SECONDS

def loop():
    print("Starting scheduler loop")
    while True:
        try:
            run()
        except Exception as e:
            print(f"Error during scheduler loop: {e}")
        time.sleep(INTERVAL_SECONDS)

# Exists for dubgging, runs dierctly
if __name__ == "__main__":
    loop()
