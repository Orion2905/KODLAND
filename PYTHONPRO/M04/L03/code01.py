import time  # Importa il modulo `time` per gestire i ritardi temporali nelle stampe e migliorare l'esperienza utente

# Dizionario delle stanze. Ogni stanza è una chiave con:
# - `rooms`: una lista delle stanze accessibili da quella stanza
# - `items`: una lista degli oggetti presenti nella stanza
rooms = {
    'start': {'rooms': ['1'], 'items': []},  # Stanza iniziale senza oggetti
    '1': {'rooms': ['Entrata', '2'], 'items': []},  # Collegamento a "Entrata" e "2"
    '2': {'rooms': ['1', '3', '4'], 'items': []},  # Collegamento a "1", "3" e "4"
    '3': {'rooms': ['2'], 'items': []},  # Stanza di morte collegata a "2"
    '4': {'rooms': ['2', '5', '6'], 'items': []},  # Collegamento a "2", "5" e "6"
    '5': {'rooms': ['4'], 'items': ['key']},  # Contiene una chiave
    '6': {'rooms': ['4', '7'], 'items': []},  # Collegamento a "4" e "7"
    '7': {'rooms': ['10', '8', '6'], 'items': []},  # Stanza con molti collegamenti
    '8': {'rooms': ['7', '9'], 'items': ['key']},  # Contiene una chiave
    '9': {'rooms': ['8'], 'items': []},  # Collegamento a "8"
    '10': {'rooms': ['7', '11'], 'items': []},  # Collegamento a "7" e "11"
    '11': {'rooms': ['10', '12'], 'items': []},  # Collegamento a "10" e "12"
    '12': {'rooms': ['Uscita', '11'], 'items': []},  # Ultima stanza prima dell'uscita
}

# Variabile iniziale che rappresenta la posizione corrente del giocatore
room = 'Entrata'

# Variabile che tiene traccia del numero di chiavi raccolte
keys = 0

# Ciclo principale del gioco
while True:
    print('============================')
    print('Sei nella stanza:', room)  # Indica al giocatore la stanza corrente
    
    # Mostra le stanze accessibili dalla stanza corrente
    for near_room in rooms[room]['rooms']:
        print('Puoi andare alla stanza:', near_room)
    
    # Richiede al giocatore di scegliere una stanza
    new_room = input('Quale stanza scegli? ')
    
    # Verifica se la stanza scelta è accessibile dalla stanza corrente
    if new_room not in rooms[room]['rooms']:
        print('Questa stanza non esiste o non è accessibile!')
        time.sleep(2)  # Aspetta 2 secondi prima di ripetere il ciclo
        continue

    # Verifica se il giocatore tenta di accedere all'uscita senza chiavi
    if new_room == 'Uscita' and keys == 0:
        print('Non hai una chiave per uscire! Trova almeno una chiave.')
        time.sleep(2)  # Aspetta 2 secondi prima di ripetere il ciclo
        continue

    # Controlla se il giocatore entra nella stanza "3", che causa la morte
    if new_room == '3':
        print('Sei morto! Gioco terminato.')  # Mostra il messaggio di morte
        time.sleep(2)  # Aspetta 2 secondi prima di terminare il ciclo
        break

    # Controlla se il giocatore ha raggiunto l'uscita con almeno una chiave
    if new_room == 'Uscita':
        print('Hai vinto! Complimenti!')  # Mostra il messaggio di vittoria
        time.sleep(2)  # Aspetta 2 secondi prima di uscire dal ciclo
        break

    # Aggiorna la posizione del giocatore alla nuova stanza
    room = new_room

    # Controlla se la stanza contiene una chiave
    if 'key' in rooms[room]['items']:
        keys += 1  # Incrementa il numero di chiavi raccolte
        print('Hai trovato una chiave! Ora hai', keys, 'chiave/i.')
        rooms[room]['items'].remove('key')  # Rimuove la chiave dalla stanza, evitando che venga raccolta di nuovo
        time.sleep(2)  # Aspetta 2 secondi per dare tempo al giocatore di leggere
