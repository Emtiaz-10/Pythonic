name = input("enter a  name: ").strip().capitalize()

match name:
    case "Harry" | "Ron" |"Hermione" :
        print("Gryffindlor")
    case "Draco":
        print("Slytherin")
    case _ :
        print("Who?")
