# Ejemplo propio: cálculo de sumas de Riemann

## 1. Función, intervalo y punto muestra

Para este ejemplo vamos a utilizar la función

$$  
f(x)=x^2+1  
$$

en el intervalo cerrado $[0,2]$. Primero, podemos calcular el valor exacto de la integral definida para después comparar ese resultado con las aproximaciones que obtengamos mediante rectángulos:

$$  
\begin{aligned}  
\int_0^2(x^2+1)\ dx  
&=\left[\frac{x^3}{3}+x\right]_0^2\  
&=\frac{8}{3}+2\  
&=\frac{14}{3}\  
&\approx 4.6666667  
\end{aligned}  
$$

Para escoger los puntos muestra, vamos a utilizar los **puntos medios** de cada subintervalo. Esto significa que vamos a elegir el punto que está justo en la mitad de cada uno. Por lo tanto, para el subintervalo $[x_{i-1},x_i]$, el punto muestra será:

$$  
x_i^*=\frac{x_{i-1}+x_i}{2}  
$$

También podríamos utilizar los extremos izquierdos o derechos, pero en este caso vamos a utilizar los puntos medios para calcular la suma de Riemann.

**Condiciones del ejemplo.** $f(x)=x^2+1$ es un polinomio, por lo que es **continua** en $[0,2]$ y, por lo tanto, **integrable**: las sumas de Riemann tienen un límite cuando $n\to\infty$ y ese límite es la integral definida. Además $f(x)>0$ en todo el intervalo, así que cada $S_n$ aproxima el **área geométrica** bajo la curva. Usamos una **partición regular** (todos los subintervalos miden $\Delta x$) y cada punto muestra está dentro de su subintervalo, $x_i^{\ast}\in[x_{i-1},x_i]$.

## 2. Fórmula que vamos a utilizar

Como el intervalo es $[0,2]$, el ancho de cada subintervalo se calcula de la siguiente manera:

$$  
\Delta x=\frac{b-a}{n}=\frac{2-0}{n}=\frac{2}{n}  
$$

Para calcular los puntos medios, podemos utilizar la siguiente expresión:

$$  
x_i^*=\left(i-\frac{1}{2}\right)\frac{2}{n},  
\qquad i=1,2,\dots,n  
$$

Esta fórmula permite obtener el punto medio de cada subintervalo según el valor de $n$ que utilicemos.

Ahora, recordemos que la **suma de Riemann** se obtiene al sumar las áreas con signo de todos los rectángulos. Como la altura de cada rectángulo es $f(x_i^*)$ y su base mide $\Delta x$, tenemos:

$$  
S_n=\sum_{i=1}^{n}f(x_i^*)\Delta x  
$$

Al reemplazar la función $f(x)=x^2+1$ y las expresiones anteriores, obtenemos:

$$  
S_n=\sum_{i=1}^{n}  
\left[  
\left(\left(i-\frac{1}{2}\right)\frac{2}{n}\right)^2+1  
\right]\frac{2}{n}  
$$

Esta es la fórmula que vamos a utilizar para calcular las sumas de Riemann con puntos medios para cada valor de $n$.

## 3. Cálculo para cada valor de $n$

### Cuando $n=4$

Primero, calculamos el ancho de cada subintervalo:

$$  
\Delta x=\frac{2}{4}=\frac{1}{2}  
$$

Como tenemos 4 subintervalos, debemos encontrar el punto medio de cada uno. En este caso, los puntos medios son:

$$  
\frac{1}{4},\quad \frac{3}{4},\quad  
\frac{5}{4},\quad \frac{7}{4}  
$$

Ahora evaluamos la función en cada punto medio y sumamos las áreas de los cuatro rectángulos. Como la base de todos mide $\frac{1}{2}$, podemos escribir:

$$
\begin{aligned}
S_4
&=\frac{1}{2}\left[
\left(\left(\frac{1}{4}\right)^2+1\right)
+\left(\left(\frac{3}{4}\right)^2+1\right)\right.\\
&\qquad\left.
+\left(\left(\frac{5}{4}\right)^2+1\right)
+\left(\left(\frac{7}{4}\right)^2+1\right)
\right]\\
&=\frac{37}{8}\\
&=4.625
\end{aligned}
$$

Por lo tanto, cuando utilizamos 4 subintervalos, obtenemos una aproximación de $4.625$.

### Cuando $n=8$, $n=16$ y $n=32$

Para los siguientes valores repetimos el mismo procedimiento: calculamos $\Delta x$, encontramos los puntos medios, evaluamos la función en esos puntos y sumamos las áreas de los rectángulos.

Los resultados obtenidos son los siguientes:

|$n$|$\Delta x$|$S_n$ exacta|$S_n$ aproximada|Diferencia con $\frac{14}{3}$|
|---|---|---|---|---|
|4|$\frac{1}{2}$|$\frac{37}{8}$|4.625000|0.041667|
|8|$\frac{1}{4}$|$\frac{149}{32}$|4.656250|0.010417|
|16|$\frac{1}{8}$|$\frac{597}{128}$|4.664063|0.002604|
|32|$\frac{1}{16}$|$\frac{2389}{512}$|4.666016|0.000651|

Para esta función también podemos expresar los resultados mediante una fórmula general:

$$  
S_n=\frac{14}{3}-\frac{2}{3n^2}  
$$

Esta expresión permite calcular la suma de Riemann para los distintos valores de $n$ sin tener que escribir cada rectángulo por separado.

### Deducción de la fórmula de $S_n$

Con puntos medios, $x_i^{\ast}=\frac{2i-1}{n}$, así que $f(x_i^{\ast})=\frac{(2i-1)^2}{n^2}+1$ y $\Delta x=\frac{2}{n}$:

```math
S_n=\sum_{i=1}^{n}\left[\frac{(2i-1)^2}{n^2}+1\right]\frac{2}{n}=\frac{2}{n^3}\sum_{i=1}^{n}(2i-1)^2+\frac{2}{n}\cdot n
```

La suma de los cuadrados de los $n$ primeros impares se obtiene restando los cuadrados pares a la suma de los cuadrados de $1$ a $2n$ (usando $\sum_{k=1}^{m}k^2=\frac{m(m+1)(2m+1)}{6}$):

```math
\sum_{i=1}^{n}(2i-1)^2=\sum_{k=1}^{2n}k^2-4\sum_{j=1}^{n}j^2=\frac{2n(2n+1)(4n+1)}{6}-\frac{4n(n+1)(2n+1)}{6}=\frac{n(4n^2-1)}{3}
```

Reemplazando:

```math
S_n=\frac{2}{n^3}\cdot\frac{n(4n^2-1)}{3}+2=\frac{8}{3}-\frac{2}{3n^2}+2=\frac{14}{3}-\frac{2}{3n^2}
```

**Comprobación con la tabla:** para $n=4$, $\frac{14}{3}-\frac{2}{48}=\frac{224-2}{48}=\frac{37}{8}=S_4$. La fórmula y la deducción también se verifican con `python verify.py`, que calcula cada $S_n$ rectángulo por rectángulo.

Como $\frac{2}{3n^2}>0$, todas las sumas quedan por debajo de $\frac{14}{3}$, y como $\frac{2}{3n^2}\to 0$ cuando $n\to\infty$:

```math
\lim_{n\to\infty}S_n=\frac{14}{3}=\int_0^2 (x^2+1)\ dx
```

Por ejemplo, cuando $n=8$:

$$  
\begin{aligned}  
S_8  
&=\frac{14}{3}-\frac{2}{3(8)^2}\  
&=\frac{149}{32}\  
&\approx 4.65625  
\end{aligned}  
$$

## 4. Comparación con el valor exacto

Como vimos al principio, el valor exacto de la integral definida es:
    
$$  
\frac{14}{3}\approx 4.6666667  
$$

Al comparar este valor con los resultados de la tabla, podemos observar que la suma $S_4$ todavía presenta una diferencia de aproximadamente $0.041667$.

Sin embargo, cuando aumentamos la cantidad de subintervalos, el ancho $\Delta x$ disminuye y las sumas de Riemann se acercan cada vez más al valor exacto de la integral.

En este ejemplo, todas las aproximaciones quedan por debajo de $\frac{14}{3}$. Aun así, la diferencia disminuye desde aproximadamente $0.041667$ cuando $n=4$ hasta $0.000651$ cuando $n=32$.

Por lo tanto, podemos observar cómo, al aumentar la cantidad de rectángulos y disminuir el ancho de cada uno, las sumas de Riemann se acercan al valor de la integral definida.
