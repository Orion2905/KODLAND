# Importa la libreria turtle
import turtle

# Crea un oggetto Turtle e lo assegna alla variabile 't'
t = turtle.Turtle()

# Imposta la forma della tartaruga
t.shape("turtle")

# Sposta la tartaruga in avanti di 20 unità e disegna una linea
t.forward(20)

# Solleva la penna (la tartaruga non disegna mentre si muove)
t.up()

# Sposta la tartaruga in avanti di altre 20 unità senza disegnare
t.forward(20)

# Riabbassa la penna (la tartaruga riprende a disegnare mentre si muove)
t.down()

# Sposta la tartaruga in avanti di altre 20 unità e disegna una linea
t.forward(20)
