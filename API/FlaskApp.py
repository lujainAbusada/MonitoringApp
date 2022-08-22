import json
from flask import Flask, jsonify
import FetchData
    

app = Flask(__name__)

@app.route('/')
def homepage():
    return json.dumps({'This is a Monitoring website' : 'Hello!'})

@app.route('/Memory')
def MemoryPage():
    return jsonify(FetchData.retrieve_Memory_data())

@app.route('/Disk')
def DiskPage():
    return jsonify(FetchData.retrieve_Disk_data())

@app.route('/CPU')
def CPUPage():
    return jsonify(FetchData.retrieve_CPU_data())

@app.route('/CPU-Now')
def CPUNowPage():
    return jsonify(FetchData.retrieve_CPUNow_data())

@app.route('/Memory-Now')
def MemoryNowPage():
    return jsonify(FetchData.retrieve_MemoryNow_data())

@app.route('/Disk-Now')
def DiskNowPage():
    return jsonify(FetchData.retrieve_DiskNow_data())

if __name__ == "__main__":
    app.run(host='0.0.0.0')
app.run()

