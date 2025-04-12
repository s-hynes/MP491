# What's This?

I've written some Python code that can (hopefully) help with checking answers to some of the Nonlinear Systems exam and tutorial questions. The useful functions themselves are written in Python scripts (.py), then the functions are used in Jupyter notebooks (.ipynb) to answer questions. The files all have the prefix "CHXX_" to indicate what chapter of the course they belong to.

**Links to specific parts of this README:**</br>
[Chapter 1: 1D ODEs](#chapter-1-1d-odes) </br>
[Chapter 2: 2D Linear ODEs](#chapter-2-2d-linear-odes) </br>
[Chapter 3: 2D Nonlinear ODEs](#chapter-3-2d-nonlinear-odes) </br>
[Chapter 4: Limit Cycles](#chapter-4-limit-cycles) </br>
[Chapter 5: 1D Maps](#chapter-5-1d-maps)

## Chapter 1: 1D ODEs

The main file here is `CH01_bifurcation.py`. It contains three functions, `stability`, `bifurc`, and `plotter`. `plotter` can be used to plot a bifurcation diagram for an inputted 1D ODE.

There are two Jupyter notebooks that make use of this: 

1. `CH01_bifurcation_diagrams.ipynb`, which plots bifurcation diagrams for every type of bifurcation that we come across in Chapter 1 (saddle node, transcritical, pitchfork) and also plots a few examples from the lecture notes and the Strogatz textbook _Nonlinear Dynamics and Chaos_.
2. `CH01_problem_sheet_1.ipynb`, which plots the bifurcation diagrams for the five questions on problem sheet 1.

## Chapter 2: 2D Linear ODEs

## Chapter 3: 2D Nonlinear ODEs

## Chapter 4: Limit Cycles

There is no code for this chapter at the minute.

## Chapter 5: 1D Maps

The code for Chapter 5 will make plots of $x_n$ against $n$ for 1D maps and it will determine if a map tends towards a fixed point after a certain number of iterations, for a given initial value $x_0$.

There's no code here for making cobweb plots, but there are a few different places that will do this online. This thing is fairly easy to use: https://mathinsight.org/applet/function_iteration_cobweb.
