import pandas as pd
import matplotlib.pyplot as plt

# Clase para manejar datos desde Excel
class ExcelData:
    def __init__(self, archivo, hoja):
        self.archivo = archivo
        self.hoja = hoja
        self.data = None

    def leer_datos(self):
        """Lee los datos del archivo Excel con pandas"""
        self.data = pd.read_excel(self.archivo, sheet_name=self.hoja)
        return self.data


# Clase para graficar usando matplotlib
class Graficador:
    def __init__(self, datos):
        self.datos = datos

    def grafico_lineas(self):
        """Crea un gráfico de líneas con los datos"""
        plt.figure(figsize=(8, 5))
        plt.plot(self.datos["Mes"], self.datos["Ventas"], marker="o", label="Ventas")
        plt.plot(self.datos["Mes"], self.datos["Gastos"], marker="s", label="Gastos")
        plt.title("Ventas vs Gastos")
        plt.xlabel("Mes")
        plt.ylabel("Monto en $")
        plt.legend()
        plt.grid(True)
        plt.savefig("grafico_lineas1.png")

    def grafico_barras(self):
        """Crea un gráfico de barras con los datos"""
        plt.figure(figsize=(8, 5))
        plt.bar(self.datos["Mes"], self.datos["Ventas"], label="Ventas", alpha=0.7)
        plt.bar(self.datos["Mes"], self.datos["Gastos"], label="Gastos", alpha=0.7)
        plt.title("Comparación de Ventas y Gastos")
        plt.xlabel("Mes")
        plt.ylabel("Monto en $")
        plt.legend()
        plt.savefig("grafico_lineas2.png")


    def grafico_pie(self):
        """Crea un gráfico de torta con el total de ventas por mes"""
        plt.figure(figsize=(6, 6))
        plt.pie(self.datos["Ventas"], labels=self.datos["Mes"], autopct="%1.1f%%", startangle=90)
        plt.title("Distribución de Ventas")
        plt.savefig("grafico_lineas3.png")



# Programa principal
if __name__ == "__main__":
    # 1. Leer datos del archivo Excel
    lector = ExcelData("datos.xlsx", "Ventas")
    datos = lector.leer_datos()

    # 2. Crear objeto graficador
    graficador = Graficador(datos)

    # 3. Mostrar gráficos
    graficador.grafico_lineas()
    graficador.grafico_barras()
    graficador.grafico_pie()


