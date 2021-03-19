class Course:

    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings

    def average(self):
        number_of_ratings = len(self.ratings)
        average = sum(self.ratings)/number_of_ratings
        print("Average Ratings For", self.name, "Is", average)


c1 = Course("Python", [1, 2, 3, 4, 5])
print(c1.name)
print(c1.ratings)
c1.average()
