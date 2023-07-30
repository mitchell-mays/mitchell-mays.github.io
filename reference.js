// This code was utilized to initially generate the map image from the Road Geojson


path = d3.geoPath().projection(projection);

geojson_base = {
"type": "FeatureCollection",
"features": []
};

// Deep copy base
geojson_highways = JSON.parse(JSON.stringify(geojson_base));
indianaRoadsHighways = indianaRoads.features.filter(function(d){ return (d.properties.speedlimit >= 50); })
geojson_highways.features = indianaRoadsHighways
console.log(indianaRoadsHighways.length)

d3.select('g')
.append('path')
    .attr('stroke', '#000')
    .attr('stroke-width', '2')
    .attr('d', path(geojson_highways))
    .attr("fill", "none");


// Deep copy base
geojson_roads1 = JSON.parse(JSON.stringify(geojson_base));
indianaRoads1 = indianaRoads.features.filter(function(d){ return (d.properties.speedlimit >= 35); })
geojson_roads1.features = indianaRoads1
console.log(indianaRoads1.length)

d3.select('g')
.append('path')
    .attr('stroke', '#aaa')
    .attr('stroke-width', '1')
    .attr('d', path(geojson_roads1))
    .attr("fill", "none");

// Deep copy base
geojson_roads2 = JSON.parse(JSON.stringify(geojson_base));
indianaRoads2 = indianaRoads.features.filter(function(d){ return (d.properties.speedlimit < 35); })
geojson_roads2.features = indianaRoads2
console.log(indianaRoads2.length)

d3.select('g')
.append('path')
    .attr('stroke', '#aaa')
    .attr('stroke-width', '0.5')
    .attr('d', path(geojson_roads2))
    .attr("fill", "none");