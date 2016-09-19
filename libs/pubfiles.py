# by Guillaume Sousa Amaral
from pymongo import MongoClient

MONGO_MGI_USER = "mgi_user"
MONGO_MGI_PASSWORD = "mgi_password"
MGI_DB = "mgi"
MONGODB_URI = "mongodb://" + MONGO_MGI_USER + ":" + MONGO_MGI_PASSWORD + "@localhost/" + MGI_DB

def _connect():
	"""
	Connect to the database
	:return: database connection
	"""
	try:
		# Connect to mongodb
		print 'Attempt connection to database...'
		client = MongoClient(MONGODB_URI)
		print 'Connected to database with success.'
		try:
			# connect to the db 'mgi'
			print 'Attempt connection to collection...'
			db = client[MGI_DB]
			print 'Connected to collection with success.'
			return db
		except Exception, e:
			print 'Unable to connect to the collection.'
	except Exception, e:
		print 'Unable to connect to MongoDB.'

db = _connect()
xml_data_col = db['xmldata']
xml_data_col.update({}, {"$set": {"ispublished": True}}, upsert=False, multi=True)
