from flask import Flask, request

app = Flask (__name__)
print(app)

@app.get("/")
def home_page():
    return "Hello, user!"

@app.get("/users")
def get_users():
    return  {
        "response": ["Alice", "Bob", "Charlie"]
    }

@app.post("/users/register")
def users_register():
    data = request.get_json()
    surname = data.get("Surname")
    print(data)
    return  {
        "response": surname,
        "status": 401
    }, 301

app.run(use_reloader=True)