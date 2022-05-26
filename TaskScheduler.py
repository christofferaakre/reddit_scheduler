from dataclasses import dataclass
from typing import Callable, List, Tuple
import time
import threading

@dataclass
class Task:
    timestamp: int
    function: Callable
    args: Tuple

class TaskScheduler:
    def __init__(self, polling_interval: int):
        self.running = False
        self.tasks: List[Task] = []
        self.polling_interval = polling_interval

    def add_task(self, task: Task):
        self.tasks.append(task)

    def complete_task(self, task: Task):
        task.function(*task.args)
        print(f"Completed task with timestamp {task.timestamp}")

    def complete_tasks(self):
        now = time.time()
        n_completed = 0
        for i, task in enumerate(self.tasks):
            if now >= task.timestamp:
                self.complete_task(task)
                del self.tasks[i]
                n_completed += 1

        print(f"completed {n_completed} out of {len(self.tasks)} tasks")

    def loop(self):
        while True:
            time.sleep(self.polling_interval)
            self.complete_tasks()

    def run(self):
        self.running = True
        thread = threading.Thread(target=self.loop)
        print(f"Starting TaskScheduler thread..")
        thread.start()
