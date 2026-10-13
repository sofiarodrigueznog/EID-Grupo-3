# Teoría del tema: partición, \Delta x y refinamiento

## 1. El problema de aproximar un área

Cuando tenemos una función definida en un intervalo cerrado $[a,b]$ y queremos calcular el área que está debajo de la curva $y=f(x)$ entre $x=a$ y $x=b$, podemos aproximarla mediante rectángulos.

La idea es _dividir_ el intervalo en partes pequeñas y construir un rectángulo sobre cada parte para sumar sus áreas. Esto permite representar una aproximación del área geométrica que está bajo la curva cuando:

$$f(x)\geq 0$$

Si la función toma valores negativos, entonces la suma representa el área con el signo respectivo. Por lo tanto, las regiones que están debajo del eje x _se restan_ de las que están por encima.

## 2. Partición del intervalo

Una **partición** de $[a,b]$ es un conjunto ordenado de puntos:

$$a=x_0<x_1<x_2<\dots<x_n=b$$

Estos puntos dividen el intervalo original en n subintervalos:

$$[x_0,x_1],\ [x_1,x_2],\ \dots,\ [x_{n-1},x_n]$$

El número n indica cuántos subintervalos hay, y por lo tanto, _cuántos rectángulos_ se van a usar. Para una _partición regular_, todos los subintervalos tienen el mismo ancho. El ancho de cada subintervalo se representa con $\Delta x$ y se calcula como:

$$\Delta x=\frac{b-a}{n}$$

En este caso, los puntos de la partición se pueden escribir de la siguiente manera:

$$x_i=a+i\Delta x,\qquad i=0,1,\dots,n$$

Por ejemplo, si $[a,b]=[0,4]$ y $n=4$, entonces: $$\Delta x=\frac{(4-0)}4=1$$Y la partición es $0,1,2,3,4$. Son 4 subintervalos y 5 puntos.

Si se mantiene el mismo intervalo y se aumenta a n=8, el ancho pasa a ser \Delta x=1/2: hay más subintervalos, pero cada uno es más angosto.  
$$\Delta x=\frac{(4-0)}8=\frac{1}2$$Y la partición es $0,\frac12,1,\frac32,2,\frac52,3,\frac72,4$. Por lo que son 8 subintervalos y 9 puntos.

## 3. Punto muestra y altura de los rectángulos

En cada subintervalo $[x_{i-1},x_i]$ se elige un **punto muestra** $x_i^*$. Este punto puede ser cualquiera que esté _dentro del subintervalo_:

$$x_i^*\in[x_{i-1},x_i]$$

Para obtener la _altura del rectángulo_, evaluamos la función en el punto muestra. Es decir, la altura será $f(x_i^*)$. Como la _base del rectángulo_ mide $\Delta x$, su área con signo se calcula multiplicando la altura por la base:

$$f(x_i^*)\Delta x$$
Podemos escoger los puntos muestra de distintas maneras. Por ejemplo:

- **Extremos izquierdos:** se utiliza el _extremo izquierdo_ de cada subintervalo, es decir, $x_i^*=x_{i-1}$.  
    
- **Extremos derechos:** se utiliza el _extremo derecho_, es decir, $x_i^*=x_i$.  
    
- **Puntos medios:** se utiliza el punto que está justo en la _mitad del subintervalo_, es decir,                   $x_i^*=\frac{x_{i-1}+x_i}{2}.$  
    

La elección del punto muestra puede cambiar el resultado de la aproximación, aunque utilicemos la misma cantidad de subintervalos. Lo importante es que el punto que escojamos esté _dentro del subintervalo correspondiente_.

## 4. Suma de Riemann S_n

Si sumamos las áreas con signo de los n rectángulos, obtenemos una **suma de Riemann**:

$$S_n=\sum_{i=1}^{n}f(x_i^*)\Delta x$$

Para una _partición regular_, sabemos que el _ancho de cada subintervalo_ es \Delta x=\frac{b-a}{n}. Si además utilizamos los extremos derechos como puntos muestra, podemos escribir la suma de Riemann de la siguiente manera:

$$S_n=\sum_{i=1}^{n} f\left(a+i\frac{b-a}{n}\right) \frac{b-a}{n}$$

Esta expresión utiliza los _extremos derechos_ de los subintervalos. Si escogemos los extremos izquierdos o los puntos medios, cambia el punto que utilizamos dentro de la función, pero la idea sigue siendo la misma: calcular el área con signo de cada rectángulo y sumar todos los resultados.

El resultado de la suma depende de la _cantidad de subintervalos_ que utilicemos y de los _puntos muestra_ que escojamos.

Por ejemplo, $S_4, S_8, S_{16}$ y $S_{32}$ representan aproximaciones de la misma integral, aunque en general sus resultados serán distintos. Esto ocurre porque, a medida que aumenta n, también aumenta la cantidad de rectángulos y disminuye el _ancho de cada uno_.

## 5. Refinamiento: $n\to\infty y \Delta x\to 0$

_Refinar una partición_ significa dividir el mismo intervalo en más subintervalos. Para hacerlo, aumentamos n, pero mantenemos _fijo el intervalo_ $[a,b]$.

Como el _ancho de cada subintervalo_ se calcula mediante:

$$\Delta x=\frac{b-a}{n}$$

si aumentamos n cada vez más, el ancho de los subintervalos se hace cada vez más pequeño. Esto se puede representar de la siguiente manera:

$$n\to\infty \qquad\Longrightarrow\qquad \Delta x\to 0$$

Esto significa que los rectángulos se vuelven cada vez más angostos y que utilizamos una cantidad cada vez mayor de ellos para aproximar el área bajo la curva. Al aumentar la cantidad de rectángulos y disminuir el ancho de cada subintervalo, podemos _aproximarnos al valor de la integral definida_.

No significa que tengamos que construir literalmente infinitos rectángulos. La idea es observar a qué valor se acercan las sumas a medida que aumentamos la cantidad de rectángulos y disminuimos su ancho.

Cuando la función es _integrable_ en $[a,b]$, las sumas de Riemann se acercan a un mismo valor a medida que el ancho de los subintervalos tiende a cero. Ese valor corresponde a la **integral definida**:

$$  
\int_a^b f(x),dx  
=\lim_{n\to\infty}S_n  
=\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i^*)\Delta x  
$$
- $\displaystyle \int_a^b f(x)\,dx$: la integral definida.
    
- $\displaystyle \lim_{n\to\infty}S_n$: el valor al que se acerca la suma de Riemann cuando aumenta la cantidad de subintervalos.
    
- La última expresión muestra _cómo se calcula esa suma_ mediante los puntos muestra y el ancho de los subintervalos.

Por lo tanto, la **integral definida** representa el valor al que se acercan las sumas de Riemann cuando los _subintervalos_ se hacen cada vez más pequeños.

En el proyecto, vamos a utilizar la secuencia $n=4\to8\to16\to32$ para observar cómo cambian las aproximaciones y cómo se acercan al valor de la integral.