import streamlit_authenticator as stauth

import database as db

usernames = ["AL", "SG", "JF", "siix", "Donovan", "jb", "Dje", "DVortex", "pap", "starseedmatrix", "Blake_R", "JwJ"]
names = ["Amir Lehmam", "Sachith Galbokka", "Jim Fredrickson", "Justin Cooper", "Douwe Jan", "Jonah the Great", "Dje Valens", "DVortex", "Pap", "Alexandra", "Blake R", "Joe just Joe"]
passwords = ["azerty94", "azerty75", "azerty99", "siix6sixty6", "numbersdontlie69", "Suns#ine882022", "Bassam06", "DVortex", "azerty94", "Starseedmatrix11", "Gann1908", "Vesica-Piscis28"]
hashed_passwords = stauth.Hasher(passwords).generate()

for (username, name, hash_password) in zip(usernames, names, hashed_passwords):
    db.insert_user(username, name, hash_password)
