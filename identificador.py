def identificar_bandeira(numero_cartao):
    numero = str(numero_cartao)

    # Visa: começa com 4 e tem 13 ou 16 dígitos
    if re.fullmatch(r"4\d{12}(\d{3})?", numero):
        return "Visa"

    # Mastercard: começa com 51-55 e tem 16 dígitos
    if re.fullmatch(r"5[1-5]\d{14}", numero):
        return "Mastercard"

    # Amex: começa com 34 ou 37 e tem 15 dígitos
    if re.fullmatch(r"3[47]\d{13}", numero):
        return "Amex"

    # Elo: começa com os prefixos e tem 16 dígitos
    elo_prefixos = [
        "636368", "438935", "504175", "451416", "636297",
        "5067", "4576", "4011"
    ]
    if any(numero.startswith(prefixo) for prefixo in elo_prefixos) and len(numero) == 16:
        return "Elo"

    return "Bandeira desconhecida"

# Loop principal para pedir o número do cartão ao usuário e mostrar a bandeira
if __name__ == "__main__":
    while True:
        print("Identificador de Bandeira de Cartão de Crédito")
        numero = input("Digite o número do cartão (ou 'sair' para terminar): ")
        if numero.lower() == 'sair':
            break

        bandeira = identificar_bandeira(numero)
        print(f"A bandeira do cartão é: {bandeira}\n")