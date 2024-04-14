import time
import feedparser
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk


# >>  Declara e inicializa la seccion de widgets (reloj y noticias).
root = tk.Tk()
root.config(bg="White")
root.title('SECCION DE NOTICIAS')
root.geometry("1080x100+0+1756")
root.overrideredirect(1)

feed1 = feedparser.parse('http://www.eltiempo.com/rss/colombia.xml')
feed2 = feedparser.parse('http://www.eltiempo.com/rss/bogota.xml')
feed3 = feedparser.parse('http://www.eltiempo.com/rss/mundo.xml')
feed4 = feedparser.parse('http://portafolio.co/rss/economia')


# >> Declara y configura el RELOJ.
time1 ='' # ++ Inicializa TIEMPO_1.
clock= tk.Label(root, font=('Arial', 40, 'bold'), bg="White", fg="Black")
clock.pack()
clock.place(x=10, y=22)

def reloj():
    global time1
    time2 = time.strftime('%H:%M')
    if time2 != time1:
        time1 = time2
        clock.configure(text = time2)
    clock.after(500, reloj)


# >> Declara y configura el ticker de NOTICIAS.
ticker_speed = 150 # ++ Configura velocidad del ticker.
ticker_data = tk.StringVar()
labl = tk.Label(root, textvariable = ticker_data, font = ('Arial', 40), bg = 'black', fg = 'white')
labl.pack()
labl.place(x = 170, y = 22, width = 830)

def ticker():
    ticker.msg = ticker.msg[1:] + ticker.msg[0]
    ticker_data.set(ticker.msg)
    root.after(ticker_speed, ticker)
    
try:
    ticker.msg = feed1['entries'][0]['title'] + '   |   ' + feed2['entries'][0]['title'] + '   |   ' + feed3['entries'][0]['title'] + '   |   ' + feed4['entries'][0]['title'] + '   |   '
except:
    ticker.msg = "     Bienvenidos     "


# >> Ejecuta los metodos de cada widget.
ticker() # ++ Ejecuta el metodo TICKER
reloj() # ++ Ejecuta el metodo RELOJ


root.lift()
root.call('wm', 'attributes', '.', '-topmost', True)
root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)


# >> Detiene y reinicia el programa.
root.mainloop()