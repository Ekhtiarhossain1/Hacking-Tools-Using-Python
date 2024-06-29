#! /usr/bin/python3
import urllib.request as ur
import pyfiglet
from termcolor import colored

print(colored("*****************Website Source Code Downloader*************************", "red"))
print(colored("*****************Website Source Code Downloader*************************", "green"))

banner = colored(pyfiglet.figlet_format("Source Code"), "red")
banner2 = colored(pyfiglet.figlet_format("Downloader"), "green")
print(banner, banner2)


url = input("Enter Target Website URL(ex: https://www.google.com): ")

source = ur.urlopen(url)
source_code = source.read()

print(source_code)
