# automatizacion-redes



**1. Datos del equipo**

•	Eder Alexander Austria Mendoza — Documentación y auditoría

•	Cristal Esmeralda Ruiz Herrejon — Instalación de Fase 1 y 3

•	Diana Xochitl Hernández García — Auditoría de GitHub

•	David Eduardo Rodríguez Romero — Instalación de Fase 2


**Propósito de la práctica**

El propósito principal de esta práctica es instalar y configurar diversas herramientas tecnológicas para preparar un entorno de desarrollo de software colaborativo destinado a la automatización de redes, así como documentar de forma correcta todo el proceso de instalación de dichas herramientas. 
Para cumplir con este propósito, la práctica se divide en cuatro fases fundamentales:

•	Fase 1 (Entorno de programación): Preparar las herramientas básicas para desarrollar scripts en Python.

•	Fase 2 (Control y herramientas de desarrollo): Preparar las herramientas necesarias para trabajar de manera colaborativa y probar servicios.

•	Fase 3 (Laboratorio de redes virtuales): Configurar el entorno de simulación donde se realizarán las prácticas posteriores de automatización utilizando GNS3 y VMware Workstation.

•	Fase 4 (Evidencia y documentación): Integrar, estructurar y documentar todo el laboratorio preparado dentro de un repositorio oficial en GitHub.


1. Herramientas instaladas
•	Python (v3.14.7) 
•	Visual Studio Code 
•	Git (v2.55.0) y GitHub 
•	Postman 
•	OpenConnect VPN 
•	Docker Desktop 
•	GNS3 y GNS3 VM 
•	VMware Workstation Pro (v17) 
2. Dificultades encontradas
•	Hubo detalles con la compatibilidad y versiones de Python y las extensiones en VS Code.
•	Al configurar Git, se requirió alinear correctamente la identidad global y la sincronización con el repositorio remoto.
•	La puesta en marcha de GNS3 fue de lo más complicado, ya que exigió sincronizar el software con VMware Workstation Pro para el arranque correcto de la GNS3 VM y la asignación de recursos.
•	Se debió cuidar la asignación de IPs en Docker Desktop y GNS3 para evitar conflictos de red.
•	Ajustar las rutas y parámetros de autenticación iniciales en la VPN.
3. Resolución de problemas
•	Se aislaron las dependencias usando entornos virtuales (python -m venv venv). 
•	Para Git, se configuraron manualmente los comandos de credenciales y el control de ramas.
•	Para GNS3, se validó de forma manual el arranque de los servicios en VMware Workstation Pro, comprobando en la consola de la máquina virtual la correcta asignación de la IP (192.168.146.128) y el puerto activo. 
•	Se validaron las interfaces de red y accesos remotos del sistema.
4. Relación entre las diferentes herramientas
Python y VS Code operan como el núcleo de desarrollo para los scripts. Git y GitHub aseguran la trazabilidad y el control de versiones de todo ese código. Postman permite validar las APIs antes de integrarlas con dispositivos de red. GNS3, VMware y Docker simulan la infraestructura física y virtual para ejecutar las pruebas de automatización sin poner en riesgo entornos reales, mientras que OpenConnect VPN interconecta el laboratorio con redes externas cuando es necesario. 
5. Resumen general
La preparación del entorno de trabajo integró el uso de Python y VS Code para el desarrollo de código, respaldado por Git y GitHub para el control de versiones. Asimismo, se emplearon herramientas como Postman para pruebas de APIs, Docker para contenedorización, y una arquitectura basada en VMware Workstation Pro y GNS3 para simular escenarios de red complejos. Resolver los retos de virtualización y dependencias permitió consolidar un entorno controlado, estable y seguro indispensable para ejecutar prácticas de automatización de redes de manera eficiente. 

