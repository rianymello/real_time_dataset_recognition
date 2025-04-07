
# Sistema de Reconhecimento Facial com OpenCV

Este é um projeto de reconhecimento facial em tempo real utilizando a biblioteca OpenCV e a técnica LBPH (Local Binary Patterns Histograms). O sistema permite capturar rostos pela webcam, associar nomes e IDs, treinar um modelo e realizar o reconhecimento ao vivo.

## Funcionalidades

- Captura de imagens faciais com webcam
- Treinamento de modelo com as imagens coletadas
- Reconhecimento facial em tempo real
- Armazenamento de nomes e IDs no arquivo `names.json`
- Script opcional para limpar dados (dataset e JSON)

## Estrutura do Projeto
- dataset/: Armazena as imagens capturadas dos rostos
- trainer/: Contém o modelo treinado (trainer.yml)
- names.json: Mapeia os IDs para nomes
- 01_face_dataset.py: Captura imagens e salva no dataset
- 02_train_model.py: Treina o modelo LBPH
- 03_face_recognition.py: Reconhecimento em tempo real
- reset_dataset.py: Limpa o dataset e o JSON (opcional)
- requirements.txt: Lista de dependências

## Como usar

### 1. Instalar as dependências do projeto

Antes de executar qualquer parte do sistema, você precisa instalar as bibliotecas necessárias. Para isso, abra o terminal (ou prompt de comando), vá até a pasta onde está o projeto e digite o seguinte comando:

```bash
pip install -r requirements.txt

```
Isso instalará automaticamente todas as bibliotecas que o sistema usa.

### 2. Adicionar uma nova pessoa ao sistema
Execute o script 01_face_dataset.py para iniciar a coleta de imagens faciais.
No terminal, digite:
```bash

python 01_face_dataset.py

```

Você verá dois campos para preencher:

- ID numérico (por exemplo: 1, 2, 3...)

- Nome da pessoa (por exemplo: Maria, João...)

Depois disso, o sistema vai ligar a webcam e começar a capturar imagens do seu rosto. Ele precisa de 30 imagens para o treinamento. 
Durante esse tempo, olhe diretamente para a câmera. Um retângulo azul aparecerá em volta do seu rosto enquanto as imagens são salvas na pasta dataset.

### 3. Treinar o modelo com os rostos coletados
Após capturar as imagens, execute o script 02_train_model.py para treinar o sistema com os rostos adicionados. Use o comando:

```bash

python 02_train_model.py
```

O script vai ler todas as imagens da pasta dataset, treinar um modelo de reconhecimento facial e salvar esse modelo treinado dentro da pasta trainer, com o nome trainer.yml.

### 4. Reconhecer os rostos ao vivo com a câmera
Agora você pode testar o sistema de reconhecimento facial. Execute o script 03_face_recognition.py com o comando:

```bash

python 03_face_recognition.py
```
A webcam será aberta e o sistema tentará reconhecer os rostos usando o modelo treinado.

Se ele reconhecer alguém, vai mostrar o nome da pessoa na tela junto com a porcentagem de confiança.

Se não reconhecer, aparecerá "Desconhecido".

Para sair, pressione a tecla ESC.

### 5. (Opcional) Limpar o sistema
Se quiser apagar os dados e começar de novo, execute o script reset_dataset.py com:

```bash

python reset_dataset.py
```

Isso apaga o conteúdo da pasta dataset/ e limpa o arquivo names.json

## Requisitos
Python 3.10 ou superior

Webcam

Bibliotecas listadas no arquivo requirements.txt
