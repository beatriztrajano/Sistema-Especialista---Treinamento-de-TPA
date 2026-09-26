import json

def carregar_base_conhecimento():
    try:
        with open("base_conhecimento.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("\n[ERRO] O ficheiro 'base_conhecimento.json' não foi encontrado!")
        print("Certifique-se de que o ficheiro JSON está na mesma pasta do código Python.")
        return None

def motor_diagnostico(texto_usuario, lista_regras):
    texto_usuario = texto_usuario.lower()
    resultados = []

    for regra in lista_regras:
        if "codigo" in regra and regra["codigo"] == texto_usuario.strip():
            return regra

        pontuacao = 0
        for sintoma in regra["sintomas"]:
            if sintoma in texto_usuario:
                pontuacao += 1

        if pontuacao > 0:
            resultados.append((regra, pontuacao))

    if not resultados:
        return None

    resultados.sort(key=lambda x: x[1], reverse=True)
    return resultados[0][0]

def codigos(base_dados):
    print("Digite o código ou descreva o problema:")
    entrada = input("> ")

    regras = base_dados.get("erros_codigo", [])
    resultado = motor_diagnostico(entrada, regras)

    exibir_resultado(resultado)

def comprovante(base_dados):
    print("Descreva o problema:")
    entrada = input("> ")

    regras = base_dados.get("problemas_fisicos", [])
    resultado = motor_diagnostico(entrada, regras)

    exibir_resultado(resultado)

def exibir_resultado(resultado):
    """Formata e exibe a resposta do Sistema Especialista."""
    if resultado:
        print("\n==================================================")
        print(f"Diagnóstico: {resultado['titulo']}")
        print(f"Explicação:  {resultado['explicacao']}")
        print(f"Ação Sugerida: {resultado['acao']}")
        print("==================================================")
    else:
        print("\nNão foi possível identificar o problema com base na descrição informada.")

def navegar():
    while True:
        print("\n---------------------------------")
        print("1- Pagamento")
        print("2- Histórico")
        print("3- Voltar")
        print("---------------------------------")
        try:
            opcao = int(input("Digite uma opção: "))
            if opcao == 1:
                print("\nPagamento:")
                print("Na realização de uma venda, o usuário irá escolher o tipo de pagamento de acordo com preferência do consumidor.")
                break
            elif opcao == 2:
                print("\nHistórico:")
                print("Toda ação de estorno, impressão e análise serão feitas aqui. Aparece uma lista com o tipo de pagamento usado, horário da compra e valor pago de vendas anteriores. É possível selecionar cada movimentação para maiores detalhes ao apertar a opção 'Detalhes' no canto inferior da tela e podendo acessar 'Imprimir' para que o relatório específico ou geral seja fisicamente impresso. Outra opção dentro de 'Detalhes' seria a de estorno do pagamento.")
                break
            elif opcao == 3:
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Por favor, digite um número válido.")

def basicas():
    while True:
        print("\n---------------------------------")
        print("1- Como navegar pelo Sistema")
        print("2- Tipos de Pagamentos permitidos")
        print("---------------------------------")
        try:
            opcao = int(input("Digite uma opção: "))
            if opcao == 1:
                print("\n==================================================")
                print("Ao ligar a máquina, a tela disponibilizará um menu de opção. Essas opções são selecionadas manualmente através da interface interativa do dispositivo e em todas as telas o usuário terá a opção de voltar para o menu inicial.")
                print("\nPagamento:Na realização de uma venda, o usuário irá escolher o tipo de pagamento de acordo com preferência do consumidor")
                print("\nHistórico: Toda ação de estorno, impressão e análise serão feitas aqui. Aparece uma lista com o tipo de pagamento usado, horário da compra e valor pago de vendas anteriores. É possível selecionar cada movimentação para maiores detalhes ao apertar a opção “Detalhes” no canto inferior da tela e podendo acessar “Imprimir” para que o relatório específico ou geral seja fisicamente impresso. Outra opção dentro de “Detalhes” seria a de estorno do pagamento.")
                print("\nFechar: O equipamento desligará.")
                print("==================================================")
                break
            elif opcao == 2:
               print("\n==================================================")
               print("Antes de iniciar o pagamento, pergunte ao cliente qual forma de pagamento ele prefere. Respeitar essa preferência torna o atendimento mais rápido, prático e adequado às necessidades de cada cliente.")
               print("\nAo selecionar o tipo de pagamento, aparece na tela para que o usuário digite o valor e entregue temporariamente o dispositivo ao cliente para que o mesmo possa realizar a transferência. A máquina pode gerar QR code, fazer scan magnético na aproximação e permitir a iserção de senha no PIN pad.")
               print("==================================================")
               break
            else:
                print("Opção inválida")
        except ValueError:
            print("Por favor, digite um número válido.")

def erro(base_dados):
    while True:
        print("\n---------------------------------")
        print("1- Códigos de Erro")
        print("2- Problemas de Comprovante")
        print("3- Voltar")
        print("---------------------------------")
        try:
            opcao = int(input("Digite uma opção: "))
            if opcao == 1:
                codigos(base_dados)
                break
            elif opcao == 2:
                comprovante(base_dados)
                break
            elif opcao == 3:
                break
            else:
                print("Opção inválida")
        except ValueError:
            print("Por favor, digite um número válido.")

def main():
    base_dados = carregar_base_conhecimento()
    if not base_dados:
        return

    while True:
        print("\n---------------------------------")
        print("1- Operações Básicas")
        print("2- Diagnóstico de Erro")
        print("3- Sair")
        print("---------------------------------")
        try:
            opcao = int(input("Digite uma opção: "))
            if opcao == 1:
                basicas()
            elif opcao == 2:
                erro(base_dados)
            elif opcao == 3:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida")
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
