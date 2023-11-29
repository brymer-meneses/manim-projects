.PHONY: all build run clean

QUALITY ?= l

all: run

run: build
	manim-slides Presentation

build: main.py
	manim $< Presentation -q$(QUALITY)

clean:
	rm -rf __pycache__ media slides