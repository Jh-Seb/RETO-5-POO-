# RETO-5-POO-
En este repositorio encontraras el reto 5 de programacion orientada a objetos

Create a package with all code of class Shape, this exersice should be conducted in two ways:
- A unique module inside of package Shape 
- Individual modules that import Shape in inheritates from it.
***

### Paquete único con todo el código de `Shape`

Aqui, el módulo shape del paquete `Shape` agrupa todo el código correspondiente a las clases `Shape`, `Point`, `Line` y sus respectivas subclases, como `Triangle`, `Rectangle`, `Square`, entre otras. 

``` bash
RETO 5.2/
│
├── main.py  # Script principal con el código de prueba
└── shapes/
    ├── __init__.py  
    └── shape.py  
```
***

### Módulos individuales

Aquí, el código se distribuye en módulos independientes, asignando cada clase a su propio archivo. La clase principal, `Shape`, reside en el archivo base_shape.py, mientras que las subclases como `Triangle`, `Rectangle`, y `Square` se implementan en módulos separados dentro del paquete.

``` bash
RETO 5.1/
│
├── main.py  # Script principal con el código de prueba
└── shapes/
    ├── __init__.py 
    ├── base_shape.py  # Contiene la clase Shape
    ├── point.py  # Contiene la clase Point
    ├── line.py  # Contiene la clase Line
    ├── triangle.py  # Contiene las clases Triangle 
    ├── rectangle.py  # Contiene la clase Rectangle
    └── square.py  # Contiene la clase Square
```
***
