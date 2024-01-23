# Proyecto Variables Python

#Definir una variable de cada tipo primitivo
es_int=31;
es_string="Carlos";
es_float=15.3758
es_boolean=True;
print(es_string)
print(es_boolean)
print(es_float)
print(es_int)

#Concatena a la cadena las otras variables aplicando la conversión correcta y guarda el resultado en una variables
es_concatenar=es_string+" tiene "+str(es_int)+" años, eso es "+str(es_boolean)
print(es_concatenar)


#Investigar sobre el limite de enteros y los flotantes
'''
De acuerdo con información buscada python presente una bondad la cual corresopnde 
a que los numeros enteros no presentan limite, sin embargo, los numeros tipo float
por el contrario si lo presentan dado que son numeros de 64 bits por lo anterior el
numero mas grande corresponde a 1.8e+308
'''

#Formula para la suma de N numeros
valor_n=6
inicio=0
for i in range (1,valor_n+1):
    if i!=0:
        if i%2==0:
            inicio=inicio+i
print("La suma de los n numeros pares contenidos en el rago de 0 a ",valor_n," es ",inicio)
    
        