def Swapper():
    print("Welcome to the Data Swapper!!!! You can switch data from two file")
    File1 = input("What is the file name of first file : ")
    File2 = input("What is the file name of second file : ")

    with open(File1, 'r') as a:
        dataA = a.read()

    with open(File2, 'r') as b:
        dataB = b.read()
        
    with open(File1, 'w') as a:
        a.write(dataB)

    with open(File2, 'w') as b:
        b.write(dataA)

    print("Successful swapped data from files Thanks a lot for using it!!!")

Swapper()