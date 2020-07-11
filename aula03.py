# Meta caracteres:  ^ $   ( )
# * 0 ou n (Até se não tiver)
# + 1 ou n (Repetir condição)
# ? 0 ou 1 (Pode exitir ou não)
# {n} ou {min,max} (N>0 vez ou mais vezes)

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemmmmmmmmm"!
Jã
'''

palavra = re.findall(r"jO+ão+",texto,flags=re.IGNORECASE)
#['João', 'joão', 'Joooooooooãooooooo']
palavra = re.sub(r"jO+ão+","pão",texto,flags=re.IGNORECASE)
"""
pão trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de pão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"pão, o café tá prontinho aqui. Veeemm"!
"""
palavra = re.sub(r"jO*ão*","pão",texto,flags=re.IGNORECASE)
"""
pão trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de pão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"pão, o café tá prontinho aqui. Veeemm"!
pão
"""
palavra = re.search(r"ve{3}m{1,}",texto,flags=re.I)
#<re.Match object; span=(415, 420), match='Veeemmmmmmmmm'>

texto2 = "João ama ser amado"
palavra = re.findall(r"ama[do]{0,2}",texto2)
#['ama', 'amado']

print(palavra)