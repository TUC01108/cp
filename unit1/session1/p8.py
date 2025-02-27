def print_todo_list(task):
    print("Pooh's To Dos:")
    if not task:
        print()
    else:
        count = 1
        for i in task:
            print(f"{count}. {i}")
            count += 1
        print()
def print_todo_list2(task):
    print("Pooh's To Dos:")
    if not task:
        print()
    else:
        for count in range(len(task)):
            print(f"{count + 1}. {task[count]}")
        print()


task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list2(task)

task = []
print_todo_list2(task)
