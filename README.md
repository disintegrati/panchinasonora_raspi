## PANCHINE SONORE

Le panchine sonore sono un'installazione parte della scultura #CUOREDINAPOLI.

## Installazione pacchetti

Aggiorna il sistema.

Scarica il pacchetto Python3.

```bash
sudo apt-get install python3
```

Scarica il pacchetti pygame.

```bash 
sudo apt-get install python3-pygame
apt-get install libsdl-mixer1.2
```
Scarica i pacchetti RPi.GPIO

```bash
sudo apt-get install python-rpi.gpio python3-rpi.gpio
```

## Scaricare da github

Installa [github](https://projects.raspberrypi.org/en/projects/getting-started-with-git/4)

Scarica da github la directory con all'interno

```bash
sudo git clone https://github.com/mediaintegrati/panchinasonora_raspi.git
```

## Utilizzo

Vai nella directory appena scaricata e fai partire il programma e testalo.

```bash
sudo python3 panchinarasp.py
```

Per farlo partire in autorun, inserisci nella cartella rc.local il percorso del file py da eseguire all'avvio.

