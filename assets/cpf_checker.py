def check(cpf_cad):
    cpf_new = cpf_cad[:-2]  # checar se o CPF é verdadeiro
    cpf_temp = ''
    multi1 = 10
    multi2 = 11
    result1 = 0
    result2 = 0

    for x in cpf_new:
        k = int(x)
        cpf_temp += x
        if multi1 <= 10:
            num1 = k * multi1
            result1 += num1
            multi1 -= 1
    d1 = (result1 * 10) % 11
    if d1 == 10:
        d1 = 0
    cpf_temp += str(d1)

    for y in cpf_temp:
        o = int(y)
        if multi2 <= 11:
            num2 = o * multi2
            result2 += num2
            multi2 -= 1
    d2 = (result2 * 10) % 11
    if d2 == 10:
        d2 = 0
    cpf_temp += str(d2)

    seq = cpf_cad == (cpf_cad[0]) * len(cpf_cad)  # evita sequências como "11111111111"

    if cpf_cad == cpf_temp and not seq:
        return True
    else:
        return False