functions = ["Parabola", "DeJong N.5", "Levy", "Styblinski-Tang", "HappyCat"]
selections = ["Best", "Roulette", "Tournament"]
crossovers = ["One Point", "Two Point", "Three Point", "Uniform", "Discrete"]
mutations = ["One Point", "Two Point", "Edge"]

import os
import time
from flask import Flask, render_template, request, redirect, send_from_directory, url_for
from evolution_manager import setup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Gather form data
        function = request.form['function']
        lower_bound = float(request.form['lower_bound'])  # Convert to float
        upper_bound = float(request.form['upper_bound'])  # Convert to float
        precision = float(request.form['precision'])  # Convert to float
        population_size = int(request.form['population_size'])  # Convert to int
        generations = int(request.form['generations'])  # Convert to int
        selection = request.form['selection']
        crossover = request.form['crossover']
        crossover_rate = float(request.form['crossover_rate'])  # Convert to float
        mutation = request.form['mutation']
        mutation_rate = float(request.form['mutation_rate'])  # Convert to float
        elitism = float(request.form['elitism'])  # Convert to float
        inverse = float(request.form['inverse'])  # Convert to float

        # Optional parameters for selection methods
        tournament_size = request.form.get('tournament_size')
        selection_size = request.form.get('selection_size')

        # Ensure to handle conversion for optional fields
        if tournament_size:
            tournament_size = int(tournament_size)  # Convert to int
        if selection_size:
            selection_size = float(selection_size)  # Convert to float

        print(function, lower_bound, upper_bound, precision, population_size, generations, selection, crossover, crossover_rate, mutation, mutation_rate, elitism, inverse, tournament_size, selection_size)
        
        start_time = time.time()
        #Call the setup function with all gathered parameters
        results = setup(
            function, lower_bound, upper_bound, precision, population_size, generations,
            selection, crossover, crossover_rate, mutation, mutation_rate, elitism,
            inverse, tournament_size, selection_size
        )
        # Calculate elapsed time
        elapsed_time = round(time.time() - start_time, 2)

        # Redirect to results page with the algorithm results
        return redirect(url_for('results', filename="Results/results.csv", best_fitness=results[1],
                                best_individual=results[0], std_dev= 0,
                                mean_fitness=0, elapsed_time=elapsed_time))

    return render_template('index.html')

@app.route('/results')
def results():
    # Retrieve the parameters passed via the URL
    filename = request.args.get('filename')
    best_fitness = request.args.get('best_fitness')
    best_individual = request.args.get('best_individual')
    std_dev = request.args.get('std_dev')
    mean_fitness = request.args.get('mean_fitness')
    elapsed_time = request.args.get('elapsed_time')

    # Determine the plot and CSV file paths
    plot1 = f'{filename}_plot1.png'
    plot2 = f'{filename}_plot2.png'
    plot3 = f'{filename}_plot3.png'
    csv_file = f'{filename}.csv'

    return render_template('results.html', best_fitness=best_fitness,
                           best_individual=best_individual, std_dev=std_dev,
                           mean_fitness=mean_fitness, elapsed_time=elapsed_time,
                           plot1=plot1, plot2=plot2, plot3=plot3, csv_file=csv_file)

@app.route('/download/<filename>')
def download_file(filename):
    # Return the CSV file for download
    directory = os.path.join(app.root_path, 'static', 'Results')
    return send_from_directory(directory, filename)

if __name__ == '__main__':
    app.run(debug=True)
