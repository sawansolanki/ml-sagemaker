import os


# with open ('/__w/ml-sagemaker/ml-sagemaker/details.txt','r') as file:
cwd = os.getcwd()

with open (os.path.join(cwd , 'details.txt' )) as file:
    output = file.read()
    
print(output)
