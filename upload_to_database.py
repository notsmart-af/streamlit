import streamlit_authenticator as stauth
import database as db

usernames = ["Am", "SG", "JF", "Guest"]
names = ["Amir Lehmam", "Sachith Galbokka", "Jim Fredrickson", "Guest"]
passwords = ["amirdu94", "azerty75", "azerty99", "Guest123"]
hashed_passwords = stauth.Hasher(passwords).generate()

for (username, name, hash_password) in zip(usernames, names, hashed_passwords):
    db.insert_user(username, name, hash_password)