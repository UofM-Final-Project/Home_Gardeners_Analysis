// Add console.log to check to see if our code is working.
console.log("working");

// Create the map object with a center and zoom level.
let map = L.map('mapid').setView([46.7296, 94.6859], 4);

// Get data from counties.js
let countyData = counties;

 // Loop through the counties array and create one marker for each county.
countyData.forEach(function(county) {
    console.log(county)
    L.circleMarker(county.location, {
        radius: county.avg_last_freeze_dayofyear/100000
    })
    .bindPopup("<h2>" + county.county + ", " + county.state + "</h2> <hr> <h3>Average Last Freeze Date" + county.avg_last_freeze_dayofyear.toLocaleString() + "</h3>")
  .addTo(map);
});

  // We create the tile layer that will be the background of our map.
let streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    accessToken: API_KEY
});
// Then we add our 'graymap' tile layer to the map.
streets.addTo(map);
