import argparse

def main():
    parser = argparse.ArgumentParser(description="Filtra líneas de un archivo por palabra clave.")
    parser.add_argument('--input', required=True, help="Ruta al archivo de entrada.")
    parser.add_argument('--filter', required=True, help="Texto para filtrar líneas.")
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        for line in f:
            if args.filter in line:
                print(line.strip())

if __name__ == '__main__':
    main()
