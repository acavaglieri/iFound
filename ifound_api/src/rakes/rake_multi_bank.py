import sys
sys.path.insert(0, '/home/gustavo/Projects/Python/CSS/Paylog/paylog/src/services')
import optparse
import colorama
import ast


def main():
    def catch_args():
        parser = optparse.OptionParser()
        print(colorama.Fore.YELLOW)
        parser.add_option("--bank", dest="bank", action="store", type="string",
                        help="Especifique o banco do qual será usada a API")
        parser.add_option("-p", "--pay", dest="pay", action="store", type="string",
                        help="Inicia pagamento para brcode especificado, deve ser acompanhado dos argumentos --to e -m")
        parser.add_option("--to", "--receiver", dest="receiver", action="store", type="string",
                        help="CPF/CNPJ do favorecido do pagamento")
        parser.add_option("-m", "--message", dest="message", action="store", type="string",
                        help="Mensagem que acompanhará o pagamento. Mínimo de 10 caracteres.")
        parser.add_option("-r", "--receive", dest="receive", action="store", type="int",
                        help="Gera cobrança com valor especificado")
        parser.add_option("-b", "--balance", dest="balance",
                        help="Passe 'show' como argumento para ver o saldo da conta.")
        parser.add_option("-t", "--transactions", dest="transactions",
                        help="Exibe extrato da conta, digite 'None' para receber todo o extrato sem filtrar, ou mude o filtro no arquivo filters.py")
        (commands, argumentos) = parser.parse_args()
        return commands

    options = catch_args()

    if options.bank:
        if options.bank == "starkbank":
            import starkbank
            if starkbank.user:
                if options.pay:
                    print(colorama.Fore.GREEN + "[+] Realizando pagamento...")
                    if not options.receiver:
                        print(colorama.Fore.RED + "[-] ERRO: Necessário CPF/CNPJ do favorecido!")
                    elif not options.message:
                        print(colorama.Fore.RED + "[-] ERRO: Necessário descrição/mensagem do pagamento")
                    elif options.message and len(options.message) < 10:
                        print(colorama.Fore.RED + "[-] ERRO: Mensagem muito curta! Mínimo 10 caracteres")
                    else:
                        print(colorama.Fore.GREEN + "[+] Pagamento realizado com sucesso!\n")
                
                if options.receive:
                    print(colorama.Fore.GREEN + "[+] Gerando cobrança...")
                    print("[+] Cobrança gerada com sucesso!\n")
                
    else:
        print(colorama.Fore.RED + colorama.Style.BRIGHT + "Escolha um banco!" + colorama.Style.RESET_ALL)

if __name__ == '__main__':
    main()