DOCKER_IMAGE_TAG = "kinemetics-solver"

all: build run

build:
	docker build -t $(DOCKER_IMAGE_TAG) .

run:
	docker run --rm -t --link rover-core:rover-core $(DOCKER_IMAGE_TAG)
