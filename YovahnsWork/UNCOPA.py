from flask import Flask, render_template_string

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UNCO Parking App</title>
    <style>
        body {
            text-align: center;
            font-family: Arial, sans-serif;
        }
        .logo {
            width: 200px;
            height: auto;
        }
        .container {
            margin: 10px auto;
        }
        input, button, select {
            padding: 8px;
            margin: 5px;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <section>
        <center>
              <img src="static\Screenshot 2025-01-23 002417.png" alt="UNCO Parking App Logo" class="logo">
        </center>
        

        <div class="container">
            <input type="text" id="searchBox" placeholder="Search for a location...">
            <button onclick="searchLocation()">Search</button>
        </div>

        <div class="container">
            <button onclick="openGoogleMaps()">Open in Google Maps</button>
        </div>

        <div class="container">
            <label for="filter">Filter Parking Lots:</label>
            <select id="filter" onchange="filterParkingLots()">
                <option value="all">All</option>
                <option value="student">Student Parking</option>
                <option value="faculty">Faculty Parking</option>
            </select>
        </div>

        <div class="container">
            <button onclick="openPassportParking()"><img src="static\passport-logo-.png" alt="UNCO Parking App Logo" class="logo"></button>
        </div>
    </section>

    <script>
        function searchLocation() {
            let query = document.getElementById("searchBox").value;
            alert("Searching for: " + query); 
        }

        function openGoogleMaps() {
            window.open("https://www.google.com/maps", "_blank");
        }

        function filterParkingLots() {
            let filterValue = document.getElementById("filter").value;
            alert("Filtering for: " + filterValue);
        }

        function openPassportParking() {
            window.open("https://park.passportparking.com/park/", "_blank");
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True)
