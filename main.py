from pyscript import document

club_members = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Draco Malfoy", "Ginny Weasley", "Luna Lovegood", "Neville Longbottom", "Sirius Black", "Remus Lupin", "James Potter"]

def verify_candidate(e):
    first_name = document.getElementById("first_name").value.strip().title()
    last_name = document.getElementById("last_name").value.strip().title()

    full_name = (first_name + " " + last_name).strip()

    is_member = full_name in club_members

    messages = {
        True: f"Congratulations {full_name}! Your enrollment at Hogwarts School of Witchcraft and Wizardry is confirmed. Welcome to Hogwarts!",
        False: f"Sorry {full_name}, your name could not be found in the Hogwarts Registry."
    }

    result = document.getElementById("result")

    result.innerHTML = (
        '<div class="letter-heading">'
        'A LETTER FROM THE ADMISSIONS OFFICE'
        '</div>'
        + messages[is_member]
        + '<div class="letter-seal">✦</div>'
    )
