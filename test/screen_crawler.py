from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

from test.test_crawler import spider, users


def displayText():
    if naverId.get().strip() == "":
        messagebox.showinfo("안내", "naver ID를 입력하세요...")
    else:
        outputData.set(naverId.get().strip())
        entity_users = users()
        entity_users.setId(naverId.get().strip())
        spider("http://blog.naver.com/PostList.nhn?blogId="+naverId.get().strip()+"&widgetTypeCall=true&topReferer=http://www.naver.com/", entity_users)
        print(naverId.get().strip())
        print(users.getItems())


class MyFrame(Frame):
    def __init__(self, master):
        global naverId
        global outputData
        # keyPresse를 이용한 키 이벤트 받기
        def keyPressed(event):
            # 키보드 문자하나 출력
            print(event.char)

        Frame.__init__(self, master)

        self.master = master
        self.master.title("크롤러")
        self.pack(fill=BOTH, expand=True)

        # 성명
        frame1 = Frame(self)
        frame1.pack(fill=X)

        lblName = Label(frame1, text="네이버 ID", width=10)
        lblName.pack(side=LEFT, padx=10, pady=10)

        naverId = Entry(frame1)
        naverId.pack(fill=X, padx=10, expand=True)

        # entryName.bind('<Key>', keyPressed)
        # entryName.place(x=0, y=0)

        # 회사
        # frame2 = Frame(self)
        # frame2.pack(fill=X)
        #
        # lblComp = Label(frame2, text="회사명", width=10)
        # lblComp.pack(side=LEFT, padx=10, pady=10)
        #
        # entryComp = Entry(frame2)
        # entryComp.pack(fill=X, padx=10, expand=True)

        # URL
        # frame3 = Frame(self)
        # frame3.pack(fill=BOTH, expand=True)
        #
        # lblComment = Label(frame3, text="관련URL", width=10)
        # lblComment.pack(side=LEFT, anchor=N, padx=10, pady=10)
        #
        # outputData = Text(frame3)
        # outputData.pack(fill=X, pady=10, padx=10)
        outputData = StringVar()

        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)
        dataLabel = Label(frame3, textvariable=outputData) # label 과 textvariable 이용하여 값 표시 하기
        dataLabel.pack(fill=X, pady=10, padx=10)

        # 저장
        frame4 = Frame(self)
        frame4.pack(fill=X)
        btnSave = Button(frame1, text="저장", command=displayText)
        btnSave.pack(side=LEFT, padx=10, pady=10)



def main():
    root = Tk()
    root.geometry("600x550+100+100")
    app = MyFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()