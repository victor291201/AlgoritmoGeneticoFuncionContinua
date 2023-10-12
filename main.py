import FunctionsGaSchaffer
import matplotlib.pyplot as plt
import numpy as np

# variables del algoritmo
configpruebas = [
    {
        "nPruebas": 40, "nIteraciones": 100, "tCruzamiento": 0.3, "tMutacion": 0.1, "tPoblacion": 200, "tElite": 0.1
    },
    {
        "nPruebas": 40, "nIteraciones": 50, "tCruzamiento": 0.6, "tMutacion": 0.3, "tPoblacion": 100, "tElite": 0.01
    },
    {
        "nPruebas": 40, "nIteraciones": 75, "tCruzamiento": 0.9, "tMutacion": 0.5, "tPoblacion": 150, "tElite": 0.001
    }
]


def med(x):
    return np.array(x, float).mean()


def var(x):
    return np.array(x, float).var()


def desv(x):
    return np.array(x, float).std()


def main():
    results = []
    for i in range(len(configpruebas)):
        results.append(FunctionsGaSchaffer.GAParams(configpruebas[i]))
    print("\n")
    print("Resultados de las pruebas: ")
    for i in range(configpruebas[i]["nPruebas"]):
        valX1 = []
        valX2 = []
        valFx = []
        valT = []
        valC = []
        for e in range(configpruebas[i]["nPruebas"]):
            valX1.append(results[i][e].get("variable")[0])
            valX2.append(results[i][e].get("variable")[1])
            valFx.append(results[i][e].get("function"))
            valT.append(results[i][e].get("time"))
            valC.append(results[i][e].get("iterationsConvergence"))
        data1 = []
        for e in range(configpruebas[i]["nPruebas"]):
            data1.append([valX1[e], valX2[e], valFx[e], valT[e], valC[e]])
        print("------------------------------------------------------------------------------------------------------")
        print("Resultados de la prueba "+str(i+1)+":")
        FunctionsGaSchaffer.generateTable(data1, [
                                          "X1", "X2", "f(x)", "time", "convergencia"], "Resultados")
        resumen = {"media": [], "varianza": [], "desv": []}
        resumen["media"].append(med(valX1))
        resumen["media"].append(med(valX2))
        resumen["media"].append(med(valFx))
        resumen["media"].append(med(valT))
        resumen["media"].append(med(valC))

        resumen["varianza"].append(var(valX1))
        resumen["varianza"].append(var(valX2))
        resumen["varianza"].append(var(valFx))
        resumen["varianza"].append(var(valT))
        resumen["varianza"].append(var(valC))

        resumen["desv"].append(desv(valX1))
        resumen["desv"].append(desv(valX2))
        resumen["desv"].append(desv(valFx))
        resumen["desv"].append(desv(valT))
        resumen["desv"].append(desv(valC))
        print("------------------------------------------------------------------------------------------------------")
        print("Resumen de los resultados de la prueba "+str(i+1)+":")
        FunctionsGaSchaffer.generateTable([[resumen["media"][0], resumen["media"][1], resumen["media"][2], resumen["media"][3], resumen["media"][4]]], [
                                          "X1", "X2", "f(x)", "time", "convergencia"], "Promedios")
        FunctionsGaSchaffer.generateTable([[resumen["varianza"][0], resumen["varianza"][1], resumen["varianza"][2], resumen["varianza"][3], resumen["varianza"][4]]], [
                                          "X1", "X2", "f(x)", "time", "convergencia"], "Varianzas")
        FunctionsGaSchaffer.generateTable([[resumen["desv"][0], resumen["desv"][1], resumen["desv"][2], resumen["desv"][3], resumen["desv"][4]]], [
                                          "X1", "X2", "f(x)", "time", "convergencia"], "Desviaciones estandar")
        iter = [g for g in range(1, configpruebas[i]["nPruebas"]+1)]
        FunctionsGaSchaffer.generateGraph(
            iter, valFx, "N. prueba", "f(x)", "f(x) vs Pruebas", True, resumen["media"][2], resumen["media"][3], resumen["media"][4])
        FunctionsGaSchaffer.generateGraph(
            iter, valT, "N. prueba", "tiempo", "Tiempo vs Pruebas", True, resumen["media"][2], resumen["media"][3], resumen["media"][4])
        FunctionsGaSchaffer.generateGraph(
            iter, valC, "N. prueba", "Numero de iteraciones para converger", "Iteraciones vs Pruebas", True, resumen["media"][2], resumen["media"][3], resumen["media"][4])


if __name__ == "__main__":
    main()
