import os
import sys

entrada = input("Digite o texto que você quer em SHA1: ")
os.system("echo " + entrada + " | openssl sha1 > result.txt")

print("Fiz um arquivo em result.txt, dá uma olhada lá :)")
