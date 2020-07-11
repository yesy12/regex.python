#youtube.com/watch?v=wBI0yv2FG6U
import re

#findall para encontrar todos os padrões em um texto
#search primeira vez encontrada e o indice
#sub substituir padrões

#compile reutilizacao de padroes

string = "Este é um teste de expressões teste regulares."

palavra = re.search(r"teste",string)
print(palavra)
#<re.Match object; span=(10, 15), match='teste'>
palavra_erro = re.search(r"teste2",string)
print(palavra_erro)
#None

palavra = re.findall(r"teste",string)
print(palavra)
#['teste', 'teste']
palavra_erro = re.findall(r"teste2",string)
print(palavra_erro)
#[]

palavra = re.sub(r"teste","ABCD", string)
print(palavra)
#Este é um ABCD de expressões ABCD regulares.Este é um ABCD de expressões ABCD regulares.
palavra = re.sub(r"teste","ABCD", string,count=1)
print(palavra)
#Este é um ABCD de expressões teste regulares.

regex = re.compile(r"teste")
print(regex.search(string))
print(regex.findall(string))
print(regex.sub("DEF",string))
#<re.Match object; span=(10, 15), match='teste'>
# ['teste', 'teste']
# Este é um DEF de expressões DEF regulares.