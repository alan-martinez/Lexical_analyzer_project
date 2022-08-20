# Proyecto_lexico
Parte uno de la practica Analizador lexico de la materia de Seminario de Traductores 2, seccion D02 con el Dr. MICHEL EMANUEL LOPEZ FRANCO.

Cadena ingresada a evaluar:

![image](https://user-images.githubusercontent.com/70921354/185727703-758c05c5-56eb-4619-8bf0-85c3b88e8c61.png)

Resultado:

![image](https://user-images.githubusercontent.com/70921354/185727725-8a25760a-2608-48e3-8132-6c1b8c7ccdb4.png)
![image](https://user-images.githubusercontent.com/70921354/185727712-3427de6c-2748-4be6-ab96-b2f6dbd435b4.png)


Observaciones:


Para realizar esta practica fue necesario implementar los diferentes simbolos, resaltando que algunos de ellos fueron divididos (como el simbolo de relacion) ya que al ser varios, se queria tener mejor control de cual seleccionaba el usuario, los cuales quedaron asi:

![image](https://user-images.githubusercontent.com/70921354/185727439-a6509c12-8269-405f-ad97-2a3f7edc4cd9.png)


Para poder analizar la cadena ingresada por el usuario fue necesario implementar diferentes estados, en el que el estado 0 verifica todos las posibles combinaciones empezando por un caracter:


![image](https://user-images.githubusercontent.com/70921354/185727518-bf841813-75be-41c4-981d-5e965a5bbd43.png)

![image](https://user-images.githubusercontent.com/70921354/185727521-06c7ef67-949c-4560-9475-e5d1ea529089.png)

Otro posible estado al ser una cadena, era si era una palabra reservada, asi pues cuando se encontraba un espacio, se hacia la verificacion si en el diccionario pusto como palabras reservadas estaba la cadena evaluada, para asi poder ser clasificada:


![image](https://user-images.githubusercontent.com/70921354/185727591-cc21ffd2-8afd-432b-885c-b9696bdd0666.png)

Para los siguientes siguientes estados, uno de ellos fue si empezaba por un digito, en el que solo podia su sucesor ser otro digito o un punto, para ser evaluado como entero o real:

![image](https://user-images.githubusercontent.com/70921354/185727550-25737cca-8793-45ae-a8d6-28b050d1a8f5.png)
