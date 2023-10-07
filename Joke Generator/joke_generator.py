#Importing library "pyjokes".
import pyjokes

#Using "get_joke()"" to generate a single joke.
#Language is "Spanish".
#Category is "All".
my_joke = pyjokes.get_joke(language="es", category="all")

print(my_joke)
