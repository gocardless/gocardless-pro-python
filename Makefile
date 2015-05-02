docker-test:
	docker run --rm -ti -v `pwd`:/opt/pypkg hmarr/python-test-tox
