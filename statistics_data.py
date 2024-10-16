#Análisis estadístico de datos. 

import statistics
import csv

#Leer los datos de ventas mensuales desde un archivo csv
monthly_sales = {}
with open('monthly_sales.csv',mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales= list(monthly_sales.values())
print(sales)

#Hallar la media de datos
mean_sales = statistics.mean(sales)
print(f"La media es:{mean_sales}")

#Hallar la mediana de datos    
median_sales = statistics.median(sales)
print(f"La mediana es:{median_sales}")
#Hallar la moda de datos    
mode_sales = statistics.mode(sales)
print(f"La moda es:{mode_sales}")

#Desviacion estandar de datos
stdev_sales = statistics.stdev(sales)
print(f'La desviación estandar es:{stdev_sales}')

#Hallar la varianza de los datos
variance_sales= statistics.variance(sales)
print(f'La varianza es:{variance_sales}')

#Hallar el maximo y el minimo de los datos
max_sales = max(sales)
min_sales = min(sales)

range_sales = max_sales - min_sales
print(f'Rango de ventas:{range_sales}')


#Comprension de la estadistica de datos.Conocer la media,
#mediana, moda, varianza, rango, máximo, mínimo y desviación estándar 
# permite comprender mejor la distribución y variabilidad de un conjunto de datos. 
# La media ofrece el promedio general, la mediana señala el valor central y la moda identifica el valor más frecuente. 
# El rango, junto con los valores máximo y mínimo, muestra la amplitud de los datos.
#  La varianza y la desviación estándar revelan cuán dispersos están los datos respecto a la media, siendo la desviación estándar más útil por estar en las mismas unidades que los datos originales. 
# Esto ayuda a interpretar la consistencia o variabilidad dentro de un conjunto de datos, crucial para la toma de decisiones informadas.