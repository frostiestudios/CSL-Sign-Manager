from appJar import gui

def newmod(btn):
    print(f"Adding {newmod}")
    with open ('modlist.md','a') as f:
        f.write(f"Mod")
        f.write(f"\n")



app=gui("Mod Manager",UseTk=True)
app.addLabel("l1","Add Mod To Database")
app.addLabelEntry("Steam URL")
app.addButton("Add",newmod)

app.go()