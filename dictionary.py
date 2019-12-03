
global dictionary
dictionary = {}

class Dict:
	def __init__(self, word, meaning):
		self.word = word
		self.meaning = meaning

	def add_new(self):
		dictionary[self.word] = self.meaning
		print("Word Successfully Added")

	def delete_word(self):
		try:
			del dictionary[self.word]
			print("Word Successfully Deleted")
		except KeyError:
			print("The Word Does Not Exist in the Dictionary. Please Try Again!")

	def edit_word(self):
		try:
			dictionary[self.word] = self.meaning
			print("Word Was Successfully Edited")
		except KeyError:
			print("The Word You Trying To Edit, Does Not Exist in the Dictionary!")

	def view_word(self):
		try:
			print(dictionary[self.word])
		except KeyError:
			print("The Word is not in the Dictionary, Please Make Sure Spellings are Correct?")

	def view_all(self):
		for i in dictionary:
			print(i ," : ", dictionary[i])

def start():
	get_op = input("Add, Delete, Edit, View, View all : ")
	if get_op in ["add", "Add"]:
		get_word = input("Word to add : ")
		get_meaning = input("Meaning : ")
		new = Dict(get_word, get_meaning)
		new.add_new()

	elif get_op in ["delete", "Delete", "DELETE"]:
		get_word_to_del = input("Word to delete : ")
		delete = Dict(get_word_to_del, None)
		delete.delete_word()

	elif get_op in ["edit", "Edit"]:
		get_word_to_edit = input("Word to edit : ")
		get_new_meaning = input("New meaning : ")
		mean = Dict(get_word_to_edit, get_new_meaning)
		mean.edit_word()

	elif get_op in ["view", "View", "VIEW"]:
		get_word_to_view = input("Word to view : ")
		view = Dict(get_word_to_view, None)
		view.view_word()

	elif get_op in ["view all", "View All", "View all"]:
		nothing = Dict(None, None)
		nothing.view_all()

	else:
		print("Invalid Input. Try Again!")

def end():
	quit()

def main():
	while True:
		s_or_e = input("Start or End : ")
		if s_or_e == "Start" | s_or_e == "start":
			start()
			print("  ")
			continue

		else:
			end()


if __name__ == "__main__":
	main()		
