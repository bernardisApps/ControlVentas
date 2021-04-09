from tkinter import Tk
from frameMain import FrameMain


def main():
    root = Tk()
    root.title("Control de Clientes")
    root.config(bg="lightgrey")
    root.geometry("640x480")
    root.resizable(False,False)

    app = FrameMain(root)
    app.mainloop()


if __name__ == "__main__":
    main()
