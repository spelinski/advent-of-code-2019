CURDIR = $(shell pwd)
DOCKER=sudo docker run -it -v $(CURDIR):/root/advent:rw advent-cpp
CHALLENGE?=1
CPPFILES = ./challenges/challenge$(CHALLENGE)/main.cpp
run: static-analysis
		./test

static-analysis: build
		$(DOCKER) cppcheck --std=c++11 $(CPPFILES) --enable=all -q -Icommon --error-exitcode=1 && \
		$(DOCKER) clang-tidy $(CPPFILES) --checks="*" --warnings-as-errors="*" -- -Icommon -std=c++1z

build:
		$(DOCKER) g++-7 -g $(CPPFILES) -Icommon -std=c++17 -o test -Werror -Wall -Wextra -pedantic

docker:
		sudo docker build -t advent-cpp .

shell:
		$(DOCKER) /bin/bash