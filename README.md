# mutantsDetector
Detector de Mutantes en las bases de la cadena de ADN para reclutar Mutantes en la lucha contra los X-Men

## Endpoints
/mutant

/stats

## Usage

La api /mutant/ detecta ADN mutante dentro de una cadena de entrada.

Si el ADN es mutante la respuesta sera HTTP 200-OK, en caso contrario un 403-Forbidden.
```
POST → /mutant/ 
BODY { “dna”:["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"] }
```

La api /stats/ devuelve un Json con las estadísticas de las verificaciones de ADN: 
```
GET → /stats/
RESPONSE { “count_mutant_dna”:40, “count_human_dna”:100, “ratio”:0.4 }
```

---

## Instalación
App Specification: Python 2.7, SQLAlchemy

Requerimientos de ambiente: Python 2.7, pip, virtualenv (opcional)

#### Se recomienda usar virualenv para crear el ambiente de desarrollo.
```
virtualenv mutantsDetector
cd mutantsDetector
Scripts\activate
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
Nota: La primer línea de esta propiedad, responde solo a la configuración de AWS.
#### Crear el modelo de tablas
Se debe ejecutar lo siguiente en el root de la aplicación:
```
python create_database.py
```
#### Levantar el ambiente
```
python application.py
```
Url de prueba:
http://localhost:5000/stats

#### Configuraciones
### Aplicación
Desde el archivo config\app_config.py se pueden modificar los siguientes parámetros:

MIN_OCURRENCE_NEEDED
##### Cantidad de bases repetidas sucesivas para tomar a un gen como mutado
MIN_MUTANT_DNA_COUNT
##### Cantidad de genes mutados requeridos para ser considerado como mutante
MATRIX_I_LENGTH
##### Largo de la matriz requerido
MATRIX_X_LENGTH
##### Ancho de la matriz requerido

### Logs
Dentro del archivo config\log_config.py se podrá configurar los distintos métodos de log.

### Configuración de AWS
Para evitar problemas de performance, se agregará una nueva instancia automáticamente cuando la salida de la red sea mayor o igual a 20000 bytes por minuto, durante 5 minutos seguidos.

### Tests
Para ejecutar los test unitarios, se debe de ejecutar el siguiente comando desde el root de la aplicación.
```
python test_application.py
```