dispositivos = [
    {
        "nombre": "R1",
        "tipo": "Router",
        "ip": "10.1.1.1",
        "direccion MAC": "0c:3d:62:52:00:00",
        "puerto": "GigabitEthernet0/0",
        "loopback": "1.1.1.1",
        "marca": "cisco",
        "estado": "Activo"
    },
    {
        "nombre": "R2",
        "tipo": "Router",
        "ip": "10.1.1.2",
        "direccion MAC": "0c:77:07:4a:00:00",
        "puerto": "GigabitEthernet0/0",
        "loopback": "2.2.2.2",
        "marca": "cisco",
        "estado": "Activo"
    },
    {
        "nombre": "S1",
        "tipo": "Switch",
        "direccion MAC": "0c:aa:8d:2c:00:00",
        "ip": "10.1.1.3",
        "puerto": "GigabitEthernet0/0" "GigabitEthernet0/1" "GigabitEthernet0/2",
        "loopback": "3.3.3.3",
        "marca": "cisco",
        "estado": "Inactivo"
    }
]

def ver_dis(dispositivo):
    print("Nombre:", dispositivo["nombre"])
    print("Tipo:", dispositivo["tipo"])
    print("IP:", dispositivo["ip"])
    print("Puerto:", dispositivo["puerto"])
    print("Dirección MAC:", dispositivo["direccion MAC"])
    print("Loopback:", dispositivo["loopback"])
    print("Marca:", dispositivo["marca"])
    print("Estado:", dispositivo["estado"])

for dispositivo in dispositivos:
    ver_dis(dispositivo)
    print(".......................")

if dispositivo["estado"] == "Activo":
    print("Dispositivo en funcionamiento")
else:
    print("Revisar dispositivo")





