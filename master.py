def gether data():
    n1 = int(input("O primeiro valor: "))
    n2 = int(input("Segundo valor: "))

    return n1,n2

def print_message(n1,n2):
    print(f'Os valores {n1} e {n2} somados dão {n1+n2}')

    return None

def main():
    n1,n2 =gether_data()

    print_menssage(n1,n2)

    return None

if __name__== "__main__":
    main()
