# Overview
This repo contain the code for the Splittab model endpoint for inference. This is to be deploy
to Runpod Serverless.

## Get Started
1. Create a `.env`file with the following variables:

    ```bash 
    LOCAL_MODEL_DIR: The path to the model directory. (e.g. /home/.../splittab-runpod/model/)
    ```
2. Follow the instructions provided by [RunPod Blog](https://docs.runpod.io/serverless/workers/get-started) for deploying the model endpoint.

## Local Development
You can launch a local test server that will provide an endpoint to send request
to by running the following command:
```bash
make test-server
```

## Secrets
1. AWS ECR Credentials username is `AWS` and password is retrieved by running
    ```bash
    aws ecr get-login-password --region us-west-2 
    ```

## Deployment
After merging changes to main, run the following command to deploy the model endpoint:
```bash
make ecr-login # Retrieve temporary password for ECR and inject it into docker
make push # push image to ECR
```