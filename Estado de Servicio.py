import subprocess

def check_bluetooth_service_status():
    try:
        # Ejecuta el comando sc para obtener el estado del servicio de Bluetooth
        result = subprocess.run(['sc', 'query', 'bthserv'], capture_output=True, text=True)
        output = result.stdout
        
        # Comprueba si el servicio está en ejecución
        if "RUNNING" in output:
            print("El servicio de compatibilidad con Bluetooth está en ejecución.")
        elif "STOPPED" in output:
            print("El servicio de compatibilidad con Bluetooth está detenido.")
        else:
            print("No se pudo determinar el estado del servicio de compatibilidad con Bluetooth.")
    except Exception as e:
        print("Ocurrió un error al intentar obtener el estado del servicio de compatibilidad con Bluetooth:", e)

if __name__ == "__main__":
    check_bluetooth_service_status()
    