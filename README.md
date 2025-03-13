# Metro Navigation System 

# Overview
This project is a Python-based Metro Navigation System designed to help users find the shortest path between two metro stations in Bangalore's metro network. It utilizes graph algorithms, specifically Dijkstra's Algorithm, to compute the most efficient travel route while also calculating the total journey cost.

# Features
-Shortest Path Calculation – Finds the most efficient route between stations using Dijkstra's Algorithm.

-Cost Estimation – Calculates the total travel cost based on the shortest distance.

-Graph Representation – Models the metro system using graph data structures.

-User-Friendly Input – Allows users to enter source and destination stations interactively.

-Error Handling – Validates user inputs to ensure station names exist in the metro network.

# Technologies Used

Python 3

Graph Data Structures

Dijkstra's Algorithm

Heap (Priority Queue) – heapq module

# Code Overview

Main Components

MetroGraph Class – Represents the metro network as a graph.

add_station(name) – Adds a station to the graph.

add_connection(station1, station2, distance) – Connects two stations with a specified distance.

dijkstra(source, destination) – Finds the shortest path between two stations.

shortest_path(source, destination) – Reconstructs the shortest path and calculates travel cost.

# Example Usage

Enter the source station: Majestic

Enter the destination station: Market

Shortest Path from Majestic to Market: ['Majestic', 'Chickpete', 'Market']

Total cost: 10
