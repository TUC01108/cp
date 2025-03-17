def bad_find_task_pair(task_times, available_time):
    task1 = 0
    for task in task_times:
        task1 = task
        for t in task_times:
            if t != task and t + task == available_time:
                return True
    return False

def find_task_pair(task_times, available_time):
    seen_tasks = set()
    for task in task_times:
        complement = available_time - task
        if complement in seen_tasks:
            return True
        seen_tasks.add(task)
    return False

# Example Usage:

task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))

# Example Output:

# True
# True
# False
