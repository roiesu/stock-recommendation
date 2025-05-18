from multiprocessing import Process
import uvicorn
from src.scheduler.scheduler import loop

def start_api():
    print("Starting API server...")
    uvicorn.run("src.api.api:app", host="127.0.0.1", port=8000, reload=False)


def start_scheduler():
    loop()

if __name__ == "__main__":
    p1 = Process(target=start_api)
    p2 = Process(target=start_scheduler)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
