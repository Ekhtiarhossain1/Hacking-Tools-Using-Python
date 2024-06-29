#! /usr/bin/python3
import socket
import pyfiglet
from termcolor import colored

print(colored("*****************Domain To IP Converter*************************", "red"))
print(colored("*****************Domain To IP Converter*************************", "green"))


banner = colored(pyfiglet.figlet_format("IP CONVERTER"), "red")

print(banner)

domain_name = input("Enter Domain Name: ")

ip = socket.gethostbyname(domain_name)

print("IP for {} is:{}".format(domain_name, ip))
