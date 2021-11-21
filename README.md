# Cython benchmark

> Comparación de rendimiento del algoritmo de la ecuación de calor utilizando python puro y cython.

El programa resuelve la ecuación de calor que es una ecuación diferencial parcial, para una simulación numerica de un plano en dos dimenciones de una botella en un entorno con cierta temperatura, de la cual se vigila la evolución en el tiempo por un determinado periodo. Para mas información sobre la ecuación, se encuentra un documento en el directorio ```docs/``` del repositorio.

El objetivo es medir el rendimiento de procesamiento del programa utilizando python puro como se hace en el archivo ```heat.py`` y con una versión optimzada del mismo, utilizando *cython*, un compilador estatico para programas en python, que permite genera codigo eficiente en *C*, obteneniendo la mayoria de ventajas del lenguaje compilado, especialemtene la velocidad. De esta forma se comparan los resultados obtenidos con ambas versiones para visualizar la mejora.

## Instalación

Para el uso del programa se debe descargar el respositorio e instalar los paquetes de python necesarios para su funcionamiento.

```zsh
git clone https://github.com/SebastianSierrajc/cython-benchmark.git
cd cython-benchmark
```

Para la instalacion de paquetes se recomienda crear un entorno virtual para el proyecto
probar con el comando ```python``` o ```python3```

> creación entorno virtual python.
```zsh
python3 -m venv venv
source venv/bin/activate  
```

> Instalación de los paquetes.
```zsh
pip install -r requirements.txt
```

## Compilación

Para usar el modulo construido en cython se debe compilar para generar el codigo en *C*
> Compilación modulo cython.
```zsh
python setup.py build_ext --inplace
```

Con esto se deben genar el codigo en *C* y el modulo con extensión ```.so``` que el programa de python puede importar, adicinalmente se genera unos archivos ```.html``` que muestran el resultado de la compilacion del codigo de python y cython (el resultado se pued ver en el directorio ```docs```). El proyecto deberia tener la siguiente estructura.

> Estructura del proyecto.
```zsh
.
├── benchmark.py
├── build
├── cyheat.c
├── cyheat.html
├── cyheat.pyx
├── data
│   ├── bottle.dat
│   ├── bottle_large.dat
│   └── bottle_medium.dat
├── heat.c
├── heat_cy.cpython-38-x86_64-linux-gnu.so
├── heat.html
├── heat_main.py
├── heat.py
├── heat_py.cpython-38-x86_64-linux-gnu.so
├── Makefile
├── outputs
├── README.md
├── requirements.txt
├── setup.py
└── venv
```
# Uso

El programa se puede usar de dos formas, utilizar el modulo para realizar el calculo de la ecuación de calor a un grupo de datos dado, o realizar el benchmark tanto de python como de cython para los archivos que se encuentran en el directorio ```data```.

## Uso del modulo

Para usar el modulo solo basta con utilizar el siguiente comando, el cual utilizara las variables asignadas por defecto en el programa. este muestra el tiempo que se realizo la ejecución y genera dos imagenes que muestran el resultado de la simulación al final y al principio de la ejecución.

> Con python puro.
```zsh
python heat_main.py
```
> Con cython.
```zsh
python heat_main.py -p cython
```
para mayor información del funcionamiento y las opciones que se le puden asignar al programa pude usar la opción ```-h```

> Opciones del programa
```zsh
$ python heat_main.py -h
usage: heat_main.py [-h] [-dx DX] [-dy DY] [-a A] [-n N] [-i I] [-f F] [-p {python,cython}] [-d]

Heat equation

optional arguments:
  -h, --help          show this help message and exit
  -dx DX              grid spacing in x-direction (default: 0.01)
  -dy DY              grid spacing in y-direction (default: 0.01)
  -a A                diffusion constant (default: 0.5)
  -n N                number of time steps (default: 200)
  -i I                image interval (default: 4000)
  -f F                input file (default: ./data/bottle.dat)
  -p {python,cython}  program to use (default: python)
  -d                  debug and print (default: True)
```

## Uso del benchmark

El benchmark ejecuta el programa N veces para cada una de las versiones (python, cython), con diferentes tamaños del plano de la simulación (bottle, bottle_large, bottle_medium) y teniendo en cuenta diferentes rangos de tiempo de la evolución de la simulacion con la ecuación (timesteps).

> Ejecutar el benchmark:
```zsh
python benchmark.py
```

El benchmark genera un archivo ```.xlsx``` con los datos de cada ejecución para los ajustes mencionados anteriormente (hojas del archivo terminadas en *-values*) y el promedio de las ejecuciones (hojas del archivo terminadas en *-results*) listos para ser analizados.
