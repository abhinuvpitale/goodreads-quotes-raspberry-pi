# goodreads-quotes-raspberry-pi

Display quotes scrapped from goodreads using a [Raspberry Pi Zero](https://www.amazon.com/Raspberry-Pi-Zero-Wireless-Essentials/dp/B06XCYGP27) and a Bonnet Keyboard

<p align="center">
  <img width="480" src="https://github.com/abhinuvpitale/goodreads-quotes-raspberry-pi/blob/master/docs/static.png" />
</p>

This widget scrapes different quotes from goodreads using this [web scrapper](https://github.com/abhinuvpitale/Spiders) and displays them on the Bonnet LED

*Additionally the quotes can be changed using a user defined time interval.*

## Setup

- Clone this repo

- Create json file of different quotes using the web spider from [here](https://github.com/abhinuvpitale/Spiders)

- Run `raspiQuotes.py 100` to start the display with quotes changing every `100 seconds`.

## Additional Goals

### Rolling display

<p align="center">
  <img height="480" src="https://github.com/abhinuvpitale/goodreads-quotes-raspberry-pi/blob/master/docs/dynamic.gif" />
</p>

> This has been implemented by [skshetty](https://github.com/skshetty)

###  Using Dataplicity to get remote access

This is pretty useful as you can then create a configurable gift for someone or access the code remotely to add more quotes!
The Dataplicity lets you create a remote header-less login over web. I found it super useful to implement my code on desktop and then push it to the pi using this headerless login.

The instructions for the same are [here](https://dataplicity.com)


