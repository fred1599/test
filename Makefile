# Makefile
.PHONY: build run-tests run-app run-debug

build:
	docker build -t my-app .

run-tests:
	docker run -it --rm my-app pytest test.py

run-app:
	docker run -it --rm -v $(PWD)/data.log:/app/data.log my-app python main.py data.log

run-debug:
	docker run -it --rm -p 5679:5678 -v $(PWD)/data.log:/app/data.log my-app python -Xfrozen_modules=off -m debugpy --listen 0.0.0.0:5678 --wait-for-client main.py data.log
