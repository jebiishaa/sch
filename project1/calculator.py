
 from tkinter imort*
 class Apllication(Frame):
     def _init_(self,master)
         super(Apllcation,self)._init_(master)
         self.task=""
         self.UserIn=StringVar()
         self.grid()
         self.Create_widgets()
      def create_widgets(self)
          self.user_input=Entry(self,bg="#5BC8AC",bd=29,insertWidth=4'width=24,font=("Vernada",20,"bold"),textVariable=self.UserIn,justify=RIGHT)
          self.user_input.grid(columnspan=4)
          self.user_input.insert(0,"0")
          self.button1=Button(self,bg="#98DBC6",bd=12,text="7",padx=33,pady=25,font=("Helvetica",20,"bold"),command=lambda:self.buttonClick())
          self.button1.grid(row=2,column=0;sticky=w)                       

    
     
