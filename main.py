
from pyscript import document

club_members = [
    "Tyler Sales",
    "Jilliane Tech",
    "Danielle Sandoval",
    "Aaliyah Pangilinan",
    "Gavin Taguiga"
]

def check_member(event):
    first_name = document.getElementById("input1").value.strip()
    last_name = document.getElementById("input2").value.strip()

    full_name = first_name + " " + last_name

    full_name = full_name.title()
    is_member = full_name in club_members

    messages = {
        True: f"Congratulations {full_name}! You are now part of the ICT club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }

    document.getElementById("div2").innerText = messages[is_member]
