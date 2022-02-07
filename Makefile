package_name = passgen
repository = toolen/passgen
version = $(shell poetry version -s)
tag = ghcr.io/$(repository):$(version)
hadolint_version=2.8.0
trivy_version=0.23.0

image:
	export DOCKER_BUILDKIT=1
	make hadolint
	docker build --pull --no-cache -t $(tag) .
	make trivy
	make size
container:
	docker run -p 127.0.0.1:8080:8080 --cap-drop=ALL $(tag)
hadolint:
	docker run --rm -i hadolint/hadolint:$(hadolint_version) < Dockerfile
trivy:
	docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v ~/.cache/trivy:/root/.cache/ aquasec/trivy:$(trivy_version) image --ignore-unfixed $(tag)
size:
	docker images | grep $(repository) | grep $(version)
digest:
	docker images --digests | grep python
push:
	docker trust sign $(tag)
test:
	poetry run pytest --cov=$(package_name) tests/
fmt:
	poetry run black .
	poetry run isort .
fmt-check:
	poetry run black . --check
	poetry run isort . --check
pre-commit:
	make fmt
	make lint
ci:
	make fmt-check
	make lint
lint:
	poetry run flake8 --ignore E501 $(package_name)/ tests/
	poetry run pydocstyle --add-ignore=D104 $(package_name)/
	poetry run bandit -r $(package_name)/
	poetry run safety check
	poetry run mypy --strict --ignore-missing-imports $(package_name)
	make test
	make radon
tag:
	git tag v$(version)
	git push origin v$(version)
push-to-ghcr:
	docker login ghcr.io -u toolen -p $(CR_PAT)
	docker push $(tag)
radon:
	poetry run radon cc --min C --show-complexity $(package_name)
	poetry run radon mi --min B $(package_name)
	poetry run radon raw --summary $(package_name) | tail -n12
.PHONY: docs
docs:
	make -C docs html
	python -m http.server 8000 --bind 127.0.0.1 --directory docs/build/html