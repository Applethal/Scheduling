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
    if "Pause" or "pause" in Job_dict[i]["Job"]:
        Weight = 1
    else:
        Weight -= 0.1

print("The given schedule is", Schedule, "with a makespan of", Makespan)
print("The weighted completion time of the schedule is ", Weighted_Makespan)
