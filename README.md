# Actividad Extracurricular 3B - Módulo `logging` en Python

**Asignatura:** Programación en Python  
**Tema:** Módulo `logging`

## Objetivo

Conocer el funcionamiento del módulo `logging` de Python y aprender a registrar eventos del programa en diferentes medios, como la consola, un archivo y mediante mensajes de Telegram.

---

## ¿Qué es el módulo `logging`?

El módulo `logging` es una biblioteca estándar de Python que permite registrar eventos ocurridos durante la ejecución de un programa. Es una herramienta muy utilizada para monitorear aplicaciones, detectar errores y facilitar el proceso de depuración, ya que ofrece un registro organizado de los mensajes generados por el sistema.

A diferencia de utilizar la función `print()`, el módulo `logging` permite clasificar los mensajes por niveles de importancia, guardar registros en archivos y personalizar el formato de salida.

---

## Niveles de logging

Python define cinco niveles principales de registro:

| Nivel | Descripción |
|--------|-------------|
| **DEBUG** | Información detallada utilizada para depuración. |
| **INFO** | Información general sobre la ejecución del programa. |
| **WARNING** | Advertencias que indican posibles problemas. |
| **ERROR** | Errores que afectan una parte del programa. |
| **CRITICAL** | Errores graves que pueden impedir el funcionamiento de la aplicación. |

---

## Archivos del proyecto

```
Actividad_Logging/
│
├── logging_consola.py
├── logging_archivo.py
├── logging_telegram.py
├── logs.log
└── README.md
```

---

## Descripción de los archivos

### logging_consola.py

Este archivo muestra mensajes de logging directamente en la consola utilizando diferentes niveles de severidad.

Características:

- Registro en consola.
- Fecha y hora.
- Nivel del mensaje.
- Nombre del archivo.
- Mensaje descriptivo.

---

### logging_archivo.py

Este programa registra la información en el archivo `logs.log`.

Características:

- Guarda automáticamente el historial de eventos.
- Registra fecha y hora.
- Incluye el nivel del mensaje.
- Guarda el nombre del archivo que generó el registro.

---

### logging_telegram.py

Este archivo envía los mensajes de logging mediante un bot de Telegram utilizando la API oficial.

Para su funcionamiento es necesario:

- Crear un bot con **@BotFather**.
- Obtener el Token del bot.
- Obtener el Chat ID del usuario.

---

## Personalización del logging

El formato utilizado en los ejemplos incluye:

- Fecha
- Hora
- Nivel del mensaje
- Nombre del archivo
- Mensaje generado

Ejemplo:

```
19/07/2026 21:44:11 | INFO | logging_archivo.py | Programa iniciado
```

También es posible modificar el color de los mensajes en consola utilizando la biblioteca **colorlog**, facilitando la identificación de cada nivel de registro.

---

## Librerías utilizadas

- logging (incluida en Python)
- requests
- colorlog

Instalación:

```bash
pip install requests
pip install colorlog
```

---

## Conclusiones

- El módulo `logging` es una herramienta más completa y profesional que el uso de `print()` para mostrar información del programa.
- Permite registrar eventos en diferentes destinos, como la consola, archivos o servicios externos.
- Facilita la detección y análisis de errores durante el desarrollo y mantenimiento de aplicaciones.
- La personalización del formato y los niveles de registro permite generar información clara y organizada para el monitoreo del software.