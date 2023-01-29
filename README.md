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

Updated the code. Adding a job named "Pause" or "pause" will cause the weight/Stamina to revert back to 1. I have no music to share for now, consider this picture instead.

<img src="https://pbs.twimg.com/media/FLt0yAhXIAEhiH4?format=jpg" alt="Cat with a hat" width="200"/>

What's next ? I will create an optimization problem out of this idea. 

## 27/01/2023 

Updated the code. A list of jobs sorted by duration in a descending manner will be printed, this will be needed much later for the optimization idea that I plan to implement, hopefully I will be able to finish it today.[On my music playlist, Jane's addiction came up while I was learning](https://www.youtube.com/watch?v=KV3ozZoQ13M)


## 30/01/2023

Reached my first road block. Spent 2 days looking for solutions for this matter. It appears that the problem belongs to the "Online Scheduling" Categorie, which is famous for having Np-hard problems. My problem goes as follows: subject to a due date, fill your schedule in a way that maximizes the score (score is defined by the weight times the duration). Sure, looks like a knapsack problem, well guess what: let us not forget that each time you add a task/job, the weight for the next job decreases by 0.1; Taking a pause recovers the weight of the next job to its default value.

I have tried to model this problem mathematically:

$$Max \space Z: = \sum\limits_{d \in D} d_j.w_j.X_j + d_p.w_j.X_p$$

Subject to: 

$$ X_j <= 1 (\forall j \in J) $$

$$ X_p <=1 (\forall p \in J) $$

$$ w_{j+1} = X_p + (X_{j-1} . (w_{j-1} - 0,1 )) (\forall J+1 \in J) $$  


$$ X_p, X_j \in \{0,1\} and w >= 0$$

