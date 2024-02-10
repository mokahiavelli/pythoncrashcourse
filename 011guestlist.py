guests = ['tony iommi', 'lemmy kilmister', 'max calavera']
message = "Dear " + guests[0].title() + ", you are cordially invited to my dinner party!"
print(message)
message = "Dear " + guests[1].title() + ", you are cordially invited to my dinner party!"
print(message)
message = "Dear " + guests[2].title() + ", you are cordially invited to my dinner party!"
print(message)
message = "Unfortunately, " + guests[1].title() + ", is busy kicking ass in heaven and can't make it. RIP."
print(message)
guests[1] = 'Harley Flanagan'
message = "Dear " + guests[0].title() + ", you are cordially invited to my dinner party!"
print(message)
message = "Dear " + guests[1].title() + ", you are cordially invited to my dinner party!"
print(message)
message = "Dear " + guests[2].title() + ", you are cordially invited to my dinner party!"
print(message)
print("Looks like we've found space for three more guests, let's send invites out for everyone again!")
guests.insert(0,'Tatsu Mikami')
guests.insert(2,'Flo Mourier')
guests.append('John Garcia')
message = "Dear " + guests[0].title() + ", you are cordially invited to my dinner party!"
print(message)
message = "Dear " + guests[1].title() + ", you are cordially invited to my dinner party!"
print(message)
message = "Dear " + guests[2].title() + ", you are cordially invited to my dinner party!"
print(message)
message = "Dear " + guests[3].title() + ", you are cordially invited to my dinner party!"
print(message)
message = "Dear " + guests[4].title() + ", you are cordially invited to my dinner party!"
print(message)
message = "Dear " + guests[5].title() + ", you are cordially invited to my dinner party!"
print(message)
group_apology = f"Unfortunately now I can only invite two people for dinner! Instead of the {len(guests)} I have invited!"
print(group_apology)
vanish_guests = guests.pop(0)
guest_apology = "Dear " + guests[0].title() + ", you're unfortunately uninvited."
print(guest_apology)
vanish_guests = guests.pop(0)
guest_apology = "Dear " + guests[0].title() + ", you're unfortunately uninvited."
vanish_guests = guests.pop(0)
print(guest_apology)
guest_apology = "Dear " + guests[0].title() + ", you're unfortunately uninvited."
vanish_guests = guests.pop(0)
print(guest_apology)
twoleft = "Dear " + guests[0].title() + " and " + guests[1].title() + " you're still invited!"
print(twoleft)
del guests[0]
del guests[0]
print(guests)