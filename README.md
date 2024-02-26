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

## Contribuciones

Si encuentras algún error o tienes alguna sugerencia de mejora, no dudes en abrir un issue o enviar un pull request.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).
