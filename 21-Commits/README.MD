# GIT-Course
<p><code>Fundamentos de GIT</code></p>
<p>Creado por <code>GncDev</code> para explicar fundamentos de <code>Sistemas operativos</code>.</p>

## Commits
Confirmar los cambios requiere agregar un mensaje corto y explicito que describa los cambios realizados al grupo de trabajo.

## Agenda
1. [Recomendaciones generales](#1-recomendaciones-generales).
1. [Guías de estilo](#2-guías-de-estilo).
1. [Estructura](#3-estructura).
1. [Emojis](#4-emojis).

<br>

---
## 1. [Recomendaciones generales](#agenda)
* Explicito siempre es mejor que implícito.
* No uses mayúsculas o signos de puntuación en el título.
* Usa un prefijo o emojis para clasificarlos por tipo.
* Usa un ámbito para clasificarlos por espacio de trabajo.
* Usa un máximo de 50 caracteres para el titulo.
* Sigue y respeta una especificación.
* Usa o construye una utilidad. 

### 1.1. Clasificación por complejidad ✔
* [__fix:__][11_1] esta relacionado con optimizaciones, ajustes menores o correcciones de errores; típicamente agrupados en un PATCH.
* [__feat:__][11_1] esta relacionado con nuevas funcionalidades que mantienen compatibilidad con hacia atrás; típicamente agrupadas en una version MINOR.
* [__Breaking-changue:__][11_1] esta relacionado con cambios que no mantienen compatibilidad con la funcionalidad anterior; agrupadas en una version MAYOR.

[11_1]:https://semver.org/lang/es/

### 1.2. Clasificación por espacio de trabajo ✔
* Un ámbito o [scope][12_1] especifica la base de código que afecta el cambio.
* El ámbito depende del proyecto específico.
* No debe ser un identificador de problema [issue][12_2].
* Puede ser un modulo [`core`, `compiler`, `controller`, `model`...]
* En un [monorepo][12_3] puede ser un proyecto [`api`, `web`, `app`...]

[12_1]:https://en.wikipedia.org/wiki/Scope_(computer_science)/
[12_2]:https://docs.github.com/es/issues/tracking-your-work-with-issues/about-issues
[12_3]:https://www.atlassian.com/git/tutorials/monorepos

## 2. [Guías de estilo](#agenda)
* Conjunto de normas usadas para escribir código.
* Útiles para trabajar en entornos colaborativos.
* Permiten automatizar procesos.
* Útiles para mantener un estilo.

### 2.1. Especificaciones ✔
* [Commits Convencionales][21_1].
* [Angular Contributing][21_2].
* [Vue Commit Message Convention][21_3].
* [Svelte Pull Request Template][21_4].

[21_1]:https://www.conventionalcommits.org/es/v1.0.0/
[21_2]:https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines
[21_3]:https://github.com/vuejs/core/blob/main/.github/commit-convention.md
[21_4]:https://github.com/sveltejs/svelte/blob/main/.github/PULL_REQUEST_TEMPLATE.md

### 2.2. Utilidades ✔
* [Commitlint:][22_1] Node Commit linter.
* [Commit-linter:][22_2] Python commit linter.
* [Commitlint.io][22_3] Online commit linter.
* [Husky:][22_4] Commit and code linter - run tests.

[22_1]:https://commitlint.js.org/
[22_2]:https://pypi.org/project/commit-linter/
[22_3]:https://commitlint.io/
[22_4]:https://typicode.github.io/husky/


## 3. [Estructura](#agenda)

```xml
<type>[OPTIONAL (<scope>)][optional !]: <description>
<blank-line>
[OPTIONAL <body max-line-length=50>]
<blank-line>
[OPTIONAL <footer(s)>]
```

### 3.1. Semántica ✔
* __Type:__ Agrega un tipo usa un verbo imperativo.
* __Scope:__ Si es necesario puedes agregar un ámbito.
* __!:__ Se incluye cuando los cambios rompen la compatibilidad.
* __Description:__ Inicia con un verbo en imperativo.
* __Body:__ Agrega todo el contexto necesario en varias lineas.
* __Footer:__ Si es necesario puedes agregar un ámbito.


### 3.2. Restricciones ✔
* Es posible restringir las opciones de clasificación.
* El tipo puede uno de [`feat`, `fix`, `refactor`, `revert`, `test`, `ci`, `chore`]
* El ámbito puede ser uno de [`api`, `web`, `app`]

### 3.3. Ejemplos sin contexto ✔
```sh
# Commit simple
fix: fix wrong calculation of request body checksum
```
```sh
# Commit scope
feat(web): add email notifications
```
```sh
# Commit breaking-changue
feat!: remove ticket list endpoint
```
```sh
# Commit refactor
refactor: implement calculation as recursion
```

## 3.4. Ejemplos con contexto ✔
```sh
# Commit breaking-changue
feat!: remove ticket list endpoint

refers to JIRA-1337

BREAKING CHANGES: ticket endpoints no longer supports list all entities.
```

## 4. [Emojis](#agenda)
* Es un pictograma incrustado en el texto.
* Están incorporados al estándar Unicode.
* Disponibles es multiples plataformas.
* 💥🔥✨🪲🐛🐞🔨♻️🚨✔️📚📖🔧💎🚀📦🎉🔙🔀


### 4.1. Tipos básicos ✔
| Type      | Version | ⬇️ | VSCode    | Code         |
|:----------|:--------|:--:|:----------|:-------------|
| BREAKING: | MAYOR   | 💥 | colisión  | `:boom:`     |
| feat:     | MINOR   | ✨ | chispas   | `:sparkles:` |
| fix:      | PATCH   | 🐞 | mariquita | `:ladybird:` |
| refactor: | PATCH   | ♻️ | reciclaje | `:recycle:`  |
| chore:    | NONE    | ⚙️ | engranaje | `:gear:`     |


### 4.2. Subtipos ✔
|  Type     | Subtype | ⬇️ | VSCode  | Code         |
|:----------|:--------|:--:|:--------|:-------------|
| refactor: | secure: | 🛡️ | escudo  | `:shield:`   |
|		    | style:  | 💄 | labial  | `:lipstick:` |
|           | perf:   | ⚡ | voltaje | `:zap:`      |
| chore:    | docs:   | 📝 | memo    | `:memo:`     |
|           | test:   | 👀 | ojos    | `:eyes:`     |
|           | ci:     | 🤖 | robot   | `:robot:`    |
|           | build:  | 🚀 | cohete  | `:rocket:`   |


### 4.4. [Ejemplos con emojis](#agenda)
```sh
# Commit simple
✨ add email notifications
```
```sh
# Commit scope
🐞 (api) fix wrong calculation of request body checksum
```
```sh
# Commit breaking-changue
💥 remove ticket list endpoint
```
```sh
# Commit refactor
♻️ implement calculation as recursion
```


---
## Mas Recursos
- [Sistema de control de versiones](https://es.wikipedia.org/wiki/Control_de_versiones) (Wikipedia)
- [Guías de código abierto](https://opensource.guide/es/) (OpenSource)
- [Versionado semántico](https://semver.org/lang/es/) (semver)
- [Especificación](https://www.conventionalcommits.org/es/v1.0.0/#especificación) (Conventional Commits)
- [Commit](https://en.wikipedia.org/wiki/Commit_(version_control)) (Wikipedia)
