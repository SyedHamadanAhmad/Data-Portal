import json
from sqlalchemy.inspection import inspect


def updateMongoDocument(sno, query, collection):
	update = {"$set": query}
	collection.update_one({"sno": sno}, update)
	return update, list(collection.find({"sno": sno}))


def deleteMongoDocument(sno, collection):

	collection.delete_one({"sno": sno})
	return "Deleted for" + str(sno)


def combineConn(railway, airport, bus):
   
	print(f'railway: {railway},\n airport: {airport},\n bus: {bus}')
	final = []

	if railway[0]:
		print('>>> Railways added!', railway[0], type(railway[0]))
		json_val = json.loads(f'[{railway[0]}]')
		if (len(json_val) > 0):
			for r in json_val:
				r[
				 'icon'] = 'https://konsa-college-website-icons.s3.ap-northeast-1.amazonaws.com/assets/icons/train.png'
				final.append(r)

	if bus[0]:
		print('>>> Buses added!', bus[0], type(bus[0]))
		json_val = json.loads(f'[{bus[0]}]')
		if (len(json_val) > 0):
			for b in json_val:
				b[
				 'icon'] = 'https://konsa-college-website-icons.s3.ap-northeast-1.amazonaws.com/assets/icons/bus.png'
				final.append(b)

	if airport[0]:
		print('>>> Airports added!', airport, type(airport))
		json_val = json.loads(f'[{airport[0]}]')
		if (len(json_val) > 0):
			for a in json_val:
				a[
				 'icon'] = 'https://konsa-college-website-icons.s3.ap-northeast-1.amazonaws.com/assets/icons/plane.png'
				final.append(a)

	return final


def seperateConn(json):

	rList = []
	bList = []
	aList = []
	for t in json:
		if t != None:
			if str(t['icon']).__contains__("train"):
				rList.append([t['trans'], t['dist']])
			if str(t['icon']).__contains__("bus"):
				bList.append([t['trans'], t['dist']])
			if str(t['icon']).__contains__("plane"):
				aList.append([t['trans'], t['dist']])
	return [rList, bList, aList]


def last_row(Table: type, *, session):  # -> Table
	primary_key = inspect(Table).primary_key.name  # must be an arithmetic type
	primary_key_row = getattr(
	 Table, primary_key)  # get first, sorted by negative ID (primary key)
	return session.query(Table).order_by(-primary_key_row).first()
