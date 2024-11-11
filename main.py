from tasks import Task
def main():
    task = Task("Task 1", "Description 1", "High")
    task.input()
    tasks = []
    tasks.append(task)
    for task in tasks:
        print(task)
if __name__ == "__main__":
    main()