# Author: Ani Hopkins
#
# Purpose: This file implements a "Pronoun" class that inserts the correct
# pronouns into strings marked for pronoun insertion.
#
# Usage: To mark a string for pronoun insertion, use:
# 	~1 to indicate the location of a subject (He/She/They/Xe)
# 	~2 to indicate the location of an object (Him/Her/Them/Hir)
# 	~3 to indicate the location of a possessive adjective (His/Her/Their/
# 	Hir)
# 	~4 to indicate the location of a possessive pronoun (His/Hers/Theirs
# 	/Hirs)
# 	~5 to indicate the location of a reflexive pronoun (Himself/Herself/
# 	Themselves/Hirself).
#
# Call Pronoun() to instantiate a new Pronoun object.
#
# Call pronoun.set(subject, object, possessive, reflexive) (ie. she/her/hers/
# herself or they/them/theirs/themselves, etc.) to set the correct pronouns for
# pronoun.
#
# Call pronoun.insert(string) method with an appropriately marked string to
# insert the correct pronouns into the string.

class Pronoun:
	# Initiates a blank Pronoun object
	def __init__(self):
		self.pronouns = {"subject":"", "object":"", "possessiveAdjective":"",
						"possessivePronoun":"", "reflexive":""}

		self.markers = {"~1":"subject", "~2":"object",
						"~3":"possessiveAdjective", "~4":"possessivePronoun",
						"~5":"reflexive"}

	# Set the pronouns for this Pronoun object. Defaults to they/them/theirs
	def set(self, subject = None, object = None, possessive = None,
			reflexive = None):

		if (subject == None):
			self.pronouns["subject"] = "they"
		else:
			self.pronouns["subject"] = subject.lower()

		if (object == None):
			self.pronouns["object"] = "them"
		else:
			self.pronouns["object"] = object.lower()

		# "His" is a special case of the possessive where the adjective
		# and the pronoun are the same. For all other 3rd person
		# pronouns, the adjective is the pronoun minus the trailing 's'
		if (possessive == None):
			self.pronouns["possessiveAdjective"] = "their"
			self.pronouns["possessivePronoun"] = "theirs"
		elif (possessive.lower() == "his" or possessive.lower() == "its"):
			self.pronouns["possessiveAdjective"] = possessive
			self.pronouns["possessivePronoun"] = possessive
		else:
			self.pronouns["possessiveAdjective"] = possessive[:-1].lower()
			self.pronouns["possessivePronoun"] = possessive.lower()

		if (reflexive == None):
			self.pronouns["reflexive"] = "themselves"
		else:
			self.pronouns["reflexive"] = reflexive.lower()

	# Replaces pronoun markers by the correct pronouns
	def insert(self, string = None):
		if string == None:
			return ""
		for marker in self.markers.keys():
			while (string.find(marker) != -1):
				string = self._pronounInsert(string, marker)
		return string

	# Produces a printable string for str()
	def __str__(self):
		pronounString = self.pronouns["subject"].capitalize() + "/" + \
						self.pronouns["possessiveAdjective"].capitalize()
		return pronounString

	# Produces a printable string for repr()
	def __repr__(self):
		pronounString = self.pronouns["subject"].capitalize() + "/" + \
						self.pronouns["possessiveAdjective"].capitalize()
		return pronounString

#--------------------------[PRIVATE FUNCTIONS]---------------------------

	# Replace a single pronoun marker by the correct pronoun
	def _pronounInsert(self, string, marker):
		pronoun = self.pronouns[self.markers[marker]]

		if self._doCapitalize(string, marker):
			pronoun = pronoun.capitalize()
		else:
			pronoun = pronoun.lower()

		string = string.replace(marker, pronoun, 1)
		return string

	# Determine whether to capitalize a pronoun or not
	def _doCapitalize(self, string, marker):
		strippedString = string.replace(" ","")
		punctuation = [".", "!", "?"]

		for punct in punctuation:

			if strippedString.rfind(punct, 0, strippedString.find(marker)) == \
				strippedString.find(marker) - 1:
				return True
