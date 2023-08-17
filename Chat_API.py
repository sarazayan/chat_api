from main import generate_response
#Ask Questions
from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def read_root():
    return {"message":"welocome Team!"}
@app.get("/ask/{question}")
def ASK(question:str):
    
    res=generate_response(question)
    answer="answer is : " +res["result"]
    return  {"answer is ":answer}
# run this :
# uvicorn Chat_API:app --reload