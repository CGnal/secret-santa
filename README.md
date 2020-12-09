# Secret Santa

Chi ha mai partecipato ad un Secret Santa? 🙋‍♀️
Le regole sono molto semplici. 
Ciascun partecipante sarà il Secret Santa per una persona che gli verrà assegnata casualmente, ovvero sarà il suo Babbo Natale segreto.
Il Secret Santa dovrà fare un regalo alla persona che gli è stata assegnata secondo un budget prestabilito.
Tutti i regali verranno scambiati prima di Natale e ciascun partecipante farà e riceverà esattamente un regalo 🎁.

In CGnal il Secret Santa è una tradizione e ogni anno i regali vengono scambiati durante la cena di Natale.

Anche se quest'anno è speciale, siamo riusciti ad organizzare lo stesso il tradizionale Secret Santa, usando il codice riportato in questo repository.
Invece che estrarre il nome del collega con dei bigliettini, il nome del collega viene comunicato via mail.


## Come funziona

Copia il repository sul tuo computer.

```
git clone https://github.com/CGnal/secret-santa.git
```

### Inserisci i nomi dei partecipanti

Cambia il file ```santacode/people.xlsx``` inserendo i nomi e l'indirizzo email di tutti i partecipanti. 
Se non potete scambiarvi i regali di persona inserisci anche gli indirizzi ed eventualmente i numeri di telefono per
poter spedire il regalo direttamente a casa. 

Puoi specificare eventuali **match non validi**. 
Se non si vuole che una persona diventi il Secret Santa di qualcuno in particolare, puoi specificarlo in "match non validi". 
Se vuoi evitare il match con più di una persona, puoi scrivere nomi e cognomi separati da virgola.

Puoi modificare il testo che verrà inviato per mail in ```santacode/text.py```

### Esegui il codice

Assicurati di aver installato Python3.6 o una versione successiva sul tuo computer con i pacchetti specificati in 
```requirements.txt```.

Da terminale esegui

```
cd secret-santa
python main.py
```

ti verrà quindi chiesto di specificare:
- indirizzo mail usato per spedire i messaggi a tutti i partecipanti;
- username (potrebbe essere la mail stessa);
- password della tua mail;
- smtp_addres: se non hai un indirizzo smtp privato puoi usare anche un indirizzo pubblico.
  Se hai un account Gmail puoi usare smtp.gmail.com, se utilizzi outlook puoi usare smtp.live.com e così via;
- protocollo: TLS o SSL.

Buon Secret Santa!
