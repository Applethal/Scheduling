# Scheduling
I am here to perform some sorceries!
Nothing crazy, I will just (try to) create some python coding to allow the creation of a schedule, it will contain some functions for the sake of fun!

## 23/01/2023
Updated the code to force the durations to be exclusively integer. At the end, the schedule will show the permutation of jobs and its makespan.
[I was listening to Free Salute · Little Barrie while making this small update](https://www.youtube.com/watch?v=kH6sJtRljW4).

## 24/01/2023

Updated the code to include information in regards to the weighted makespan of the schedule. 
This project was meant to reflect a **human environement**. In scheduling theory, the methods and art we learned was adapted for a machine based environement, as one of the basics of the theory stated that **machine can process a given job with full capacity after finishing its prior task, and that there are no ressources to be consumed.** 

The weighted makespan represents a score that a human achieves after performing all the tasks. The weight in this context represents the stamina and that defaults to 1 for all the jobs(for now); everytime a job is added, the weight of the next job will be reduced by 0,1.

What I plan to do soon is to make it so that adding a task named "Pause/pause" will restore the weight's value to 1, and add a function that allows a schedule netting the best performance.
[While writing this update, I was listening to Analyzing Evil: Warden Samuel Norton From The Shawshank Redemption, an analysis of an antagonist that comes from one of my favourite movies](https://www.youtube.com/watch?v=07sIviggH8M)


## 25/01/2023

Updated the code. Adding a job named "Pause" or "pause" will cause the weight/Stamina to revert back to 1. I have no music to share for now, how about I share a small picture that I love ? 

![Cat with a hat](https://pbs.twimg.com/media/FLt0yAhXIAEhiH4?format=jpg)
