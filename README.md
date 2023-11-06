# ComercialQuimica_CDA_MINE
Estrategia de datos para la empresa Comercial Quimica SA desarrollada por la universidad de los Andes para resolver la problematica del inventario y cumplimiento de presupuestos<br>
Estrategia elebaorada por:<br>

Andrés Mauricio Martínez Celis &nbsp;  &nbsp; &nbsp;     202322624 <br>
Danilo Andrés Alfonso Bohórquez  &nbsp;      201611827 <br>
Jairo Vladimir Chaparro Rodríguez     201531080 <br>
Oscar Duvan Giraldo Romero  &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;  202324939   <br>  
Estructura de carpetas:<br>
Comercial Quimica <br>
├── EDA_proyecto_Comercial_Quimica.ipynb<br>
├── Primera Entrega Proyecto Comercial Química.pdf<br>
└── Mockup DashBoard CQ.png<br>
└── Archivos<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── base_ventas.xlsx (No incluido, Material Sensible,Disponible en el enlace adjunto) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── COMPRAS 2023 Dashboard.xlsm (No incluido, Material Sensible,Disponible en el enlace adjunto)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Dataset_Operacion_Anual.csv (No incluido, Material Sensible,Disponible en el enlace adjunto)

Los archivos con extension .pdf contienen la interpretacion del proyecto asi:
- Primera Entrega Proyecto Comercial Química: Contiene el desarrollo del taller, como se indicó en bloque Neon, asi como la interpretación de datos de este Notebook.
- El Mockup del dashboard a construir no se incluyo en el documento pero es la imagen Mockup DashBoard CQ.png para que la pueda detallar

Para el Notebook EDA_proyecto_Comercial_Quimica.ipynb, este carga los 3 archivos de la carpeta Archivos, de los dos documentos tipo excel solo se cargan las hojas DATOS VENTAS de el archivo COMPRAS 2023 Dashboard.xlsm y base_ajustada de el archivo base_ventas.xlsx

El cuaderno contiene dos funciones dinámicas las cuales miden el comportamiento de los medicamentos en el tiempo, como su popularidad también, estos son: <br>

_getSeriesByMaterial(material, anio_<br>
_graphPareto (material,anio)_

Uso:La primera mira el comportamiento de ventas de un material según el año, y la segunda los materiales más vendidos en un año, la segunda es automática y no requiere modificación, la primera si puede variar según el medicamento que usted quiera enviar.

Los archivos se pueden descargar en: https://uniandes-my.sharepoint.com/:f:/g/personal/am_martinezc123_uniandes_edu_co/Eo7U36SUOxZKlAbPiBtc-gsB2CKVGKzjya6Y-U5CyyX_6g?e=Bzooiq

__NOTA__: Solo el docente del curso tiene acceso a estos archivos, guardelos en la carpeta Archivos una vez clone o descargue el Repositorio.

# Segunda Entrega:
Los archivos agregados en esta entrega se dividen en dos partes, el procesamiento y los entrenamientos del modelo, los cuadernos se listan a continuación:
- Procesamiento.ipnyb: Este cuaderno tiene el procesamiento de los datos del archivo, es decir es la entrada de los archivos al proceso y mejora de daots, la salida de este cuaderno es un archivo de excel que tiene los datos estandarizados listos para el entrenamiento.
- Series_Tiempo_2.ipynb: Este cuaderno tiene entrenamiento de modelos VAR,ExponentialSmoothin,ARMA y regresión lineal (Base line)Finalmente, se llevan a cabo dos modelos de regresión lineal con y sin ventanas deslizantes para crear el modelo baseline;estas revisiones son mes a mes, se consolidan los modelos usando los meses de ventas y cantidades agrupadas por esa categoría de fecha, con sus conclusiones y revisiones de errores.

Contacto: jv.chaparro@uniandes.edu.co, o.giraldor@uniandes.edu.co, da.alfonso2@uniandes.edu.co,am.martinezc123@unaindes.edu.co
