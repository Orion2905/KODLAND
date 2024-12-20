# Importa la libreria turtle per disegnare grafica vettoriale
import turtle

# Crea un oggetto Turtle e lo assegna alla variabile 't'
t = turtle.Turtle()

# Imposta la forma della tartaruga (apparirà visivamente come una tartaruga)
t.shape("turtle")

# Disegnare un quadrato:
# Sposta la tartaruga in avanti di 100 unità
t.forward(100)

# Ruota la tartaruga di 90 gradi a sinistra (antiorario)
t.left(90)

# Sposta la tartaruga in avanti di 100 unità (secondo lato del quadrato)
t.forward(100)

# Ruota la tartaruga di 90 gradi a sinistra
t.left(90)

# Sposta la tartaruga in avanti di 100 unità (terzo lato del quadrato)
t.forward(100)

# Ruota la tartaruga di 90 gradi a sinistra
t.left(90)

# Sposta la tartaruga in avanti di 100 unità (quarto lato del quadrato, chiudendo la figura)
t.forward(100)
