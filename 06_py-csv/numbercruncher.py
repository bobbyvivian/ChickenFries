file = open("occupations.csv", 'r')
content = file.read()
#splitting the file's info by line and making it a list
job_list = content.split('\n')
# getting rid of first line
total_list = job_list[1:-2]

job_dict = {}

for job in total_list:
    job_list = job.rsplit(',',1)
    job_dict[job_list[0]] = job_list[1]
    
print(job_dict)    

def weighted_random(job_dict):

