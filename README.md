# Evolutionary Algorithm
## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Algorithm Overview](#algorithm-overview)
  - [Selection strategies](#selection-strategies)
  - [Crossover strategies](#crossover-strategies)
  - [Mutation strategies](#mutation-strategies)
  - [Implemented functions](#implemented-functions)
- [Authors](#contributing)
- [License](#license)

## Overview

This repository implements various evolutionary algorithms, which are optimization techniques inspired by the process of natural selection. The primary goal is to provide a flexible framework for researchers and developers to experiment with and apply evolutionary algorithms to solve complex problems.

## Features

- **Modular Design**: Easily extend or modify algorithms to fit your needs.
- **Multiple Algorithms**: Implementations of many different algorithms for selection, mutation and crossover.
- **Visualization Tools**: Flask interface for easy and accesible usage.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- Required packages listed in `requirements.txt` installed.

### Installation

1. Clone the repository:
   ```bash
   git https://github.com/Arwers/evolutionary-algorithms.git
   cd evolutionary-algorithms
   ```

### Usage

1. Run the flask server
    ```bash
    python App/index.py
    ```
2. Connect to the address that the server is running on

## Algorithm overview

### Selection strategies

-**Selection of the best**: \
This strategy selects the best individuals from the current population based on their fitness values. It ensures that only the most fit individuals contribute to the next generation, promoting convergence towards optimal solutions.\
-**Roulette selection**: \
Roulette selection (also known as fitness proportionate selection) chooses individuals based on their fitness proportion. Individuals with higher fitness have a higher chance of being selected, which mimics the roulette wheel's spinning process. \
-**Tournament selection**: \
In tournament selection, a subset of individuals is randomly chosen from the population, and the individual with the highest fitness from this subset is selected. This method introduces selection pressure while maintaining diversity in the population.

### Crossover strategies

-**One point crossover**: \
One point crossover involves selecting a random crossover point on the parent individuals. The genetic material is exchanged at this point, creating two offspring. \
-**Two point crossover**: \
In two point crossover, two crossover points are selected randomly. The genetic material between these two points is exchanged, allowing for more variability in the offspring. \
-**Three point crossover**: \
Three point crossover extends the concept of two-point crossover by introducing a third point for genetic material exchange, creating greater diversity among offspring. \
-**Uniform crossover**: \
Uniform crossover randomly selects genes from either parent for each position in the offspring, leading to a more balanced combination of traits from both parents. \
-**Discrete crossover**: \
Discrete crossover selects genes from one parent or the other for the entire chromosome, maintaining the integrity of the parent's genetic makeup while allowing for the introduction of new traits. 

### Mutation strategies

-**One point mutation**: \
One point mutation randomly alters a single gene in an individual’s chromosome. This strategy introduces small variations, helping to maintain genetic diversity. \
-**Two point mutation**: \
Two point mutation changes the values of two randomly chosen genes in the chromosome, allowing for more significant alterations compared to one point mutation. \
-**Edge mutation**: \
Edge mutation focuses on altering the connections between genes or nodes in a representation, typically used in graph-based or network problems, to explore the solution space effectively.

### Implemented functions
-**Parabola**: \
Simple parabola, described by f(x) = 2x^2 + 5.

-**Levy**: \
The Levy function is a complex multimodal function often used in testing optimization algorithms due to its numerous local minima.

-**DeJong N. 5**: \
De Jong N. 5 is a well-known benchmark function in optimization that presents a challenge due to its many local optima.

-**HappyCat**: \
The HappyCat function is a multimodal test function with multiple local optima, useful for evaluating the performance of evolutionary algorithms.

-**Stybliński-Tang**: \ 
The Stybliński-Tang function is another benchmark optimization function characterized by its numerous local minima, providing a challenging landscape for optimization tasks.

## Authors
**Marcin Fortuna** \
**Jakub Konieczny**

## License
This project is licensed under the MIT License - see the License.txt file for details.
