Prueba Técnica de QA

Estas pruebas cubren los diferente escenarios de éxito y de error, estas son basadas en las API'S proporcionadas

APIs Probadas
1. Personas: https://www.swapi.tech/api/people/ID
2. Planetas: https://www.swapi.tech/api/planets/ID
3. Naves Espaciales: https://www.swapi.tech/api/starships/ID


- Bibliotecas de Python:
  - requests
  - unittest


Ejecutar el siguiente comando para instalar las dependencias necesarias de Python:
bash
pip install requests 


1. Navega a la carpeta del proyecto.
2. Ejecuta las pruebas con:
   bash
   python -m unittest test_api.py
   

1. Se hicieron pruebas dinámicas que cubren los siguientes escenarios

   - IDs aleatorios se generan para cubrir la mayor cantidad de datos
   - Las pruebas validan la respuesta para personas, planetas y naves espaciales.

2. Manejo de Errores:

   - Se valida que la API responda con 404 para IDs inválidos o fuera de rango.
   - Se valida que la API responda con 400 para IDs en formato diferente al numerico.
