#!/bin/bash

nbqa isort pde-book/**/*.ipynb --float-to-top
nbqa black pde-book/**/*.ipynb
nbqa pyupgrade pde-book/**/*.ipynb --py311-plus

isort pde-book/**/*.py --float-to-top
black pde-book/**/*.py
pyupgrade pde-book/**/*.py --py311-plus
