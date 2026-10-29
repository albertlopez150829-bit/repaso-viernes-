"""Las 40 afirmaciones del examen, cada una con tres versiones redactadas de forma distinta.

La primera versión de cada pregunta es la del examen original.
"""

PARTES = {1: 'Algoritmos, seudocódigo y diagramas',
 2: 'Variables, constantes, archivos y arreglos',
 3: 'Estructura de datos II',
 4: 'Complejidad de algoritmos'}

PREGUNTAS = [{'n': 1,
  'parte': 1,
  'versiones': [{'respuesta': 'V',
                 'texto': 'Un algoritmo es un conjunto ordenado y finito de pasos que permite resolver un '
                          'problema.',
                 'explicacion': 'Es la definición: pasos ordenados, finitos y precisos que llevan a la '
                                'solución de un problema.'},
                {'respuesta': 'F',
                 'texto': 'Un algoritmo puede tener infinitos pasos, siempre que al final resuelva el '
                          'problema.',
                 'explicacion': 'Un algoritmo debe ser finito: tiene que terminar en un número limitado de '
                                'pasos.'},
                {'respuesta': 'V',
                 'texto': 'Para que una serie de instrucciones sea un algoritmo, sus pasos deben seguir un '
                          'orden y terminar en algún momento.',
                 'explicacion': 'El orden y la finitud son características obligatorias de todo '
                                'algoritmo.'}]},
 {'n': 2,
  'parte': 1,
  'versiones': [{'respuesta': 'F',
                 'texto': 'Los algoritmos solo se clasifican en un único tipo: los computacionales.',
                 'explicacion': 'Hay varios tipos: cualitativos y cuantitativos, computacionales y no '
                                'computacionales.'},
                {'respuesta': 'V',
                 'texto': 'Además de los computacionales, existen algoritmos no computacionales, como las '
                          'instrucciones para armar un mueble.',
                 'explicacion': 'Los algoritmos no computacionales los realiza una persona, no una '
                                'computadora.'},
                {'respuesta': 'F',
                 'texto': 'Una receta de cocina no puede considerarse un algoritmo, porque no la ejecuta una '
                          'computadora.',
                 'explicacion': 'Sí es un algoritmo: uno no computacional y cualitativo.'}]},
 {'n': 3,
  'parte': 1,
  'versiones': [{'respuesta': 'F',
                 'texto': 'El seudocódigo es un lenguaje de programación que la computadora ejecuta '
                          'directamente.',
                 'explicacion': 'El seudocódigo es una descripción informal, parecida al lenguaje humano; la '
                                'computadora no lo ejecuta.'},
                {'respuesta': 'V',
                 'texto': 'El seudocódigo no tiene que respetar la sintaxis exacta de ningún lenguaje de '
                          'programación.',
                 'explicacion': 'Es informal; lo importante es que la lógica se entienda.'},
                {'respuesta': 'F',
                 'texto': 'Un programa escrito en seudocódigo se puede compilar y ejecutar sin hacerle '
                          'cambios.',
                 'explicacion': 'Primero hay que traducirlo a un lenguaje de programación real.'}]},
 {'n': 4,
  'parte': 1,
  'versiones': [{'respuesta': 'V',
                 'texto': 'El seudocódigo se usa para planificar la lógica de un programa antes de '
                          'escribirlo en un lenguaje de programación.',
                 'explicacion': 'Sirve como borrador de la lógica antes de pasarla a un lenguaje real como '
                                'Python o C++.'},
                {'respuesta': 'F',
                 'texto': 'El seudocódigo se escribe después de terminar el programa, solo para '
                          'documentarlo.',
                 'explicacion': 'Normalmente se escribe antes, para planificar la lógica.'},
                {'respuesta': 'V',
                 'texto': 'Escribir seudocódigo ayuda a pensar la solución sin preocuparse todavía por la '
                          'sintaxis del lenguaje.',
                 'explicacion': 'Primero se piensa la lógica y después se codifica.'}]},
 {'n': 5,
  'parte': 1,
  'versiones': [{'respuesta': 'V',
                 'texto': 'Un diagrama de flujo es la representación gráfica de un algoritmo mediante '
                          'símbolos conectados por flechas.',
                 'explicacion': 'Usa símbolos estándar (óvalo para inicio y fin, rectángulo para procesos, '
                                'rombo para decisiones) unidos por flechas.'},
                {'respuesta': 'F',
                 'texto': 'En un diagrama de flujo, el rombo representa el inicio y el fin del algoritmo.',
                 'explicacion': 'El rombo es para las decisiones; el inicio y el fin se representan con un '
                                'óvalo.'},
                {'respuesta': 'V',
                 'texto': 'En un diagrama de flujo, las flechas indican el orden en que se ejecutan los '
                          'pasos.',
                 'explicacion': 'Las flechas marcan el recorrido del algoritmo de un símbolo a otro.'}]},
 {'n': 6,
  'parte': 1,
  'versiones': [{'respuesta': 'V',
                 'texto': 'Un algoritmo cuantitativo se basa en cálculos numéricos, mientras que uno '
                          'cualitativo se describe con palabras y no requiere cálculos.',
                 'explicacion': 'Cuantitativo: calcular un promedio. Cualitativo: los pasos de una receta.'},
                {'respuesta': 'F',
                 'texto': 'Calcular el promedio de tres notas es un ejemplo de algoritmo cualitativo.',
                 'explicacion': 'Es cuantitativo, porque se basa en cálculos numéricos.'},
                {'respuesta': 'V',
                 'texto': 'Las instrucciones para cambiar una llanta son un ejemplo de algoritmo '
                          'cualitativo.',
                 'explicacion': 'Se describen con palabras y no requieren cálculos.'}]},
 {'n': 7,
  'parte': 1,
  'versiones': [{'respuesta': 'V',
                 'texto': 'El lenguaje de algoritmo es el conjunto de símbolos y reglas que se usan para '
                          'describir de forma clara los pasos de un proceso.',
                 'explicacion': 'Son las reglas y símbolos que permiten escribir los pasos sin ambigüedad.'},
                {'respuesta': 'F',
                 'texto': 'El lenguaje de algoritmo permite escribir los pasos de forma ambigua, porque cada '
                          'lector los interpreta a su manera.',
                 'explicacion': 'Al contrario: busca describir los pasos de forma clara y sin ambigüedad.'},
                {'respuesta': 'V',
                 'texto': 'El lenguaje de algoritmo usa reglas y símbolos para que cualquier persona '
                          'entienda los pasos de la misma manera.',
                 'explicacion': 'Su objetivo es que los pasos sean claros para todos.'}]},
 {'n': 8,
  'parte': 1,
  'versiones': [{'respuesta': 'F',
                 'texto': 'El diagrama N-S (Nassi-Shneiderman) usa flechas para conectar los pasos, igual '
                          'que el diagrama de flujo.',
                 'explicacion': 'El diagrama N-S usa cajas o bloques contiguos, sin flechas.'},
                {'respuesta': 'V',
                 'texto': 'El diagrama N-S representa el algoritmo con cajas o bloques contiguos, sin usar '
                          'flechas.',
                 'explicacion': 'Esa es su característica principal frente al diagrama de flujo.'},
                {'respuesta': 'F',
                 'texto': 'El diagrama N-S y el diagrama de flujo son lo mismo; solo cambia el nombre.',
                 'explicacion': 'Son distintos: el de flujo usa símbolos y flechas; el N-S usa cajas '
                                'contiguas.'}]},
 {'n': 9,
  'parte': 1,
  'versiones': [{'respuesta': 'V',
                 'texto': 'En el lenguaje de algoritmo, los operadores se clasifican en aritméticos, '
                          'relacionales y lógicos.',
                 'explicacion': 'Aritméticos (+, −, *, /), relacionales (>, <, =) y lógicos (Y, O, NO).'},
                {'respuesta': 'F',
                 'texto': 'Los operadores >, < y = son operadores lógicos.',
                 'explicacion': 'Son relacionales, porque comparan valores. Los lógicos son Y, O y NO.'},
                {'respuesta': 'V',
                 'texto': 'Los operadores Y, O y NO son operadores lógicos.',
                 'explicacion': 'Sirven para combinar o negar condiciones.'}]},
 {'n': 10,
  'parte': 1,
  'versiones': [{'respuesta': 'F',
                 'texto': 'La complejidad de un algoritmo se mide únicamente por la cantidad de líneas que '
                          'tiene.',
                 'explicacion': 'Se mide por los recursos que consume (tiempo y memoria), no por la cantidad '
                                'de líneas.'},
                {'respuesta': 'V',
                 'texto': 'Un algoritmo corto, con pocas líneas, puede ser más lento que uno largo.',
                 'explicacion': 'La complejidad depende de los recursos que consume, no del largo del '
                                'código.'},
                {'respuesta': 'F',
                 'texto': 'Mientras más líneas tiene un algoritmo, siempre es más complejo.',
                 'explicacion': 'La cantidad de líneas no mide la complejidad; se mide por tiempo y '
                                'memoria.'}]},
 {'n': 11,
  'parte': 2,
  'versiones': [{'respuesta': 'V',
                 'texto': 'Una variable es un espacio en memoria cuyo valor puede cambiar durante la '
                          'ejecución del programa.',
                 'explicacion': 'Por ejemplo, un contador que pasa de 0 a 1, luego a 2, y así '
                                'sucesivamente.'},
                {'respuesta': 'F',
                 'texto': 'Una vez que a una variable se le asigna un valor, ese valor ya no puede cambiar.',
                 'explicacion': 'Eso describe a una constante; la variable sí puede cambiar.'},
                {'respuesta': 'V',
                 'texto': 'Una variable tiene un nombre que identifica un espacio en la memoria donde se '
                          'guarda un dato.',
                 'explicacion': 'Por ejemplo, la variable edad guarda el número 18.'}]},
 {'n': 12,
  'parte': 2,
  'versiones': [{'respuesta': 'F',
                 'texto': 'Una constante es un valor que puede modificarse libremente mientras el programa '
                          'se ejecuta.',
                 'explicacion': 'Una constante mantiene el mismo valor durante toda la ejecución, como PI = '
                                '3.1416.'},
                {'respuesta': 'V',
                 'texto': 'El valor PI = 3.1416 dentro de un programa es un buen ejemplo de constante.',
                 'explicacion': 'Su valor no cambia durante toda la ejecución.'},
                {'respuesta': 'F',
                 'texto': 'Un contador que aumenta de uno en uno debe declararse como constante.',
                 'explicacion': 'Como su valor cambia, debe ser una variable.'}]},
 {'n': 13,
  'parte': 2,
  'versiones': [{'respuesta': 'V',
                 'texto': 'La diferencia principal entre una variable y una constante es que la variable '
                          'puede cambiar su valor y la constante no.',
                 'explicacion': 'Variable: su valor cambia. Constante: su valor queda fijo.'},
                {'respuesta': 'F',
                 'texto': 'Una variable y una constante son iguales; la única diferencia es el nombre que se '
                          'les da.',
                 'explicacion': 'La diferencia es que la variable cambia su valor y la constante no.'},
                {'respuesta': 'V',
                 'texto': 'Si un dato debe mantenerse igual durante todo el programa, conviene guardarlo en '
                          'una constante.',
                 'explicacion': 'Así se evita modificarlo por error.'}]},
 {'n': 14,
  'parte': 2,
  'versiones': [{'respuesta': 'F',
                 'texto': 'Un campo contiene varios registros, y un registro contiene varias bases de datos.',
                 'explicacion': 'Es al revés: la base de datos contiene registros y cada registro contiene '
                                'campos.'},
                {'respuesta': 'V',
                 'texto': 'De menor a mayor, el orden es: campo, registro y base de datos.',
                 'explicacion': 'Los campos forman registros, y los registros forman la base de datos.'},
                {'respuesta': 'F',
                 'texto': 'Un registro es más grande que una base de datos.',
                 'explicacion': 'Es al revés: la base de datos contiene muchos registros.'}]},
 {'n': 15,
  'parte': 2,
  'versiones': [{'respuesta': 'V',
                 'texto': 'Un archivo en programación es un conjunto de datos guardados en un medio de '
                          'almacenamiento e identificados con un nombre.',
                 'explicacion': 'Por ejemplo, un archivo notas.txt guardado en el disco.'},
                {'respuesta': 'F',
                 'texto': 'Un archivo solo existe mientras el programa está abierto y se borra al apagar la '
                          'computadora.',
                 'explicacion': 'Un archivo se guarda en un medio de almacenamiento, así que permanece '
                                'aunque se apague.'},
                {'respuesta': 'V',
                 'texto': 'Cada archivo se identifica con un nombre, por ejemplo, notas.txt.',
                 'explicacion': 'El nombre permite encontrarlo y abrirlo después.'}]},
 {'n': 16,
  'parte': 2,
  'versiones': [{'respuesta': 'V',
                 'texto': 'Un registro es un conjunto de campos relacionados que describen un mismo '
                          'elemento, por ejemplo, los datos de un estudiante.',
                 'explicacion': 'El nombre, la matrícula y la edad de un mismo estudiante forman un '
                                'registro.'},
                {'respuesta': 'F',
                 'texto': 'Un registro es un solo dato aislado, como el nombre de una persona.',
                 'explicacion': 'Eso es un campo; el registro es el conjunto de campos de un mismo '
                                'elemento.'},
                {'respuesta': 'V',
                 'texto': 'En una tabla de estudiantes, cada fila con los datos de un estudiante es un '
                          'registro.',
                 'explicacion': 'La fila agrupa todos los campos de ese estudiante.'}]},
 {'n': 17,
  'parte': 2,
  'versiones': [{'respuesta': 'V',
                 'texto': 'Un campo es la unidad mínima de información dentro de un registro, como “nombre” '
                          'o “edad”.',
                 'explicacion': 'Cada dato individual dentro del registro es un campo.'},
                {'respuesta': 'F',
                 'texto': 'Un campo agrupa todos los datos de un estudiante: nombre, edad y matrícula.',
                 'explicacion': 'Eso es un registro; cada uno de esos datos por separado es un campo.'},
                {'respuesta': 'V',
                 'texto': 'En una tabla de estudiantes, la columna “edad” corresponde a un campo.',
                 'explicacion': 'Cada columna representa un campo.'}]},
 {'n': 18,
  'parte': 2,
  'versiones': [{'respuesta': 'F',
                 'texto': 'Una base de datos es un conjunto de datos desorganizados que no guardan relación '
                          'entre sí.',
                 'explicacion': 'Una base de datos es un conjunto de datos organizados y relacionados entre '
                                'sí.'},
                {'respuesta': 'V',
                 'texto': 'Una base de datos guarda la información de forma organizada para poder '
                          'consultarla fácilmente.',
                 'explicacion': 'Organización y relación entre los datos son su base.'},
                {'respuesta': 'F',
                 'texto': 'Una base de datos y un registro son lo mismo.',
                 'explicacion': 'La base de datos es el conjunto completo; un registro es solo una de sus '
                                'partes.'}]},
 {'n': 19,
  'parte': 2,
  'versiones': [{'respuesta': 'F',
                 'texto': 'Un arreglo almacena elementos de distintos tipos sin orden y sin posiciones '
                          'identificadas por índice.',
                 'explicacion': 'Un arreglo guarda elementos del mismo tipo, cada uno en una posición '
                                'identificada por un índice.'},
                {'respuesta': 'V',
                 'texto': 'En un arreglo, cada elemento ocupa una posición que se identifica con un índice.',
                 'explicacion': 'Por ejemplo, el primer elemento suele estar en la posición 0.'},
                {'respuesta': 'F',
                 'texto': 'En un mismo arreglo se pueden mezclar libremente números, textos y fechas.',
                 'explicacion': 'Un arreglo guarda elementos del mismo tipo.'}]},
 {'n': 20,
  'parte': 2,
  'versiones': [{'respuesta': 'V',
                 'texto': 'Un arreglo unidimensional (vector) se parece a una tabla de una sola fila o '
                          'columna, y sus elementos se acceden mediante un índice.',
                 'explicacion': 'Por ejemplo: notas[0], notas[1], notas[2].'},
                {'respuesta': 'F',
                 'texto': 'Para acceder a un elemento de un arreglo unidimensional se necesitan dos índices: '
                          'fila y columna.',
                 'explicacion': 'El unidimensional usa un solo índice; dos índices son para el '
                                'bidimensional.'},
                {'respuesta': 'V',
                 'texto': 'Un arreglo unidimensional también se conoce como vector.',
                 'explicacion': 'Es una sola fila (o columna) de elementos.'}]},
 {'n': 21,
  'parte': 3,
  'versiones': [{'respuesta': 'V',
                 'texto': 'Los arreglos bidimensionales organizan los datos en filas y columnas, como una '
                          'matriz.',
                 'explicacion': 'Cada elemento se ubica con dos índices: matriz[fila][columna].'},
                {'respuesta': 'F',
                 'texto': 'Un arreglo bidimensional organiza los datos en una sola fila.',
                 'explicacion': 'Eso es un arreglo unidimensional; el bidimensional usa filas y columnas.'},
                {'respuesta': 'V',
                 'texto': 'Una tabla de notas, con estudiantes en las filas y materias en las columnas, se '
                          'puede guardar en un arreglo bidimensional.',
                 'explicacion': 'Cada nota se ubica con dos índices: estudiante y materia.'}]},
 {'n': 22,
  'parte': 3,
  'versiones': [{'respuesta': 'F',
                 'texto': 'Una lista es una estructura estática cuyo tamaño nunca puede cambiar.',
                 'explicacion': 'La lista es una estructura dinámica: puede crecer o reducirse mientras el '
                                'programa se ejecuta.'},
                {'respuesta': 'V',
                 'texto': 'En una lista se pueden insertar y eliminar elementos mientras el programa se '
                          'ejecuta.',
                 'explicacion': 'Por eso se dice que la lista es una estructura dinámica.'},
                {'respuesta': 'F',
                 'texto': 'Antes de usar una lista hay que fijar su tamaño, y ese tamaño no se puede cambiar '
                          'después.',
                 'explicacion': 'Eso describe un arreglo estático; la lista es dinámica.'}]},
 {'n': 23,
  'parte': 3,
  'versiones': [{'respuesta': 'V',
                 'texto': 'En una lista simplemente encadenada, cada nodo contiene un dato y un enlace al '
                          'nodo siguiente.',
                 'explicacion': 'Por eso solo se recorre en una dirección, del primer nodo hacia el último.'},
                {'respuesta': 'F',
                 'texto': 'En una lista simplemente encadenada, desde un nodo se puede regresar directamente '
                          'al nodo anterior.',
                 'explicacion': 'Solo tiene enlace al siguiente, así que no puede ir hacia atrás.'},
                {'respuesta': 'V',
                 'texto': 'En una lista simplemente encadenada, el enlace del último nodo no apunta a ningún '
                          'otro nodo.',
                 'explicacion': 'Su enlace es nulo, lo que indica el final de la lista.'}]},
 {'n': 24,
  'parte': 3,
  'versiones': [{'respuesta': 'F',
                 'texto': 'En una lista doblemente encadenada, cada nodo tiene un solo enlace, que apunta al '
                          'nodo siguiente.',
                 'explicacion': 'Cada nodo tiene dos enlaces: uno al siguiente y otro al anterior, así se '
                                'recorre en ambos sentidos.'},
                {'respuesta': 'V',
                 'texto': 'Una lista doblemente encadenada se puede recorrer hacia adelante y hacia atrás.',
                 'explicacion': 'Porque cada nodo tiene un enlace al siguiente y otro al anterior.'},
                {'respuesta': 'F',
                 'texto': 'La lista simplemente encadenada y la doblemente encadenada se recorren '
                          'exactamente igual.',
                 'explicacion': 'La simple solo hacia adelante; la doble, en ambos sentidos.'}]},
 {'n': 25,
  'parte': 3,
  'versiones': [{'respuesta': 'V',
                 'texto': 'Una pila funciona con el principio LIFO: el último elemento en entrar es el '
                          'primero en salir.',
                 'explicacion': 'Como una pila de platos: el último que pones es el primero que quitas.'},
                {'respuesta': 'F',
                 'texto': 'En una pila, el primer elemento que entra es el primero que sale.',
                 'explicacion': 'Eso es FIFO (cola). La pila es LIFO: el último en entrar sale primero.'},
                {'respuesta': 'V',
                 'texto': 'El botón “Deshacer” de un editor funciona como una pila: deshace primero la '
                          'última acción.',
                 'explicacion': 'La última acción guardada es la primera que sale.'}]},
 {'n': 26,
  'parte': 3,
  'versiones': [{'respuesta': 'F',
                 'texto': 'Una cola funciona con el principio FIFO, por lo que el último en llegar es el '
                          'primero en ser atendido.',
                 'explicacion': 'En FIFO, el primero en llegar es el primero en ser atendido, como la fila '
                                'de un banco.'},
                {'respuesta': 'V',
                 'texto': 'La fila para pagar en un supermercado funciona como una cola: atienden primero al '
                          'que llegó primero.',
                 'explicacion': 'Eso es el principio FIFO.'},
                {'respuesta': 'F',
                 'texto': 'Una cola funciona con el principio LIFO.',
                 'explicacion': 'La cola es FIFO; LIFO es el principio de la pila.'}]},
 {'n': 27,
  'parte': 3,
  'versiones': [{'respuesta': 'V',
                 'texto': 'Los elementos principales de un árbol son la raíz, los nodos, las ramas y las '
                          'hojas.',
                 'explicacion': 'La raíz es el nodo inicial; las hojas son los nodos que no tienen hijos.'},
                {'respuesta': 'F',
                 'texto': 'En un árbol, la raíz es el nodo que no tiene hijos.',
                 'explicacion': 'Esa es la hoja. La raíz es el nodo inicial, el que no tiene padre.'},
                {'respuesta': 'V',
                 'texto': 'En un árbol, las hojas son los nodos que no tienen hijos.',
                 'explicacion': 'Están al final de las ramas.'}]},
 {'n': 28,
  'parte': 3,
  'versiones': [{'respuesta': 'V',
                 'texto': 'En un árbol binario cada nodo tiene como máximo dos hijos, mientras que en un '
                          'árbol general puede tener cualquier cantidad.',
                 'explicacion': 'Binario: máximo dos hijos (izquierdo y derecho). General: sin límite de '
                                'hijos.'},
                {'respuesta': 'F',
                 'texto': 'En un árbol binario, cada nodo debe tener exactamente tres hijos.',
                 'explicacion': 'En un árbol binario cada nodo tiene como máximo dos hijos.'},
                {'respuesta': 'V',
                 'texto': 'Un nodo de un árbol general puede tener más de dos hijos.',
                 'explicacion': 'En el árbol general no hay límite de hijos.'}]},
 {'n': 29,
  'parte': 3,
  'versiones': [{'respuesta': 'F',
                 'texto': 'Un grafo está formado únicamente por nodos, sin conexiones entre ellos.',
                 'explicacion': 'Un grafo tiene vértices (nodos) y aristas que los conectan.'},
                {'respuesta': 'V',
                 'texto': 'Las aristas de un grafo son las conexiones entre sus vértices.',
                 'explicacion': 'Un grafo se forma con vértices (nodos) y aristas.'},
                {'respuesta': 'F',
                 'texto': 'Un grafo es igual que una lista: sus elementos siempre van uno detrás de otro.',
                 'explicacion': 'El grafo es no lineal: sus nodos se conectan de muchas formas, como una '
                                'red.'}]},
 {'n': 30,
  'parte': 3,
  'versiones': [{'respuesta': 'V',
                 'texto': 'Las pilas y las colas son estructuras lineales, mientras que los árboles y los '
                          'grafos son estructuras no lineales.',
                 'explicacion': 'Lineales: un elemento tras otro. No lineales: jerarquías (árboles) o redes '
                                '(grafos).'},
                {'respuesta': 'F',
                 'texto': 'Los árboles y los grafos son estructuras lineales.',
                 'explicacion': 'Son no lineales; las lineales son las pilas, las colas y las listas.'},
                {'respuesta': 'V',
                 'texto': 'En una pila o en una cola, los elementos se organizan uno detrás de otro.',
                 'explicacion': 'Por eso son estructuras lineales.'}]},
 {'n': 31,
  'parte': 4,
  'versiones': [{'respuesta': 'V',
                 'texto': 'En informática, la complejidad se refiere a la cantidad de recursos, como tiempo '
                          'o memoria, que requiere resolver un problema.',
                 'explicacion': 'Cuantos más recursos exige un problema, más complejo es.'},
                {'respuesta': 'F',
                 'texto': 'En informática, la complejidad mide qué tan difícil es leer el código de un '
                          'programa.',
                 'explicacion': 'Mide los recursos, como tiempo y memoria, que se necesitan para resolver un '
                                'problema.'},
                {'respuesta': 'V',
                 'texto': 'El tiempo y la memoria son los recursos principales que se miden al hablar de '
                          'complejidad.',
                 'explicacion': 'Son la base de la complejidad temporal y espacial.'}]},
 {'n': 32,
  'parte': 4,
  'versiones': [{'respuesta': 'V',
                 'texto': 'La complejidad de un algoritmo mide cuánto tiempo y espacio necesita según el '
                          'tamaño de los datos de entrada.',
                 'explicacion': 'Indica cómo crecen el tiempo y la memoria cuando aumentan los datos de '
                                'entrada.'},
                {'respuesta': 'F',
                 'texto': 'La complejidad de un algoritmo no depende del tamaño de los datos de entrada.',
                 'explicacion': 'Sí depende: indica cómo crecen el tiempo y la memoria al aumentar los '
                                'datos.'},
                {'respuesta': 'V',
                 'texto': 'Dos algoritmos que resuelven el mismo problema pueden tener complejidades '
                          'distintas.',
                 'explicacion': 'Por ejemplo, la búsqueda lineal y la binaria buscan lo mismo con distinta '
                                'eficiencia.'}]},
 {'n': 33,
  'parte': 4,
  'versiones': [{'respuesta': 'F',
                 'texto': 'Las medidas asintóticas describen el comportamiento de un algoritmo cuando la '
                          'cantidad de datos es muy pequeña.',
                 'explicacion': 'Describen el comportamiento cuando la entrada crece mucho (tiende al '
                                'infinito).'},
                {'respuesta': 'V',
                 'texto': 'Las medidas asintóticas analizan qué pasa con un algoritmo cuando la cantidad de '
                          'datos crece mucho.',
                 'explicacion': 'Estudian el comportamiento cuando la entrada tiende al infinito.'},
                {'respuesta': 'F',
                 'texto': 'Las medidas asintóticas dicen exactamente cuántos segundos tarda un programa en '
                          'una computadora.',
                 'explicacion': 'No dan segundos exactos; describen cómo crece el tiempo según los datos.'}]},
 {'n': 34,
  'parte': 4,
  'versiones': [{'respuesta': 'V',
                 'texto': 'La notación O (Big O) indica una cota superior, Ω (Omega) una cota inferior y Θ '
                          '(Theta) una cota ajustada.',
                 'explicacion': 'O marca lo más que puede crecer el tiempo, Ω lo menos, y Θ el crecimiento '
                                'exacto.'},
                {'respuesta': 'F',
                 'texto': 'La notación Ω (Omega) indica la cota superior de un algoritmo.',
                 'explicacion': 'Ω es la cota inferior; la superior es O (Big O).'},
                {'respuesta': 'V',
                 'texto': 'La notación Θ (Theta) se usa cuando el límite superior y el inferior coinciden.',
                 'explicacion': 'Por eso se le llama cota ajustada.'}]},
 {'n': 35,
  'parte': 4,
  'versiones': [{'respuesta': 'V',
                 'texto': 'Los órdenes de complejidad sirven para comparar la eficiencia de distintos '
                          'algoritmos.',
                 'explicacion': 'Por ejemplo, O(log n) es mejor que O(n), y O(n) es mejor que O(n²).'},
                {'respuesta': 'F',
                 'texto': 'Con muchos datos, un algoritmo O(n²) es más eficiente que uno O(n).',
                 'explicacion': 'Es al revés: O(n) crece mucho más despacio que O(n²).'},
                {'respuesta': 'V',
                 'texto': 'Con muchos datos, un algoritmo O(log n) es más eficiente que uno O(n).',
                 'explicacion': 'O(log n) crece muy despacio aunque los datos aumenten mucho.'}]},
 {'n': 36,
  'parte': 4,
  'versiones': [{'respuesta': 'F',
                 'texto': 'En una lista ordenada y grande, la búsqueda lineal es más rápida que la búsqueda '
                          'logarítmica (binaria).',
                 'explicacion': 'La binaria, O(log n), es mucho más rápida que la lineal, O(n), porque '
                                'descarta la mitad de los datos en cada paso.'},
                {'respuesta': 'V',
                 'texto': 'La búsqueda binaria solo funciona si los datos están ordenados.',
                 'explicacion': 'Necesita el orden para descartar la mitad en cada paso.'},
                {'respuesta': 'F',
                 'texto': 'La búsqueda lineal descarta la mitad de los datos en cada paso.',
                 'explicacion': 'Eso lo hace la búsqueda binaria; la lineal revisa elemento por elemento.'}]},
 {'n': 37,
  'parte': 4,
  'versiones': [{'respuesta': 'V',
                 'texto': 'Las clases de problemas, como P y NP, agrupan los problemas según la dificultad '
                          'para resolverlos.',
                 'explicacion': 'P: se resuelven en tiempo razonable (polinomial). NP: una solución '
                                'propuesta se puede verificar rápido.'},
                {'respuesta': 'F',
                 'texto': 'Los problemas de la clase P son los que no se pueden resolver con ningún '
                          'algoritmo.',
                 'explicacion': 'Los problemas P sí se resuelven, y en tiempo polinomial (razonable).'},
                {'respuesta': 'V',
                 'texto': 'En los problemas NP, si alguien propone una solución, se puede verificar rápido '
                          'si es correcta.',
                 'explicacion': 'Verificar es rápido, aunque encontrar la solución pueda ser difícil.'}]},
 {'n': 38,
  'parte': 4,
  'versiones': [{'respuesta': 'F',
                 'texto': 'Las medidas asintóticas no son importantes, porque todos los algoritmos tardan lo '
                          'mismo con cualquier cantidad de datos.',
                 'explicacion': 'Son importantes porque permiten predecir cómo escala un algoritmo cuando '
                                'hay más datos.'},
                {'respuesta': 'V',
                 'texto': 'Las medidas asintóticas permiten predecir si un algoritmo seguirá siendo útil '
                          'cuando haya muchos más datos.',
                 'explicacion': 'Por eso son importantes al elegir un algoritmo.'},
                {'respuesta': 'F',
                 'texto': 'Con las computadoras modernas, analizar la complejidad de un algoritmo ya no '
                          'tiene utilidad.',
                 'explicacion': 'Sigue siendo importante: con muchos datos, un mal algoritmo es lento en '
                                'cualquier computadora.'}]},
 {'n': 39,
  'parte': 4,
  'versiones': [{'respuesta': 'V',
                 'texto': 'Los dos tipos principales de complejidad son la complejidad temporal y la '
                          'complejidad espacial.',
                 'explicacion': 'Temporal: cuánto tiempo tarda. Espacial: cuánta memoria usa.'},
                {'respuesta': 'F',
                 'texto': 'La complejidad espacial mide cuánto tiempo tarda un algoritmo.',
                 'explicacion': 'La espacial mide la memoria; la temporal mide el tiempo.'},
                {'respuesta': 'V',
                 'texto': 'La complejidad temporal se relaciona con el tiempo de ejecución, y la espacial '
                          'con la memoria usada.',
                 'explicacion': 'Son los dos tipos principales de complejidad.'}]},
 {'n': 40,
  'parte': 4,
  'versiones': [{'respuesta': 'F',
                 'texto': 'En una complejidad cuadrática, O(n²), si la cantidad de datos se duplica, el '
                          'tiempo de ejecución solo se duplica.',
                 'explicacion': 'En O(n²), al duplicar los datos el tiempo se cuadruplica aproximadamente '
                                '(2² = 4).'},
                {'respuesta': 'V',
                 'texto': 'En un algoritmo O(n²), si los datos se triplican, el tiempo aumenta unas nueve '
                          'veces.',
                 'explicacion': 'Porque 3² = 9.'},
                {'respuesta': 'F',
                 'texto': 'Un algoritmo con dos ciclos anidados que recorren todos los datos suele tener '
                          'complejidad lineal, O(n).',
                 'explicacion': 'Dos ciclos anidados sobre n datos suelen dar complejidad cuadrática, '
                                'O(n²).'}]}]
