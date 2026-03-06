from flask import Flask, render_template_string
import sys
import os
import time
import threading

# connect to scanner module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from process_scanner import scan_processes, detect_suspicious

app = Flask(__name__)

# global storage
suspicious_processes = []

HTML = """
<!DOCTYPE html>
<html>
<head>

<title>Keylogger Detection Dashboard</title>

<meta http-equiv="refresh" content="5">

<style>

body{
font-family: Arial;
background:#121212;
color:white;
text-align:center;
}

table{
margin:auto;
border-collapse:collapse;
width:80%;
}

th,td{
border:1px solid white;
padding:10px;
}

th{
background:#444;
}

.alert{
color:red;
font-weight:bold;
}

</style>

</head>

<body>

<h1>🛡 Keylogger Detection Dashboard</h1>

<h2>System Status: Monitoring</h2>

<h2>Suspicious Processes</h2>

{% if suspicious %}

<table>

<tr>
<th>PID</th>
<th>Name</th>
<th>Path</th>
</tr>

{% for proc in suspicious %}

<tr class="alert">
<td>{{proc.pid}}</td>
<td>{{proc.name}}</td>
<td>{{proc.exe}}</td>
</tr>

{% endfor %}

</table>

{% else %}

<p>✅ No suspicious processes detected</p>

{% endif %}

</body>
</html>
"""


def background_scanner():
    global suspicious_processes

    while True:

        processes = scan_processes()

        suspicious_processes = detect_suspicious(processes)

        time.sleep(5)


@app.route("/")
def dashboard():

    return render_template_string(HTML, suspicious=suspicious_processes)


if __name__ == "__main__":

    scanner_thread = threading.Thread(target=background_scanner)
    scanner_thread.daemon = True
    scanner_thread.start()

    app.run(debug=True)