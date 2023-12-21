.DEFAULT_GOAL := help
IMG_NAME=talana/test
CONTAINER_NAME=talana-test
REQUIREMENTS=requirements.txt

.PHONY : help
help : 
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

build : ## Build the image.
	@docker build --no-cache --rm -t $(IMG_NAME) .

run : ## Run the container (after building the image).
	@docker run --name $(CONTAINER_NAME) -v $(PWD):/talana -d $(IMG_NAME)

bash : ## Interactive access to the container.
	@docker exec -it $(CONTAINER_NAME) bash

stop : ## Stop the container.
	@docker stop $(CONTAINER_NAME)

start : ## Start or resume the contairner after it has been stopped.
	@docker start $(CONTAINER_NAME)

remove-container : ## Remove ONLY the container.
	@docker rm $(CONTAINER_NAME)

remove-image : ## Remove ONLY the image.
	@docker rm $(IMG_NAME)

purge : ## Purge the container and the image.
	@docker rm $(CONTAINER_NAME)
	@docker rmi $(IMG_NAME)

requirements : ## Install depedencies listed in the requirements file.
	@docker exec $(CONTAINER_NAME) pip install --root-user-action=ignore -r $(REQUIREMENTS)
