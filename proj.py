import json


class Persons:
    Data = dict()

    def Jason_Upload(self):

        with open("Persons_List.json", "r") as file:
            self.Data = json.load(file)
            print(str(self.Data) + ' Read')
            Person.Verify_Function(input("Enter the name of the person "))

    def Verify_Function(self, name):
        self.name = name
        print(self.name)
        # Persons.Jason_Upload(self)
        if self.name in self.Data:
            print("Yeap")
            Persons.Check_List(self)
        else:
            self.Data[self.name] = 0
            print(self.Data)
            Persons.Check_List(self)

    def Check_List(self):
        score = input("Enter check score: ")
        self.score = int(score)
        Persons.Quastion_Function(self)

    def Quastion_Function(self):

        Quastion = input("Collect scores? ")

        if Quastion == "Yes":
            Persons.Score_Collection(self)
        elif Quastion == "No":
            Persons.Score_Spending(self)


    def Score_Collection(self):
        self.Data[self.name] += self.score * 0.1
        print(self.Data[self.name])
        Persons.Jason_Download(self)


    def Score_Spending(self):

        self.Data[self.name] = self.Data[self.name] - self.score
        Persons.Jason_Download(self)

    def Jason_Download(self):

        with open("Persons_List.json", "w") as write_file:
            self.Data[self.name] = self.Data[self.name]
            print(str(self.Data) + " Write")
            json.dump(self.Data, write_file)


mind = "Mad"
while mind == "Mad":
    mind = input("Mad? ")
    Person = Persons()  # Person_1 = Persons(input("Enter the name of the person_1 "), 0)
    Person.Jason_Upload()