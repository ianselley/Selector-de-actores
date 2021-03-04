import pandas as pd
from pandas.core.frame import DataFrame
pd.options.display.max_rows = None
pd.options.display.max_columns = None

Actores = 'actores'
NombreArchivo = f'Base_de_datos_{Actores}.ods'
df_rows = pd.read_excel(NombreArchivo) #, index_col=0
df_rows2 = pd.read_excel(NombreArchivo, skiprows=range(0,1))

rows = df_rows.values.tolist()
df_cols = df_rows.T
cols = df_cols.values.tolist()

rows2 = df_rows2.values.tolist()
df_cols2 = df_rows2.T
cols2 = df_cols2.values.tolist()

# Defino la función para averiguar la columna que quiere elegir
def col_of_list(lis, print1, print2):
    i = ''
    n = 0
    col_eleg_l = 'a' # str cualquiera diferente de i
    while col_eleg_l != i.lower():
        if n >=1:
            print('\nOPCIÓN NO VÁLIDA')
        print(print1)
        for caracteristica in lis[:-1]:
            print(caracteristica, end=", ")
        print(lis[-1])
        columna_elegida = input(print2)
        col_eleg_l = columna_elegida.lower()
        for i in lis:
            if col_eleg_l.lower() == i.lower():
                break
        n += 1
    columna = lis.index(i)
    return columna, col_eleg_l

repetir = 's'
lista_de_columnas_elegidas = [0, 2, 4]
while repetir == 's':
    # Uso la función
    columna, col_eleg_l = col_of_list(rows[0], '\nDe estas características:',
                                    '\n¿Qué característica quieres elegir?: ')
    if columna not in lista_de_columnas_elegidas: 
        lista_de_columnas_elegidas.append(columna)

    # Especifico para cuando escoge edad o altura, porque son números
    if col_eleg_l == 'edad' or col_eleg_l == 'estatura' or col_eleg_l == 'numero de actor':
        obj1 = float(input(f'\n¿Qué {col_eleg_l} mínima tiene la persona que buscas? (Decimales con punto y sin uds): '))
        obj2 = float(input(f'¿Qué {col_eleg_l} máxima tiene la persona que buscas? (Decimales con punto y sin uds): '))
        if obj1 > obj2:
            obj1, obj2 = obj2, obj1
        n2 = 1
        n1 = 0
        for i2 in cols2[columna]:
            if obj1 > i2 or i2 > obj2:
                rows.pop(n2-n1) # Quitar la fila que no cumpla el requisito
                rows2.pop(n2-n1-1)
                n1 += 1
            n2 += 1

    # Especifico para cuando escoge las demás que no son números
    obj = 'a' # str cualquiera diferente de i
    if col_eleg_l == 'edad' or col_eleg_l == 'estatura' or col_eleg_l == 'numero de actor':
        pass
    else:
        while obj.lower() not in [elementos.lower() for elementos in cols2[columna]]:
            if col_eleg_l == 'sexo':
                obj = input(f'¿A qué {col_eleg_l} pertenece la persona que buscas?: ')
            elif col_eleg_l == 'ciudad':
                obj = input(f'¿En qué {col_eleg_l} vive la persona que buscas?: ')
            elif col_eleg_l == 'idiomas':
                obj = input(f'¿Qué {col_eleg_l} sabe la persona que buscas?: ')
            elif col_eleg_l == 'carnet de conducir':
                obj = input(f'¿Tiene {col_eleg_l} la persona que buscas?: ')
            else:
                obj = input(f'¿Qué {col_eleg_l} tiene la persona que buscas?: ')

        n4 = 1
        n3 = 0
        for i3 in cols2[columna]:
            if obj.lower() != i3.lower():
                rows.pop(n4-n3) # Quitar la fila que no cumpla el requisito
                rows2.pop(n4-n3-1)
                n3 += 1
            n4 += 1
        
    df_rows = DataFrame(rows)
    lista_de_columnas_elegidas = sorted(lista_de_columnas_elegidas) #ordena las columnas del dataframe
    print(df_rows[lista_de_columnas_elegidas])

    cols = DataFrame(rows).T.values.tolist()
    cols2 = DataFrame(rows2).T.values.tolist()

    repetir = input('\nQuieres repetir el proceso para reducir la selección? (S/N): ').lower()
    while repetir != 's' and repetir != 'n':
        repetir = input('\nQuieres repetir el proceso para reducir la selección? (S/N): ').lower()
    
retirada_manual = input('\nQuieres retirar algún actor de esta lista de forma manual? (S/N): ').lower()
while retirada_manual == 's':
    while retirada_manual != 's' and retirada_manual != 'n':
        retirada_manual = input('\nQuieres retirar algún actor de esta lista de forma manual? (S/N): ').lower()

    if retirada_manual == 's':
        while True:
            num_actor_a_quitar = int(input('\nEl actor que quieres eliminar, ¿qué número ocupa en la lista?: '))
            if num_actor_a_quitar == 0:
                print('El 0 quitaría el título, elige otro número (el 1 es el primero)')
            elif num_actor_a_quitar <= len(cols2[0]):
                break
        rows.pop(num_actor_a_quitar)
        df_rows = DataFrame(rows)
        print(df_rows[lista_de_columnas_elegidas])
        
    retirada_manual = input('\nQuieres retirar algún actor de esta lista de forma manual? (S/N): ').lower()
