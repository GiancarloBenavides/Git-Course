# GIT-Course
<p><code>Fundamentos de GIT</code></p>
<p>Creado por <code>GncDev</code> para explicar fundamentos de <code>Sistemas operativos</code>.</p>

## Control de Versiones
Se llama control de versiones a la gestión de los diversos cambios que se realizan sobre los elementos de algún producto o una configuración del mismo

## Agenda
1. [Instalación](#1-instalación).
1. [Configuración](#2-configuración).
1. [Comandos](#3-comandos).
1. [Buenas practicas](#4-buenas-practicas).

<br>

---
## 1. [Instalación](#agenda)
Antes de comenzar a usar Git, debe hacerlo disponible en su computadora. Incluso si ya está instalado, probablemente sea una buena idea actualizar a la última versión.

## 1.1. Instalación de WSL ✔


## 1.2. Instalación de git en Linux o dentro de WSL ✔
* Eliminar versiones antiguas de GIT.
* Agregar repositorio PPA Oficial.
* Actualizar lista de paquetes.
* Instalar la ultima version de git.

```bash
# Eliminar versiones antiguas de GIT
sudo apt remove git
# Agregar repositorio PPA
sudo add-apt-repository ppa:git-core/ppa -y
# Actualice su sistema
sudo apt update && sudo apt install git-all -y
# Verifique la versión
git --version
```

## 1.3. Pasos adicionales ✔
* Crear una cuenta en [github][13_1].
* Instalar [VSCode][13_2]
* Instalar la [extension de github][13_3] para VScode.
* Crear un [repositorio nuevo][13_4] en Github.

[13_1]:https://github.com/
[13_2]:https://code.visualstudio.com/download
[13_3]:https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github
[13_4]:https://github.com/new


```bash
echo $SHELL
ls -hal /usr/share/git-core/contrib/

```


Instalar [Git][1_2]
[1_2]:https://git-scm.com/download/win





## 2. [Configuración](#agenda)
* Agregar <code>Usuario</code> y <code>Correo</code> globalmente para Git.
* clonar el repositorio remoto desde VScode.


```bash
# Para agregar Usuario y Contraseña a GIT
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

## 2.1. Excluir archivos y carpetas ✔
* Puedes configurar [Git][21_1] para que ignore archivos que no quieres indexar.
* No se hará seguimiento ([versionado][21_2]) de estos archivos o carpetas.
* No se enviaran al [repositorio remoto][21_3] los cambios realizados en estos archivos.
* Cree un archivo [.gitignore][21_4] en el repositorio.
* Incluir los [patrones][21_5] a ignorar en el archivo .gitignore.

[21_1]:https://es.wikipedia.org/wiki/Git
[21_2]:https://es.wikipedia.org/wiki/Control_de_versiones
[21_3]:https://docs.github.com/es/get-started/getting-started-with-git/ignoring-files
[21_4]:https://git-scm.com/docs/gitignore
[21_5]:https://github.com/github/gitignore


## 3. [Comandos](#agenda)


## 4. [Buenas practicas](#agenda)

## 4.1. Mensajes en los commits ✔
* Usar la especificación de [Commits Convencionales][41_1].

[41_1]:https://www.conventionalcommits.org/es/v1.0.0/



---
## Mas Recursos
- [GIt Book](https://git-scm.com/book/en/v2) (Wikipedia)
- [Reference](https://git-scm.com/docs) (Wikipedia)
- [Video-curso](https://www.youtube.com/watch?v=GwkgaANyjjw&list=PLTd5ehIj0goMCnj6V5NdzSIHBgrIXckGU) (YouTube)