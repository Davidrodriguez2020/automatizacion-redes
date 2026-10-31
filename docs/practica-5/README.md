## Objetivo
Configuramos y ejecutamos un script de Python que se conecta por Telnet a un
router Cisco en GNS3 para aplicar configuraciones y verificar los cambios.

## Relación con las prácticas anteriores
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

