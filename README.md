# Overview
This repo contain the code for the Splittab model endpoint for inference.

# Get Started
1. Create a `.env`file with the following variables:

```bash 
LOCAL_MODEL_DIR: The path to the model directory. (e.g. /home/.../splittab-runpod/model/)
```
2. Follow the instructions provided by [RunPod Blog](https://docs.runpod.io/serverless/workers/get-started) for deploying the model endpoint.


# Secrets
1. AWS ECR Credentials username is `AWS` and password is retrieved by running
    ```bash
    aws ecr get-login-password --region us-west-2 
    ```
