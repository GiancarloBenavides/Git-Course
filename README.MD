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

![Arquitectura WSL](https://code.visualstudio.com/assets/docs/remote/wsl/architecture-wsl.png)

[1]:https://es.wikipedia.org/wiki/Git

## 1.1. Habilitar pre-requisitos para WSL en Windows ✔
* Habilitar [virtualización por hardware][11_1] sino esta habilitado. 
* Activar plataforma [Hyper-V][11_2] para virtualización.
* Activar el [subsistema Linux][11_3] para Windows.
* Instalar [windows Terminal][11_4] de Microsoft.
* Elegir una distribución [compatible][11_5] con desarrollo remoto.

[11_1]:https://community.acer.com/kb/articles/14750
[11_2]:https://support.microsoft.com/es-es/windows/habilitar-la-virtualizaci%C3%B3n-en-equipos-windows-11-c5578302-6e43-4b4b-a449-8ced115f58e1
[11_3]:https://learn.microsoft.com/es-mx/windows/wsl/install
[11_4]:https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=es-co&gl=co&rtc=1
[11_5]:https://apps.microsoft.com/store/detail/ubuntu-22042-lts/9PN20MSR04DW

>Nota: Versiones superiores a Windows 10.19041 y Windows 11.22621

### 1.1.1. Comandos.

```ps
# Habilitar Hyper-V en windows 10
pushd "%~dp0"
dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hyper-v.txt
for /f %%i in ('findstr /i . hyper-v.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"
del hyper-v.txt
Dism /online /enable-feature /featurename:Microsoft-Hyper-V -All /LimitAccess /ALL
pause
# Activar WSL
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
# Lista de las distribuciones de Linux disponibles
wsl --list --online
```

## 1.2. Instalación de WSL para desarrollo ✔
* Instalar [subsistema Linux][12_1] para Windows.
* Instalar [distribución de Linux][12_2] elegida.
* Instalar y [configurar nano][12_3] en WSL. 

[12_1]:https://learn.microsoft.com/es-mx/windows/wsl/install
[12_2]:https://code.visualstudio.com/docs/remote/linux
[12_3]:https://ubunlog.com/nanorc-configura-editor-texto/

### 1.2.1. Comandos.

```ps
# EN POWERSHELL DE WINDOWS
# ------------------------
# Instalar WSL
# El comando --install realiza las acciones siguientes:
#   * Habilita los componentes opcionales de WSL.
#   * Descarga e instala el kernel de Linux más reciente.
#   * Establece WSL 2 como valor predeterminado.
#   * Descarga e instala la distribución de Ubuntu Linux
wsl --update
wsl --install
# Nota: es posible que sea necesario reiniciar
```

```bash
# EN BASH DE WSL
# --------------
#   * Mantener la distribución WSL actualizada
sudo apt update && sudo apt upgrade
#   * Instalar nano
sudo apt install nano
#   * Prueba la siguiente tubería de comandos en WSL
ipconfig.exe | grep -a IPv4 | cut -d: -f2
```

```ps
# EN POWERSHELL DE WINDOWS
# ------------------------
#   * Prueba la siguiente tubería de comandos en Windows
ipconfig | wsl grep -a IPv4 | wsl cut -d: -f2
```

## 1.3. Instalación de Git en Linux o dentro de WSL ✔
* Eliminar versiones antiguas de Git incluidas en la distribución.
* Agregar repositorio oficial de los mantenedores de Git.
* Actualizar lista de paquetes.
* Instalar la ultima version de Git.
* Agregar un <code>usuario</code> y un <code>correo</code> globalmente para Git.

### 1.3.1. Comandos.

```bash
# Eliminar versiones antiguas de GIT
sudo apt remove git
# Agregar repositorio PPA
sudo add-apt-repository ppa:git-core/ppa -y
# Actualice su sistema
sudo apt update && sudo apt install git-all -y
# Verifique la versión
git --version
# Para agregar usuario y correo globales a GIT
git config --global user.name "GncDev"
git config --global user.email gncdev@dominio.com
```

## 1.4. Agregar GitHub ✔
* Crear una cuenta en [GitHub][14_1].
* Crear una [clave publica][14_2] en wsl.
* Registra la [clave publica][14_3] en Github.
* Crear un [repositorio nuevo][14_4] en GitHub.
* Clonar [repositorio][14_5] desde Wsl.

[14_1]:https://github.com/
[14_2]:https://docs.github.com/es/authentication/connecting-to-github-with-ssh
[14_3]:https://github.com/settings/ssh/new
[14_4]:https://github.com/new
[14_5]:https://github.com/GiancarloBenavides/Git-Course.git

### 1.4.1. Comandos.

```bash
# Crear una clave publica
mkdir ~/.ssh && cd ~/.ssh

id
ssh-keygen -t ed25519 -f id_github  # sever_name=file=github, pass=***
eval $(ssh-agent -s)                # start ssh-agent in background
ssh-add ~/.ssh/id_github
# Crear un nuevo repositorio local
git init
# Clonar un repositorio remoto por http con usuario y contraseña
git clone https://github.com/GiancarloBenavides/Git-Course.git
# Clonar un repositorio remoto por http con usuario y contraseña
git clone https://github.com/GiancarloBenavides/Git-Course.git
```

## 1.4. Instalación del editor de código ✔
* Instalar [visual studio code][13_1] en Windows.
* Instalar [extensión WSL][13_2] o el [paquete para desarrollo remoto][13_3].
* Instalar [extension para corregir ortografía][13_4] y la [extension del idioma][13_5].
* Instalar la [extension de GitHub][14_3] para VScode.

[13_1]:https://code.visualstudio.com/download
[13_2]:https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl
[13_3]:https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack
[13_4]:https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker
[13_5]:https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker-spanish
[14_3]:https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github



## 2. [Configuración](#agenda)
Antes de comenzar a usar Git, debe hacerlo disponible en su computadora. Incluso si ya está instalado, probablemente sea una buena idea actualizar a la última versión.

## 2.1. Extensiones de VScode ✔
* Instalar [corrector ortográfico][21_1].
* Agregar [diccionario español][21_1].
* Colorear [indentation][21_3].

[21_1]:https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker
[21_2]:https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker-spanish
[21_3]:https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow



* clonar el repositorio remoto desde VScode.




```bash
lsb_release -a
echo $SHELL
git --version

ls -hal /usr/share/git-core/contrib/
find / -type d -name 'httpdocs'
sudo nano -l /usr/lib/git-core/git-sh-prompt

```



Instalar [Git][1_2]

[1_2]:https://git-scm.com/download/win











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
- [Hyper-V](https://es.wikipedia.org/wiki/Hyper-V) (Wikipedia)
- [GIt Book](https://git-scm.com/book/en/v2) (Git-scm)
- [Reference](https://git-scm.com/docs) (Git-scm)
- [Video-curso](https://www.youtube.com/watch?v=GwkgaANyjjw&list=PLTd5ehIj0goMCnj6V5NdzSIHBgrIXckGU) (YouTube)