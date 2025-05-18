import gdown

# Replace with your actual Google Drive file IDs
files = {
    "train.conll": "18AdsE5YNd7TdQxewXSJne1-1rsV7ha9q",
    "sec0.conll: 1uk_XO8qZvl6Iq--eNp2OagdEoRFpe1dk"
    "dev.conll": "15C0GG_gXANEI2o0hRBkU5qoi1arHo1Se",
    "test.conll": "1NgN95eNM2PHRBgX3cWklekvhuHLnE9-q"
}

for filename, file_id in files.items():
    url = f"https://drive.google.com/uc?id={file_id}"
    print(f"Downloading {filename}...")
    gdown.download(url, filename, quiet=False)

print("All files downloaded.")
