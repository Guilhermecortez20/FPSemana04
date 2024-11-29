import json

def read_json(file_path):
    try:
        with open(file_path, 'rt', encoding='utf-8') as file:
            print(json.load(file))
    except:
        print("Ocorreu um erro!")
    finally:
        print("Processo concluído!")


if __name__ == "__main__":
    read_json(input("Insira o caminho para o ficheiro JSON: ").strip())

