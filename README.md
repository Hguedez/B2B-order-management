<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://www.tribuco.mx/">
    <img src="https://www.tribuco.mx/static/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">B2B Order Management</h3>

  <p align="center">
Plataforma de ventas  
    <br>
    <a href="https://github.com/Hguedez/B2B-order-management/issues">Solicitar función</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de contenidos</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Pre requisitos</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#todo">TODO</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Acerca del proyecto

Aplicación web para una empresa B2B que gestiona pedidos y productos para sus clientes. 
Se proporciona un caso de estudio para un cliente específico y se debe implementar la solución 
utilizando Django y Django Rest Framework.

<p align="right">(<a href="#top">back to top</a>)</p>



### Construido con

* [![Next][python-shield]][python-url]
* [![Next][sqlserver-shield]][sqlserver-shield]
* [![Next][django-shield]][django-url]

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Empecemos

Para obtener una copia local del proyecto, siga los siguientes pasos.

### Requisitos Previos

* pip
  ```sh
    python get-pip.py
  ```
* Django
  ```sh
    pip install django
  ```
* Microsoft SQL Server

### Instalación

1. Clonar repositorio
   ```sh
   git clone https://github.com/Hguedez/B2B-order-management.git
   ```
2. Instalar 
   ```sh
    pip install djangorestframework
    pip install mssql-django
    pip install requests
   ```
3. Ejecute `python manage.py migrate` para la migracion de las tablas auth y `python manage.py createsuperuser` para crear tu usuario
4. Abre SQL Server Management Studio
5. Conéctese usando la autenticación de Windows
6. Haga click en `New Query`
7. Copie y pegue el contenido del archivo `db/Creates.sql` en el manejador de base de datos y ejecute el SQL
8. Copie el contenido de `Inserts.sql` para la base de datos `TechCo` y ejecute el SQL
9. Ejecute el comando `python manage.py runserver` dentro de la carpeta principal del proyecto para poder desplegarlo en la web

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- TODO -->
## TODO
Unit tests

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contacto

* hguedez21#0734

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[python-shield]: https://img.shields.io/badge/PYTHON-3.11-blue?style=for-the-badge&logo=python
[python-url]: https://www.python.org/downloads/release/python-3110/
[sqlserver-shield]: https://img.shields.io/badge/SQL%20SERVER-2022-red?style=for-the-badge&logo=microsoft%20sql%20server
[sqlserver-url]: https://www.microsoft.com/en-us/sql-server/sql-server-downloads
[django-shield]: https://img.shields.io/badge/DJANGO-4.2-white?style=for-the-badge&logo=django
[django-url]: https://www.djangoproject.com/download/
