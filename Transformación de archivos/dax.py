
import pandas as pd
import pylev

ciudades = [
    'BOGOTA', 'ITAGUI', 'TOLIMA', 'TOCANCIPA', 'MEDELLIN',
    'ENVIGADO', 'YUMBO', 'SABANETA', 'GIRON', 'COTA', 'JAMUNDI',
    'CUNDINAMARCA', 'CARTAGENA', 'ZIPAQUIRA', 'CALI', 'FUNZA',
    'IPIALES', 'SAN PEDRO (Valle del Cauca)', 'SOPO', 'BUGA', 'CHIA',
    'BUCARAMANGA', 'FLORIDABLANCA', 'VALLE','SAN PEDRO', 'SANTANDER', 'IBAGUE', 'ANTIOQUIA',
    'RIONEGRO', 'BARRANQUILLA', 'PEREIRA', 'LA ESTRELLA', 'TOCANCIPA',
    'FUSAGASUGA', 'FLORIDABLANCA', 'GUARNE', 'TENJO',
    'CUCUTA', 'ESPINAL', 'MOSQUERA', 'TURBO', 'CUENCA',
    'VILLAVICENCIO', 'SANTA MARTA', 'SINCELEJO', 'MISTRATO',
    'PAMPLONA', 'BUENAVENTURA', 'ARMENIA (Quindio)', 'POPAYAN',
    'CARACAS', 'YOPAL', 'SOACHA', 'LA CAPILLA', 'VELEZ', 'PALMIRA',
    'BELTRAN', 'MANIZALES'
]

def procesarArchivo():
    datos = pd.DataFrame(ventas)
    datos = datos.rename(columns={'Nombre de cliente/proveedor': 'nombre_cliente'})
    datos = datos.rename(columns={'LOTE': 'Lote'})
    datos = datos.rename(columns={'Descripción artículo/serv.': 'Descripción del artículo'})
    datosCompletos=pd.DataFrame( base)
    datos = datos[~datos['Descripción del artículo'].str.contains('SALDOS INICIAL')]

    dfActulizado=completar_ciudad(datos,datosCompletos)
    dfActulizado.loc[dfActulizado['nombre_cliente'] == 'SITUANDO SAS', 'Ciudad'] = 'BOGOTÁ'
    dfActulizado.loc[dfActulizado['nombre_cliente'] == 'LABORATORIOS BIOSINFAR S.A.S', 'Ciudad'] = 'BOGOTÁ'

    for index, row in dfActulizado.iterrows():
        if row["Ciudad"] not in ciudades:
            citycorrect= getbestCity(row["Ciudad"])
            dfActulizado.loc[index, "Ciudad"] = citycorrect
            
    inventarioFile=pd.DataFrame(inve)
    filterDF=['Número de artículo','Descripción del artículo','Lote','Atributo de lote 2','Fecha de vencimiento','Fecha de fabricación']
    InventarioFilter=inventarioFile[filterDF]
    InventarioFilter = InventarioFilter.drop_duplicates(subset=['Descripción del artículo', 'Lote'])
    dfFinalTodo=pd.merge(dfActulizado, InventarioFilter, on=['Lote', 'Descripción del artículo'], how='left')
    cruza_data = dfFinalTodo.dropna(subset=['Número de artículo'])
    noCruza_data = dfFinalTodo[dfFinalTodo['Número de artículo'].isnull()]
    noCruza_data = noCruza_data.drop(['Número de artículo','Lote','Atributo de lote 2','Fecha de vencimiento','Fecha de fabricación'],axis=1)
    InventarioonlDescrip=InventarioFilter.drop_duplicates(subset=['Descripción del artículo'])
    dfsinlote=pd.merge(noCruza_data, InventarioonlDescrip, on='Descripción del artículo', how='inner')
    resultFinal = pd.concat([cruza_data, dfsinlote])
    resultFinal["DecripcionLote"] = resultFinal["Descripción del artículo"].str.strip() + resultFinal["Lote"].astype(str).str.strip()
    bodegas= pd.DataFrame(bodegasSapA)
    finalProcesoCQ=pd.merge(resultFinal, bodegas, on=['DecripcionLote'], how='inner')
    
    finalProcesoCQ['Cantidad'] = finalProcesoCQ['Cantidad'].astype('int64')
    finalProcesoCQ['Precio Unitario'] = finalProcesoCQ['Precio Unitario'].astype('int64')
    finalProcesoCQ['Total líneas'] = finalProcesoCQ['Total líneas'].astype('int64')
    finalProcesoCQ['Cantidad'] = pd.to_numeric(finalProcesoCQ['Cantidad'], errors='coerce')
    finalProcesoCQ['Precio Unitario'] = pd.to_numeric(finalProcesoCQ['Precio Unitario'], errors='coerce')
    finalProcesoCQ['calculo_total_lineas'] = finalProcesoCQ['Cantidad'] * finalProcesoCQ['Precio Unitario']
    finalProcesoCQ['diferencia_total_lineas'] = finalProcesoCQ['Total líneas'] - finalProcesoCQ['calculo_total_lineas']
    finalProcesoCQ['porcentaje_diferencia'] = (finalProcesoCQ['diferencia_total_lineas'] / finalProcesoCQ['Total líneas']) * 100
    finalProcesoCQ['coincide'] = finalProcesoCQ['Total líneas'] == finalProcesoCQ['calculo_total_lineas']
    finalProcesoCQ = finalProcesoCQ.drop(columns=['diferencia_total_lineas','porcentaje_diferencia','coincide','Total líneas'])
    data=finalProcesoCQ
    return data


def completar_ciudad(df_principal, df_secundario):
    for index, row in df_principal.iterrows():
        if pd.isnull(row['Ciudad']):  # Verificar si el campo "ciudad" está vacío
            nombre_cliente = row['nombre_cliente']
            filtro = df_secundario.loc[df_secundario['nombre_cliente'] == nombre_cliente, 'ciudad']
            ciudad_alternativa = filtro.iloc[0] if not filtro.empty else 'NA'
            df_principal.at[index, 'Ciudad'] = ciudad_alternativa
    return df_principal

def getbestCity(ciudad):
    best_correction = None
    best_distance = float('inf')
    for correct_city in ciudades:
            distance = pylev.levenshtein(ciudad, correct_city)
            if distance < best_distance:
                best_distance = distance
                best_correction = correct_city
    return best_correction

data=procesarArchivo()
data
