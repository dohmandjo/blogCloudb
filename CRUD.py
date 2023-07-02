# Import pymongo
from pymongo import MongoClient

# Store the url of the db in a variable
MONGODB_URI = "mongodb+srv://dohmandjo:Mylife05009@blogapp.cgcx5kj.mongodb.net/?retryWrites=true&w=majority"

# Store the database in a variable
client = MongoClient(MONGODB_URI)

# get all the databases from the client
db = client.get_database('blog_app')

# get the blog collection
records = db.blog

# Count the number of documents in the database
records.count_documents({})

# Add a new document to the collection
new_blog = {
    'title':'My Entrepreneur Journey',
    'description':'The ups and downs I had in my entrepreneurship experience.',
    'author':'Joel'
    }
records.insert_one(new_blog)

# Add many documents to the collection
new_blogs = [
    {
        'title':'My family',
        'description':'The people I love the most.',
        'author':'John'
    },
    {
        'title':'Eternal Family',
        'description':'Family is essential to the divine plan of God.',
        'author':'Sarah'
    },
    {
        'title':'Artificial Intelligence',
        'description':'AI is the present and the future of world.',
        'author':'Allen'
    }]
records.insert_many(new_blogs)

# Show the document with author name Joel
records.find_one({'author':'Joel'})

# Update document title "Best Recipe Ever" with new name author
author_update = {
    'author':'Nathan'
}
records.update_one({'title':'Best Recipe Ever'}, {'$set': author_update})

# Delete document with name Joel
records.delete_one({'author':'Joel'})

# Add a new document to the collection
new_blog = {
    'title':'My Entrepreneur Journey',
    'description':'The ups and downs I had in my entrepreneurship experience.',
    'author':'Joel'
    }
records.insert_one(new_blog)

# Show the list of all documents in the collection
list(records.find())

# Show the list of database in the cluster
for db in client.list_database_names():
    print(db)