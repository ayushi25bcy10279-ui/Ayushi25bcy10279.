# Road Traffic Management System

## Overview

This project implements a simple **Road Traffic Management System**
using graph traversal algorithms. It finds optimal routes between two
points on a road map using **BFS**, **DFS**, and **A\*** search
techniques.\
The program demonstrates how different search algorithms behave in
finding paths.

## Features

-   Breadth-First Search (BFS) for shortest path in terms of number of
    steps.
-   Depth-First Search (DFS) for exploring deeper routes.
-   A\* Search for shortest distance using heuristic estimation.
-   Road map implemented as an adjacency dictionary.
-   Clear output for all algorithms.

## Technologies / Tools Used

-   **Python 3**
-   **heapq** (for A\* priority queue)
-   **Basic data structures** such as lists, sets, and dictionaries

## Steps to Install & Run

1.  Ensure Python 3 is installed on your system.

2.  Download the project files.

3.  Open a terminal and navigate to the project folder.

4.  Run the script using:

        python traffic_management.py

## Instructions for Testing

-   Modify the `rm` dictionary to add or remove nodes/roads.
-   Change `start` and `end` points to test different routes.
-   Compare BFS, DFS, and A\* output to observe their behaviors.
-   Validate that the A\* algorithm always returns the lowest cost route
    based on distance.
