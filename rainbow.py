import sys
from pystyle import *
from colorama import Fore

ikki = r"""




██╗██╗░░██╗██╗░░██╗██╗
██║██║░██╔╝██║░██╔╝██║
██║█████═╝░█████═╝░██║
██║██╔═██╗░██╔═██╗░██║
██║██║░╚██╗██║░╚██╗██║
╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝

"""
# https://fsymbols.com/ このサイトで↑みたいなやつを作れます。
System.Size(120, 30)
System.Clear()
Anime.Fade(Center.Center(ikki), Colors.red_to_blue,  Colorate.Diagonal, interval=0.130, enter=True)
                             #  ここで色変える