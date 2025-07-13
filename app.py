from flask import Flask, render_template, request, send_file
import pandas as pd


app  = Flask(__name__) #creates an instance
@app.route("/add", methods = ['GET','POST']) # tells if someone visits /add it returns the add.html page, also tells we will be using get and post
def expense_page():   #what get does? it fetches the visted url , and post fetches the submit data
    if request.method == 'POST':
        date = request.form["date"]
        amount = request.form["amount"]
        category = request.form["category"]
        note = request.form["note"]

        new_expense = pd.DataFrame([{                                         #create a data frame with date , amount etc as a table title and value as a row
            "date": date,
            "amount": amount,
            "category": category,
            "note": note
        }])

        new_expense.to_csv("expenses.csv", mode="a", index=False, header=not pd.io.common.file_exists("expenses.csv"))


# pd.DataFrame([{...}])==> Creates a one-row table with the data you got
# to_csv(..., mode="a")==> Appends this row to the CSV file
# header=not file_exists(...)==> Adds headers only if file doesn’t exist yet
    return render_template("add.html") #loads the file
@app.route("/download")
def csv_download():
    return send_file("expenses.csv",as_attachment=True)
    
@app.route("/view") #to view stuff
def view():
    try:
        df = pd.read_csv("expenses.csv") #pandas reads csv
        return df.to_html(index=False) #returns the table into html format
    except FileNotFoundError:
        return "<h2>No expenses recorded yet.</h2>"
    
@app.route("/clear")
def clear_expenses():
    # Create empty DataFrame with headers
    df = pd.DataFrame(columns=["date", "amount", "category", "note"]) #resetting it like a list 
    df.to_csv("expenses.csv", index=False)
    return "<h3>All expenses cleared.</h3><a href='/add'>← Back</a>" #redirecting to add

    

if __name__ == "__main__": #runs the server
    app.run(debug=True)
