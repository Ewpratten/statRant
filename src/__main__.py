import devRantSimple as dRS

def getCounts(user):
	return dRS.getUserData(dRS.getUserId(user), {"app":3})["profile"]["content"]["counts"]

def getRants(user, skip):
	return dRS.getUserData(dRS.getUserId(user), {"app":3, "skip":skip})["profile"]["content"]["content"]["rants"]

def getAllRantsToArray(user):
	i = 0
	rantcount = getCounts(user)["rants"]
	rants = []
	while i < rantcount:
		for rant in getRants(user, i):
			rants.append(rant)
		i += 30
	return rants

username = input("Username: ")

if not dRS.userExsists(username):
	print("That user does not exsist")
	exit(1)

print("Fetching rants...")
rants = getAllRantsToArray(username)

print("Parsing score data...")
scores = []
for rant in rants:
	scores.append([rant["score"], rant["id"]])

print("Sorting score data...")
scores = sorted(scores, key=lambda x: x[0], reverse=True)

print("\nTotal number of rants: " + str(len(scores)))
print("Is eligible for stickers: " + (str(True) + " https://devrant.com/rants/" + str(scores[0][1]) if scores[0][0] >= 30 else str(False)))
print("Is eligible for stress ball: " + (str(True) + " https://devrant.com/rants/" + str(scores[0][1]) if scores[0][0] >= 750 else str(False)))
print("Most popular rant: https://devrant.com/rants/" + str(scores[0][1]))
print("Least popular rant: https://devrant.com/rants/" + str(scores[getCounts(username)["rants"] - 1][1]))