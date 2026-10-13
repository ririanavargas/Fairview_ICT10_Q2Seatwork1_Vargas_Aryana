from pyscript import document, display

def check_candidate_status(e):

 club_members = (
 'Tyler Sales',
 'Jilliane Tech',
 'Danielle Sandoval',
 'Aaliyah Pangilinan',
 'Gavin Taguiga',
 
) 

 document.getElementById("div2").innerHTML = "" 
 first_name = document.getElementById("fname").value.strip()
 last_name = document.getElementById("lname").value.strip()
 candidate_name = f"{first_name} {last_name}"
 is_member = candidate_name in club_members

 messages = {
     True: f"Congratulations {candidate_name}! You are now part of the ICT Club!",
     False: f"Sorry {candidate_name}, you are not a member of the ICT Club."
 }

 result = messages[is_member]
 display(result, target = "div2")