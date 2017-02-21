email = "shannon@hearmecode.com"
print email.find("@")
print email.find("b")
print email.replace("shannon", "jenny")
print email
email2 = email.replace("shannon", "jenny")
print "email = {0}".format(email)
print "email2 = {0}".format(email2)
print len (email)
print len (email2)
len_email = len (email)
print len_email
email_position = email.find("@")
print email_position
print "UserName is {0} it's length is {1}".format(email[0:email_position],email_position)


address = "                1725 Indian Field Rd"
print address
print address.strip()


students = 10
capacity = 50
teaching_assistants = 5

if students < capacity:
	print "Keep recruiting"
else:
	print "End ticket signups"


if teaching_assistants == 0:
	print "None? Uh oh!"
elif teaching_assistants < students /5:
	print "Keep recruiting TAs"
else:
	print "We have plenty of TAs"	

