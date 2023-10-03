import tkinter

class Application(tkinter.Frame):
    def __init__(self, root=None):
        super() .__init__(root, width=380, height=280, borderwidth=1, relief="groove")

        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        button = tkinter.Button(self, text="実行", command=self.submit)
        button.pack()

        menu = tkinter.Menu(self.root)
        menu1 = tkinter.Menu(menu, tearoff=False)
        menu1.add_command(labe="画面設定", command=self.screen_setting)
        menu1.add_command(label="音量設定", command=self.volume_setting)
        menu.add_cascade(label="設定", menu=menu1)
        self.root.config(menu=menu)

    def screen_setting(self):
        print("画面設定が押されました")

    def volume_setting(self):
        print("音量設定が押されました")
  

    def submit(self):
        print("ボタンが押されました")
        print(self.sp.get())

root = tkinter.Tk()
root.title("アプリ")
root.geometry("400x300")
app = Application(root=root)
app.mainloop()