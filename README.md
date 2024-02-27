# TheraCity
***pharmacy made easy...***

## Introduction
TheraCity is a pharmaceutical solution that brings medicines and pharmacy stores closer to the user. The TheraCity app uses the user's location to display pharmacies closest to the user who have a searched medicine in their stock.

Theracity is available online at [https://www.oganiru.tech/theracity](https://www.oganiru.tech/theracity)

## The TheraCity Story
The vision behind the TheraCity project is to create a one stop online mega pharmacy store which comprises of all the physical pharmacies in a location. We dreamt of an online location where a user could search for a medicine, learn more about the medication, make informed decisions about what brand to select, compare prices across pharmacies, and be able to make a purchase in one of the pharmacies closest to them. This purchase could then be delivered to the user in the comfort of their home.

The TheraCity vision is to make the life easier for the convalescent in society through easier solutions to their pharmaceutical needs made available through technology.

## Usage
### Search for a Pharmacy
- Click on the `Pharmacy` option on the navigation bar. This drops down a search bar
- Enter the name of the pharmacy you intend to search for. A list of pharmacies in our database with similar name are displayed as you enter the pharmacy name
- Click on the pharmacy you intend to get more details about. Information about the pharmacy selected will be displayed in a new page.
- You can click on the `Website` button to be redirected to the pharmacy's website
- An interactive Google map location of the pharmacy is also displayed on the screen

### Search for a Medicine
- Click on the `Medicine` option on the navigation bar. This drops down a search bar
- Start to enter in the name of the medicine you intend to search for into the search bar. A list of suggestions of medicines whose names are similar to the term you entered are displayed
- When you click on any of the medicines, a list of pharmacies closest to your location are displayed on a new page. Click on any of the pharmacies displayed and you will be redirected to a new page that displays the following information aout the medicine and the pharmacy:
	* Medicine name
	* About the medicine
	* Manufacturer's name
	* Manufacturer's country

	* Pharmacy name
	* Pharmacy image
	* Button to link to the pharmacy's website
	* Button to display the pharmacy's location and direction on Google map

## Technical Details
### Frontend Implementation
The structure of the Theracity frontend is layed out using HTML5 and styled using CSS3. User interactivity is implemented using JavaScript. JavaScript is also the bridge between the client-side and the server-side through specified urls.

### Backend Implementation
The backend of the TheraCity project is implemented using Django web framework. Django's `urls` module listens for requests to the urls agreed upon and maps those urls to corresponding view functions in the `views` module of the Django app. The view functions handle the application logic, database querying, and in some occassions, the rendering of the templates to the browser.

A frontend web framework was not used for this project as at the v1 release. As a result, the static files (CSS, JavaScript, and image files) are all located within the Django file structure specfically within  the `static` folder. In the same manner, the HTML files are stored within the `templates` folder within the Django app.

### Database Implementation
The TheraCity project uses MySQL as its database. Django's ORM allows for seamless creation of the tables and queryng of the database using Pythonic syntax using Django's `models` module. The `makemigrations` and `migrate` Django commands then convert the ORM syntax into SQL implementations.

### Geospatial Implementation
The frontend environment handles the setting up of the Google map section, while Django handles the geospatial calculations that are a part of the application logic.

JavaScript is responsible for querying the Google map API to return the map, location marker, as well as direction lines implemented in the TheraCity project.

Django handles the point calculation of pharmacies **closest** to the user. To be able to handle geospatial calculations, GeoDjango's `gis` module is imported into the app.

## Future Implementations
In line with the TheraCity vision, the following features will be implemented in the coming weeks to months:
- Pharmacy admin CRUD functionality
- Improvements to the application design
- Implementation of user profiles
- Implementation of e-commerse features

## Collaborators
- Oluwatosin Eziekel Ajayi - Frontend Engineer (TheraCity Design)
- Mahder Welde Giorgis - Frontend Engineer (TheraCity User Interaction and Google map imlementation)
- Daniel Herbert - Backend Engineer and Systems Administrator
