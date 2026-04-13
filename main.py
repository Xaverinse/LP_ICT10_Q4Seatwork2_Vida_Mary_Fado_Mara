from pyscript import document

takenuser = {
    "Ancheta, Arthur Eugene Maximus Adarna" : ("Sapphire", "Jon Snow"),
    "Asuncion, Miguelito Alonso Brigoli" : ("Sapphire", "Spongebob Squarepants"),
    "Battung, John Lorenzo Quisumbing" : ("Sapphire", "Luffy"),
    "Buenvenida, Victor Emmanuel Bernardino" : ("Sapphire", "OBMC Butterfly"),
    "Casul, McKayla Analisse Gabor" : ("Sapphire", "Snoopy"),
    "Catapang, Athena La Verne Sarabia" : ("Sapphire", "Shane Hollander"),
    "Chua, Cade Rylie Rivera" : ("Sapphire", "Angel Devil"),
    "Eusebio, Zyan Riley Tancinco" : ("Sapphire", "Astolfo"),
    "Evangelio, Princess Radhika Zayn Divino" : ("Sapphire", "Francesca Bridgerton"),
    "Fado, Marianna Reinne Fabie" : ("Sapphire", "Shinji Ikari"),
    "Fermocil, Kleiser Ferida" : ("Sapphire", "Spiderman"),
    "Fernando, Curt Joshua Nicolas" : ("Sapphire", "Spiderman"),
    "Francia, Ethan Raphael Juanga" : ("Sapphire", "Spiderman"),
    "Jimenez, Sophia San Buenaventura" : ("Sapphire", "Bocchi the Rock"),
    "Mabilog, Javier Antonio Villadolid" : ("Sapphire", "Zets"),
    "Mactal, Al Chrian Abueme" : ("Sapphire", "Mr. Bean"),
    "Magday, Constance Soleil Gustilo" : ("Sapphire", "Superman"),
    "Moya, Yanna Clarisse Obial" : ("Sapphire", "Cooper"),
    "Mutia, Francheska Zoe Abesamis" : ("Sapphire", "Eloise Bridgerton"),
    "Nazareno, Luis Gabriel IV Villarico" : ("Sapphire", "Goku"),
    "Romero, Jose Inigo Abalajon" : ("Sapphire", "Tom Robinson"),
    "Santos, Kyler" : ("Sapphire", "Muscular"),
    "Sarao, Jaedin Hailey Balberan" : ("Sapphire", "Zhang Linghe"),
    "Sy, Briana Gabrielle Calaranan" : ("Sapphire", "Shin Asakura"),
    "Sy, Charlotte Anne Estrada" : ("Sapphire", "Stitch"),
    "Udono, Jared Daniel Maulas" : ("Sapphire", "Ayumu Kasuga"),
    "Vida, Mary Kristine Claire Parra" : ("Sapphire", "Natural Harmonia Gropius")
}


def ShowClassmates(event):
    classmates = ""
    for username, (section, fav_character) in takenuser.items():
        classmates += f"Name: {username}\nSection: {section}\nFavorite Character: {fav_character}\n\n"
    document.getElementById("classmate-list").innerText = classmates

def AddClassmate(event):

    username = document.getElementById("username").value.strip()
    section = document.getElementById("section").value.strip()
    fav_character = document.getElementById("fav").value.strip()

    if not username or not section or not fav_character:
        document.getElementById("signed").innerText = "Please fill in all fields."
    elif username in takenuser:
        document.getElementById("signed").innerText = "You're already here lil' bro"
    else:
        takenuser[username] = (section, fav_character)
        document.getElementById("signed").innerText = f"{username} added as a classmate!"

        document.getElementById("username").value = ""
        document.getElementById("section").value = ""
        document.getElementById("fav").value = ""