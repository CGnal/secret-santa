# Secret Santa

Chi ha mai partecipato ad un Secret Santa? 🙋‍♀️
Le regole sono molto semplici. 
Ciascun partecipante sarà il Secret Santa 🎅 per una persona che gli verrà assegnata casualmente, ovvero sarà il suo Babbo Natale segreto.
Il Secret Santa dovrà fare un regalo alla persona che gli è stata assegnata secondo un budget prestabilito.
Tutti i regali verranno scambiati prima di Natale e ciascun partecipante riceverà esattamente un regalo 🎁.

In CGnal il Secret Santa è una tradizione e ogni anno i regali vengono scambiati durante la cena di Natale.

Anche se quest'anno è un anno speciale, siamo riusciti ad organizzare lo stesso il tradizionale Secret Santa.
Abbiamo usato il codice riportato in questo repository per organizzarlo.
Invece che estrarre il nome del collega con dei bigliettini, il nome del collega sarà comunicato via mail.


## Come funziona

Copia il repository sul tuo computer.

```
git clone 
```

### Inserisci i nomi dei partecipanti

Cambia il file people.xlsx e inserisci i nomi e l'indirizzo email di tutti i partecipanti. 
Se non potete scambiarvi i regali di persona inserite anche gli indirizzi ed eventualmente i numeri di telefono per
poter spedire il regalo direttamente a casa. 
Puoi specificare eventuali match non validi. Specifica nome e cognome nella colonna "match non validi".
Se vuoi evitare un match con più di una persona separa i nomi con una virgola. 

Puoi modificare il testo che verrà inviato per mail in ```code/text.py```

### Esegui il codice

Assicurati di aver installato Python3.6 sul tuo computer con i pacchetti specificati in 
```requirements.txt```.

Da riga di comando esegui

```
cd secretsanta
python main.py
```

ti verrà quindi chiesto di specificare:
- indirizzo mail usato per spedire i messaggi a tutti i partecipanti;
- username (potrebbe essere la mail stessa);
- password della tua mail;
- smtp_addres: se non hai un indirizzo smtp privato puoi usare anche un indirizzo pubblico;
  Ad esempio se invii una mail con Gmail puoi usare smtp.gmail.com, se utilizzi outlook puoi usare smtp.live.com e così via;
- protocollo: TLS o SSL.


Buon Secret Santa!


