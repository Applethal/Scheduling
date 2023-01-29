##### Nested dict for jobs and their durations

Number_of_jobs = int(input("Please input the number of jobs that you wish to include within the schedule."))
Job_dict = {}
Schedule = []
for i in range(Number_of_jobs):
    job_dict = {}
    job = input("Name the job")
    Job_duration = int(input("For how long does the job occure ?"))
    job_dict["Job"] = job
    job_dict["Duration"] = Job_duration
    Job_dict[i] = job_dict

#### due date

due_date = int(input("Please enter the deadline subject to the activities that you wish to acomplish"))

Jobs_sorted = sorted(Job_dict.items(), key=lambda i: i[1]["Duration"], reverse=True)
Jobs_sorted = dict(Jobs_sorted)
Schedule_max_performance = []


def max_performance(Jobs_sorted):
    weight = 1
    max_performance_weighted = 0
    Jobs_sorted_by_ratio = dict(Job_dict.items(), key=lambda i: weight / (i[1]["Duration"]))
    list_jobs = list(Jobs_sorted_by_ratio.keys())
    while Jobs_sorted_by_ratio[list_jobs[-1]].get("Duration") > due_date:
        list_jobs.pop(-1)
        Jobs_sorted_by_ratio.pop(list_jobs[-1])
    max_performance_makespan = 0
    for i in Jobs_sorted_by_ratio:
        max_performance_weighted += weight * Jobs_sorted[i].get("Duration")
        weight -= 0.1
    while max_performance_makespan <= due_date:
        Schedule_max_performance.append(Jobs_sorted_by_ratio[i].get["Jobs"])
        max_performance_makespan += Jobs_sorted_by_ratio[i].get("Duration")
    return max_performance_weighted, Schedule_max_performance, max_performance_makespan


###### Makespan
Makespan = 0
for i in range(Number_of_jobs):

    Schedule.append(Job_dict[i].get("Job"))
    Makespan += Job_dict[i].get("Duration")

##### Weight defaults to 1 unless I update the code to let custome values to be added by the user

Weighted_Makespan = 0
Weight = 1
for i in range(Number_of_jobs):

    Weighted_Makespan += Weight * Job_dict[i].get("Duration")
    if ("Pause" in Job_dict[i]["Job"]) or ("pause" in Job_dict[i]["Job"]):
        Weight = 1
    else:
        Weight -= 0.1

print("The given schedule is", Schedule, "with a makespan of", Makespan)
print("The weighted completion time of the schedule is ", Weighted_Makespan)

max_performance_weighted, Schedule_max_performance, max_performance_makespan = max_performance(Jobs_sorted)

print(
    "If you wish to achieve the maximum performance, this would be your schedule", Schedule_max_performance,
    "with a makespan of ", max_performance_makespan, "and a performance score of ", max_performance_weighted
