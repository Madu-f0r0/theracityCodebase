function showMap() {
  console.log("I entered the showMap function");

  var container = document.getElementById("map");
  const lat = parseFloat(container.getAttribute("lat"));
  const lng = parseFloat(container.getAttribute("lng"));
  const pharmacyName = container.getAttribute("name");

  console.log(`In the showMap function, lat = ${lat} and type is ${typeof lat}`);
  console.log(`lng = ${lng} and type is ${typeof lng}`);
  const position = { lat: lat, lng: lng };

  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 18,
    center: position
  });

  const marker = new google.maps.Marker({
    position: position,
    map: map,
    title: pharmacyName
  });
}
