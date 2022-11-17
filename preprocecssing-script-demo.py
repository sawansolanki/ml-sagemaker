import os

s= "this is captain speaking!"
# with open ('/__w/ml-sagemaker/ml-sagemaker/details.txt','r') as file:
cwd = os.getcwd()

with open ('details.txt','w') as file:
    output = file.write(s)
    
print(output)
