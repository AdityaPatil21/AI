def get_profit(job):
    return job[2]

def get_deadline(job):
    return job[1]

def job_sequencing(jobs):
    # Sort the jobs in descending order according to their profit
    jobs.sort(key=get_profit, reverse=True)
    
    # Find the maximum deadline among the jobs
    max_deadline = max(jobs, key=get_deadline)[1]
    
    # Create a list to store the job sequence
    sequence = [None] * max_deadline
    
    # keep track of the number of jobs assigned
    job_count = 0
    
    # Iterate over the jobs and assign them to appropriate slots
    for job in jobs:
        deadline = job[1] - 1  # Convert deadline to zero-based index
        while deadline >= 0: #terates from the current deadline value towards earlier slots until it reaches index 0.
            if sequence[deadline] is None:  # Check if slot at current deadline is empty
                sequence[deadline] = job[0]  # Assign the job to slot job[0] represents the job ID
                job_count += 1 #indicating that another job has been successfully assigned.
                break
            deadline -= 1 #If the slot is already filled, the algorithm tries the previous slot by decrementing the deadline.
    
    # Remove the empty slots from the sequence
    new_sequence = [] #creates an empty list called new_sequence, which will be used to store the non-empty slots (i.e., slots with assigned jobs).
    for job in sequence:
        if job is not None:
            new_sequence.append(job)
    sequence = new_sequence
    #he code removes the None elements from the sequence list and creates a new list (new_sequence) containing only the non-empty job values. Finally, the sequence list is updated to the new_sequence list, resulting in a list without any empty slots.
    
    return (sequence, job_count)


jobs = [(1, 3, 35), (2, 4, 30), (3, 4, 25), (4, 2, 20), (5, 3, 15), (6, 1, 12), (7, 2, 5)]
result = job_sequencing(jobs)
print("Job Sequence: ", result[0]) # sequence contains the updated list without empty slots
print("Job Count: ", result[1])  # job_count contains the total number of assigned jobs
