.PHONY: all build run

QUALITY ?= l

all: run

run: build
	manim-slides Presentation

build: main.py
	manim $< Presentation -q$(QUALITY)