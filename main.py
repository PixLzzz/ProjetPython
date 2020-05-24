import tkinter as tk
import simple
import dictionary

class Application(tk.Frame):
    strRes = ""
    listMDP = ["67ca881ef876c622c093419d0d8dbe13",
               "14bfcc4be324181b91812b0b2f70ce40",
               "e11f4bff1b9aa4c9b65224295dd22e16",
               "42167255eb290439c4200edfe3639ab5",
               "a9b0cd97f83f9251411af4b5f1f0bd59",
               "6c69a73f35abf6c80c88f1e3801ca150",
               "4eb01b0c1900c192da5c2aba253de3c0",
               "a409f32fef1cc24d4fbe7256accf8eb9",
               "8699fc754c2e40dc7ef0ca9634b92d17",
               "4bda49907d7f2d949d6ba4ff299a280c",
               "54fd8fb2eaf6b40ecd347713770e83d5"]

    listStudent = ["kojak",
                   "vivien",
                   "maxime",
                   "louis",
                   "abdelkarim",
                   "jordan",
                   "jules",
                   "corentin",
                   "vincent",
                   "augustin",
                   "oussama",
                   "mickaël",
                   "remi",
                   "jérémy"]

    def __init__(self, master=None):
        tk.Frame.__init__(self,master , width=1000, height=500)

        self.master = master
        self.pack(fill=tk.BOTH)



        self.create_widgets()

    def create_widgets(self):

        self.prenom = tk.Label(self)
        self.prenom["text"] = "                     Prénom :                        "
        self.prenom.pack(side="top")

        self.listPrenoms = tk.Listbox(self,width=60 )
        self.listPrenoms.pack(side="top")
        for item in Application.listStudent:
            self.listPrenoms.insert("end", item)

        self.pwd = tk.Label(self)
        self.pwd["text"] = "Mot de passe :"
        self.pwd.pack(side="top")

        self.listHashedMDP = tk.Listbox(self , width=60)
        self.listHashedMDP.pack(side="top")
        for item in Application.listMDP:
            self.listHashedMDP.insert("end", item)

        self.simple1 = tk.Button(self)
        self.simple1["text"] = "Simple"
        self.simple1.configure(command = self.startSimple)
        self.simple1.pack(side="top")

        self.simple2 = tk.Button(self)
        self.simple2["text"] = "Dictionary"
        self.simple2.configure(command=self.startDictionary)
        self.simple2.pack(side="top")

        self.inputpwd = tk.Text(self ,width=80,height=10)
        self.inputpwd.pack(side="top")

    # Action apres click sur l'interface
    def startSimple(self):
         a =simple.method1(Application.listStudent, Application.listMDP)
         self.inputpwd.insert('end', a)
         self.inputpwd.insert('end',"\n")

         b = simple.method2(Application.listStudent, Application.listMDP)
         if b :
             self.inputpwd.insert('end', b)
             self.inputpwd.insert('end', "\n")

         c = simple.UpAndDown(Application.listStudent, Application.listMDP)
         if c :
             self.inputpwd.insert('end' , c)
             self.inputpwd.insert('end', "\n")

    def startDictionary(self):
         a = dictionary.Animals(Application.listMDP)
         self.inputpwd.insert('end', a)
         self.inputpwd.insert('end', "\n")

         b = dictionary.concatAnimals(Application.listMDP)
         if b:
            self.inputpwd.insert('end', b)
            self.inputpwd.insert('end', "\n")

         c = dictionary.reverseConcatAnimals(Application.listMDP)
         if c:
            self.inputpwd.insert('end', c)
            self.inputpwd.insert('end', "\n")

         d = dictionary.digAnimals(Application.listMDP)
         if d:
             self.inputpwd.insert('end', d)
             self.inputpwd.insert('end', "\n")

         e = dictionary.AnimalScramble(Application.listMDP)
         if e:
             self.inputpwd.insert('end', e)
             self.inputpwd.insert('end', "\n")

         f = dictionary.AnimalAndReverse(Application.listMDP)
         if f:
             self.inputpwd.insert('end', f)
             self.inputpwd.insert('end', "\n")


    def supprime_accent(self, ligne):
        accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
        sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
        i = 0
        while i < len(accent):
            ligne = ligne.replace(accent[i], sans_accent[i])
            i += 1
        return ligne


root = tk.Tk()
app = Application(master=root)
app.mainloop()
