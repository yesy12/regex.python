# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | ou
# . Qualquer caractere (com exceção da quebra de linha)
# [ ] conjunto de caracteres
import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

palavra = re.findall(r"João|Maria|adultos",texto)
#['João', 'Maria', 'adultos', 'Maria']
palavra = re.findall(r"João|M.r.a|.d.ltos",texto)
#['João', 'Maria', 'adultos', 'Maria']
palavra = re.findall(r"[Jj]oão|[Mm]aria",texto)
#['João', 'Maria', 'joão', 'maria', 'Maria']
palavra = re.findall(r"[a-z]aria",texto)
#['maria']
palavra = re.findall(r"[a-zA-z]aria",texto)
#['Maria', 'maria', 'Maria']
palavra = re.findall(r"jOão|mAriA",texto,flags=re.IGNORECASE)
#['João', 'Maria', 'joão', 'maria', 'Maria']

print(palavra)