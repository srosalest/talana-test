# Talana-Kombat

* Notes:
    * Repo folder must be shared with Docker, so it can be mounted.
    * Code and documentation related to the code is in english.
    * Questions are in spanish.

## To run and build the image use the included Makefile.
- To build the image run `$ make build`
- To run the image for the first time, execute `$ make run`
- To stop without deleting the running container, `$ make stop`
- To restart the container, `$ make start`
- To access the container bash (container must be running), `$ make bash`
- To remove images and container (container must be stopped before), execute `$ make purge`
- To remove the container, `$ make container`
- To remove the image, `$ make remove-image`
- To install install depedencies listed in the requirements file, `$ make requirements`
- For help please execute `$ make help`

### Documentation:
- The architecture is a simple monolith.
- Folder structure is clear to read, code is not documented as the tests and code it self its readable and understandable
- Engineering requirements are clear and given in the Desafio TalanaKombat - Software Developer Engineer.docx which is private.
- To execute the code given an arg, which can be a file path or a json string, `$ python3 code/kombat/kombat.py {arg}`

### Preguntas generales:
* Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. Explica cómo se soluciona si hiciste push, y cómo si aún no hiciste. De ser posible, que quede solo un commit con los cambios.

    * Mediante el uso de fixup y con rebase interactivo con auto-squash.
    
    ```
    git add {forgotten_file}
    git commit --fixup {commit_hash}
    git rebase --autosquash -i HEAD~2
    git push -f
    ```
    Para el caso de aún no realizar el push, simplemente usando --amend
    
    ```
    git add {forgotten_file}
    git commit --amend --no-edit
    ```

* Si has trabajado con control de versiones ¿Cuáles han sido los flujos con los que has
trabajado?

    * Principalmente CI/CD, lo que implica la creacion de branchs para desarrollo, pull requests y merge. Dentro de estos estan los flujos de código usuales de desarrollo, pull, fetch, rebase, merge, cherry-picking, reverts.

* ¿Cuál ha sido la situación más compleja que has tenido con esto?

    * Al hacer reverts en branch de desarrollo (previo a producción) en los cuales modelos fueron afectados. (Revert y solucionar conflictos en contra del tiempo.)

* ¿Qué experiencia has tenido con los microservicios?

    * 1 año en Uber trabajando con microservicios (Eats-platform), en los cuales hubo que crear nuevos endpoints orientados a integraciones en Uber eats. Comunicación entre microservicios con grpc protoc.

* ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué?

    * Lamda, permite escalar de forma serverless, procesando a demanda con estados o triggers. Fácil de integrar y combinado con S3 o BD permiten un flujo de datos on demand.
