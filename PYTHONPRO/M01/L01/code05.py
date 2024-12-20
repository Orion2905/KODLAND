# Importa la libreria turtle
import turtle

# Crea un oggetto Turtle e lo assegna alla variabile 't'
t = turtle.Turtle()

# Imposta la forma della tartaruga
t.shape("turtle")

# Cambia il colore della tartaruga e disegna la prima parte
t.color("green")  # Colore verde
t.forward(20)     # Disegna una linea di 20 unità

# Solleva la penna e si sposta senza disegnare
t.up()
t.forward(20)     # Sposta la tartaruga in avanti di 20 unità senza traccia

# Riabbassa la penna per riprendere il disegno
t.down()

# Cambia il colore della tartaruga e disegna la seconda parte
t.color("yellow")  # Colore giallo
t.forward(20)      # Disegna una linea di 20 unità

# Solleva la penna e si sposta senza disegnare
t.up()
t.forward(20)      # Sposta la tartaruga in avanti di 20 unità senza traccia

# Riabbassa la penna per riprendere il disegno
t.down()

# Cambia il colore della tartaruga e disegna la terza parte
t.color("red")     # Colore rosso
t.forward(20)      # Disegna una linea di 20 unità

# Solleva la penna e si sposta senza disegnare
t.up()
t.forward(20)      # Sposta la tartaruga in avanti di 20 unità senza traccia

# Riabbassa la penna per riprendere il disegno
t.down()
