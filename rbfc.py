# Rule Based Fuzzy Classifier

import copy

from membership_function import MembershipFunction

from plot import Plot

import numpy as np

from rule import Rule

import general_functions as gf

import plotly.graph_objs as go

from plotly.offline import plot

import time


class RuleBasedFuzzyClassifier:

    def __init__(self, train_set, train_targets):
        self.data_set = train_set
        self.targets = train_targets

        self._sorted_data_set = None
        self._membership_functions = []
        self.rules = []
        self.target_categories = None

        self.graph = {}

        self.sort_data_set()
        self.generate_membership_functions()
        self.generate_rules()

    def show_data_set(self):
        """
        Prints each sample in data set along with its target
        """
        print("Cojunto de Entrenamiento:")
        for i in range(self.data_set.shape[0]):
            print("Muestra [", i, "]: ", self.data_set[i], " Objetivo: ", self.targets[i])

    def sort_data_set(self):
        """
        Sorts dataset's individual columns and inserts them in self._sorted_data_set.
        """
        self._sorted_data_set = copy.copy(self.data_set)
        for i in range(self._sorted_data_set.shape[1]):
            self._sorted_data_set[self._sorted_data_set[:, i].sort()]

    def generate_membership_functions(self):
        for i in range(self._sorted_data_set.shape[1]):  # Loop through columns
            self._membership_functions.append(MembershipFunction(self._sorted_data_set[:, i]))

    def show_membership_functions_plot(self):

        # Graficas en Matplotlib, mostrados en una cascada de ventanas.


        pos_x = 30
        pos_y = 30

        for key, mem_funcs in enumerate(self._membership_functions):
            # x-axis values
            x_left = []
            x_right = []
            # Y-axis values
            y_left = []
            y_right = []

            for j in range(len(mem_funcs.membership_function_left)):
                x_left.append(j)
                y_left.append(mem_funcs.membership_function_left[j])                
                
            for k in range(len(mem_funcs.membership_function_right)):
                x_right.append(k)                
                y_right.append(mem_funcs.membership_function_right[k])

            self.graph[key] = Plot(pos_x, pos_y, x_left, y_left, x_right, y_right, "Parametro: " + str(key + 1))

            pos_x += 30
            pos_y += 30

            x_left.clear()
            y_left.clear()
            
            x_right.clear()
            y_right.clear()

        for i in range(key):
            self.graph[i].show()

        # Graficas  en plotly, mostradas en archivos .html que se guardan en la carpeta de este programa.

        '''
        smoothing_value = 1
        for key, mem_funcs in enumerate(self._membership_functions):
            left_plot_smoothed = go.Scatter(x=list(range(len(mem_funcs.membership_function_left))),
                                            y=gf.smooth_data(mem_funcs.membership_function_left, smoothing_value),
                                            mode="lines",
                                            marker=go.Marker(color="#df80ff"), name="Left Membership function")
            right_plot_smoothed = go.Scatter(x=list(range(len(mem_funcs.membership_function_left))),
                                             y=gf.smooth_data(mem_funcs.membership_function_right, smoothing_value),
                                             mode="lines",
                                             marker=go.Marker(color="#8600b3"), name="Right Membership function")
            left_plot = go.Scatter(x=list(range(len(mem_funcs.membership_function_left))),
                                   y=mem_funcs.membership_function_left, mode="markers",
                                   marker=go.Marker(color="#df80ff"), opacity=0.3, name="Left Membership function")
            right_plot = go.Scatter(x=list(range(len(mem_funcs.membership_function_left))),
                                    y=mem_funcs.membership_function_right, mode="markers",
                                    marker=go.Marker(color="#8600b3"), opacity=0.3, name="Right Membership function")

            plot([left_plot_smoothed, right_plot_smoothed, left_plot, right_plot],
                 filename="Characteristic {} membership function.html".format(key + 1))
            # Add delay between plots showing to avoid crashing of browser
            time.sleep(1.5)        
        '''


    def generate_rule(self, sample, target=None):
        mem_activation = []
        for key, mem_fun in np.ndenumerate(self._membership_functions):
            # key es una tupla de tamano 1.
            # print("key del generaterule: ", key)
            # print("key.type del generaterule: ", type(key), "tamano: ", len(key))
            # print("key[0] del generaterule: ", key[0])
            # print("sample[key[0]] del generaterule: ", sample[key[0]])
            mem_activation.append(mem_fun.membership_functions_activation(sample[key[0]]))
        # print("Fin del for: generaterule.")

        activations_left, activations_right = [], []
        for (activ_l, activ_r) in mem_activation:
            activations_left.append(activ_l > 0)
            activations_right.append(activ_r > 0)

        return Rule(rule=np.concatenate((activations_left, activations_right)), target=target)

    def generate_rules(self):
        # print("En Generate rules: ")

        for key, sample in enumerate(self.data_set):
            # El key es un numero
            # El sample es un arreglo de 4 numeros reales
            # print("Key: ", key)
            # print("Sample: ", sample)
            self.rules.append(self.generate_rule(sample, self.targets[key]))

        # Remove duplicate rules
        # self.rules = gf.remove_doubles(self.rules)
        # Keep categories names in self.target_categories (ex. ["Iris-setosa", "Iris-virginica", ...])
        self.target_categories = gf.remove_doubles(self.targets)

        print("Las categorias: ")
        print(self.target_categories)

    def print_rules(self):
        print("Reglas: ")
        counter = 1
        for rule in self.rules:
            print('{}. {}'.format(counter, rule))
            counter += 1

    def classify_samples(self, samples):
        """
        Classifies the samples using the existing rules.
        :param samples: Samples array.
        :return: Numpy array with categories of the classified samples.
        """
        # Used to hold classifications of all samples for return
        classifications = []
        # Used to hold category name as key and number of times category
        # was found during classification of sample (ex. categories{"setosa": 2, "virginia": 2, ...}
        categories = {}

        for sample in samples:
            # Initialize categories values to 0
            for cat in self.target_categories:
                categories[cat] = 0
            # Generate rule for sample
            sample_rule = self.generate_rule(sample)
            # print("Sample rule: ", sample_rule)
            # Classify sample
            for rule in self.rules:
                if (sample_rule.rule == rule.rule).all():
                    categories[rule.target] += 1

            # Sort categories dict base on its values
            classifications.append(sorted(categories, key=categories.get, reverse=True)[0])

        print("Clasificar Muestra: ")
        print(classifications)

        array_of_classifications = np.array(classifications)

        print("En modo de matriz numpy: ")
        print(array_of_classifications)

        return array_of_classifications
