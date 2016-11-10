from tkinter import *

def keyPressed(event):
    # 키보드 문자하나 출력
    print(event.char)

root = Tk()

lbl = Label(root, text="이름")
lbl.pack()

txt = Entry(root)
txt.pack()

txt.bind('<Key>', keyPressed) # 키프레스 이벤트를 걸 수 있따..........짱

btn = Button(root, text="OK")
btn.pack()

root.mainloop()

