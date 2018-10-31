


def knock():

    inp = input("Do you want to hear a joke? ")


    if (inp.upper() == "YES"):

        inp = input("It's a knock knock joke but you have to start: ")

        if (inp.upper() == "KNOCK KNOCK"):

            inp = input("Who's there? ")

            inp = input("Who " + inp + "? ")

        else:
            knock()

    else:
        knock()

knock()
