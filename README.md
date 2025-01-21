# reentrega
# Proyecto Django

Este es un proyecto web desarrollado con Django. A continuación, se detallan los pasos necesarios para configurar y ejecutar el proyecto en tu máquina local.

## Requisitos

Asegúrate de tener instalado lo siguiente:
- Python 3.x
- Django 5.x
- Pillow (para manejo de imágenes)

## Instalación

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/CapitanTsubasa/reentrega.git
   cd reentrega

2. **Crear un entorno virtual**:

python -m venv .venv
.\.venv\Scripts\activate

3. **Instalar dependencias**:

pip install -r requirements.txt

3. **Crear las migraciones y base de datos**:

python manage.py migrate


**Crear un superusuario**
python manage.py createsuperuser