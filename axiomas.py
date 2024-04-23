import time

espacoVetorial = "Real"
dimensao = 2
soma = "x1 + x2, y1, + y2"
multipliEscalar = "a * x, a * y"

def checarAdicaoComutativa():
    # u + v = v + u
    x1 = x2 = y1 = y2 = 0
    vetorx1 = x1 + x2
    vetorx2 = x2 + x1
    vetory1 = y1 + y2
    vetory2 = y2 + y1
    time.sleep(1)
    if vetorx1 == vetorx2 and vetory1 == vetory2:
        print("A adição comutativa foi satisfeita")
        return True
    print("A adição comutativa NÃO foi satisfeita")
    return False

def checarAdicaoAssociativa():
    # (u + v) + w = u + (v + w)
    x1 = x2 = x3 = y1 = y2 = y3 = 0
    vetorx1 = x1 + (x2 + x3)
    vetorx2 = x3 + (x1 + x2)
    vetory1 = y1 + (y2 + y3)
    vetory2 = y3 + (y1 + y2)
    time.sleep(1)
    if vetorx1 == vetorx2 and vetory1 == vetory2:
        print("A adição associativa foi satisfeita")
        return True
    print("A adição associativa NÃO foi satisfeita")
    return False

def checarExistenciaVetorNulo():
    # v + 0 = v
    x, y = 1, 1
    vetorx = x + 0
    vetory = y + 0
    time.sleep(1)
    if vetorx == x and vetory == y:
        print("O elemento nulo foi satisfeito")
        return True
    print("O elemento nulo NÃO foi satisfeito")
    return False

def checarExistenciaVetorOposto():
    # v + (-v) = 0
    x, y = 1, 1
    vetorx = x + (-x)
    vetory = y + (-y)
    time.sleep(1)
    if vetorx == 0 and vetory == 0:
        print("O elemento inverso foi satisfeito")
        return True
    print("O elemento inverso NÃO foi satisfeito")
    return False

def checarDistribuicaoVetores():
    # a * (u + v) = a * u + a * v
    x1 = x2 = y1 = y2 = 0
    a = 1
    vetorx1 = a * (x1 + x2)
    vetorx2 = a * x1 + a * x2
    vetory1 = a * (y1 + y2)
    vetory2 = a * y1 + a * y2
    time.sleep(1)
    if vetorx1 == vetorx2 and vetory1 == vetory2:
        print("A multiplicão escalar sobre adição de vetores foi satisfeita")
        return True
    print("A multiplicão escalar sobre adição de vetores NÃO foi satisfeita")
    return False

def checarDistribuicaoEscalares():
    # (a + b) * v = a * v + b * v
    x, y = 1, 1
    a, b = 1, 1
    vetorx1 = (a + b) * x
    vetorx2 = a * x + b * x
    vetory1 = (a + b) * y
    vetory2 = a * y + b * y
    time.sleep(1)
    if vetorx1 == vetorx2 and vetory1 == vetory2:
        print("A multiplicão escalar sobre adição de escalares foi satisfeita")
        return True
    print("A multiplicão escalar sobre adição de escalares NÃO foi satisfeita")
    return False

def checarAssociativadeEscalar():
    # (a * b) * v = a * (b * v)
    x, y = 1, 1
    a, b = 1, 1
    vetorx1 = (a * b) * x
    vetorx2 = a * (b * x)
    vetory1 = (a * b) * y
    vetory2 = a * (b * y)
    time.sleep(1)
    if vetorx1 == vetorx2 and vetory1 == vetory2:
        print("A multiplicação associativa foi satisfeita")
        return True
    print("A multiplicação associativa NÃO foi satisfeita")
    return False

def checarIdentidadeMultiplicativa():
    # 1 * v = v
    x, y = 1, 1
    vetorx = 1 * x
    vetory = 1 * y
    time.sleep(1)
    if vetorx == x and vetory == y:
        print("A identidade multiplicativa foi satisfeita")
        return True
    print("A identidade multiplicativa NÃO foi satisfeita")
    return False

def testarEspacoVetorial():
    axm1 = checarAdicaoComutativa()
    axm2 = checarAdicaoAssociativa()
    axm3 = checarExistenciaVetorNulo()
    axm4 = checarExistenciaVetorOposto()
    axm5 = checarDistribuicaoVetores()
    axm6 = checarDistribuicaoEscalares()
    axm7 = checarAssociativadeEscalar()
    axm8 = checarIdentidadeMultiplicativa()
    print("----------------")
    if (axm1 == axm2 == axm3 == axm4 == axm5 == axm6 == axm7 == axm8 == True):
        print("É um espaço vetorial, pois cumpri todos os 8 axiomas")
    else:
        print("Não é um espaço vetorial, pois não cumpri todos os 8 axiomas")
    
testarEspacoVetorial()