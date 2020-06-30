class movie():
	def __init__(self, name, rating, director, budget, description):
		self.name = name
		self.rating = rating
		self.director = director
		self.budget = budget
		self.description = description

	def good_movie(self):
		if self.rating >= 4:
			return("It's a good movie.")


toy_story = movie("ToyStory2" , 4 , "John Lasseter , Lee Unkrich , Ash Brannon" , "90 millon USD" , """When Woody is toy-napped by a greedy toy collector and is nowhere to be found, Buzz and his friends set out to rescue him.But Woody too is tempted by the idea of becoming immortal in a museum.
""")				

print("Title : " + str(toy_story.name))
print("Rating : " + str(toy_story.rating))
print("Director : " + str(toy_story.director))
print("Budget : " + str(toy_story.budget) + "\n")
print("Description :  " + str(toy_story.description))
print(toy_story.good_movie())
