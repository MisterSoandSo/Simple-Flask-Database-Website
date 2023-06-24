from flask import Flask, render_template
from waitress import serve
import sqlite3

mode = "dev" #or "prod"
database_name = 'blackmarket.db'

app = Flask(__name__)

def analysis(result):
    avg_price = 0.00
    minimum = 0
    maximum = 0
    number = 0
    for row in result:
        print(row)
        value = float(row[2].replace("$",""))
        avg_price += value
        if number == 0:
            minimum = value
            maximum = value
        else:
            if value < minimum:
                minimum = value
            if value > maximum:
                maximum = value
        number += 1

    avg = round(avg_price/number,2)

    return avg, minimum, maximum

def get_detail_item_list():
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("SELECT * FROM blackmarket")
    result = c.fetchall()
    conn.close()

    start = result[0][3]
    end = result[-1][3]
    item_set = set([row[1] for row in result])

    return  start,end, sorted(list(item_set))

def get_single_item(item):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("SELECT * FROM blackmarket WHERE item = ?", [item])
    result = c.fetchall()
    conn.close()

    return result


@app.route("/")
def home():
    start,end, _items = get_detail_item_list()
    return render_template('index.html',start_date = start, end_date = end,items= _items)

@app.route("/item/<it>")
def list_item(it):
    result = get_single_item(it)
    print(type(result))
    if result:
        avg, min, max, = analysis(result)
        return render_template('items/index.html',item=it, items= result, average = avg, min = min, max = max)
    else:
        return render_template('items/index.html',item=it, items= [], average = 'N/A', min = 'N/A', max = 'N/A')


if __name__ == "__main__":
    if mode == 'dev':   
        #dev mode
        app.run(debug=True)
    else:
        #production mode
        serve(app, host='0.0.0.0', port = 5000, threads = 1)