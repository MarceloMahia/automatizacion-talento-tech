# Pre-Entrega - Automatización QA

## Descripción

Proyecto de automatización de pruebas web desarrollado con Python, Selenium WebDriver y Pytest sobre la aplicación de demostración [SauceDemo](https://www.saucedemo.com/).

El objetivo es validar el inicio de sesión, la navegación del catálogo de productos y la interacción con el carrito de compras.

## Tecnologías utilizadas

* Python
* Selenium WebDriver 4
* Pytest
* pytest-html
* Google Chrome
* Git y GitHub

## Estructura del proyecto

* `tests/`: casos de prueba y configuración de Pytest.
* `utils/`: funciones auxiliares reutilizables.
* `reports/`: reportes HTML y capturas de pantalla.
* `requirements.txt`: dependencias del proyecto.

## Requisitos previos

* Python instalado.
* Google Chrome instalado.
* Git instalado.
* Conexión a Internet para acceder a SauceDemo.

## Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
cd NOMBRE_DEL_REPOSITORIO
```

Crear y activar un entorno virtual en Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Ejecución de las pruebas

Ejecutar todos los tests:

```bash
python -m pytest -v -s
```

Generar el reporte HTML:

```bash
python -m pytest tests/test_saucedemo.py -v -s --html=reports/reporte.html --self-contained-html
```

El reporte incluye el resultado de las pruebas ejecutadas.

## Casos de prueba

1. Login exitoso: valida la redirección al inventario y los títulos esperados.
2. Catálogo: valida la presencia de productos, el menú, el filtro y la información del primer producto.
3. Carrito: añade el primer producto y verifica el contador y su presencia en el carrito.

## Evidencias

Cuando una prueba falla durante su ejecución, se intenta guardar una captura de pantalla en `reports/capturas/`.

## Observaciones

Las pruebas utilizan las credenciales de demostración publicadas por SauceDemo. Los resultados pueden variar si el sitio de prueba presenta interrupciones o modificaciones.

Este proyecto tiene fines educativos y de práctica de automatización QA.
