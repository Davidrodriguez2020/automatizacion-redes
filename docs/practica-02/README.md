# Práctica 02: Construcción de la red simulada en GNS3

## 1. Descripción

En esta práctica se construyó y configuró una infraestructura de red simulada mediante GNS3, con el propósito de trabajar con dispositivos de red, configurar el direccionamiento IP y comprobar la conectividad entre los equipos. También se trabajó con el protocolo de enrutamiento OSPF para observar la comunicación entre routers y el intercambio de información de rutas.

## 2. Objetivos

* Construir topologías de red utilizando GNS3.
* Configurar los dispositivos y el direccionamiento IP.
* Comprobar la conectividad entre los dispositivos mediante pruebas de ping.
* Configurar y verificar el funcionamiento del protocolo OSPF.
* Documentar las configuraciones y evidencias obtenidas durante la práctica.

## 3. Topología 1: PC-Switch-PC

Esta topología representa una red básica formada por dos equipos conectados mediante un switch. Se realizaron configuraciones para permitir la comunicación entre los equipos y se documentaron las pruebas de conectividad disponibles.

**Documentación y evidencias:**

* [Evidencia 1: Topología 1](topologia-01/evidencias/01-topologia-01.jpeg)
* [Evidencia 2: Topología 1](topologia-01/evidencias/02-topologia-01.jpeg)
* [Evidencia 3: Ping de PC1 a PC2](topologia-01/evidencias/03-ping-pc1-pc2.jpeg)

## 4. Topología 2: Enrutamiento con OSPF

En esta topología se trabajó con dos routers y un switch multicapa. Se realizaron configuraciones de los dispositivos y se revisó la información relacionada con el protocolo OSPF para comprobar el establecimiento de vecinos entre routers.

**Documentación y evidencias:**

* [Evidencia 1: Topología 2](topologia-02/evidencias/01-topologia-02.jpeg)
* [Evidencia 2: Configuración de R1](topologia-02/evidencias/02-configuracion-r1.jpeg)
* [Evidencia 3: Configuración de R2](topologia-02/evidencias/03-configuracion-r2.jpeg)
* [Evidencia 4: Configuración de S1](topologia-02/evidencias/04-configuracion-s1.jpeg)
* [Evidencia 5: Verificación de vecinos OSPF](topologia-02/evidencias/05-ospf-neighbor-01.jpeg)
* [Evidencia 6: Verificación de vecinos OSPF](topologia-02/evidencias/06-ospf-neighbor-02.jpeg)

## 5. Pruebas y verificaciones

Durante la práctica se recopilaron evidencias de las topologías construidas, las configuraciones de los dispositivos, una prueba de conectividad entre PC1 y PC2 y la verificación de vecinos OSPF.

Las pruebas adicionales, como la conectividad entre routers y la revisión de las tablas de enrutamiento, deben documentarse cuando se disponga de sus respectivas evidencias.

## 6. Resultados

Se documentaron dos topologías de red simuladas en GNS3. La primera corresponde a una conexión básica entre dos equipos mediante un switch; la segunda incorpora dos routers y un switch multicapa, junto con configuraciones y evidencias relacionadas con OSPF.

Las capturas y los archivos de configuración se encuentran organizados en las carpetas correspondientes a cada topología.

## 7. Conclusión

Esta práctica permitió trabajar con la construcción de redes simuladas en GNS3, la configuración de dispositivos y el registro de evidencias para documentar su funcionamiento. Además, se abordó el protocolo OSPF como parte de la comunicación entre routers, dejando organizada la documentación para futuras actividades de automatización de infraestructura de red.
