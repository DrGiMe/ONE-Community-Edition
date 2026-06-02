# ONE Community Edition 0.1

**ONE** es un lenguaje de intención computable para que personas que no programan puedan crear aplicaciones simples escribiendo lo que quieren construir.

La meta de esta edición comunitaria no es ser perfecta: es ser **usable, compartible y modificable**.

## Qué puede hacer ahora

- Crear proyectos desde plantillas.
- Leer archivos `.one`.
- Validar una intención.
- Generar una app web local con HTML, CSS y JavaScript.
- Guardar datos en el navegador con `localStorage`.
- Crear, editar, eliminar, buscar, importar y exportar datos.
- Usarse desde una interfaz gráfica básica: **ONE Studio**.
- Usarse desde terminal para desarrolladores.

## Para personas que no programan

1. Instala Python 3.10 o superior.
2. Descarga este proyecto.
3. Abre `one_studio.py` con Python.
4. Elige una plantilla.
5. Modifica la intención.
6. Presiona **Construir app**.
7. Presiona **Abrir app**.

## Para desarrolladores

```bash
python one.py templates
python one.py new tareas -o mi_proyecto.one
python one.py validate mi_proyecto.one
python one.py build mi_proyecto.one -o app_generada
```

## Ejemplo `.one`

```one
objetivo:
crear una aplicación simple para administrar tareas personales

usuarios:
personas

entidades:
    tarea:
        titulo texto
        descripcion texto opcional
        completada booleano defecto falso

funciones:
crear tarea
editar tarea
eliminar tarea
buscar tarea

restricciones:
no permitir título vacío

plataformas:
web

crear
```

## Estructura

```text
src/one/       Núcleo del lenguaje
one.py         CLI principal
one_studio.py  Interfaz gráfica básica
templates/     Plantillas iniciales
examples/      Ejemplos .one
docs/          Documentación
tests/         Pruebas automatizadas
```

## Filosofía

ONE no intenta reemplazar a Python, JavaScript, Rust o C++. ONE intenta abrir una puerta: que más personas puedan construir software describiendo intenciones de forma clara.

La comunidad puede hacerlo crecer.

## Licencia

MIT.
