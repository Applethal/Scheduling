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

######
Makespan = 0
for i in range(Number_of_jobs):

    Schedule.append(Job_dict[i].get("Job"))
    Makespan += Job_dict[i].get("Duration")

print("The given schedule is", Schedule, "with a makespan of", Makespan)
