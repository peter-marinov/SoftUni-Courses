
cpu_jobs = list(map(int, input().split(', ')))
needed_index = int(input())


needed_value = cpu_jobs[needed_index]

jobs_to_be_done = [job for job in cpu_jobs if job <= needed_value]
# jobs_to_be_done.append(needed_value)
print(sum(jobs_to_be_done))