from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/books", methods=["GET", "POST"])
def books():
    if request.method == "GET":
        return render_template("show-books.html")
    elif request.method == "POST":
        book_name = request.args["name"]
        book_price = request.args["price"]
        book_category = request.args["category"]
        #you may work with the received data
        #like inserting into database, or updating a column for the record
        return {"status" : "Book added to library."}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)