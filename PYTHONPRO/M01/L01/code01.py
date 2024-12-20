# Importa la libreria turtle per creare disegni grafici
import turtle

# Crea un oggetto Turtle e lo assegna alla variabile 't'
t = turtle.Turtle()

# Imposta la forma della tartaruga (la renderà visibile come una tartaruga)
t.shape("turtle")

# Fa avanzare la tartaruga di 100 unità
t.forward(100)

# Fa tornare indietro la tartaruga di 100 unità
t.backward(100)

# Ruota la tartaruga di 90 gradi verso sinistra (in senso antiorario)
t.left(90)

# Ruota la tartaruga di 90 gradi verso destra (in senso orario)
t.right(90)
