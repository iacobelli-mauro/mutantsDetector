# mutantsDetector
Detector de Mutantes en base a la cadena de ADN para reclutar Mutantes en la lucha contra los X-Men

## Endpoints
/v1/mutant

/v1/stats

## Usage

La api /mutant/ detecta si un humano es mutante enviando la secuencia de ADN mediante un HTTP POST
En caso de verificar un mutante, devuelve un HTTP 200-OK, en caso contrario un 403-Forbidden

```
POST → /mutant/ 
BODY {“dna”:["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]}
```

La api /stats/ devuelve un Json con las estadísticas de las verificaciones de ADN: 

{“count_mutant_dna”:40, “count_human_dna”:100, “ratio”:0.4}

```
GET→“/stats/” 
```

---

## Instalación
App Specification: Python 2.7, SQLAlchemy

Requerimientos de ambiente: Python 2.7, pip, virtualenv (opcional)

#### Se recomienda usar virualenv para crear el ambiente de desarrollo.
```
virtualenv mutantsDetector
```
#### Clonar el repo dentro del directorio creado en el paso anterior.
```
git clone https://github.com/iacobelli-mauro/mutantsDetector.git
```
#### Actualizar las dependencias del proyecto
```
pip install -r requerimients.txt
```
#### Configurar la base de datos
Se debe modificar el archivo app_config.py. 
La linea a modificar es la siguiente.
```
SQLALCHEMY_DATABASE_URI = 'mysql://user:password@host/database?charset=utf8'
```
#### Crear el modelo de tablas
Se debe ejecutar lo siguiente:
```
python config\create_database.py
```
#### Levantar el ambiente
```
python application.py
```
Url de prueba:
http://localhost:5000/stats

#### Configuraciones
### Picos de trafico dinamicos 

Para evitar problemas de performance, se agregara una nueva instancia automaticamente cuando el uso del CPU sea de 20000 bytes por minuto, durante 5 minutos. 

### Tests
Para ejecutar los test unitarios, se debe de ejecutar el siguiente comando.
```
python test_application.py
```