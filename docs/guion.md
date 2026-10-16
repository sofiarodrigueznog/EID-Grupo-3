# Guion de presentación
## Nota de coordinación
Este guion está coordinado con los tres videos entregados:

`escena1.mp4`: Construcción de la suma para $n=4$ 
`escena2.mp4`: Refinamiento desde $n=4$ hasta $n=32$ 
`escena3.mp4`: Paso del límite a la integral definida 

Las marcas que se ven abajo indican cuándo debe comenzar cada parte de la voz. La duración puesta es para que se ubiquen en el video correspondiente, no porque el audio tenga que durar esa cifra.

Para poder alcanzar la duración de 4 a 6 minutos, tenemos que leer con calma y naturalmente, como si estuviéramos explicando, y hay que mantener más las escenas en pantalla.



## Video 1: construcción de la suma — `escena1.mp4`
### 0:00–0:03 — Paulo
**Pantalla negra y aparece el título.**
Cuando tenemos una función definida en un intervalo y queremos calcular el área que está debajo de la curva, podemos aproximarla mediante rectángulos. Esa es la idea principal de nuestro proyecto.



### 0:03–0:09 — Paulo
**Aparecen los ejes y la curva $f(x)=x^2+1$ en $[0,2]$.**
En este caso trabajaremos con la función: 
$$
f(x)=x^2+1
$$

en el intervalo $[0,2]$. Además, $f(x)=x^2+1$ es mayor que cero en todo este intervalo. Por eso, en nuestro ejemplo las sumas representan directamente una aproximación del área geométrica que está bajo la curva. La pregunta que queremos responder es ¿por qué una suma de Riemann puede aproximar cada vez mejor una región cuando aumentamos el número de rectángulos?

  

### 0:09–0:14 — Sofía
**Se muestran $n=4$, $\Delta x=2/4=0.5$ y el criterio de puntos medios.**
Bueno, para comenzar, dividimos el intervalo en cuatro subintervalos. El número $n$ indica cuántas partes tenemos y, por lo tanto, cuántos rectángulos vamos a utilizar. Como la partición es regular, todos tienen el mismo ancho:
$$
\Delta x=\frac{b-a}{n}=\frac{2}{4}=\frac{1}{2}
$$
En este caso, restamos los extremos del intervalo, $2-0$, y dividimos ese largo por la cantidad de partes, que es $4$. Así obtenemos $\Delta x=0.5$, que es el ancho de cada rectángulo.



### 0:14–0:22 — Sofía
**Aparecen los puntos muestra y se construyen los rectángulos uno por uno.**
Para obtener la altura de cada rectángulo escogemos un punto muestra dentro de cada subintervalo. En nuestro caso usamos los puntos medios. Para el subintervalo $[x_{i-1},x_i]$, el punto muestra es:
$$
x_i^*=\frac{x_{i-1}+x_i}{2}
$$
La altura es $f(x_i^*)$ y la base mide $\Delta x$. Por lo tanto, el área de cada rectángulo se obtiene multiplicando esos dos valores.

Elegimos los puntos medios porque cada altura se obtiene en una posición intermedia del subintervalo. Así, la aproximación no depende solamente de uno de sus extremos.



### 0:22–0:29.5 — Renato
**La escena termina con los cuatro rectángulos y el valor de $S_4$.**
Al sumar las áreas de los cuatro rectángulos obtenemos la suma de Riemann:
$$
S_4=\sum_{i=1}^{4}f(x_i^*)\Delta x =\frac{37}{8} =4.625
$$
Para ver cómo se calcula, tomemos el primer rectángulo. Su intervalo va desde $0$ hasta $0.5$, así que para encontrar el punto medio sumamos esos dos extremos y dividimos el resultado por $2$: $x_1^*=(0+0.5)/2=0.25$. Después reemplazamos este valor en la función. Primero calculamos $0.25^2$, que es $0.0625$, y luego le sumamos $1$, por lo que la altura es $f(0.25)=0.0625+1=1.0625$. Finalmente multiplicamos esta altura por el ancho del rectángulo, que es $0.5$, y obtenemos $A_1=1.0625\cdot0.5=0.53125$. Hacemos lo mismo con los otros tres rectángulos y sumamos las cuatro áreas para obtener $S_4=4.625$. En esta expresión, $f(x_i^*)$ representa la altura de cada rectángulo, $\Delta x$ representa su base y la sumatoria reúne las cuatro áreas. Este es el primer valor que vamos a comparar con las sumas que se obtienen cuando aumentamos la cantidad de subintervalos.

  

## Video 2: refinamiento — `escena2.mp4`
### 0:00–0:05 — Renato
**Aparece el título y luego la curva sin rectángulos.**
Ahora mantenemos la misma función y el mismo intervalo. Lo único que vamos a cambiar es la cantidad de subintervalos. Así podemos observar qué efecto tiene aumentar $n$.

  

### 0:05–0:12 — Renato
**Aparecen los cuatro rectángulos y la primera fila de la comparación.**
Partimos con $n=4$. En este caso, $\Delta x=0.5$ y obtenemos $S_4=4.625000$. Los rectángulos todavía son relativamente anchos, por lo que la aproximación se separa más de la curva.

  

### 0:12–0:17 — Renato
**La escena pasa a $n=8$ y agrega la segunda fila de la tabla.**
Cuando usamos $n=8$, el ancho disminuye a $\Delta x=0.25$ y la suma aumenta a $S_8=4.656250$. Al tener el doble de rectángulos, la forma de la región se representa mejor.

  

### 0:17–0:24 — Sofía
**Aparece $n=16$ y se completa otra fila de la comparación numérica.**
Si aumentamos a $n=16$, tenemos $\Delta x=0.125$ y $S_{16}=4.664063$. Se puede observar que los rectángulos se hacen más angostos y que la suma se acerca al valor que buscamos.



### 0:24–0:35.2 — Sofía
**Aparece $n=32$, la tabla queda completa y comienza a mostrarse la integral.**
Finalmente, para $n=32$ tenemos $\Delta x=0.0625$ y $S_{32}=4.666016$. El valor exacto de la integral es:
$$
\int_0^2(x^2+1)\,dx=\frac{14}{3}\approx4.666667
$$
Este valor se obtiene integrando cada término: la integral de $x^2$ es $x^3/3$ y la de $1$ es $x$. Después evaluamos el resultado entre $0$ y $2$, por lo que queda $2^3/3+2=14/3$.
La diferencia entre $S_4$ y el valor exacto es aproximadamente $0.041667$, mientras que para $n=32$ disminuye a $0.000651$. Por lo tanto, a medida que aumenta $n$, la aproximación mejora.

  

## Video 3: del límite a la integral — `escena3.mp4`
### 0:00–0:06 — Antonio
**Aparece el título y se muestra la región bajo la curva.**
En este punto ya no solo queremos comparar algunos valores. Queremos explicar qué ocurre si seguimos aumentando la cantidad de subintervalos.

  

### 0:06–0:12 — Antonio
**Aparece la suma de Riemann y la integral definida.**
Refinar una partición significa dividir el mismo intervalo en más subintervalos. Como:
$$
\Delta x=\frac{b-a}{n}
$$
si $n$ aumenta cada vez más, entonces $\Delta x$ se hace cada vez más pequeño.

  

### 0:12–0:18 — Antonio
**Se muestra la transición entre la suma y la integral.**
Esto se representa mediante el límite:
$$
\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i^*)\Delta x=\int_a^b f(x)\,dx
$$
No significa que tengamos que construir literalmente infinitos rectángulos.
La idea es observar a qué valor se acercan las sumas cuando sus bases se hacen cada vez más pequeñas.

En las escenas solo mostramos algunos valores finitos, hasta $n=32$. El paso hacia $n\to\infty$ se interpreta como un límite: seguimos aumentando $n$ y observamos a qué valor se acercan las sumas.
### 0:18–0:23 — Paulo
**Aparece la expresión $S_n=\frac{14}{3}-\frac{2}{3n^2}$.**
En nuestro ejemplo también podemos ver el error de forma directa:
$$
S_n=\frac{14}{3}-\frac{2}{3n^2}
$$
La diferencia con el valor exacto es $\frac{2}{3n^2}$. Por ejemplo, si usamos $n=4$, reemplazamos en la expresión y obtenemos $2/(3\cdot4^2)=2/48\approx0.041667$. Si usamos $n=32$, el error es $2/(3\cdot32^2)=2/3072\approx0.000651$. Como el número del denominador crece al aumentar $n$, esta diferencia se acerca a cero.

  

### 0:23–0:27.4 — Todos
**Aparece la respuesta a la pregunta central y luego los créditos.**
**Paulo:** Entonces, una suma de Riemann aproxima cada vez mejor la región porque al aumentar $n$ disminuye $\Delta x$.
**Sofía:** Cada rectángulo representa una parte más pequeña de la curva.
**Renato:** Por eso las sumas se acercan al valor de la integral definida.
**Antonio:** Para realizar el proyecto usamos el apunte base *Introducción a la integral*, el libro de Stewart, OpenStax, 3Blue1Brown y la documentación de Manim. Muchas gracias por su atención.