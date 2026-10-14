dispositivos = [
    {
        "nombre": "R1",
        "tipo": "Router",
        "ip": "10.1.1.1",
        "estado": "Activo"
    },
    {
        "nombre": "R2",
        "tipo": "Router",
        "ip": "10.1.1.2",
        "estado": "Activo"
    },
    {
        "nombre": "S1",
        "tipo": "Switch",
        "ip": "10.1.1.3",
        "estado": "Inactivo"
    }
]

for dispositivo in dispositivos:
    print(f"Nombre: {dispositivo['nombre']}")
    print(f"Tipo: {dispositivo['tipo']}")
    print(f"IP: {dispositivo['ip']}")
    print(f"Estado: {dispositivo['estado']}")
    print(".......................")

if dispositivo["estado"] == "Activo":
    print("Dispositivo en funcionamiento")
else:
    print("Revisar dispositivo")





