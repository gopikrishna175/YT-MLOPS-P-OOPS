class Employee:
    def __init__(self):
        print("Started executing attributes/data")
        self.id=1
        self.salary=100000
        self.designation="SDE"
        print("Self completed")

    def travel(self,destination):
        print(f"My fav place is {destination}")


sam=Employee()

print(sam.salary)

sam.travel('Kerala')
print(type(sam))