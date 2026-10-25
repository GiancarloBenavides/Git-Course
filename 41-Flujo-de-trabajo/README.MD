# GIT-Course

<p><code>Fundamentos de GIT</code></p>
<p>Creado por <code>GncDev</code> para explicar fundamentos de <code>Sistemas operativos</code>.</p>

## Comandos Git

Confirmar los cambios requiere agregar un mensaje corto y explicito que describa los cambios realizados al grupo de trabajo.

## Agenda

1. [Plataformas en la nube](#1-plataformas-en-la-nube).
1. [Estrategias de ramificación](#2-estrategias-de-ramificación).
1. [Prefijos comunes en la industria](#2-identificar-commits).
1. [Gestión de ramas](#3-gestión-de-ramas).
1. [Corrección avanzada](#4-corrección-avanzada).

<br>

---

## 1. [Plataformas en la nube](#agenda)

- Son servicios web o plataformas en la nube.
- Almacenan repositorios de Git de forma centralizada.
- Requieren conexión a internet.
- Permiten acceder a tu código a través del navegador, interfaz gráfica o consola.

### 1.1. Servicios web mas populares ✔

| Característica              | GitHub                              | GitLab              | Bitbucket                  |
| :-------------------------- | :---------------------------------- | :------------------ | :------------------------- |
| Fundación                   | 2008                                | 2011                | 2008                       |
| Propietario                 | Microsoft                           | GitLab              | Atlassian                  |
| Open Source                 | Núcleo privativo                    | Community Edition   | Código privativo           |
| CI/CD Integrado             | GitHub Actions                      | GitLab CI/CD nativo | Bitbucket Pipelines nativo |
| Repositorios publico        | Sí, ilimitado                       | Sí, ilimitado       | Sí, ilimitado              |
| Almacenamiento privado - RP | 1GB                                 | 10GB                | 2GB                        |
| Minutos/mes de CI/CD en RP  | 2.000                               | 400                 | 50                         |
| Ideal para                  | Portfolios, Open Source, Personales | DevOps todo en uno  | si usas Jira               |



### 1.2. Herramientas ✔

- [GitHub CLI][12_1]: Consola (Windows, Linux, Mac)
- [GitHub Desktop][12_2]: Software de escritorio (Windows, Mac)
- [GitHub Pull Requests][12_3]: Extencion de VS Code

[12_1]:https://cli.github.com/
[12_2]:https://github.com/apps/desktop?locale=es-419
[12_3]:https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github

## 2. [Estrategias de ramificación](#agenda)

- Rama principal (**main**/**master**): El software listo y estable para el usuario final.
- Rama de integración (**develop**): El punto de encuentro de las nuevas funciones en desarrollo.
- Ramas de soporte (**<_prefijo_>/<_característica_>**): con prefijos que indican la tarea soportada.
- Las ramas main y develop, las ramas de soporte son de vida corta.

### 2.1. Prefijos comunes en la industria ✔

- Funcionalidades nuevas: (**feature/<_característica_>**). Ej: _feature/login-screen_
- Corrección de errores (**bugfix/<_nombre-error_>**). Ej: bugfix/fix-login-button
- Errores críticos (**hotfix/<_nombre-error_>**). Ej: bugfix/crash-on-checkout

### 2.2 Modelos populares que el arquitecto suele elegir ✔

- [GitFlow][22_1]: diseñado por [Vincent Driessen][22_2] en 2010.
- GitFlow es un modelo complejo enfocado en [versioned releases][22_3].
- [GitHub Flow][22_4]: diseñado por GitHub en 2011.
- GitHub Flow es un modelo simple enfocado en [continuous delivery][22_5].
- [GitLab Flow][22_6]: diseñado por GitLab en 2014.
- GitLab Flow añade ramas para entornos a GitFlow.
- Cualquier flujo se puede usar en [GitHub][22_7], [GitLab][22_8] o [Bitbucket][22_9].

[22_1]: https://about.gitlab.com/blog/what-is-gitflow/
[22_2]: https://nvie.com/posts/a-successful-git-branching-model/
[22_3]: https://es.wikipedia.org/wiki/Release_Management
[22_4]: https://docs.github.com/en/get-started/using-github/github-flow
[22_5]: https://es.wikipedia.org/wiki/Entrega_continua
[22_6]: https://about.gitlab.com/es/topics/version-control/what-is-gitlab-flow/
[22_7]: https://github.com/
[22_8]: https://about.gitlab.com/es/
[22_9]: https://bitbucket.org/product/

### 1.3 Tabla Comparativa: GitFlow vs GitHub Flow ✔

| Característica           | GitFlow                                         | GitHub Flow                                  |
| :----------------------- | :---------------------------------------------- | :------------------------------------------- |
| Ramas principales        | `main` `develop` (producción y desarrollo)      | Únicamente `main`                            |
| Ramas de soporte         | `feature/*`, `release/*`, `hotfix/*`            | `feature/*` de vida corta                    |
| Complejidad              | `Alta`; protocolo estricto                      | `Baja`; simple y ligera                      |
| Ciclo de lanzamientos    | versioned releases                              | Continuous Delivery                          |
| Corrección en producción | Mediante ramas `hotfix/*` desde `main`          | directamente desde `main`                    |
| Ideal para               | Equipos grandes y [Waterfall development][13_1] | Equipos pequeños y [Agile development][13_2] |

[13_1]: https://es.wikipedia.org/wiki/Desarrollo_en_cascada
[13_2]: https://es.wikipedia.org/wiki/Desarrollo_%C3%A1gil_de_software

---

## Mas Recursos

- [Herramienta Gráfica](https://git-school.github.io/visualizing-git/) (Git-school)
- [Git Tutorial](https://www.atlassian.com/git/glossary#commands) (Atlassian)
- [GIt Book](https://git-scm.com/book/en/v2) (Git-scm)
- [Reference](https://git-scm.com/docs) (Git-scm)
- [Video-curso](https://www.youtube.com/watch?v=GwkgaANyjjw&list=PLTd5ehIj0goMCnj6V5NdzSIHBgrIXckGU) (YouTube)
