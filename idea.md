USUARIO:
Esta aplicación es un formulario que te dice que delfin sos

Resolves un test y luego te dice, en base a tus respuestas, cual delfin sos.

Cada respuesta que le des al formulario termina traduciendose a un valor entero entre -2 y 2. 

Como usuario lo ves como campo de formulario comun, que recibe respuestas de la lista: "muy en desacuerdo - en desacuerdo - neutral - de acuerdo - muy de acuerdo".

Tu resultado queda guardado y luego podes acceder al mismo y/o compartirlo.


ADMIN:

Vas a poder cargar nuevos delfines, con sus parametros setteados a algun valor predefinido, con un nombre y texto descriptivo.


DEV:
Vas a usar bootstrap o algo así para que se vea bien la página.
Vas a hacer paginas con templates de django.
Vas a hacer deploy a DigitalOcean usando fabric



paginas:

    P0: pagina principal (de bienvenida)

    P1: pagina del test (formulario)

    P2: pagina de respuesta (resultado)

flujo de las paginas:
    
    P0-->P1-->P2

dificultad:

    P0: facil
    P1: casi facil (hay que colocar las preguntas y los atributos)
    P2: media (hay que hacer imagenes y escribir para cada delfin)

orden de manofactura de cada pagina:
    
    P0-->P1-->P2

tareas a concretar de P0:

    hacer un croquis muy simple
    repasar y usar bootstrap para implementar esto
    pulir asperezas
    colocar enlace a P1
