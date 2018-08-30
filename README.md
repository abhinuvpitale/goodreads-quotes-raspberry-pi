# goodreads-quotes-raspberry-pi
Display quotes scrapped from goodreads using a Raspberry Pi Zero and a Bonnet Keyboard

![](https://github.com/abhinuvpitale/goodreads-quotes-raspberry-pi/blob/master/docs/static.png)

This widget scrapes different quotes from goodreads using this [web scrapper](https://github.com/abhinuvpitale/Spiders) and displays them on the Bonnet LED

Additionally the quotes can be changed using a user defined time interval.

## Setup

1. Clone this repo

2. Create json file of different quotes using the web spider from [here](https://github.com/abhinuvpitale/Spiders)

3. run `raspiQuotes.py 100` to start the display with quotes changing every 100 seconds.

## Additional Goals

1. Rolling display

![](https://github.com/abhinuvpitale/goodreads-quotes-raspberry-pi/blob/master/docs/dynamic.gif)

This has been implemented by [skshetty](https://github.com/skshetty)


2. Using Dataplicity to get remote access

This is pretty useful as you can then create a configurable gift for someone or access the code remotely to add more quotes!
The Dataplicity lets you create a remote header-less login over web. I found it super useful to implement my code on desktop and then push it to the pi using this headerless login.

The instructions for the same are [here](https://dataplicity.com)


