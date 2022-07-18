while True:    
    link=input("link: ")
    odgovor=input("is the date the same/if not asked before don't answer yes? ").lower()
    if odgovor=="yes":
        date=date
    else:
        date =input("date: ")
    header = input("website header: ")
    name =input("website name: ")
    
    print(header, name , link , "cited/visited:",date)


