from PyQt5 import QtCore, QtWidgets

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 697)
        MainWindow.setStyleSheet("background-color: rgb(211, 211, 211);")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(16, 0, 641, 681))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.show_train_set_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.show_train_set_button.setEnabled(False)
        self.show_train_set_button.setStyleSheet("color: rgb(233, 233, 233);\n"
                                                 "background-color: rgb(96, 96, 96);")
        self.show_train_set_button.setObjectName("show_train_set_button")
        self.horizontalLayout.addWidget(self.show_train_set_button)
        self.show_membership_functions_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.show_membership_functions_button.setEnabled(False)
        self.show_membership_functions_button.setStyleSheet("color: rgb(233, 233, 233);\n"
                                                            "background-color: rgb(96, 96, 96);")
        self.show_membership_functions_button.setObjectName("show_membership_functions_button")
        self.horizontalLayout.addWidget(self.show_membership_functions_button)
        self.show_rules_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.show_rules_button.setEnabled(False)
        self.show_rules_button.setStyleSheet("color: rgb(233, 233, 233);\n"
                                             "background-color: rgb(96, 96, 96);")
        self.show_rules_button.setObjectName("show_rules_button")
        self.horizontalLayout.addWidget(self.show_rules_button)
        self.gridLayout.addLayout(self.horizontalLayout, 13, 0, 1, 3)
        self.browse_button = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.browse_button.setStyleSheet("color: rgb(233, 233, 233);\n"
                                         "background-color: rgb(96, 96, 96);")
        self.browse_button.setObjectName("browse_button")
        self.gridLayout.addWidget(self.browse_button, 2, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.train_to_test_ratio_slider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.train_to_test_ratio_slider.setStyleSheet("")
        self.train_to_test_ratio_slider.setMinimum(5)
        self.train_to_test_ratio_slider.setMaximum(100)
        self.train_to_test_ratio_slider.setProperty("value", 50)
        self.train_to_test_ratio_slider.setOrientation(QtCore.Qt.Horizontal)
        self.train_to_test_ratio_slider.setObjectName("train_to_test_ratio_slider")
        self.horizontalLayout_3.addWidget(self.train_to_test_ratio_slider)
        self.train_to_test_ratio_spinbox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.train_to_test_ratio_spinbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.train_to_test_ratio_spinbox.setMinimum(5)
        self.train_to_test_ratio_spinbox.setMaximum(100)
        self.train_to_test_ratio_spinbox.setProperty("value", 50)
        self.train_to_test_ratio_spinbox.setObjectName("train_to_test_ratio_spinbox")
        self.horizontalLayout_3.addWidget(self.train_to_test_ratio_spinbox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 3)
        self.dataset_path_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.dataset_path_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dataset_path_input.setObjectName("dataset_path_input")
        self.gridLayout.addWidget(self.dataset_path_input, 2, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.testing_section_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.testing_section_label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                                 "color: rgb(67, 67, 67);\n"
                                                 "")
        self.testing_section_label.setObjectName("testing_section_label")
        self.gridLayout.addWidget(self.testing_section_label, 19, 0, 1, 1)
        self.train_to_test_ratio_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.train_to_test_ratio_label.setStyleSheet("color: rgb(67, 67, 67);")
        self.train_to_test_ratio_label.setAlignment(QtCore.Qt.AlignCenter)
        self.train_to_test_ratio_label.setObjectName("train_to_test_ratio_label")
        self.gridLayout.addWidget(self.train_to_test_ratio_label, 4, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 31, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 15, 0, 1, 1)
        self.characteristics_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.characteristics_label.setStyleSheet("color: rgb(67, 67, 67);")
        self.characteristics_label.setAlignment(QtCore.Qt.AlignCenter)
        self.characteristics_label.setObjectName("characteristics_label")
        self.gridLayout.addWidget(self.characteristics_label, 24, 0, 1, 3)
        self.training_section_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.training_section_label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                                  "color: rgb(67, 67, 67);")
        self.training_section_label.setObjectName("training_section_label")
        self.gridLayout.addWidget(self.training_section_label, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 18, 0, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout.addLayout(self.horizontalLayout_2, 30, 0, 1, 3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.first_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.first_label.setStyleSheet("color: rgb(67, 67, 67);")
        self.first_label.setObjectName("first_label")
        self.horizontalLayout_5.addWidget(self.first_label)
        self.second_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.second_label.setStyleSheet("color: rgb(67, 67, 67);")
        self.second_label.setObjectName("second_label")
        self.horizontalLayout_5.addWidget(self.second_label)
        self.third_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.third_label.setStyleSheet("color: rgb(67, 67, 67);")
        self.third_label.setObjectName("third_label")
        self.horizontalLayout_5.addWidget(self.third_label)
        self.fourth_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.fourth_label.setStyleSheet("color: rgb(67, 67, 67);")
        self.fourth_label.setObjectName("fourth_label")
        self.horizontalLayout_5.addWidget(self.fourth_label)
        self.gridLayout.addLayout(self.horizontalLayout_5, 25, 0, 1, 3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.classify_sample_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.classify_sample_button.setEnabled(False)
        self.classify_sample_button.setStyleSheet("color: rgb(233, 233, 233);\n"
                                                  "background-color: rgb(96, 96, 96);")
        self.classify_sample_button.setObjectName("classify_sample_button")
        self.horizontalLayout_6.addWidget(self.classify_sample_button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_6, 32, 0, 1, 3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.classify_test_set_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.classify_test_set_button.setEnabled(False)
        self.classify_test_set_button.setStyleSheet("color: rgb(233, 233, 233);\n"
                                                    "background-color: rgb(96, 96, 96);")
        self.classify_test_set_button.setObjectName("classify_test_set_button")
        self.horizontalLayout_4.addWidget(self.classify_test_set_button)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_4, 20, 0, 1, 3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        # Combo Box
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(0, 11, 11, 11)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.juego_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.juego_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                            "color: rgb(67, 67, 67);")
        self.juego_label.setObjectName("juego_label")
        self.horizontalLayout_11.addWidget(self.juego_label)
        self.tipo_juego = QtWidgets.QComboBox(MainWindow)
        self.tipo_juego.setObjectName("tipo_juego")
        self.horizontalLayout_11.addWidget(self.tipo_juego)
        self.gridLayout.addLayout(self.horizontalLayout_11, 25, 0, 1, 3)
        self.tipo_juego.setStyleSheet("color: rgb(67, 67, 67);\n"
                                                    "background-color: rgb(255, 255, 255);")
        self.tipo_juego.addItem("")
        self.tipo_juego.addItem("")
        self.tipo_juego.addItem("")
        self.tipo_juego.addItem("")
        self.tipo_juego.addItem("")
        self.tipo_juego.addItem("")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(0, 11, 11, 11)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.parametro1_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.parametro1_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                            "color: rgb(67, 67, 67);")
        self.parametro1_label.setObjectName("parametro1_label")
        self.horizontalLayout_9.addWidget(self.parametro1_label)
        self.parametro2_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.parametro2_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                            "color: rgb(67, 67, 67);")
        self.parametro2_label.setObjectName("parametro2_label")
        self.horizontalLayout_9.addWidget(self.parametro2_label)
        self.parametro3_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.parametro3_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                            "color: rgb(67, 67, 67);")
        self.parametro3_label.setObjectName("parametro3_label")
        self.horizontalLayout_9.addWidget(self.parametro3_label)
        self.parametro4_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.parametro4_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                            "color: rgb(67, 67, 67);")
        self.parametro4_label.setObjectName("parametro4_label")
        self.horizontalLayout_9.addWidget(self.parametro4_label)
        self.gridLayout.addLayout(self.horizontalLayout_9, 26, 0, 1, 3)
        self.horizontalLayout_8 =  QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(0, 11, 11, 11)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.parametro_1 = QtWidgets.QComboBox(MainWindow)
        self.parametro_1.setObjectName("parametro_1")
        self.horizontalLayout_8.addWidget(self.parametro_1)
        self.parametro_1.setStyleSheet("color: rgb(67, 67, 67);\n"
                                      "background-color: rgb(255, 255, 255);")
        self.parametro_2 = QtWidgets.QComboBox(MainWindow)
        self.parametro_2.setObjectName("parametro_2")
        self.horizontalLayout_8.addWidget(self.parametro_2)
        self.parametro_2.setStyleSheet("color: rgb(67, 67, 67);\n"
                                       "background-color: rgb(255, 255, 255);")
        self.parametro_3 = QtWidgets.QComboBox(MainWindow)
        self.parametro_3.setObjectName("parametro_3")
        self.horizontalLayout_8.addWidget(self.parametro_3)
        self.parametro_3.setStyleSheet("color: rgb(67, 67, 67);\n"
                                       "background-color: rgb(255, 255, 255);")
        self.parametro_4 = QtWidgets.QComboBox(MainWindow)
        self.parametro_4.setObjectName("parametro_4")
        self.horizontalLayout_8.addWidget(self.parametro_4)
        self.parametro_4.setStyleSheet("color: rgb(67, 67, 67);\n"
                                       "background-color: rgb(255, 255, 255);")
        self.gridLayout.addLayout(self.horizontalLayout_8, 27, 0, 1, 3)
        self.train_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.train_button.setEnabled(True)
        self.train_button.setStyleSheet("color: rgb(233, 233, 233);\n"
                                        "background-color: rgb(96, 96, 96);")
        self.train_button.setObjectName("train_button")
        self.horizontalLayout_7.addWidget(self.train_button)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.gridLayout.addLayout(self.horizontalLayout_7, 7, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralWidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.show_train_set_button.setToolTip(_translate("MainWindow",
                                                         "<html><head/><body><p><span style=\" font-weight:600;\">Cantidad de Entrenamientos</span></p></body></html>",
                                                         None))
        self.show_train_set_button.setText(_translate("MainWindow", "Muestra de Entrenamiento", None))
        self.show_membership_functions_button.setToolTip(_translate("MainWindow",
                                                                    "<html><head/><body><p><span style=\" font-weight:600;\">Miembros de la funcion creados por el entrenamiento</span></p></body></html>",
                                                                    None))
        self.show_membership_functions_button.setText(_translate("MainWindow", "Activacion de los Parametros", None))
        self.show_rules_button.setToolTip(_translate("MainWindow",
                                                     "<html><head/><body><p><span style=\" font-weight:600;\">Reglas creadas por el entrenamiento</span></p></body></html>",
                                                     None))
        self.show_rules_button.setText(_translate("MainWindow", "Reglas", None))
        self.browse_button.setToolTip(_translate("MainWindow",
                                                 "<html><head/><body><p><span style=\" font-weight:600;\">Seleccionar la base de datos usada para el entrenamiento</span></p></body></html>",
                                                 None))
        self.browse_button.setText(_translate("MainWindow", "Buscar", None))
        self.train_to_test_ratio_slider.setToolTip(_translate("MainWindow",
                                                              "<html><head/><body><p><span style=\" font-weight:600;\">Adjustar la serie de prueba de relacion</span></p></body></html>",
                                                              None))
        self.train_to_test_ratio_spinbox.setToolTip(_translate("MainWindow",
                                                               "<html><head/><body><p><span style=\" font-weight:600;\">Adjustar la serie de prueba de relacion</span></p></body></html>",
                                                               None))
        self.dataset_path_input.setToolTip(_translate("MainWindow",
                                                      "<html><head/><body><p><span style=\" font-weight:600;\">Conjunto de Datos</span></p></body></html>",
                                                      None))
        self.testing_section_label.setText(_translate("MainWindow", "Prueba", None))
        self.train_to_test_ratio_label.setText(_translate("MainWindow",
                                                          "<html><head/><body><p><span style=\" font-size:12pt;\">Cantidad de Entrenamiento</span></p></body></html>",
                                                          None))
        self.characteristics_label.setText(_translate("MainWindow",
                                                      "<html><head/><body><p><span style=\" font-size:12pt;\">Caracteristicas</span></p></body></html>",
                                                      None))
        self.training_section_label.setText(_translate("MainWindow", "Entrenamiento", None))


        self.classify_sample_button.setToolTip(_translate("MainWindow",
                                                          "<html><head/><body><p><span style=\" font-weight:600;\">Clasificar una muestra utilizando las entradas anteriores como parametros</span></p></body></html>",
                                                          None))
        self.classify_sample_button.setText(_translate("MainWindow", "Muestra", None))
        self.classify_test_set_button.setToolTip(_translate("MainWindow",
                                                            "<html><head/><body><p><span style=\" font-weight:600;\">Clasificar las muestras dentro del equipo de prueba</span></p></body></html>",
                                                            None))
        self.classify_test_set_button.setText(_translate("MainWindow", "Conjunto de Prueba", None))
        self.train_button.setToolTip(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-weight:600;\">Iniciar el Modelo de Entrenamiento</span></p></body></html>",
                                                None))
        self.train_button.setText(_translate("MainWindow", "Entrenamiento", None))
        self.juego_label.setText(_translate("MainWindow", "Genero de Videojuego", None))
        self.tipo_juego.setItemText(0, _translate("MainWindow", "Plataforma", None))
        self.tipo_juego.setItemText(1, _translate("MainWindow", "Calculo", None))
        self.tipo_juego.setItemText(2, _translate("MainWindow", "Deportivo", None))
        self.tipo_juego.setItemText(3, _translate("MainWindow", "Simulacion", None))
        self.tipo_juego.setItemText(4, _translate("MainWindow", "Disparos", None))
        self.tipo_juego.setItemText(5, _translate("MainWindow", "Pelea", None))
        self.parametro1_label.setText(_translate("MainWindow", "Parametro 1", None))
        self.parametro2_label.setText(_translate("MainWindow", "Parametro 2", None))
        self.parametro3_label.setText(_translate("MainWindow", "Parametro 3", None))
        self.parametro4_label.setText(_translate("MainWindow", "Parametro 4", None))

