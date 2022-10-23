
# Amazon Reviews Data Pipeline, Analytics and Machine Learning 

<div align="center">
    <img src="img\skaivuinsightslogo.png" alt="Project Screenshot" width="80%">
</div>
<br>

## **Contenido:**

1. Descripción general del proyecto
2. Equipo de trabajo
3. Metodología de trabajo
4. Objetivo General
5. Descripción y diccionario de los datos originales
6. EDA
7. Solución: Data Pipeline
8. Diccionario de los datos - Data Analytics 

## **Descripción general del proyecto**

La compañía Amazon contrataron los servicios de ingeniería y análisis de datos de la empresa Skaivu Insights con el objetivo de apoyar el desarrollo de nuevas perspectivas para mejorar ventas y experiencia al usuario.

La empresa se encargó de almacenar, transformar, estructurar, analizar y modelar la información proporcionada para crear un reporte de inteligencia empresarial, y adicionalmente un sistema automático de recomendación de productos relevantes, basado en la información de opiniones provenientes de otros usuarios.

## Equipo de Trabajo

Skaivu Insights consta con un grupo de profesionales en diferentes áreas que estarán encargados del desarrollo del proyecto. El equipo de trabajo asignado a este proyecto estará conformado por: 

* [Ingmar Orta](https://www.linkedin.com/in/ingmarorta/) - Data Scientist ( _Project Manager_ )
* [Tomás Astrada](https://www.linkedin.com/in/tom%C3%A1s-astrada-370b73171/) - Data Engineer
* [Jean Fabra](https://www.linkedin.com/in/jeanfabra/) - Data Engineer 
* [Jorge Fonseca](https://www.linkedin.com/in/jorge-fonseca-alba-83433b117/) - Data Scientist 
* [Daniela Hugueth](https://www.linkedin.com/in/dhugueth/) - Data Analytic

## **Metodología de trabajo**

<div align="center">
    <img src="img\agilemetodology.png" alt="Project Screenshot" width="100%">
</div>
<br>

Se utilizó un método de trabajo ágil con enfoque en la metodología de gestión de proyectos Kanban utilizando el software de administración de proyectos [Trello](https://trello.com/en), en donde los integrantes del proyecto dividimos y asignamos las actividades a realizar y manteníamos un seguimiento a todo el proyecto.

La unión de estas metodologías ofreció:

* Gestión de trabajo colaborativo
* Resoluciones rápidas y efectivas
* Visualización del flujo de trabajo
* Simplicidad

## **Objetivo General**

Realizar un análisis de reseñas y ventas de productos a partir de la información proporcionada por el cliente Amazon, así, extraer información objetiva y concisa de indicadores claves de desempeño e idear un sistema de recomendaciones de productos. 

## **Descripción y diccionario de los datos originales**

<div align="center">
    <img src="img\amazonreviews.png" alt="Project Screenshot" width="50%">
</div>
<br>

Se recibieron 24 tablas con datos de reviewes hecho por clientes sobre artículos comprados en su tienda virtual, una (1) tabla por categoría de producto, y una tabla de metadata con informacion de los producto ofrecidos en la plataforma.

* El rango de fecha presente en las tablas de reviews data desde 1996 hasta 2014
* Se poseen alrededor de 20gb con un total de 17 millones de reviews
* 10 gb de metadata  

**Nombre de las categorías:**

            Books
            Electronics
            Movies and TV
            CD and Vinyl
            Clothing
            Shoes and Jewelry
            Home and Kitchen
            Kindle Store
            Sports and Outdoors
            Cell Phones and Accessories
            Health and Personal Care
            Toys and Games
            Video Games
            Tools and Home Improvment
            Beauty
            Apps for Android
            Office Products
            Office Products
            Pet Supplies
            Automotive
            Grocery and Gourmet Food
            Patio
            Lawn and Garden
            Baby
            Digital Music
            Musical Instruments
            Amazon Instant Video
            
**Diccionario de los datos originales**

### **Reseñas**

            reviewerID      --->    ID del usuario, ejemplo: A2SUAM1J3GNN3B
            asin            --->    ID del producto, ejemplo: 0000013714
            reviewerName    --->    nombre del usuario
            helpful         --->    Puntaje de utilidad de la reseña (votos externos), e.g. 2/3
            reviewText      --->    Texto de la reseña
            overall         --->    Puntaje dado al producto
            summary         --->    Resumen de la reseña
            unixReviewTime  --->    Fecha de la reseña (unix time)
            reviewTime      --->    Fecha de la reseña


### **Metadata**

            asin            --->    ID del producto, ejemplo: 0000031852
            title           --->    Nombre del producto
            price           --->    Precio en dólares
            imUrl           --->    URL de la imagen del producto
            related         --->    Productos relacionados (comprados juntos, también revisados, comprados por el mismo usuario, comprados luego de verlos)
            salesRank       --->    Información sobre cómo rankea en ventas
            brand           --->    Nombre de la marca del producto
            categories      --->    Lista de la categoría a la que pertenece el producto.

***La gran cantidad de volumen y variedad de dato son indicativos para emplear herramientas de Big Data***

## **EDA**

Se realizo un análisis exploratorio no gráfico de los datos originales para describir los datos, encontrar los patrones que existen en ellos e Identificar valores atípicos. El análisis se realizó en el entorno de trabajo colaborativo Apache Spark de [Azure Databricks](https://azure.microsoft.com/en-us/products/databricks/) por la facilidad que nos daba para manejas grandes cantidades de datos. 

Las observaciones y características resultantes del análisis son las siguientes:
 
 ### **Reseñas**

***reviewerID :***
* Tipo de dato "string" alfanumérico.
* No presenta valores faltantes.
* Hay repetición de códigos, lo cual no representa un error ya que un mismo usuario puede hacer más de una recomendación a productos distintos.

***asin :***
* Tipo de dato "string" alfanumérico.
* No presenta valores faltantes.
* Hay repetición de códigos, lo cual no representa un error ya que un producto puede tener varias reseñas

***reviewerName :***
* Tipo de dato "string".
* Tiene algunos valores faltantes (null)

***helpful :***
* Tipo de dato "string" alfanumérico.
* No presenta valores faltantes
* El primer valor del intervalo representa calificaciones positivas de la reseña y el ultimo representa el total de calificaciones a la reseña

***reviewText :***
* Tipo de dato "string" alfanumérico de gran longitud.

***overall :***
* Tipo de dato "float".
* No presenta valores faltantes.
* Sus valores varían desde 1.0 a 5.0

***summary :***
* Tipo de dato "string".

***unixReviewTime :***
* Tipo de dato "int".
* No presenta valores faltantes.
* Hay repetición de fechas, lo cual no representa un error ya que un mismo día se pudieron registrar varias reseñas

***reviewTime :***
* Tipo de dato "string" alfanumérico.
* No presenta valores faltantes.
* Hay repetición de fechas, lo cual no representa un error ya que que un mismo día se pudieron registrar varias reseñas

### **Metadata**

***asin :***
* Tipo de dato "string" alfanumérico.
* No presenta valores faltantes.
* No hay repetición de códigos.

***title :***
* Tipo de dato "string" alfanumérico.

***price :***
* Tipo de dato "float".
* Tiene algunos valores faltantes (null)

***imUrl :***
* Tipo de dato "string".

***related :***
* Tipo de dato "string".

***salesRank :***
* Tipo de dato "string".
* Tiene muchos valores faltantes (null).

***brand :***
* Tipo de dato "string" alfanumérico.
* Tiene muchos valores faltantes (null)
* Presenta muchos datos sucios, incoherentes y faltan referencias

***categories :***
* Tipo de dato "string".
 
## **Solución: Data Pipeline**
***Diagrama flujo del dato***
<div align="center">
    <img src="img\pipeline_diagram.png" alt="Project Screenshot" width="100%">
</div>
<br>

En esta sección se estructurará el flujo del dato desde la recepción hasta la salida del ETL.

### 1. **Data Ingest**

Los datasets entregados por el Product Owner, se descargaron y fueron almacenados de manera temporal en el localhost de la máquina.

Dado que trabajaremos sobre el esquema de Microsoft Azure se decidió crear un contenedor donde se almacenarán los datasets raw en la nube. Para esto, fue necesario crear una cuenta de trabajo en el portal de Azure. En dicha cuenta se crea un grupo de recursos donde incluímos una Storage Account con un contenedor.

### 2. **Conexión con Databricks**

Una vez almacenados los datasets en el contenedor de Azure se procede a realizar la conexión con Databricks, nuestro lugar de trabajo principal.

En el grupo de recursos previamente creado se añade un workspace de Databricks. Ahí se crea el clúster que permite computar nuestros datos (*Single Node 10.4 LTS Apache Spark 14GB Memory, 4 Cores*), el criterio de selección fue en base al alcance de nuestros recursos.

Dentro de Databricks creamos un Notebook y lo conectamos con el clúster. En dicho Notebook establecemos las variables necesarias para la conexión con el contenedor (Información detallada en el Notebook de ETL-Reviews)

### 3. **ETL**

El ETL de Reviews sigue los siguientes pasos:

* **Extracción** de los links de conexión al contenedor
* Definición de una función que permita crear un dataframe a partir de la URL de conexión
* Creación de los dataframes divididos por categorías
* **Transformación** de los datos:
  * Unión de todos los datasets
  * Cambio de nombre de columnas
  * Eliminación de columnas
  * Normalización      
* **Carga** de los datos en la base de datos de Databricks. Se empleó el formato de datos "delta" que permite la rápida ejecución de querys. 

### 4. **Conexión SQL Database**

Al no poseer Databricks premium no podemos realizar la conexión directa a PowerBI. Para esto, decidimos crear una base de datos en el portal de Azure y desde ahí crear la conexión. La creación de la base de datos en SQL se realiza de manera estándar, sin embargo, fue necesario cambiar la configuración de networking en donde se habilitan las IPs que trabajaran sobre esta.

Creada la SQL Database de Azure se realiza la conexión con Databricks por medio del protocolo [jdbc](https://www.infoworld.com/article/3388036/what-is-jdbc-introduction-to-java-database-connectivity.html#:~:text=JDBC%20(Java%20Database%20Connectivity)%20is,developed%20for%20the%20Java%20language.).

Para aliviar la carga de los datos se establece una carga en delta por años:

* Año 2014
* Año 2013
* Año 2012
* Del 2010 y 2011
* Del 2005 al 2009
* Del 2000 al 2004

*Para más información acerca del proceso de ETL por favor revisar los Notebooks dentro de la carpeta de Scripts.*

## **Diccionario de los datos - Data Analytics**

### **Reviews**

            reviewID         --->    ID unico de la reseña
            reviewerID       --->    ID del usuario, ejemplo: A2SUAM1J3GNN3B
            asinID           --->    ID del producto, ejemplo: 0000013714
            overall          --->    Puntaje dado al producto
            positiveScore    --->    Puntajes positivos de la reseña
            TotalScore       --->    Puntajes totales en reseña
            helpfulness      --->    Porcentaje de utilidad
            groupHelpfulness --->    Descripción de utilidad
            datetime         --->    Fecha de la reseña

### **Product average Score**

            productID       --->    ID de productos calificados
            averageScore    --->    Promedio de calificacion del producto

### **User Table**

            reviewerID      --->    ID unicos de los usuarios
            reviewerName    --->    nombre del usuario
            
### **Product table**

            asinID     --->    ID unico de productos
            title      --->    nombre del producto
            price      --->    precio 
            brand      --->    marca
            Categorie  --->    categoria
            
### **Score table**

            scoreID             --->    Calificaciones validas, numericas
            ScoreName           --->    Calificaciones validas, descripción
            customerPercention  --->    Equivalencia de calificacion segun percepcion del cliente 
            
### **Utility Table**

            ranting helpfulness  --->    Calificaciones validas, numericas
            description          --->    Calificaciones validas, descripción
            
### **Calendar**

            Fecha    --->    Fecha formato dd/mm/yyyy
            year     --->    año
            Month    --->    Mes
            
Para ver el dashboard realizado en PowerBI clic [aqui](https://app.powerbi.com/view?r=eyJrIjoiYjFjYWFkMzItOTllMy00ZDQ1LWEwNDctMTk2NTBjZjBiYzE2IiwidCI6ImJhYjBiNjc5LWJkNWYtNGZlOC1iNTE2LWM2YjhiMzE3Yzc4MiIsImMiOjR9)
