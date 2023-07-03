Genetic Algorithm


This project is focused on solving a neighborhood optimization problem using a genetic algorithm approach. The goal is to find the optimal configuration of telecommunication towers in a given set of neighborhoods, considering factors such as population, user satisfaction, tower construction and maintenance costs.

## Problem Description

The problem revolves around determining the placement and configuration of telecommunication towers in a city with multiple neighborhoods. Each neighborhood has a population and requires a certain level of bandwidth to satisfy user demands. The goal is to find the best allocation of towers to maximize user satisfaction while minimizing costs.

## Project Structure

The project code consists of the following main components:

1. **Chromosome Representation**: The chromosome represents a possible solution to the problem. It consists of a collection of genes, each representing a tower with its location, associated blocks, and allocated bandwidth.

2. **Fitness Function**: The fitness function evaluates the quality of a chromosome by calculating the total user satisfaction score minus the cost incurred by tower construction and maintenance.

3. **Genetic Operators**: The genetic operators include crossover and mutation. Crossover combines genetic information from two parent chromosomes to create new offspring chromosomes. Mutation introduces small changes in the chromosome to explore new solutions.

4. **Genetic Algorithm**: The genetic algorithm iteratively applies genetic operators to a population of chromosomes, evolving towards better solutions over successive generations.

5. **Data Input**: The code reads input data from two files: "problem_config.json" and "blocks_population.txt". The former contains configuration parameters such as tower costs and user satisfaction levels, while the latter provides information about the population of each block in the city.

6. **Visualization**: The code includes a function to generate a line plot showing the fitness values of the best chromosome in each generation.

## Usage

To use this code for your own optimization problem, follow these steps:

1. Set up the input data files:
   - Create a "problem_config.json" file containing the problem configuration parameters.
   - Create a "blocks_population.txt" file with the population information for each block in the city.

2. Import the required libraries:
   - numpy
   - random
   - json
   - operator
   - copy
   - matplotlib.pyplot
   - matplotlib.animation

3. Run the code:
   - Set the problem parameters such as the number of neighborhoods, speed limits, cost limits, and genetic algorithm parameters.
   - Call the `find_best_city` function, passing the lower and higher bound chromosomes for the initial population.

4. Analyze the results:
   - The code will output the best chromosome found, representing the optimal configuration of telecommunication towers.
   - The line plot generated during the genetic algorithm execution can provide insights into the convergence and performance of the algorithm.

## Conclusion

This project demonstrates the application of a genetic algorithm to solve a neighborhood optimization problem. By considering the population, user satisfaction levels, and tower costs, the algorithm aims to find the best configuration of telecommunication towers. The code provides a framework that can be adapted and extended to other optimization problems by modifying the fitness function and genetic operators.

Please note that this readme provides a high-level overview of the project. For more details and a deeper understanding of the code, refer to the code comments and documentation within the project files.

Feel free to explore and experiment with the code to solve your own optimization problems!
