from rbfc import RuleBasedFuzzyClassifier
from termcolor import colored
import general_functions as gf
import plotly
import numpy as np

import colorama

times_to_test = 5  # estaba en 100

if __name__ == '__main__':
    (data_set, targets) = gf.csv_to_data_set("reglasMarioBross.data")
    accs = []
    colorama.init()
    for y in range(times_to_test):
        print("-" * 20, "Test No: ", y + 1, "-" * 20)
        # Train - test set split
        (train_set, test_set, train_targets, test_targets) = gf.split_data_set(data_set, targets, test_size=.6)
        # Train model
        rbfc = RuleBasedFuzzyClassifier(train_set, train_targets)
        print(colored("Entrenamiento fue Exitoso.", "yellow"))
        rbfc.show_data_set()
        # Classify test set
        predictions = rbfc.classify_samples(test_set)
        # Print confusion matrix
        labels = ["Salta y Dispara", "Corre y Salta", "Corre y Dispara "]
        gf.show_confusion_matrix(test_targets, predictions, labels)

        # El for estaba comentado
        for i in range(len(predictions)):
            if test_targets[i] == predictions[i]:
                print(colored("Categoria Verdadera: {}, Clasificacion: {}".format(test_targets[i], predictions[i]), 'green'))
            else:
                print(colored("Categoria Falsa: {}, Clasificacion: {}".format(test_targets[i], predictions[i]), 'red'))

        print(colored("-" * 10 + " Exactitud " + "-" * 10, 'cyan'))
        # Append accuracy to accs array
        accs.append(gf.accuracy(predictions, test_targets))
        print(colored(accs[y], 'cyan'))

print(colored("Promedio de Exactitud: " + str(sum(accs) / times_to_test), "green"))
# rbfc.show_data_set_plot()
