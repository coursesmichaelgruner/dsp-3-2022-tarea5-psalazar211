# Sistema de Supresión de Ruido de Red Eléctrica

>1. La libreria spicy.io.wave tiene una funcionalidad que permite  leer de un archivo wav la señal y la frecuencia de muestreo Fs. De esta forma se obtuvo que la frecuencia de meustreo de 48000 Hz. La señal obtenida en el dominio del tiempo  es la de la siguiente figura:
><img width="836" alt="image" src="https://user-images.githubusercontent.com/104046146/201721628-0ad896a0-21a2-4ca1-bc21-70052b5ac2d2.png">
<br />
2. Usando la fft de spicy para otener la Dtf se obtiene la señal en el dominio de la frecuencia: 
<img width="819" alt="image" src="https://user-images.githubusercontent.com/104046146/201722400-1f270ef0-0031-4fd7-9c1e-d9f0b469135b.png">

3.Realizando un ampliacion de espectros se ve que hay componentes de frecuencia cada multiplo de 60, en 120Hz, 180Hz, 240Hz, 300Hz, 360Hz...

<img width="813" alt="image" src="https://user-images.githubusercontent.com/104046146/202114869-81308b80-a2c8-4460-9f9e-bc8e2efbd709.png">
<br />
4. Para 4 ventanas a 4 ventanas distintas demucho menor tamano., se tiene: 
<img width="446" alt="image" src="https://user-images.githubusercontent.com/104046146/202115299-948b20bc-5034-464e-98c7-f886145d7167.png">
<img width="461" alt="image" src="https://user-images.githubusercontent.com/104046146/202115426-00638008-3857-4d3b-8067-249bf7b51776.png">
<img width="452" alt="image" src="https://user-images.githubusercontent.com/104046146/202115535-0b956795-3c67-4fd7-a43f-afe9e54be246.png">
<img width="442" alt="image" src="https://user-images.githubusercontent.com/104046146/202115657-98c175e2-6edc-4f11-8100-cd59ae558b81.png">
<br />
5. Para filtrar la senal se colocaron 7 filtros notch para suprimir 60Hz y 6 de sus armonicas en serie. Para disenar el filtro notch se uso el diagrama de polos y ceros. Para conseguir este patron se  colocan un par de ceros conjugados y un par de polos conjugados con angulo θ. Los ceros deben ser dominantes, mientras que los polos deben estar dentro del circulo unitario para mantener la estabilidad.  Recordando que:
<br />
θ = wT = 2*pi*f/Fs
Por ejemplo para f=60Hz:
<br />
θ = 2*pi*60/4800 = pi/400
<br />
De esta forma:
<br />
H(z)= (z-exp(j*pi/400))(z-exp(-j*pi/400))/(z-0.95exp(j*pi/400))(z-0.95exp(-j*pi/400))
<br />
H(z)= (z^2-2cos(pi/400)z+1)/(z^2-2*0.95*cos(pi/400)z+0.95^2)

Notese que como las  otras  frecuencias eliminar son los armonicos de 60, para el armonico n:
H(z)= (z^2-2cos(pi*n/400)z+1)/(z^2-2*0.95*cos(pi*n/400)z+0.95^2)

Digrama de polso y ceros:
<img width="360" alt="image" src="https://user-images.githubusercontent.com/104046146/202119556-f33c2094-2cf8-4fa4-9e17-291267ea6da8.png">


6. Respuesta a la frecuencia: <img width="860" alt="image" src="https://user-images.githubusercontent.com/104046146/202120632-241c5f98-5062-4ddc-a149-2ea49d503cc8.png">
<img width="832" alt="image" src="https://user-images.githubusercontent.com/104046146/202120876-f0e58fa1-7381-4b9a-a6c1-3e669e8cf460.png">
<img width="848" alt="image" src="https://user-images.githubusercontent.com/104046146/202121557-7300e425-e4b8-4156-83bf-b79ec15527a9.png">

7. Pasando la senal por los 7 filtros en serie se obtiene:
<img width="449" alt="image" src="https://user-images.githubusercontent.com/104046146/202126851-428f5d6d-8433-4611-a638-0551e700ec08.png">

8. Comparando la senal filtrada con la senal de referencia:
![Uploading image.png…]()

Se ve que aunque el comportamiento se asemeja, no son iguales. Para ello hay que tomar en cuenta que como se ve en la respuesta a la frecuencia la magnitud antes de bajar a 0 en la frecuncia correspondientes se muy baja. Esta deberia ser 1 al igual, Estas perdidas pueden ser compesadas por alguna ganancia, haciendo un rediseno. Sin embargo, eneste primer intento se logra apreciar como el diagrama de polos y ceros conjunto a la respuesta a la frecuencia permiten tener una idea de como se va a comportar el filtro. 

Fuentes:
el codigo para graficar el plano z en python fue tomado de : https://www.dsprelated.com/showcode/244.php






