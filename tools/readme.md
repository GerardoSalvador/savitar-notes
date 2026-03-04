# Utilidades y herramientas

## Git y github

### Curso de Git con SoyDalto

#### Configuración de Git

[Uso de Git](https://www.youtube.com/watch?v=9ZJ-K-zk_Go&t=307s)

Minuto 15:23

* Ir a descargar Git para el S.O. que tengamos
* Definir nuestro alias y correo
  * Sistema:
  * Global:
    * git config --global user.name "Nombre de persona que usará Git"
    * git config --global user.email "correo"
  * Local ->
* Para ver las configuraciones que hemos hecho en nuestras configuraciones
  * git config list
  * git config --global --list

Carpeta guardada con git.

* Ir a la carpeta con la que deseamos trabajar con git
* Estando en el directorio: **git init**
![Imagen despues de git init](/img/1.png)
* En la carpeta se nos crea carpeta oculta .git
* git status en directorio

* Para agregar todos los archivos modificados: **git add .**

* **git commit -m** "Comentario con modificaciones hechas"
* **git log** para ver los cambios hechos y por quien
* **git checkout 30077fac96c3877c83e5ed8cb3551a42ce0b6fbd** para crear una rama a partir de un punto dado, en este caso desde el inicio
* **git switch master** para volver a master
* **git branch** para ver ramas
* **git remote add origin "Direccion Url del proyecto"** para sincronizar con un repositorio de github
* **git push origin master**
