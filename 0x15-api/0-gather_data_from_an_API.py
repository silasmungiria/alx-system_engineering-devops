import requests
import sys

def get_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    return user_data, todo_data

def display_progress(employee_name, done_tasks, total_tasks, completed_task_titles):
    print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
    for title in completed_task_titles:
        print(f"    {title}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_data, todo_data = get_employee_data(employee_id)

    employee_name = user_data["name"]
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task["completed"]]
    completed_task_titles = [task["title"] for task in completed_tasks]

    display_progress(employee_name, len(completed_tasks), total_tasks, completed_task_titles)
