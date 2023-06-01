import os

def compile():
  os.system('pyinstaller --onefile github.py')

if __name__ == "__main__":
  compile()
