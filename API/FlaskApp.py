import json
from flask import Flask, jsonify, render_template
import FetchData

app = Flask(__name__)

@app.route('/', endpoint='homepage')
def homepage():
    return render_template('Home.html' )

@app.route('/Memory', endpoint='MemoryPage')
def MemoryPage():
    return jsonify(FetchData.retrieve_Memory_data())

@app.route('/Disk', endpoint='DiskPage')
def DiskPage():
    return jsonify(FetchData.retrieve_Disk_data())

@app.route('/CPU', endpoint='CPUPage')
def CPUPage():
    return jsonify(FetchData.retrieve_CPU_data())

@app.route('/CPU-Now', endpoint='CPUNowPage')
def CPUNowPage():
    return jsonify(FetchData.retrieve_CPUNow_data())

@app.route('/Memory-Now', endpoint='MemoryNowPage')
def MemoryNowPage():
    return jsonify(FetchData.retrieve_MemoryNow_data())

@app.route('/Disk-Now', endpoint='DiskNowPage')
def DiskNowPage():
    return jsonify(FetchData.retrieve_DiskNow_data())

if __name__ == "__main__":
    app.run(host='0.0.0.0')


