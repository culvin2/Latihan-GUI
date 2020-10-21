from tkinter import Tk, Frame, Menu
class memSubMenu(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.windom = parent
        self.initUI()
        self.memSubMenu()
    def initUI(self):
        self.window.title("Submenu")
        self.window.geometry("250 x 150")
    def memSubMenu(self):
        menubar = Menu (self.window)
        self.window.config(menu = menubar)
        fileMenu = Menu (menubar)
        submenu = Menu (fileMenu)
        submenu.add_command(label = "New Feed")
        submenu.add_command(label = "Book Marks")
        submenu.add_command(label = "Mail ")
        fileMenu.add_cascade(label= "Import",
menu=submenu,underline = 0)
        fileMenu.add_separator()
        fileMenu.add_command(label = "Exit",
underline = 0, menu=fileMenu)
        menubar.add_cascade(label = "File",
underline = 0, menu = fileMenu)
    def onExit(self):
        self.quit()
if __name__ == "__main__":
    root = Tk()
    app = memSubMenu(root)
    root.mainloop()
    