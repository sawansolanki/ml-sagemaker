    
from sagemaker.sklearn.estimator import SKLearn
import sagemaker
from sagemaker import get_execution_role
import json

#role = get_execution_role()
role = 'arn:aws:iam::256537223841:role/mlops-role-sa1'

#output has been taken from "#running the processing job", this where it is defined
# output = {'OutputName': 'test_data',
#  'S3Output': {'S3Uri': 's3://sagemaker-us-east-1-256537223841/sagemaker-scikit-learn-2022-11-16-12-08-12-357/output/train_data',
#   'LocalPath': '/opt/ml/processing/train',
#   'S3UploadMode': 'EndOfJob'},
#  'AppManaged': False}

with open ('/__w/ml-sagemaker/ml-sagemaker/details.txt','r') as file:
    output = file.read()
    output = output.replace("'" , "\"")
    output=json.loads(output)

preprocessed_training_data = output["S3Output"]["S3Uri"]
preprocessed_test_data = output["S3Output"]["S3Uri"]


def run_training():    

    sklearn = SKLearn(
        entry_point="train.py", framework_version="0.20.0", instance_type="ml.c4.2xlarge", role=role
    )

    sklearn.fit({"train": preprocessed_training_data})
    training_job_description = sklearn.jobs[-1].describe()
    model_data_s3_uri = "{}{}/{}".format(
        training_job_description["OutputDataConfig"]["S3OutputPath"],
        training_job_description["TrainingJobName"],
        "output/model.tar.gz",
    )


if __name__ == "__main__":
    run_training()
