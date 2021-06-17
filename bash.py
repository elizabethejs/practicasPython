import os

def main():
    ejecutarGit()
    addAllFiles()
    addRepository()
    getStatus()

def ejecutarGit():
    print("Ejecutando git")
    os.system("echo git init practicasPython")

def addAllFiles():
    print("Añadiendo todos los ficheros")
    os.system("echo git add main.py")
    os.system("echo git commit -m 'Primer commit'")

def addRepository():
    print("Añadiendo al repositorio")
    os.system("echo git remote add origin https://github.com/elizabethejs/practicasPython.git")
    os.system("echo git push -u origin master")

def getStatus():
    print("Comprobando estado")
    os.system("echo git log")


if __name__=='__main__':
    main()