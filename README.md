# Monitor de Estado del Servicio de Compatibilidad con Bluetooth de Windows

Este script de Python permite monitorear el estado del servicio de compatibilidad con Bluetooth en sistemas operativos Windows. Puede ser útil para verificar si el servicio está en ejecución o detenido.

## Requisitos

- Python 3.x
- Sistema operativo Windows

## Uso

1. Clona este repositorio o descarga el archivo `monitor_bluetooth_service.py`.
2. Abre una terminal en el directorio donde se encuentra el archivo `monitor_bluetooth_service.py`.
3. Ejecuta el script con Python:

    ```
    python monitor_bluetooth_service.py
    ```

4. El script imprimirá el estado actual del servicio de compatibilidad con Bluetooth.

## Detalles de Implementación

El script utiliza el módulo `subprocess` de Python para ejecutar el comando `sc query bthserv`, el cual consulta el estado del servicio de compatibilidad con Bluetooth en Windows. Luego analiza la salida de este comando para determinar si el servicio está en ejecución o detenido.

-Importación del módulo subprocess: En la primera línea del código, importamos el módulo subprocess. Este módulo nos permite ejecutar comandos del sistema operativo desde Python y obtener la salida del comando.

-Definición de la función check_bluetooth_service_status: Esta función es donde ocurre la mayor parte del trabajo. Toma el nombre del servicio de compatibilidad con Bluetooth (bthserv) y utiliza el comando sc query para obtener información sobre este servicio.

-Ejecución del comando sc query bthserv: Usamos subprocess.run() para ejecutar el comando sc query bthserv. Este comando consulta el estado del servicio de compatibilidad con Bluetooth en el sistema operativo Windows.

-Análisis de la salida del comando: Después de ejecutar el comando, capturamos la salida utilizando result.stdout. Esta salida contiene información sobre el estado del servicio. Analizamos esta salida para determinar si el servicio está en ejecución o detenido.

-Impresión del estado del servicio: Dependiendo de la salida del comando, imprimimos un mensaje indicando si el servicio está en ejecución, detenido o si no se pudo determinar su estado.

-Manejo de excepciones: Utilizamos un bloque try-except para manejar cualquier excepción que pueda ocurrir durante la ejecución del código. Esto nos ayuda a identificar y manejar posibles errores de manera adecuada.

En resumen, el código utiliza el módulo subprocess para ejecutar un comando del sistema operativo que consulta el estado del servicio de compatibilidad con Bluetooth en Windows. Luego, analiza la salida de este comando para determinar el estado del servicio y finalmente imprime un mensaje indicando el estado del servicio. Esto nos permite monitorear el estado del servicio de Bluetooth desde un script de Python.
