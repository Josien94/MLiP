import json
import matplotlib.pyplot as plt
import numpy as np


def load_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def parseData(trainingData):
    plotData = {"losses": [], "learning_rates": []}
    epochs = []

    for row in trainingData:
        plotData["losses"].append(row["loss"])
        plotData["learning_rates"].append(row["learning_rate"])
        epochs.append(row["epoch"])

    return plotData, epochs


def createLineGraph(plotData_BERT, plotData_SciBERT, epochs, xlabel, ylabel, title, save_filename):

    plt.plot(epochs, plotData_BERT, label='BERT')
    plt.plot(epochs, plotData_SciBERT, label="SciBERT")

    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(save_filename)
    plt.show()


def main():

    filename = 'trainingResults.json'
    trainingData = load_json(filename)

    parsedData_BERT, epochs_BERT = parseData(trainingData["BERT"])
    parsedData_SCiBERT, epochs_SciBERT = parseData(trainingData["SciBERT"])

    # Create linegraph for learing rate
    createLineGraph(parsedData_BERT["learning_rates"], parsedData_SCiBERT["learning_rates"],
                    epochs_SciBERT, 'epochs', 'learning rate', 'Learning rate versus epochs', 'learningRates.png')
    # # Create linegraph for training loss
    createLineGraph(parsedData_BERT["losses"], parsedData_SCiBERT["losses"],
                    epochs_SciBERT, 'epochs', 'losses', 'Trainig loss versus epochs', 'trainingLosses.png')


if __name__ == "__main__":
    main()
