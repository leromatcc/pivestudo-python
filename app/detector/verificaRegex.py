
import re

"""
REGEX para Placas Brasileiras (incluindo Mercosul) 

Em conformidade com a Resolução 780/2019 CONTRAN(http://www.in.gov.br/web/dou/-/resolucao-n-780-de-26-de-junho-de-2019-179414765), de 26 de junho de 2019, a expressão regular abaixo valida todas as placas em uso no Brasil incluindo aquelas no formato pré-Mercosul:

[A-Z]{3}[0-9][0-9A-Z][0-9]{2}

https://ricardo.coelho.eti.br/regex-mercosul/
"""


def contemPlacaBr(texto_original):
    regex = ".*[A-Z]{3}[0-9][0-9A-Z][0-9]{2}.*"
    return re.search(regex, texto_original)


print("contemPlaca 1:" + str( contemPlacaBr("AAAA1A11"))                                             )
print("contemPlaca 2:" + str( contemPlacaBr("The life in spain is great if it is London"))  )
print("contemPlaca 3:" + str( contemPlacaBr("The life in spain AAAA1A11 is great if it is Spain"))   )
print("contemPlaca 4:" + str( contemPlacaBr("lalallalaAAAA1A11"))                                    )



def contemPlacaUSA(texto_original):
    # essa regex e incompleta e usada para testes, nao é a definicao oficial de qualquer estado dos USA
    # usado com as imagens de desenvolvimento
    regex = "[0-9A-Z]{7}"
    return re.search(regex, texto_original)


print("contemPlacaUSA 1:" + str( contemPlacaUSA("AAAA1A11"))                                            )
print("contemPlacaUSA 2:" + str( contemPlacaUSA("6S0D986"))                                             )
print("contemPlacaUSA 3:" + str( contemPlacaUSA("The life in spain 6S0D986 is great if it is London"))  )
print("contemPlacaUSA 4:" + str( contemPlacaUSA("The life in spain AAAA1A11 is great if it is Spain"))  )
print("contemPlacaUSA 5:" + str( contemPlacaUSA("The life in spain is great if it is Spain"))           )
print("contemPlacaUSA 6:" + str( contemPlacaUSA("lalallala"))                                           )


