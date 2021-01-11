from PyQt5 import QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Plot(QtWidgets.QMainWindow):

    def __init__(self, pos_x, pos_y, x_left, y_left, x_right, y_right, title=""):
        super(Plot, self).__init__()

        # Create the matplotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)

        # Plot the data
        #sc.axes.plot(x, y_left)
        sc.axes.scatter(x_left, y_left, label='Activacion hacia la Izquierda')
        sc.axes.scatter(x_right, y_right, label='Activacion hacia la Derecha')
        sc.axes.legend()
        sc.axes.grid(True)
        sc.axes.title.set_text(title)

        # Create toolbar, passing canvas as first parameter, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setWindowTitle(title)

        self.setGeometry(pos_x, pos_y, 640, 480)

        self.show()
