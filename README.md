\# 📋 Gestor de Tareas - Django + Bootstrap



Este es un \*\*proyecto de examen (PC1)\*\* desarrollado en \*\*Django 5 + Bootstrap 5\*\*, que implementa un \*\*Gestor de Tareas con Categorías\*\*.  

La aplicación permite \*\*crear, listar, editar, eliminar y buscar tareas\*\*, cada una asociada a una categoría personalizada con nombre y color.  



---



\## ✨ Características



\- ✅ \*\*CRUD de Tareas\*\* (crear, listar, editar, eliminar).  

\- ✅ \*\*CRUD de Categorías\*\* (crear, listar, editar, eliminar).  

\- ✅ \*\*Relación\*\*: cada tarea pertenece a una categoría.  

\- ✅ \*\*Buscador\*\* de tareas por título.  

\- ✅ \*\*Interfaz moderna\*\* con \*\*Bootstrap 5\*\*.  

\- ✅ \*\*Validación de fecha límite\*\* con calendario en formularios.  



---



\## 🖥️ Vista previa



\### 🔹 Lista de tareas

!\[Tareas](https://img.shields.io/badge/Screenshot-Tareas-blue?style=for-the-badge\&logo=django)



\### 🔹 Lista de categorías

!\[Categorías](https://img.shields.io/badge/Screenshot-Categorías-green?style=for-the-badge\&logo=bootstrap)



---



\## ⚙️ Instalación



Clona este repositorio e instala las dependencias:



```bash

\# Clonar el repo

git clone https://github.com/Hazielcode/EXAM-PC1-DJANGO.git

cd EXAM-PC1-DJANGO



\# Crear entorno virtual

py -m venv venv

venv\\Scripts\\activate   # (en Windows)

\# o source venv/bin/activate en Linux/Mac



\# Instalar dependencias

pip install -r requirements.txt



🚀 Uso



Ejecuta las migraciones:



py manage.py migrate





Inicia el servidor:



py manage.py runserver





Abre en el navegador:

👉 http://127.0.0.1:8000/



Flujo recomendado:



Crear categorías desde http://127.0.0.1:8000/categorias/



Luego crear tareas y asignarles categoría



Usar el buscador para filtrar por título



📂 Estructura del proyecto

EXAM-PC1-DJANGO/

│── gestor/               # App principal (modelos, vistas, templates)

│   ├── templates/

│   │   ├── tareas/       # Templates de tareas

│   │   └── categorias/   # Templates de categorías

│── tareas/               # Configuración principal de Django

│── db.sqlite3            # Base de datos (ignorada en Git)

│── manage.py             # Script principal

│── requirements.txt      # Dependencias del proyecto

│── README.md             # Documentación



📦 Tecnologías usadas



Python 3.12 🐍



Django 5.x ⚡



Bootstrap 5 🎨



SQLite (base de datos por defecto)



👨‍💻 Autor



✨ Proyecto desarrollado por Hazielcode



🎓 Examen PC1 - Django



⭐ Contribuye



Si este proyecto te sirvió, no olvides dejar una ⭐ en el repo 😉





---



📌 Guardalo como `README.md` en tu proyecto, y luego haz:  



```powershell

git add README.md

git commit -m "Agregué README.md espectacular"

git push



