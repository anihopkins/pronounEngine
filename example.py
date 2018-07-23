# Import the "pronouns module"
import pronouns

# Instantiate objects for male and xe-series pronouns
malePronoun = pronouns.Pronoun()
xePronoun = pronouns.Pronoun()

# Set pronouns for both objects
malePronoun.set("He", "Him", "His", "Himself")
xePronoun.set("Xe", "Hir", "Hirs", "Hirself")

markedString = "~1 is hungry. I gave ~2 a burger. ~3 dog ate the burger \
instead! ~1 was sad because that burger was ~4. ~1 decided to make a burger ~5."

# Insert both sets of pronouns into the marked string
maleString = malePronoun.insert(markedString)
xeString = xePronoun.insert(markedString)

print(maleString + "\n")
print(xeString)

# RESULTS IN:
# He is hungry. I gave him a burger. His dog ate the burger instead! He was sad
# because that burger was his. He decided to make a burger himself.
#
# Xe is hungry. I gave hir a burger. Hir dog ate the burger instead! Xe was sad
# because that burger was hirs. Xe decided to make a burger hirself.
