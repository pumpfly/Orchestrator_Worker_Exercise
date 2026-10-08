import requests
import time
import random

if __name__ == "__main__":
    while True:
        task: str = requests.get("http://127.0.0.1:7999/task").text
        if task == "finished":
            break
        id = task.split(".) ")[0]
        print(f"got {task}")
        time.sleep(2)
        answer = random.randint(0, 1000)

        handover = requests.get(f"http://127.0.0.1:7999/handover?answer={answer}&id={id}")
        print(f"gave answer {answer} for {id}")

    print("finished -> quitting")
