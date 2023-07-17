# python_django

this is a test proyect

## Creamos el entorno virtual

* Para crear el entorno virtual, vamos a instalar virtualenv con el siguiente comando <pip install virtualenv>
* Despúes de la instalación se ejecuta <virtualenv venv> para crear la carpeta que contiene el entorno virtual

## Instalar django

* Instalamos django con <pip install django>
* Creamos la carpeta del proyecto con <django-admin "project" .> (sustituir el nombre de project con el nombre del proyecto, sin comillas) al final se agrega un <.> punto para indicar que la carpeta del proyecto se cree en la raiz, de lo caontrario se crea una carpeta con el nombre del proyecto y dentro otra carpeta con el nombre del proyecto ("name_project/name-project")
* Activar el servidor del proyecto, ejecutamos <python manage.py runserver> y nos mostrará la dirección IP del servidor local y el puerto.
* Si se requiere cambiar el puerto se debe de especificar <python manage.py runserver "3000"> sustituyendo el "3000" por el puerto que queramos, por default se asigna el puerto 8000

## Proyectos en django

Cada proyecto en django se componen por app, que son funcionalidades que permiten al proyecto trabajar adecuadamente. Se crean a través del archivo de configuración <python manage.py startapp "name"> reemplazando "name" con el nombre de la aplicación.
Se crea una carpeta con el nombre de la aplicación el cual contiene archivos para la configuración de dicha aplicación.

## Migrations

Se utilizan para interactuar con la base de datos.
* <python manage.py makemigrations> permite crear los archivos necesarios para la creacion, modificación de las bases de datos a traves de modelos.

* <python manage.py migrations> ejecuta los archivos que se crearon con <makemigrations>

## Usuarios
django ya incluye un panel de administración, se accede a él con /admin. 
Para crear un usuaraio y contraseña se ejecuta <python manage.py createsuperuser> y colocamos el nombre de usuario, correo y contraseña