import os
import json

dataset_path = "dataset"
names_file = "names.json"

def clear_dataset():
    if os.path.exists(dataset_path):
        files_removed = 0
        for filename in os.listdir(dataset_path):
            file_path = os.path.join(dataset_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    files_removed += 1
            except Exception as e:
                print(f"[ERRO] Não foi possível excluir {file_path}. Motivo: {e}")

        if files_removed > 0:
            print(f"[INFO] {files_removed} arquivos removidos do dataset.")
        else:
            print("[INFO] Nenhum arquivo encontrado para remover.")

def clear_names_file():
    try:
        with open(names_file, 'w') as f:
            json.dump({}, f)
        print("[INFO] names.json limpo com sucesso.")
    except Exception as e:
        print(f"[ERRO] Não foi possível limpar names.json. Motivo: {e}")

if __name__ == "__main__":
    clear_dataset()
    clear_names_file()
