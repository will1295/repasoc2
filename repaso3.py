import sys
import pandas as pd
from PyQt5.QtWidgets import(QApplication,QMainWindow,QWidget,
                            QVBoxLayout,QLabel)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grafico con matplotlib")
        self.resize(600,400)

        df = pd.read_csv('inventario.csv')
        df_agrupado = df.groupby("Sucursal")["Stock"].sum()
        self.figura = Figure(figsize=(5,3))
        self.canvas = FigureCanvas(self.figura)
        ax = self.figura.add_subplot(111)
        ax.set_title("Stocks por sucursal")
        ax.bar(df_agrupado.index,df_agrupado.values,color="blue")
        ax.set_xlabel("Sucursales")
        ax.set_ylabel("Stock")
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
sys.exit(app.exec_())
