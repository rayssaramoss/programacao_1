def senha_segura(senha):
    tamanho = len(senha)
    
    if tamanho < 8:
        return False

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False

    for char in senha:
        if 'A' <= char <= 'Z': 
            tem_maiuscula = True
        elif 'a' <= char <= 'z':  
            tem_minuscula = True
        elif '0' <= char <= '9':  
            tem_numero = True

    if tem_maiuscula and tem_minuscula and tem_numero:
        return True
    else:
        return False
    
senha1 = "MinhaSenha123"
print(f"'{senha1}' é segura? {senha_segura(senha1)}")
senha2 = "Curta1"
print(f"'{senha2}' é segura? {senha_segura(senha2)}")
senha3 = "minhasenha123"
print(f"'{senha3}' é segura? {senha_segura(senha3)}")
senha4 = "MINHASENHA123"
print(f"'{senha4}' é segura? {senha_segura(senha4)}")