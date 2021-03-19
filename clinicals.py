class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.clinical = []

    def addClinicalData(self, clinical):
        self.clinical.append(clinical)


class Clinical:
    def __init__(self, componentName, componentValue):
        self.componentName = componentName
        self.componentValue = componentValue


p = Patient("John",48)
c1 = Clinical('bp','88/120')
p.addClinicalData(c1)

c2 = Clinical('hear beat', '88')
p.addClinicalData(c2)
print(p.name)
for eachClinical in p.clinical:
    print(eachClinical.componentName)
    print(eachClinical.componentValue)