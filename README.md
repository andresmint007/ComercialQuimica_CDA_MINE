# ComercialQuimica_CDA_MINE
Estrategia de datos para la empresa Comercial Quimica SA desarrollada por la universidad de los Andes para resolver la problematica del inventario y cumplimiento de presupuestos<br>
Estrategia elaborado por:<br>

Andrés Mauricio Martínez Celis &nbsp;  &nbsp; &nbsp;     202322624 <br>
Danilo Andrés Alfonso Bohórquez  &nbsp;      201611827 <br>
Jairo Vladimir Chaparro Rodríguez     201531080 <br>
Oscar Duvan Giraldo Romero  &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;  202324939   <br>  
Estructura de carpetas:<br>
Comercial Quimica <br>
├── EDA_proyecto_Comercial_Quimica.ipynb<br>
├── Primera Entrega Proyecto Comercial Química.pdf<br>
├── Segunda Entrega Proyecto Comercial Química.pdf<br>
├── Tercera Entrega Proyecto Comercial Química.pdf<br>
└── Proyecto Dashboard.pdf<br>
└── Mockup DashBoard CQ.png<br>
└── Series_Tiempo_1.ipynb<br>
└── Series_Tiempo_2.ipynb<br>
└── Diagrama de flujo Procesamiento.pdf<br>
└── Archivos<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── base_ventas.xlsx (No incluido, Material Sensible,Disponible en el enlace adjunto) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── COMPRAS 2023 Dashboard.xlsm (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Dataset_Operacion_Anual.csv (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── base_ventas.xlsx (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── BodegasSAP.xlsx (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── DatosCQ.xlsx (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── INFORMACION INVENTARIO Y VENTAS 22-09-2023.xlsx (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── INVENTARIO (CODIGO DE PRODCUTOS).xlsx (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── arima.csv (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>
└── Transformación de archivos<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── form.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── funcion_dashboard.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── LogoComercial.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── dax.py<br>


Los archivos con extension .pdf contienen la interpretacion del proyecto asi:
- Primera Entrega Proyecto Comercial Química: Contiene el desarrollo del taller, como se indicó en bloque Neon, asi como la interpretación de datos de este Notebook.
- El Mockup del dashboard a construir no se incluyo en el documento pero es la imagen Mockup DashBoard CQ.png para que la pueda detallar

Para el Notebook EDA_proyecto_Comercial_Quimica.ipynb, este carga los 3 archivos de la carpeta Archivos, de los dos documentos tipo excel solo se cargan las hojas DATOS VENTAS de el archivo COMPRAS 2023 Dashboard.xlsm y base_ajustada de el archivo base_ventas.xlsx

El cuaderno contiene dos funciones dinámicas las cuales miden el comportamiento de los medicamentos en el tiempo, como su popularidad también, estos son: <br>

_getSeriesByMaterial(material, anio)_<br>
_graphPareto (material,anio)_

Uso:La primera mira el comportamiento de ventas de un material según el año, y la segunda los materiales más vendidos en un año, la segunda es automática y no requiere modificación, la primera si puede variar según el medicamento que usted quiera enviar.

Los archivos se pueden descargar en: https://uniandes-my.sharepoint.com/:f:/g/personal/am_martinezc123_uniandes_edu_co/Eo7U36SUOxZKlAbPiBtc-gsB2CKVGKzjya6Y-U5CyyX_6g?e=Bzooiq

__NOTA__: Solo el docente del curso tiene acceso a estos archivos, guardelos en la carpeta Archivos una vez clone o descargue el Repositorio.

# Segunda Entrega:
El archivo Segunda Entrega Proyecto Comercial Química.pdf tiene toda la informacion requerida para la entrega 2 de este proyecto, da inicio desde el apendice 8, ahi encuentran toda la información de esta entrega
Se incluye una muestra del dashboard construido en la etapa preliminar con el acceso a datos necesarios para demostrar un demo en formato PDF 
Los archivos agregados en esta entrega se dividen en dos partes, el procesamiento y los entrenamientos del modelo, los cuadernos se listan a continuación:
- Procesamiento.ipnyb: Este cuaderno tiene el procesamiento de los datos del archivo, es decir es la entrada de los archivos al proceso y mejora de datos, la salida de este cuaderno es un archivo de excel que tiene los datos estandarizados listos para el entrenamiento.
- Series_Tiempo_1.ipynb: Este cuaderno tiene entrenamiento de modelos ARIMA, SARIMA, ARMA, XGBOOST y mas todos estos modelos son de aplicacion diaria, es decir que no se agrupa la informacion si no se usa la informacion diaria. Al final se encuentran las descripciones de cada modelo y se usa el csv Arima para el proceso.
- Series_Tiempo_2.ipynb: Este cuaderno tiene entrenamiento de modelos VAR, ExponentialSmoothin, ARMA y regresión lineal (Base line) Finalmente, se llevan a cabo dos modelos de regresión lineal con y sin ventanas deslizantes para crear el modelo baseline; estas revisiones son mes a mes, se consolidan los modelos usando los meses de ventas y cantidades agrupadas por esa categoría de fecha, con sus conclusiones y revisiones de errores.

Los modelos anteriormente evaluados suman 11, dentro de los dos cuadernos; cada modelo tiene una conclusión.

# Tercera Entrega:

A continuación se listan los archivos y entregables relacionados con la última entrega del proyecto:

Sobre el documento se encuentra los siguientes apartados:
- Construcción de productos de datos: Estructura del dashboard con información sobre bodegas, proveedores, país de importación, evolución mensual, ventas, cantidades, precio promedio e índice de rotación.
- Despliegue de la solución de la manera local: 
- Despliegue de la solución en un proveedor de nube: Detalles del flujo de trabajo desde Dataiku hasta Power BI, explicando la integración con Google Cloud Platform, el diagrama de arquitectura se detalla el flujo de datos y la solución ofrecida con GCP para entregar el Power BI.
- Retroalimentación por parte de la organización: Descripción detallada de las interacciones clave con el cliente, desde el establecimiento del canal de comunicación hasta la entrega final.
- Conclusiones del proyecto: Resumen de las etapas del proyecto, incluyendo la identificación de un error en el modelo, ajustes sugeridos y la conclusión del proyecto el 24 de noviembre.

Adicional se cuentan con los siguientes archivos indispensables para la solución:
- Arquitectura.jpg: Arquitectura sobre draw.io donde se puede visualizar el flujo de conexión de los agentes externos con el proveedor de nube.
- Tutorial Integracion Google Cloud Plataform.pdf: Sustento del despliegue en  la nube de la solución y paso a paso de la integración para la organización del Dashboard
- Dashboard.pbix: Los datos sensibles los encontrará en el siguiente link donde únicamente tendrá acceso el docente, es el link de los archivos de la parte superior del dashboard.

Transformación de archivos (carpeta):
- Funciones DAX con Power BI (dax.py)
- Scripts y formulario de transformación de datos: Exporta un archivo de Excel adecuado para la toma de datos desde el Power BI.(Todos los archivos de la carpeta excepto dax.py)

Contacto: jv.chaparro@uniandes.edu.co, o.giraldor@uniandes.edu.co, da.alfonso2@uniandes.edu.co,am.martinezc123@unaindes.edu.co
