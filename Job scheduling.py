def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(jobs, key=lambda x: x[1])[1]
    time_slots = [-1] * (max_deadline + 1)

    for job in jobs:
        profit = job[2]
        deadline = job[1]

        # Find the maximum available time slot before the deadline
        for i in range(deadline, 0, -1):
            if i <= max_deadline and time_slots[i] == -1:
                time_slots[i] = job[0]  # Schedule the job
                break

    scheduled_jobs = [time_slots[i] for i in range(1, max_deadline + 1) if time_slots[i] != -1]
    total_profit = sum([jobs[job_id - 1][2] for job_id in scheduled_jobs])

    return scheduled_jobs, total_profit


def print_schedule(jobs, total_profit):
    print("Scheduled Jobs:", jobs)
    print("Total Profit:", total_profit)

def main():
    jobs = []
    while True:
        print("\nJob Scheduling Problem Menu:")
        print("1. Add Job")
        print("2. Schedule Jobs")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            job_id = int(input("Enter Job ID: "))
            deadline = int(input("Enter Deadline: "))
            profit = int(input("Enter Profit: "))
            jobs.append((job_id, deadline, profit))
        elif choice == "2":
            if jobs:
                scheduled_jobs, total_profit = job_scheduling(jobs)
                print_schedule(scheduled_jobs, total_profit)
            else:
                print("No jobs added yet. Please add jobs first.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()




The provided Python code addresses the Job Scheduling problem, where the goal is to maximize the total profit by scheduling jobs with given deadlines and profits. The code includes functions for adding jobs, scheduling jobs to maximize profit, and a menu-driven interface for user interaction. Let's break down the code and explain the concepts in detail:

1. **`job_scheduling` Function**:
   - This function takes a list of jobs as input, where each job is represented by a tuple containing the job ID, deadline, and profit.

   - It first sorts the jobs in decreasing order of their profits, ensuring that jobs with higher profits are scheduled first.

   - It determines the maximum deadline among the jobs to create a list `time_slots` of that length, initialized with `-1` values. This list will represent time slots for scheduling jobs.

   - For each job, it iterates through the `time_slots` list from the job's deadline towards 1. It looks for the first available time slot before the job's deadline and schedules the job in that slot. If no available time slot is found before the deadline, the job is not scheduled.

   - The function then creates a list of scheduled jobs and calculates the total profit by summing the profits of the scheduled jobs.

   - Finally, it returns the list of scheduled jobs and the total profit.

2. **`print_schedule` Function**:
   - This function takes a list of scheduled job IDs and the total profit as input and prints the list of scheduled jobs and the total profit.

3. **`main` Function**:
   - The main part of the code initializes an empty list `jobs` to store the job information.

   - It presents a menu to the user for interaction. The user can add jobs, schedule jobs to maximize profit, or exit the program.

   - When the user chooses to add a job, they are prompted to enter the job ID, deadline, and profit, and the job is appended to the `jobs` list.

   - When the user chooses to schedule jobs, the `job_scheduling` function is called to find the optimal schedule and maximize profit. The scheduled jobs and total profit are then printed.

   - The program continues to loop until the user chooses to exit.

In summary, this code provides an interactive way to solve the Job Scheduling problem, where users can add jobs with deadlines and profits, find an optimal schedule to maximize profit, and visualize the results using a user-friendly menu-driven interface. It's a practical implementation of a scheduling algorithm for job optimization.
