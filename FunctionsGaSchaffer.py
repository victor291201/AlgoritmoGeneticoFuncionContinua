import numpy as np
from GeneticalAlgorithm.geneticalgorithmMaster.geneticalgorithm.geneticalgorithm import geneticalgorithm as ga
import numpy
import time
import matplotlib.pyplot as plt


def f(X):
    return (0.5 +
            (
                (numpy.sin(numpy.cos(abs(X[0]**2-X[1]**2)))**2) - 0.5
            )
            /
            (
                (1 + (0.001*(X[0]**2+X[1]**2)))**2
            )
            )


varbound = np.array([[-100, 100]]*2)


def GAParams(x):
    nPruebas = x.get("nPruebas")
    nIteraciones = x.get("nIteraciones")
    tCruzamiento = x.get("tCruzamiento")
    tMutacion = x.get("tMutacion")
    tPoblacion = x.get("tPoblacion")
    tElite = x.get("tElite")
    soluciones = []
    algorithm_param = {'max_num_iteration': nIteraciones,
                       'population_size': tPoblacion,
                       'mutation_probability': tMutacion,
                       'elit_ratio': tElite,
                       'crossover_probability': tCruzamiento,
                       'parents_portion': 0.3,
                       'crossover_type': 'uniform',
                       'max_iteration_without_improv': None}

    model = ga(function=f, dimension=2, variable_type='real',
               variable_boundaries=varbound, algorithm_parameters=algorithm_param)
    for i in range(nPruebas):

        inicio = time.time()
        model.run()
        final = time.time()
        tiempo = final-inicio
        solution = model.output_dict
        solution.update({"time": tiempo})
        soluciones.append(solution)
    return soluciones


def generateGraph(x, y, labelX, labelY, title, all=False, var=0, med=0, desv=0):
    plt.title(title)
    if (all == False):
        plt.plot(x, y, 'bo', x, y, 'b--')
    else:
        plt.plot(x, y, 'bo', x, y, 'b--', x, [var for i in range(len(x))], "r", x, [
                 med for i in range(len(x))], "y", x, [desv for i in range(len(x))], "g")
    plt.ylabel(labelY)
    plt.xlabel(labelX)
    plt.grid(True)
    plt.show()


def generateTable(x, y, title):
    fig, ax = plt.subplots(1, 1)
    data = x
    column_labels = y
    ax.axis("off")
    fig.suptitle(title)
    table = ax.table(cellText=data, colLabels=column_labels,
                     loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(9)

    plt.show()
