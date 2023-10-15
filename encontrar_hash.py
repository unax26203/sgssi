import zipfile
import hashlib


target_md5 = "e5ed313192776744b9b93b1320b5e268"


zip_file_path = "imagen.zip"


with zipfile.ZipFile(zip_file_path, 'r') as zip_file:

    for file_info in zip_file.infolist():

        with zip_file.open(file_info) as image_file:

            md5_hash = hashlib.md5(image_file.read()).hexdigest()


            if md5_hash == target_md5:
                print(f"El archivo {file_info.filename} contiene el mensaje oculto.")
                break
    else:
        print("No se encontró el archivo con el MD5 objetivo en el ZIP.")
