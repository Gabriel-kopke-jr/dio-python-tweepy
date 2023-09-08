from fastapi import FastAPI
import os
import api_tweepy
#conexao = MongoConnection.create_connection()
#db = MongoConnection.create_dabase(conexao,'teste')
#posts = db.post
#post = {
#    "author": "eu",
#    "message": "sou o cara"
#}

#post_id = posts.insert_one(post).inserted_id
#count = posts.count_documents({})
#print(count)

#conexao.close()
#app = FastAPI()

#@app.get("/")
#async def hello():
 #   return{"message":"hello my boy"}

api_tweepy.get_tweets()