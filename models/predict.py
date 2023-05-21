from config import *
from flask import jsonify, request
import psycopg2
import pandas as pd
import numpy as np
from matplotlib import pyplot as pyplot
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from pickle import GLOBAL

class Predict():

    def m_predict(self):
        try:

            console = int(request.json['console'])
            gender = int(request.json['gender'])
            publisher = int(request.json['publisher'])

            ## Conexión a la base de datos
            conn = psycopg2.connect(host='db.erfxswbdagjrxdnkimsd.supabase.co', database='postgres', port=5432, user='postgres', password='mineria2023.com')
            df_Principal = pd.read_sql('SELECT * FROM "tblGames"', conn)
            f_absoluta_sv = pd.value_counts(df_Principal['Console'])
            f_relativa_sv = 100 * df_Principal['Console'].value_counts() / len(df_Principal['Console'])
            grafica_1_sv = df_Principal['Console'].value_counts().plot(kind='bar', title ='Console')
            grafico_2_sv = df_Principal['Console'].value_counts().plot(kind = 'pie', autopct = '%.2f' , figsize = (6,6), title = 'Consola').legend(loc='upper left')
            media_ev = df_Principal['Global'].mean()
            mediana_ev = df_Principal['Global'].median()
            maximo_ev = max(df_Principal['Global'])
            min_ev = min(df_Principal['Global'])
            histograma_mv = pyplot.hist(x = df_Principal['Global'], color = "#f2ab60", rwidth = 0.95)
            pyplot.xlabel("Global")
            pyplot.ylabel("Cantidad")
            histograma_mv
            bigotes_mv = pyplot.boxplot(x = df_Principal['Global'])
            pyplot.xlabel("Global")
            pyplot.ylabel("Cantidad")
            bigotes_mv
            Q1 = df_Principal['Global'].quantile(0.25)
            print("Primer Cuartil", Q1)

            Q3 = df_Principal['Global'].quantile(0.75)
            print("Tercer Cuartil", Q3)

            IQR = Q3 - Q1
            print("Rango Intercuartil", IQR)

            Mediana = df_Principal['Global'].median()
            print("Mediana", Mediana)

            Valor_Miniom = df_Principal['Global'].min()
            print("Valor Minimo", Valor_Miniom)

            Valor_Maximo = df_Principal['Global'].max()
            print("Valor Máximo", Valor_Maximo)

            BI_Calculado = (Q1 - 1.5 * IQR)
            print("BI_CALCULADO \n", BI_Calculado)

            BS_Calculado = (Q3 + 1.5 * IQR)
            print("BS_CALCULADO \n", BS_Calculado)

            ubicacion_outliers = ((df_Principal['Global'] < BI_Calculado) | (df_Principal['Global'] > BS_Calculado))
            print("\n Ubicacion de Outliers \n", ubicacion_outliers)
            outliers = df_Principal[ubicacion_outliers]
            print("\n Lista de Outliers \n", outliers)

            Outliers_Ordenados = outliers.sort_values("Global")
            Outliers_Ordenados
            Ubicacion_sin_out = ((df_Principal['Global'] >= BI_Calculado) & (df_Principal['Global'] <= BS_Calculado))
            sin_outliers = df_Principal[Ubicacion_sin_out]
            sin_outliers
            bigotes_mv = pyplot.boxplot(x = sin_outliers['Global'])
            pyplot.xlabel("Global")
            pyplot.ylabel("Cantidad")
            bigotes_mv
            Q1 = sin_outliers['Global'].quantile(0.25)
            print("Primer Cuartil", Q1)

            Q3 = sin_outliers['Global'].quantile(0.75)
            print("Tercer Cuartil", Q3)

            IQR = Q3 - Q1
            print("Rango Intercuartil", IQR)

            Mediana = sin_outliers['Global'].median()
            print("Mediana", Mediana)

            Valor_Miniom = sin_outliers['Global'].min()
            print("Valor Minimo", Valor_Miniom)

            Valor_Maximo = sin_outliers['Global'].max()
            print("Valor Máximo", Valor_Maximo)
            BI_Calculado = (Q1 - 1.5 * IQR)
            print("BI_CALCULADO \n", BI_Calculado)

            BS_Calculado = (Q3 + 1.5 * IQR)
            print("BS_CALCULADO \n", BS_Calculado)

            ubicacion_outliers = ((sin_outliers['Global'] < BI_Calculado) | (sin_outliers['Global'] > BS_Calculado))
            print("\n Ubicacion de Outliers \n", ubicacion_outliers)

            outliers = sin_outliers[ubicacion_outliers]
            print("\n Lista de Outliers \n", outliers)

            Outliers_Ordenados = outliers.sort_values("Global")
            Outliers_Ordenados

            Ubicacion_sin_out = ((sin_outliers['Global'] >= BI_Calculado) & (sin_outliers['Global'] <= BS_Calculado))
            sin_outliers_2 = sin_outliers[Ubicacion_sin_out]
            sin_outliers_2

            bigotes_mv = pyplot.boxplot(x = sin_outliers_2['Global'])
            pyplot.xlabel("Global")
            pyplot.ylabel("Cantidad")
            bigotes_mv

            Q1 = sin_outliers_2['Global'].quantile(0.25)
            print("Primer Cuartil", Q1)

            Q3 = sin_outliers_2['Global'].quantile(0.75)
            print("Tercer Cuartil", Q3)

            IQR = Q3 - Q1
            print("Rango Intercuartil", IQR)

            Mediana = sin_outliers_2['Global'].median()
            print("Mediana", Mediana)

            Valor_Miniom = sin_outliers_2['Global'].min()
            print("Valor Minimo", Valor_Miniom)

            Valor_Maximo = sin_outliers_2['Global'].max()
            print("Valor Máximo", Valor_Maximo)

            BI_Calculado = (Q1 - 1.5 * IQR)
            print("BI_CALCULADO \n", BI_Calculado)

            BS_Calculado = (Q3 + 1.5 * IQR)
            print("BS_CALCULADO \n", BS_Calculado)

            ubicacion_outliers_2 = ((sin_outliers_2['Global'] < BI_Calculado) | (sin_outliers_2['Global'] > BS_Calculado))
            outliers_2 = sin_outliers_2[ubicacion_outliers_2]
            Outliers_Ordenados_2 = outliers_2.sort_values("Global")
            Ubicacion_sin_out_2 = ((sin_outliers_2['Global'] >= BI_Calculado) & (sin_outliers_2['Global'] <= BS_Calculado))
            sin_outliers_3 = sin_outliers_2[Ubicacion_sin_out_2]
            sin_outliers_3
            bigotes_mv = pyplot.boxplot(x = sin_outliers_3['Global'])
            pyplot.xlabel("Global")
            pyplot.ylabel("Cantidad")
            bigotes_mv

            range_global = [-1, 5, 10, 15, 20]
            df_Principal['Range Global'] = pd.cut(df_Principal['Global'], range_global)
            print(df_Principal)

            # Seleccionar la columna que se desea convertir
            genero = 'Genre'
            empresa = 'Publisher'
            console = 'Console'
            range = 'Range Global'
            # Crear un objeto LabelEncoder
            encoder = LabelEncoder()

            # Ajustar y transformar la columna de texto en valores numéricos categorizados
            df_Principal[console + '_numerico'] = encoder.fit_transform(df_Principal[console])
            df_Principal[genero + '_numerico'] = encoder.fit_transform(df_Principal[genero])
            df_Principal[empresa + '_numerico'] = encoder.fit_transform(df_Principal[empresa])
            df_Principal['Range' + '_numerico'] = encoder.fit_transform(df_Principal[range])

            df_data = pd.DataFrame(df_Principal[['Console_numerico', 'Genre_numerico', 'Publisher_numerico', 'Range_numerico']])
            X = df_data.drop(["Range_numerico"],axis = 1)
            y = df_data['Range_numerico']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)
            clf = GaussianNB()
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)
            y_pred = clf.predict(X_test)
            print(X_test)
            # Calcular la precisión del modelo
            accuracy = accuracy_score(y_test, y_pred)
            print("Precisión: {:.2f}".format(accuracy))

            data_predict = {
                'Console_numerico':[0],
                'Genre_numerico':[0],
                'Publisher_numerico':[116]
                }

            df_predict = pd.DataFrame(data=data_predict)
            Z_pred = clf.predict(df_predict)

            if (Z_pred == 0):
                response = '0 a 5'
            elif (Z_pred == 1):
                response = '5 a 10'
            elif (Z_pred == 2):
                response = '10 a 15'
            else:
                response = '15 a 20'
            print(Z_pred)
            print(response)
            return jsonify({'answer':response})
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'information':error})