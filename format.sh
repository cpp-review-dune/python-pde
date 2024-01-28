#!/bin/zsh

nbqa isort pde-book/*.ipynb --float-to-top
nbqa black pde-book/*.ipynb
nbqa pyupgrade pde-book/*.ipynb --py311-plus