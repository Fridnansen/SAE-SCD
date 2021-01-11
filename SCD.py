import sys
import general_functions as gf
import easygui

from rbfc import RuleBasedFuzzyClassifier

from PyQt5 import QtWidgets
from rbfc_gui import Ui_MainWindow

from termcolor import colored
import colorama
import numpy as np

#Parametros Arcade Juego
parametro1_arcade = ["Hongo", "Tortuga", "Planta", "Dragon", "None"]#Enemigo
parametro2_arcade = ["Corto", "MedioCorto", "MedioLargo", "Largo", "None"]#Hueco
parametro3_arcade = ["Tubo", "Piedra", "Lava", "Llama", "None"]#Obstaculo
parametro4_arcade = ["Fuego", "Bala", "Nube", "Bomba", "None"]#Armas
#Parametros Accion Juego
parametro1_accion = ["Nivel 1", "Nivel 2", "Nivel 3", "Nivel 4", "Nivel 5", "None"]#Nivel de Juego
parametro2_accion = ["Golpe_Debil", "Golpe_Fuerte", "Patada_Debil", "Patada_Fuerte", "None"]#Golpe y Patada
parametro3_accion = ["Correr_Adelante", "Correr_Atras", "Saltar_Adelante", "Saltar_Atras",  "None"]#Correr y Saltar
parametro4_accion = ["Combo1", "Combo2", "Combo3", "Combo4", "None"]#Combos a mayor numero más golpes
#Parametros Deportivo Juego
parametro1_sport = ["Nivel 1", "Nivel 2", "Nivel 3", "Nivel 4", "Nivel 5", "None"]#Equipo
parametro2_sport = ["Pase_corto", "Pase_largo", "Drible", "Sprint", "None"]#Manejo del balon
parametro3_sport = ["Barrer", "Cubrir", "Agarrar", "Correr", "None"]#Accion sin balon
parametro4_sport = ["Chute", "Globo", "Colocar", "Chilena","Cabecita", "None"]#Disparo a la porteria 
#Parametros Shooter Juego
parametro1_shoot = ["Soldado", "Francotirador", "Ingeniero", "Medico", "None"]#Personaje
parametro2_shoot = ["Corto", "MedioCorto", "MedioLargo", "Largo", "None"]#Proximidad
parametro3_shoot = ["Cuchillo", "Rifle", "Pistola", "Escopeta", "Lanzagranadas", "Sniper", "None"]#Tipos de Arma
parametro4_shoot = ["Bajo", "Medio", "Alto", "Infinito", "None"]#Cantidad de Municiones
#Parametros Simulacion Juego
parametro1_sim = ["Muy_Baja", "Baja", "Media", "Alta", "Apagado"]#Velocidad 
parametro2_sim = ["Simple", "Pronunciada", "Recta", "None"]#Curva
parametro3_sim = ["Adelante", "Adelante_Derecha", "Adelante_Izquierda", "Atras", "Atras_Derecha", "Atras_Izquierda", "None"]#Movimiento
parametro4_sim = ["Corto", "MedioCorto", "MedioLargo", "Largo", "None"]#Distancia
#Parametros calculo Juego
parametro1_calc = ["Suma", "Resta", "Multiplicacion", "Division", "None"]#Operacion
parametro2_calc = ["Baja", "Media", "Alta", "None"]#Puntaje
parametro3_calc = ["Simple",  "Intermedio", "Complejo", "None"]#Dificultad
parametro4_calc = ["Completo", "Incompleto", "None"]#Progreso



class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    # main class that creates the GUI and its functions

    def __init__(self):
        self.train_ratio = 0.5  # the default ratio is 0,5
        super(self.__class__, self).__init__()
        self.setupUi(self)  # create the GUI

        # the code below creates the functions in the GUI
        self.browse_button.clicked.connect(self.browse_button_clicked)
        self.classify_sample_button.clicked.connect(self.classify_sample_button_clicked)
        self.show_membership_functions_button.clicked.connect(self.show_membership_functions_button_clicked)
        self.show_train_set_button.clicked.connect(self.show_train_set_button_clicked)
        self.show_rules_button.clicked.connect(self.show_rules_button_clicked)
        self.train_to_test_ratio_slider.valueChanged.connect(self.train_to_test_ratio_slider_value_changed)  # here
        self.train_to_test_ratio_spinbox.valueChanged.connect(self.train_to_test_ratio_spinbox_value_changed)  # here
        self.train_button.clicked.connect(self.train_button_clicked)
        self.classify_test_set_button.clicked.connect(self.classify_test_set_button_clicked)
        if self.tipo_juego.currentTextChanged:
            #text = str(self.tipo_juego.currentText())
            self.tipo_juego.currentTextChanged.connect(self.combo_box_change)
        self.rbfc = None

        colorama.init()

    def browse_button_clicked(self):
        # open a filechooser and pick the dataset used for the training and testing
        path = easygui.fileopenbox()

        if path:
            self.dataset_path_input.setText(path)

    def show_membership_functions_button_clicked(self):
        # show the membership functions created during the training
        self.rbfc.show_membership_functions_plot()

    def show_train_set_button_clicked(self):
        # show the training set
        self.rbfc.show_data_set()

    def show_rules_button_clicked(self):
        # print the rules generated during the training into the console
        self.rbfc.print_rules()

    def train_to_test_ratio_slider_value_changed(self):
        # change the ratio of train/test samples both in variable and in spinner
        self.train_to_test_ratio_spinbox.setValue(self.train_to_test_ratio_slider.value())
        self.train_ratio = 1 - self.train_to_test_ratio_slider.value() / 100

    def train_to_test_ratio_spinbox_value_changed(self):
        # change the ratio of train/test samples both in variable and in slider
        self.train_to_test_ratio_slider.setValue(self.train_to_test_ratio_spinbox.value())
        self.train_ratio = 1 - self.train_to_test_ratio_spinbox.value() / 100

    def train_button_clicked(self):
        # begin the training
        try:
            (data_set, targets) = gf.csv_to_data_set(self.dataset_path_input.text())

            print("Conjunto de Datos: ")
            print(data_set)

            print("Objetivo: ")
            print(targets)
            print("------------------------")

            (self.train_set, self.test_set, self.train_targets, self.test_targets) = gf.split_data_set(data_set,
                                                                                                       targets,
                                                                                                       test_size
                                                                                                       =
                                                                                                       self.train_ratio)

            print("Conjunto de Entrenamiento: ")
            print(self.train_set)
            print(self.train_set.shape)

            print("Conjunto del Test: ")
            print(self.test_set)
            print(self.test_set.shape)

            print("Entrenamiento para el Objetivo: ")
            print(self.train_targets)

            print("Test Objetivo: ")
            print(self.test_targets)
            print("------------------------")

            print(colored("Entrenamiento Exitoso: ", 'green'))

            # Dynamically add inputs
            self.characteristics_inputs = []

            print("Forma del Conjunto de datos - data_set.shape[1]: ", data_set.shape[1])

            for i in range(data_set.shape[1]):
                self.characteristics_inputs.append(QtWidgets.QLineEdit(self.gridLayoutWidget))
                self.characteristics_inputs[i].setStyleSheet("background-color: rgb(255, 255, 255);")
                self.characteristics_inputs[i].setText("0")
                self.horizontalLayout_2.addWidget(self.characteristics_inputs[i])

            self.rbfc = RuleBasedFuzzyClassifier(self.train_set, self.train_targets)

            # Activando los botones de resultados

            self.show_train_set_button.setEnabled(True)
            self.show_membership_functions_button.setEnabled(True)
            self.show_rules_button.setEnabled(True)

            self.classify_test_set_button.setEnabled(True)
            self.classify_sample_button.setEnabled(True)

            # Desactivando este boton
            self.train_button.setEnabled(False)


        except FileNotFoundError:
            print("Un archivo no fue especificado.")
        except:
            print("Algo salio mal.")

    def classify_test_set_button_clicked(self):

        # begin the testing of the samples found in the test set
        self.classifications = self.rbfc.classify_samples(self.test_set)

        self.accs = []
        self.accs.append(gf.accuracy(self.classifications, self.test_targets))

        for i in range(len(self.classifications)):
            if self.test_targets[i] == self.classifications[i]:
                print(colored(
                    "Categoria Verdadera: {}, Clasificacion: {}".format(self.test_targets[i], self.classifications[i]),
                    'green'))
            else:
                print(colored(
                    "Categoria Falsa: {}, Clasificacion: {}".format(self.test_targets[i], self.classifications[i]),
                    'red'))
        print(colored("\nExactitud\n-----------", 'cyan'))
        print(colored(gf.accuracy(self.classifications, self.test_targets), 'cyan'))

    def classify_sample_button_clicked(self, texto):


        self.ins = []
        for characteristic_input in self.characteristics_inputs:
            self.ins.append(characteristic_input.text())

        nparray = np.array([self.ins]).astype(float)

        self.ins.clear()

        print(nparray)

        es_valido = True
        # print("Valor por valor:")
        for i in np.nditer(nparray):
            print(i)
            if i <= 0:
                es_valido = False

        if es_valido == False:
            print("Es necesario que todos los parametros sean mayores que cero.")
        else:
            self.rbfc.classify_samples(nparray)

    def combo_box_change(self, text):
        if self.tipo_juego.currentText() == "Plataforma":
            self.parametro_1.clear()
            self.parametro_2.clear()
            self.parametro_3.clear()
            self.parametro_4.clear()
            self.parametro1_label.setText("Enemigo")
            self.parametro1_label.adjustSize()
            self.parametro_1.addItems(parametro1_arcade)
            self.parametro2_label.setText("Hueco")
            self.parametro2_label.adjustSize()
            self.parametro_2.addItems(parametro2_arcade)
            self.parametro3_label.setText("Obstaculo")
            self.parametro3_label.adjustSize()
            self.parametro_3.addItems(parametro3_arcade)
            self.parametro4_label.setText("Arma")
            self.parametro4_label.adjustSize()
            self.parametro_4.addItems(parametro4_arcade)
        elif self.tipo_juego.currentText() == "Pelea":
            self.parametro_1.clear()
            self.parametro_2.clear()
            self.parametro_3.clear()
            self.parametro_4.clear()
            self.parametro1_label.setText("Personaje")
            self.parametro1_label.adjustSize()
            self.parametro_1.addItems(parametro1_accion)
            self.parametro2_label.setText("Tipo de Golpe")
            self.parametro2_label.adjustSize()
            self.parametro_2.addItems(parametro2_accion)
            self.parametro3_label.setText("Corre/Salto")
            self.parametro3_label.adjustSize()
            self.parametro_3.addItems(parametro3_accion)
            self.parametro4_label.setText("Combos")
            self.parametro4_label.adjustSize()
            self.parametro_4.addItems(parametro4_accion)
        elif self.tipo_juego.currentText() == "Deportivo":
            self.parametro_1.clear()
            self.parametro_2.clear()
            self.parametro_3.clear()
            self.parametro_4.clear()
            self.parametro1_label.setText("Equipo")
            self.parametro1_label.adjustSize()
            self.parametro_1.addItems(parametro1_sport)
            self.parametro2_label.setText("Manejo de Balon")
            self.parametro2_label.adjustSize()
            self.parametro_2.addItems(parametro2_sport)
            self.parametro3_label.setText("Accion sin Balon")
            self.parametro3_label.adjustSize()
            self.parametro_3.addItems(parametro3_sport)
            self.parametro4_label.setText("Tiro al Arco")
            self.parametro4_label.adjustSize()
            self.parametro_4.addItems(parametro4_sport)
        elif self.tipo_juego.currentText() == "Simulacion":
            self.parametro_1.clear()
            self.parametro_2.clear()
            self.parametro_3.clear()
            self.parametro_4.clear()
            self.parametro1_label.setText("Velocidad")
            self.parametro1_label.adjustSize()
            self.parametro_1.addItems(parametro1_sim)
            self.parametro2_label.setText("Curva")
            self.parametro2_label.adjustSize()
            self.parametro_2.addItems(parametro2_sim)
            self.parametro3_label.setText("Movimiento")
            self.parametro3_label.adjustSize()
            self.parametro_3.addItems(parametro3_sim)
            self.parametro4_label.setText("Distancia")
            self.parametro4_label.adjustSize()
            self.parametro_4.addItems(parametro4_sim)
        elif self.tipo_juego.currentText() == "Disparos":
            self.parametro_1.clear()
            self.parametro_2.clear()
            self.parametro_3.clear()
            self.parametro_4.clear()
            self.parametro1_label.setText("Profesion")
            self.parametro1_label.adjustSize()
            self.parametro_1.addItems(parametro1_shoot)
            self.parametro2_label.setText("Proximidad")
            self.parametro2_label.adjustSize()
            self.parametro_2.addItems(parametro2_shoot)
            self.parametro3_label.setText("Arma")
            self.parametro3_label.adjustSize()
            self.parametro_3.addItems(parametro3_shoot)
            self.parametro4_label.setText("Municion")
            self.parametro4_label.adjustSize()
            self.parametro_4.addItems(parametro4_shoot)
        elif self.tipo_juego.currentText() == "Calculo":
            self.parametro_1.clear()
            self.parametro_2.clear()
            self.parametro_3.clear()
            self.parametro_4.clear()
            self.parametro1_label.setText("Operacion")
            self.parametro1_label.adjustSize()
            self.parametro_1.addItems(parametro1_calc)
            self.parametro2_label.setText("Puntaje")
            self.parametro2_label.adjustSize()
            self.parametro_2.addItems(parametro2_calc)
            self.parametro3_label.setText("Dificultad")
            self.parametro3_label.adjustSize()
            self.parametro_3.addItems(parametro3_calc)
            self.parametro4_label.setText("Progreso")
            self.parametro4_label.adjustSize()
            self.parametro_4.addItems(parametro4_calc)
        else:
            print("no aplica")
            self.parametro_1.clear()
            self.parametro_2.clear()
            self.parametro_3.clear()
            self.parametro_4.clear()





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    rbfc_window = Main()
    rbfc_window.setWindowTitle("Sistema de Clasificador Difuso (Basado en Reglas)")
    rbfc_window.show()
    sys.exit(app.exec_())
