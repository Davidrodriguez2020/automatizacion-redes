## 1. Objetivo
Configuramos y ejecutamos un script de Python que se conecta por Telnet a un
router Cisco en GNS3 para aplicar configuraciones y verificar los cambios.

## 2. Relación con las prácticas anteriores
Usando el conocimiento de las practicas anteriores creando scripts en python y agregando y configurando dispositivos, los implementamos en esta practica, uniendo todo lo aprendido anteriormente.

## 3. Topología y direccionamiento
(Captura o descripción de la topología: NAC, NAT Cloud, switch, IOSvL2, R1)

| Dispositivo | Interfaz | Dirección IP |
|---|---|---|
| R1 | Gi0/0 | 192.168.122.70/24 |
| R1 | Loopback0 | 1.1.1.1/32 |
| R1 | Loopback1 | 2.2.2.2/32 |

## 4. Versión de Python

*python3 python31.py*

## 5. Explicación del scripts
Ejecuta desde el Network Automation Container (NAC) y se conecta por Telnet al router R1 para configurarlo de forma automatica y lo que hace es: 

1. Definir la IP de R1 (`192.168.122.70`) y pedir el usuario y las contraseñas con `input()` y `getpass`, para no escribirlas en el código.
2. Abre la conexión Telnet, espera los mensajes `Username:` y `Password:` y
   envía las credenciales.
3. Entra al modo `enable` y a `configure terminal`.
4. Crea las interfaces Loopback0 (1.1.1.1) y Loopback1 (2.2.2.2).
5. Configura OSPF (proceso 1) con `network 0.0.0.0 255.255.255.255 area 0`.
6. Cierra la sesión y muestra en pantalla los comandos ejecutados.

## 6. Tabla de pruebas y resultados

En la siguiente tabla se relaciona cada evidencia con el procedimiento que se observa y el resultado que realmente permite comprobar. Las imágenes de preparación y edición del código se identifican como tales, sin presentarlas como pruebas de configuración exitosa.

| Prueba o actividad | Procedimiento realizado | Resultado observado | Evidencia |
|---|---|---|---|
| 1. Preparación de la topología | Revisar en GNS3 los dispositivos y las conexiones del laboratorio. | Se observa el contenedor Network Automation conectado al switch, al switch Cisco IOSvL2 y al router Cisco IOSv; también aparece la conexión hacia la nube NAT. | [evidecia1.png](https://github.com/Davidrodriguez2020/automatizacion-redes/blob/main/docs/practica-5/evidencias/evidecia1.png) |
| 2. Comprobación de la interfaz de red del contenedor | Ejecutar `ifconfig` en el Network Automation Container. | La interfaz `eth0` aparece activa con la dirección `192.168.42.235` y máscara `255.255.255.0`. | [evidencia2.png](https://github.com/Davidrodriguez2020/automatizacion-redes/blob/main/docs/practica-5/evidencias/evidencia2.png) |
| 3. Revisión de la configuración de red del contenedor | Abrir el archivo `/etc/network/interfaces` con el editor nano. | Se observa la configuración de `eth0` para obtener una dirección mediante DHCP. La captura documenta la edición del archivo, no una prueba independiente de conectividad. | [evidencia3.png](https://github.com/Davidrodriguez2020/automatizacion-redes/blob/main/docs/practica-5/evidencias/evidencia3.png) |
| 4. Comprobación del acceso a Internet | Ejecutar una actualización de paquetes y después realizar un ping a `www.google.com`. | La actualización presenta un error de clave pública del repositorio de HashiCorp; sin embargo, el ping muestra respuestas de Google. Se comprueba conectividad externa, pero no que todos los repositorios puedan actualizarse correctamente. | [evidencia4.jpeg](https://github.com/Davidrodriguez2020/automatizacion-redes/blob/main/docs/practica-5/evidencias/evidencia4.jpeg) |
| 5. Elaboración inicial del script | Crear el archivo `python31.py` e incorporar la importación de `getpass` y `telnetlib`, además de la solicitud de credenciales y los comandos iniciales. | Se observa una primera versión del código que contempla la conexión Telnet y el envío de comandos. Esta captura documenta la elaboración del script, no la configuración final de las interfaces. | [evidencia5.png](https://github.com/Davidrodriguez2020/automatizacion-redes/blob/main/docs/practica-5/evidencias/evidencia5.png) |
| 6. Configuración de la interfaz del router | Configurar `GigabitEthernet0/0`, asignar `192.168.42.70 255.255.255.0` y ejecutar `no shutdown`. Después, consultar `show ip interface brief`. | La interfaz `GigabitEthernet0/0` aparece con la dirección `192.168.42.70` y los estados `up/up`. | [evidencia6.png](https://github.com/Davidrodriguez2020/automatizacion-redes/blob/main/docs/practica-5/evidencias/evidencia6.png) |
| 7. Prueba de conexión Telnet al router | Desde el contenedor, ejecutar `telnet 192.168.42.70`, ingresar las credenciales y entrar al modo privilegiado. | Se observa la conexión establecida, la solicitud de autenticación y el acceso al modo privilegiado mediante `enable`. | [evidencia7.png](https://github.com/Davidrodriguez2020/automatizacion-redes/blob/main/docs/practica-5/evidencias/evidencia7.png) |
| 8. Incorporación de comandos de configuración al script | Editar `python31.py` para conectarse a `192.168.42.70`, entrar al modo privilegiado y configurar las dos interfaces Loopback y OSPF. | El código contiene los comandos para crear Loopback0, Loopback1 y configurar el proceso OSPF 1. La captura demuestra que los comandos están escritos, pero no confirma por sí sola su ejecución exitosa. | [evidencia8.png](https://github.com/Davidrodriguez2020/automatizacion-redes/blob/main/docs/practica-5/evidencias/evidencia8.png) |
| 9. Preparación de la sesión Telnet en el código | Revisar la versión del script que solicita las credenciales, abre Telnet y envía los comandos `enable` y `exit`. | Se observa la lógica de autenticación y acceso al modo privilegiado. Esta versión todavía no muestra los comandos para crear las interfaces Loopback ni configurar OSPF. | [evidencia9.png](https://github.com/Davidrodriguez2020/automatizacion-redes/blob/main/docs/practica-5/evidencias/evidencia9.png) |
| 10. Ejecución del script de Python | Ejecutar `python3 python31.py` desde el contenedor e iniciar la sesión con el router. | La salida muestra el inicio de la conexión y comandos de configuración, incluido el trabajo sobre Loopback0. La captura está parcialmente recortada, por lo que no permite comprobar por sí sola toda la configuración. | [evidencia10.png](https://github.com/Davidrodriguez2020/automatizacion-redes/blob/main/docs/practica-5/evidencias/evidencia10.png) |
| 11. Verificación de las interfaces y de OSPF | En R1, ejecutar `show ip interface brief`, `show running-config \| section router ospf` y `show running-config \| section interface Loopback`. | Se observan Loopback0 con `1.1.1.1`, Loopback1 con `2.2.2.2`, ambas interfaces en estado `up/up` y la configuración del proceso OSPF 1 con la sentencia `network 0.0.0.0 255.255.255.255 area 0`. Esta es la evidencia principal de la configuración final. | [evidencia11.jpeg](https://github.com/Davidrodriguez2020/automatizacion-redes/blob/main/docs/practica-5/evidencias/evidencia11.jpeg) |
| 12. Comprobación de conectividad y corrección de la IP de destino | Realizar ping a `192.168.42.70` e intentar conexiones Telnet a `192.168.122.70` y `192.168.42.70`. | El ping a `192.168.42.70` recibe respuestas. La conexión a `192.168.122.70` es rechazada, mientras que la conexión a `192.168.42.70` se establece. Esto permite identificar la dirección utilizada correctamente en el laboratorio. | [evidencia12.png](https://github.com/Davidrodriguez2020/automatizacion-redes/blob/main/docs/practica-5/evidencias/evidencia12.png) |
| 13. Registro de la actividad Telnet en la consola del router | Revisar los mensajes que aparecen en la consola de IOS durante la sesión Telnet. | Se observan mensajes de negociación del protocolo Telnet y un registro de configuración desde una sesión VTY. La captura sirve como evidencia complementaria de la actividad de administración remota. | [scripts.png](https://github.com/Davidrodriguez2020/automatizacion-redes/blob/main/docs/practica-5/evidencias/scripts.png) |

## 7. Problemas y soluciones

Durante esta práctica pueden presentarse problemas de conectividad, autenticación Telnet o compatibilidad de Python con la biblioteca `telnetlib`. Para identificar su causa, es necesario comprobar la dirección IP del router, el acceso remoto, las credenciales y la versión de Python utilizada.

En caso de presentarse algún error, se deberá registrar el mensaje obtenido, la solución aplicada y el resultado de la nueva prueba. Si no se presentaron problemas, se indicará que no hubo incidencias durante la ejecución.


## 8. Conclusiones individuales

### Eder Alexander Austria Mendoza

Esta práctica permitió comprender cómo Python puede utilizarse para automatizar configuraciones en un router mediante Telnet. También destacó la importancia de documentar los procedimientos y resultados para facilitar el trabajo del equipo.

### Cristal Esmeralda Ruiz Herrejon

La actividad permitió relacionar la programación con la administración de redes, utilizando un script para enviar comandos a un router. La verificación de las configuraciones ayuda a comprobar que las tareas de automatización se ejecuten correctamente.

### Diana Xochitl Hernández García

La práctica mostró la importancia de organizar el código, las pruebas y las evidencias en GitHub. Mantener la documentación actualizada facilita el seguimiento de los cambios y la colaboración entre los integrantes del proyecto.

### David Eduardo Rodríguez Romero

Esta práctica representa un avance en el proyecto integrador al pasar de representar información de dispositivos con Python a automatizar configuraciones mediante Telnet. También permite reconocer la importancia de comprobar la conectividad, validar los cambios y documentar los resultados obtenidos.
