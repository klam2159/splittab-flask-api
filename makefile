# IMAGE_NAME := splittab-model-runpod
IMAGE_NAME := adamcodd-donut-extract
TAG := 2.0.0-runpod-0.6.2
REGISTRY := klam34 #DockerHub

build:
	docker build -t $(IMAGE_NAME):$(TAG) .

run:
	docker run -it --rm $(IMAGE_NAME):$(TAG)

push:
	export DOCKER_CLIENT_TIMEOUT=1200
	export COMPOSE_HTTP_TIMEOUT=1200
	docker tag $(IMAGE_NAME):$(TAG) $(REGISTRY)/$(IMAGE_NAME):$(TAG)
	docker push $(REGISTRY)/$(IMAGE_NAME):$(TAG)

ecr-login:
	aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin $(REGISTRY)
	
.PHONY: build push run