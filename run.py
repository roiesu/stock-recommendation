from multiprocessing import Process
import uvicorn
import sys
import traceback
from src.scheduler.scheduler import loop

def start_api():
    try:
        print("Starting API server")
        uvicorn.run("src.api.api:app", host="127.0.0.1", port=8000, reload=False)
    except Exception as e:
        print("API server crashed:")
        traceback.print_exc()
        sys.exit(1)

def start_scheduler():
    try:
        print("Starting scheduler loop...")
        loop()
    except Exception as e:
        print("Scheduler crashed:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    p1 = Process(target=start_api)
    p2 = Process(target=start_scheduler)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
