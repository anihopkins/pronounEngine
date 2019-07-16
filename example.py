# Import the "pronouns module"
import pronouns

# Instantiate objects for male and xe-series pronouns
hePronoun = pronouns.Pronoun()
shePronoun = pronouns.Pronoun()
xePronoun = pronouns.Pronoun()
itPronoun = pronouns.Pronoun()

# Set pronouns for both objects
hePronoun.set("He", "Him", "His", "Himself")
shePronoun.set("She", "Her", "Hers", "Herself")
xePronoun.set("Xe", "Hir", "Hirs", "Hirself")
itPronoun.set("It", "It", "Its", "Itself")

markedString = "~1 is hungry. I gave ~2 a burger. ~3 dog ate the burger \
instead! ~1 was sad because that burger was ~4. ~1 decided to make a burger ~5."

# Insert both sets of pronouns into the marked string
heString = hePronoun.insert(markedString)
sheString = shePronoun.insert(markedString)
xeString = xePronoun.insert(markedString)
itString = itPronoun.insert(markedString)

print(heString + "\n")
print(sheString + "\n")
print(xeString + "\n")
print(itString)

# RESULTS IN:
# He is hungry. I gave him a burger. His dog ate the burger instead! He was sad
# because that burger was his. He decided to make a burger himself.
#
# Xe is hungry. I gave hir a burger. Hir dog ate the burger instead! Xe was sad
# because that burger was hirs. Xe decided to make a burger hirself.
