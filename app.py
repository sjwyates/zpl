from flask import Flask, render_template, redirect
import pandas as pd

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world():
    samples_df = pd.read_excel('test_excel.xlsx')
    samples_df['Date'] = samples_df['Date'].dt.strftime('%d%b%Y')
    columns = samples_df.columns
    samples = samples_df.to_dict('records')
    tests = ["Conductivity", "TOC", "Bioburden", "Endotoxin", "Conductivity"]
    return render_template("index.html", tests=tests, columns=columns, samples=samples)


def grab_excel(path, filename):
    samples_df = pd.read_excel('test_excel.xlsx')
    samples_df['Date'] = samples_df['Date'].dt.strftime('%d%b%Y')
    columns = samples_df.columns
    samples = samples_df.to_dict('records')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
