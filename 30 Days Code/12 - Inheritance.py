class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, id, scores = []):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = id
        self.scores = scores

    def calculate(self):
        result = ''
        
        avg_score = round(sum(self.scores) / len(self.scores))
        if avg_score < 40:
            result = 'T'
        elif 40 <= avg_score < 55:
            result = 'D'
        elif 55 <= avg_score < 70:
            result = 'P'
        elif 70 <= avg_score < 80:
            result = 'A'
        elif 80 <= avg_score < 90:
            result = 'E'
        elif 90 <= avg_score <= 100:
            result = 'O'

        return result


if __name__ == '__main__':
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(input()) # not needed for Python
    scores = list( map(int, input().split()) )
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())