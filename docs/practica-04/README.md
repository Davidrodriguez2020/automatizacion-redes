# Práctica 4: Exploración de comunidades, documentación y recursos de colaboración

## Propósito de la práctica
Aprender a localizar, evaluar, utilizar y documentar recursos técnicos y comunidades confiables para la resolución de problemas en el desarrollo de software y automatización de redes, sin necesidad de instalar nuevas herramientas.

## Relación con el proyecto integrador
Proporciona una base de conocimiento organizada dentro del repositorio para facilitar la resolución de futuros errores de programación y configuración en scripts de Python y topologías de GNS3 vinculados al proyecto integrador.

## Evaluar la confiabilidad de los recursos
=======
# Evaluar la confiabilidad de los recursos

Recursos evaluados:
- **Recurso 1:** 
The Python Tutorial (https://docs.python.org/3/tutorial/)

- **Recurso 2:** 
Documentación oficial de GNS3 (https://docs.gns3.com/docs-3.1-en/)

- **Recurso 3:**
 Stack Overflow, etiqueta Python (https://es.stackoverflow.com/questions/tagged/python)


| Criterio | Recurso 1: Documentación de Python | Recurso 2: Documentación de GNS3 | Recurso 3: Stack Overflow en español |
|---|---|---|---|
| ¿Quién publica o mantiene el recurso? | La Python Software Foundation y la comunidad de desarrolladores de Python. | El proyecto GNS3, que mantiene el software. Su documentación tiene un repositorio en GitHub donde se pueden reportar errores o proponer cambios. | Cualquier usuario registrado de la comunidad; los moderadores y los votos ayudan a filtrar la calidad. |
| ¿La información corresponde al tema investigado? | Sí. Explica variables, listas, diccionarios, ciclos y funciones, que es lo que usa dispositivos.py. | Sí. Cubre instalación de la GNS3 VM, proyectos, topologías, plantillas de dispositivos y enlaces, que es lo que usamos en las prácticas anteriores. | Depende de cada pregunta. Hay que leer si el caso se parece al nuestro (versión, error y contexto). |
| ¿Incluye ejemplos o instrucciones verificables? | Sí. Incluye ejemplos de código cortos que se pueden copiar y ejecutar en la terminal para comprobar el resultado. | Sí. Incluye pasos de instalación y configuración que se pueden repetir en nuestro equipo, y se verifica viendo si la topología funciona. | Sí, muchas respuestas incluyen código, pero solo se verifica si lo probamos nosotros. Una respuesta marcada como aceptada o con muchos votos es un indicio, no una garantía. |
| ¿Se identifica la versión o fecha de actualización cuando corresponde? | Sí. La dirección incluye la versión (`/3/`), hay un selector de versiones y las páginas muestran la fecha de última actualización. | Sí. La versión aparece en la dirección y el título (3.1). | Cada pregunta y respuesta muestra su fecha, pero muchas veces no indican la versión de Python o de la herramienta, y pueden estar desactualizadas. |
| ¿Es posible comprobar la información con otra fuente? | Sí. Se puede comparar con la referencia de la biblioteca estándar, con los laboratorios de Cisco DevNet o con el código ejecutándose. | Sí. Se puede comparar con las incidencias del proyecto en GitHub, con la comunidad de GNS3 y con la práctica en nuestro propio equipo. | Sí, y es necesario ya que conviene contrastar con la documentación oficial antes de usar la respuesta. |
| ¿Qué utilidad tiene para el proyecto integrador? | Es la base para escribir y corregir dispositivos.py (listas, diccionarios, ciclos y funciones). | Es la guía para armar, configurar y corregir las topologías con R1 y R2 en GNS3. | Sirve para resolver errores concretos de Python que la documentación no cubre con un caso parecido. |

-----

**•	¿Cuál de los recursos consideras más útil para resolver dudas de Python? ¿Por qué?**
A. Seria la documentacion oficial de Python ya que es documentada y matenida por los desarrolladores de el lenguaje, por lo que explica de manera entendible y ordenada, muestra ejemplos que pueden ser probados y indican la version de Python, por lo que suena a la mas segura de usar.

**•	¿Cuál consultarías para resolver un problema relacionado con GNS3?**
A. La documentacion de GNS3 que proporciona, ya que ahi explica como se instala la GNS3 VM y documenta como armar pryectos, como configurar las plantillas de los dispositivos, y si no encontramos alguna solucion ahi, se podria consultar la comunidad de GNS3 o sus incidencias en GitHub para consultar si otras personas tuvieron el mismo error.


**•	¿Por qué no conviene copiar directamente una solución sin comprobar que funciona en el entorno de trabajo?**
A. Por que podria generar mas problemas, ya que podria ser para otra version o sistema operativo, lo que generaria otro problema, esto sin contar si el codigo tiene algun error, esta incompleto o funciona como nosotros queremos, por lo que se suguiere de leer primero el codigo, probarlo en un entorno de prueba y revisar los cambios que genero. 

## Estrategia de solución del problema

| Elemento | Respuesta del equipo |
| :--- | :--- |
| **Problema identificado** | `dispositivos.py` muestra la información general de R1 y R2, pero falla al buscar un equipo por su nombre. |
| **Palabras clave para la búsqueda** | `Python find dictionary in list by key`, `Netmiko search device name`, `Python search key error`. |
| **Documentación o comunidad** | Documentación oficial de Python y Stack Overflow[cite: 1]. |
| **Información a revisar en el código** | La estructura de datos (lista de diccionarios) y la función que compara la entrada del usuario con el nombre del equipo[cite: 1]. |
| **Tipo de ejemplo o solución** | Un fragmento de código con comprensiones de listas o bucles condicionales para filtrar diccionarios por clave. |
| **Cómo comprobar que funciona** | Ejecutar el script ingresando nombres válidos e inválidos para verificar que devuelva los datos correctos o el aviso de error. |
| **Cómo documentar la solución** | Registrar en el repositorio la causa del error, el código corregido y el enlace del recurso consultado. |

## Aprendizajes obtenidos
El análisis estructurado de la documentación oficial y de las comunidades de desarrollo permite dejar de depender de búsquedas al azar. Esto fomenta una depuración de código más eficiente, metódica y reutilizable para todo el equipo de trabajo, optimizando los tiempos de desarrollo en la automatización de redes.

## Conclusiones individuales

### Conclusión - Eder Alexander Austria Mendoza:
La documentación oficial ofrece una estructura formal, precisa y respaldada directamente por los creadores de la tecnología, mientras que una respuesta comunitaria se basa en casos prácticos y experiencias reales de otros desarrolladores. Para determinar la confiabilidad de un recurso, es fundamental evaluar la autoridad de la fuente, la presencia de ejemplos verificables y la vigencia de la información. Las comunidades son herramientas poderosas para resolver problemas de Python al brindar múltiples perspectivas y soluciones a errores específicos que a veces no se detallan en los manuales teóricos. Conviene documentar las soluciones encontradas en GitHub para construir una base de conocimiento sólida y reutilizable que evite la pérdida de tiempo en futuros errores recurrentes. Finalmente, utilizaré estos recursos en las siguientes prácticas para optimizar el desarrollo de scripts de automatización y la resolución autónoma de fallas técnicas en el proyecto.

### Conclusión - Diana Xochitl Hernandez García
Comprender la diferencia entre la documentación oficial y los foros de la comunidad permite elegir la fuente más adecuada según el tipo de duda que enfrentemos en el proyecto. Los criterios principales de confiabilidad incluyen la actualización constante del contenido, la reputación de la plataforma y la validación mediante ejemplos reproducibles en el entorno de trabajo. Cuando nos enfrentamos a un error de sintaxis o lógica en Python, las comunidades permiten encontrar casos similares y entender rápidamente cómo otros usuarios superaron el mismo obstáculo. Documentar las soluciones en el repositorio de GitHub es indispensable para mantener una trazabilidad clara del trabajo en equipo y asegurar que todos los integrantes tengan acceso al mismo conocimiento técnico. Todo este aprendizaje estructurado será clave para afrontar con éxito las prácticas posteriores de integración y gestión de redes.

### Conclusión - David Eduardo Rodriguez Romero:
La documentación oficial establece las bases teóricas y funcionales de una herramienta, en contraste con las comunidades de colaboración que aportan agilidad y soluciones directas a problemas atípicos de programación. Un recurso confiable debe demostrar trazabilidad, soporte activo y congruencia técnica con la versión del software que estamos implementando en nuestros equipos. Al trabajar con Python, las comunidades facilitan la comprensión de errores complejos mediante la experiencia colectiva de programadores experimentados. Registrar cada solución en GitHub transforma el repositorio en una memoria institucional del equipo, facilitando el aprendizaje colaborativo continuo. Aplicaremos estos recursos metodológicos en las próximas etapas del proyecto integrador para garantizar estabilidad y orden en la automatización de infraestructura.

### Conclusión - Cristal Esmeralda Ruiz Herrejón:
Mientras que la documentación oficial es el estándar definitivo y normativo de un lenguaje o software, las comunidades representan la práctica viva y la resolución de incidencias cotidianas. Evaluamos la confiabilidad observando el respaldo institucional, las referencias cruzadas y la verificación de los fragmentos de código provistos. Una comunidad en red acelera la resolución de problemas en Python al ofrecer depuraciones paso a paso de errores comunes que ralentizan el desarrollo. La documentación en GitHub garantiza que el esfuerzo de investigación no se pierda y sirva como manual de consulta interno para todo el equipo. Emplearemos estas estrategias de búsqueda y validación de recursos de manera constante en las actividades venideras de nuestra formación técnica.