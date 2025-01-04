import os
import shutil

def organize_downloads(download_folder):
    #Define a categoria de cada extensão
    categories = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "PDFs": [".pdf"],
        "Word e Textos": [".doc", ".docx", ".txt"],
        "Excel": [".xls", ".xlsx"],
        "PowerPoint": [".ppt", ".pptx"],
        "Áudios": [".mp3", ".wav", ".aac", ".flac"],
        "Vídeos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
        "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Programas": [".exe", ".msi", ".bat", ".sh"],
        "Outros": []  # Para extensões não categorizadas
    }

    #Verifica se a pasta de downloads existe
    if not os.path.exists(download_folder):
        print(f"A pasta {download_folder} não foi encontrada.")
        return

    #Lista todos os arquivos na pasta de downloads
    files = [f for f in os.listdir(download_folder) if os.path.isfile(os.path.join(download_folder, 
f))]

    #Cria pastas para cada categoria e move os arquivos
    for file in files:
        file_path = os.path.join(download_folder, file)
        file_extension = os.path.splitext(file)[1].lower()

        #Determina a categoria do arquivo
        destination_folder = None
        for category, extensions in categories.items():
            if file_extension in extensions:
                destination_folder = os.path.join(download_folder, category)
                break
        else:
            #Se não houver correspondência de extensão, mover para "Outros"
            destination_folder = os.path.join(download_folder, "Outros")

        #Cria a pasta de destino se não existir
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        #Move o arquivo para a pasta correspondente
        shutil.move(file_path, os.path.join(destination_folder, file))
        print(f"Movido: {file} -> {destination_folder}")

    print("Organização concluída!")

#Caminho para a pasta de Downloads
downloads_folder = r"C:\Users\Downloads"  #Altere para o caminho correto
organize_downloads(downloads_folder)