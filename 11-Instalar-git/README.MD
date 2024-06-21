# GIT-Course
<p><code>Fundamentos de GIT</code></p>
<p>Creado por <code>GncDev</code> para explicar fundamentos de <code>Sistemas operativos</code>.</p>

## Control de Versiones
Antes de comenzar a usar Git, debe hacerlo disponible en su computadora. Incluso si ya está instalado, probablemente sea una buena idea actualizar a la última versión.

## Agenda
1. [Instalación de wsl](#1-instalación-de-wsl).
1. [Instalación de git](#2-instalación-de-git).
1. [Instalación de SSH](#3-instalación-de-ssh).
1. [Instalación de Github](#4-instalación-de-github).
1. [Instalación de VSCode](#5-instalación-de-vscode).

<br>

---
## 1. [Instalación de wsl](#agenda)
El Subsistema de Windows para Linux, [WSL][1]; es una capa de compatibilidad desarrollada por Microsoft para ejecutar binarios de Linux

![Arquitectura WSL](https://code.visualstudio.com/assets/docs/remote/wsl/architecture-wsl.png)

[1]:https://es.wikipedia.org/wiki/Subsistema_de_Windows_para_Linux

### 1.1. Habilitar pre-requisitos para WSL en Windows ✔
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

#### 1.1.1. Comandos.

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

### 1.2. Instalación de WSL para desarrollo ✔
* Instalar [subsistema Linux][12_1] para Windows.
* Instalar [distribución de Linux][12_2] elegida.
* Instalar y [configurar nano][12_3] en WSL. 

[12_1]:https://learn.microsoft.com/es-mx/windows/wsl/install
[12_2]:https://code.visualstudio.com/docs/remote/linux
[12_3]:https://ubunlog.com/nanorc-configura-editor-texto/

#### 1.2.1. Comandos instalación.

```ps
# EN POWERSHELL DE WINDOWS
# ------------------------
# Instalar WSL
# El comando --install realiza las acciones siguientes:
#   * Habilita los componentes opcionales de WSL.
#   * Descarga e instala el kernel de Linux más reciente.
#   * Establece WSL 2 como valor predeterminado.
#   * Descarga e instala la distribución de Ubuntu Linux.
wsl --update
wsl --install
# Nota: es posible que sea necesario reiniciar.
```

#### 1.2.2. Comandos actualización y prueba.

```bash
# EN BASH DE WSL
# --------------
#   * Mantener la distribución WSL actualizada.
sudo apt update && sudo apt upgrade
#   * Instalar nano.
sudo apt install nano
#   * Prueba la siguiente tubería en el subsistema Linux
#     notar que combina comandos de win32 y comandos de WSL. (poderoso)
ipconfig.exe | grep -a IPv4 | cut -d: -f2
#   * Obtener el shell que se esta ejecutando en wsl 
echo $SHELL
```

### 1.2.2. Comandos prueba desde windows.

```ps
# EN POWERSHELL DE WINDOWS
# ------------------------
#   * Prueba la siguiente tubería de comandos en Windows y comunica el resultado a WSL
ipconfig | wsl grep -a IPv4 | wsl cut -d: -f2
wsl lsb_release -a
```

## 2. [Instalación de Git](#agenda)
* Recomendamos instalar [Git][2] en Linux o dentro de WSL (git nativo)
* Eliminar versiones antiguas de Git incluidas en la distribución.
* Agregar repositorio oficial de los mantenedores de Git.
* Actualizar lista de paquetes.
* Instalar la ultima version de Git.
* Agregar un <code>usuario</code> y un <code>correo</code> globalmente para Git.

[2]:https://es.wikipedia.org/wiki/Git

### 2.1. Comandos instalar Git ✔

```bash
# Eliminar versiones antiguas de GIT
sudo apt remove git
# Agregar repositorio PPA
sudo add-apt-repository ppa:git-core/ppa -y
# Actualice su sistema
sudo apt update && sudo apt install git-all -y
# Verifique la versión desde WSL
git --version
# Verifique la versión desde la terminal de windows
wsl git --version
# Para agregar usuario y correo globales a GIT
git config --global user.name "GncDev"
git config --global user.email gncdev@dominio.com
# Para agregar usuario empresarial a un solo repositorio
git config user.email gncdev@empresa.com
# Para verificar las configuraciones añadidas
git config -l
```
## 3. [Instalación de SSH](#agenda)
* La mayoría de distribuciones Linux incluye un cliente [ssh][31_1].
* wsl/ubuntu incluye una suite [OpenSSH][31_2].
* La suite OpenSSH incluye un [agente SSH][31_3].
* Verificar la instalación de un [cliente][31_4] ssh.
* Verificar que el [agente][31_5] este configurado.

[31_1]:https://es.wikipedia.org/wiki/Secure_Shell
[31_2]:https://es.wikipedia.org/wiki/OpenSSH
[31_3]:https://es.wikipedia.org/wiki/SSH-Agent
[31_4]:https://manpages.ubuntu.com/manpages/noble/en/man1/ssh.1.html
[31_5]:https://manpages.ubuntu.com/manpages/noble/en/man1/ssh-agent.1.html

### 3.1. Comandos para verificar el funcionamiento de ssh ✔
```bash
# Verifique la version de ssh y openssl version
apt list openssh-client
# Instale un cliente SSH si no esta instalado
sudo apt update && sudo apt install openssh-client
# Verifique el agente tiene un identificador de proceso asociado
ps -C ssh-agent
# Verifique que existen las variables de entorno necesarias $SSH_AGENT_PID, $SSH_AUTH_SOCK
echo $SSH_AGENT_PID $SSH_AUTH_SOCK
env | grep -i ssh
# Si no se esta ejecutando inicie el ssh-agent in background
eval $(ssh-agent -s)  
```


## 4. [Instalación de GitHub](#agenda)
* Crear una cuenta en [GitHub][4_1].
* Crear una [clave publica][4_2] en wsl.
* Registra la [clave publica][4_3] en Github.
* Crear un repositorio [nuevo][4_4] en github.
* Clonar este [repositorio][4_5] desde wsl.

[4_1]:https://github.com/
[4_2]:https://docs.github.com/es/authentication/connecting-to-github-with-ssh
[4_3]:https://github.com/settings/ssh/new
[4_4]:https://github.com/new
[4_5]:https://github.com/GiancarloBenavides/Git-Course.git


### 4.1. Comandos configurar al agente ssh ✔

```bash 
# Crear un directorio oculto en la carpeta de usuario de wsl </home/user>
mkdir ~/.ssh && cd ~/.ssh
# Generar un par de llaves (publica:privada) para usar con github
	# -f id_ed25519 			:para nombrar al archivo
	# -C "gncdev@dominio.home"	:Agrega comentario al final de la llave
ssh-keygen -t ed25519 -f id_ed25519 -C "gncdev@dominio.home"             	
# Agregue la clave privada al agente ssh
ssh-add ~/.ssh/id_ed25519
# Copie el contenido de la clave púbica y agréguelos a las claves en github
cat ~/.ssh/id_ed25519.pub | clip.exe
# Puede usar esta misma clave para autenticarse por ssh con otros remotos
```


### 4.2. Comandos para clonar un repositorio desde github ✔
```bash
# En wsl crear o dirigirse a la carpeta donde se almacenaran repositorios
mkdir ~/repositorios && cd ~/repositorios
# En la carpeta clonar por SSH el repositorio remoto (sin usuario y contraseña)
git clone git@github.com:GiancarloBenavides/Git-Course.git
# Ahora puedes modificar este repositorio en local
```


### 4.3. Comandos para crear y enviar un repositorio a github ✔
```bash
# Crear un repositorio y enviar cambios
mkdir ~/repositorio && cd ~/repositorio
git init
echo "Repositorio de prueba" > README.MD
git add .
git commit -m "feat: readme initial commit"
git remote add origin git@github.com:GiancarloBenavides/repositorio
git push origin master
# Recuerde que puede gestionar git desde windows anteponiendo wsl
# log de los últimos 10 commits en formato de una linea
wsl git log -10 --oneline
```


### 4.4. Comandos adicionales por si no puede conectarse a github ✔

```bash
# Verifique que no existen multiples agentes ejecutándose
ps -C ssh-agent
# Elimine los agentes que no coincidan con la variable $SSH_AGENT_PID
kill -9 {PID}
# Verifique que la clave privada se agrego al agente ssh
ssh-add -l
# Verifique que las URL remotos están agregados 
git remote -v
# Verifique la conexión con github (You've successfully authenticated)
ssh -vT git@github.com
# Verifique la conexión con el repositorio
git fetch
```


## 5. [Instalación de VSCode](#agenda)
* Instalar [visual studio code][5_1] en Windows.
	* Agregar abrir con code a los menus contextuales.
	* Agregar code al PATH code a los menus contextuales.
* Instalar [extensión WSL][5_2] o el [paquete para desarrollo remoto][5_3].
* Conectar el editor code con wsl.

[5_1]:https://code.visualstudio.com/download
[5_2]:https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl
[5_3]:https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack


## 5.1 Configuración del editor de código ✔
Antes de comenzar a usar Git, debe hacerlo disponible en su computadora; Incluso si ha instalado la [version compatible][51_1] de git para windows, probablemente sea una buena idea actualizar a la última versión.


[51_1]:https://git-scm.com/download/win


### 5.1.1. Instalar extensiones básicas de VScode ✔
* Instalar [corrector ortográfico][511_1].
* Instalar [diccionario español][511_2].
* Instalar [indentación][511_3] en colores.
* Instalar la [extension de GitHub][511_4] para VScode.
* Instalar la [extension wsl][511_5] para desarrollo remoto.
* Instalar la [extension iconos][511_6] para desarrollo remoto.


[511_1]:https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker
[511_2]:https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker-spanish
[511_3]:https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow
[511_4]:https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github
[511_5]:https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl
[511_6]:https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons


### 5.1.2. Excluir archivos y carpetas ✔
* Abrir el repositorio remoto (en WSL) desde VScode.
* Puedes configurar [Git][512_1] para que ignore archivos que no quieres indexar.
* No se hará seguimiento ([versionado][512_2]) de estos archivos o carpetas.
* No se enviaran al [repositorio remoto][512_3] los cambios realizados en estos archivos.
* Cree un archivo [.gitignore][512_4] en el repositorio desde VSCode.
* Incluir los [patrones][512_5] a ignorar en el archivo .gitignore.

[512_1]:https://es.wikipedia.org/wiki/Git
[512_2]:https://es.wikipedia.org/wiki/Control_de_versiones
[512_3]:https://docs.github.com/es/get-started/getting-started-with-git/ignoring-files
[512_4]:https://git-scm.com/docs/gitignore
[512_5]:https://github.com/github/gitignore

#### 5.1.2.1. Ejemplo gitignore
```bash
# VS Code files for those working on multiple tools
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
```


---
## Mas Recursos
- [Hyper-V](https://es.wikipedia.org/wiki/Hyper-V) (Wikipedia)
- [GIt Book](https://git-scm.com/book/en/v2) (Git-scm)
- [Reference](https://git-scm.com/docs) (Git-scm)