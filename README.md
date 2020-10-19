# incognito-project

The incognito project is an App developped to assist the squireelfobic in their attemps to avoid any contact with squirrels.
On this first version we have deployed the app to cover only Central Park. For this app we used the 2018-Central-Park-Squirrel-Census as our database

## Install Dependencies

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all incognito-project requirements.

```bash
pip install -r requirements.txt
```

## App

The name of this app is simply Squirrels

## Pages
This App will connect you through 5 different pages:

- Main page:
Connecting you to the other 3 is accesible through /sightings/
This page contains the Uniqued Id of every squirrel detected on Central Park and the links to all other pages

- Add a squirrel sighting
  Inside the Main Page you will see a link for Add that will take you to the Add page in order for you to add a new Squirrell sighting
  Also accesible through /sightings/add
  
- Map of Squirrels in Central Park
  Inside the Main Page you will see a link for Map that will take you to the Map page where you can see a map of a some of the Squirrel exact location 
  (limited to under 100 for computer capacity)
  Also accesible through /sightings/map
  
- Relevant Stats
  Inside the Main Page you will see a link for Some Stats that will take you to the Stats where you can see a table rendering relevant stats of the squirrels
  Also accesible through /sightings/stats
  
- Update a Squirrel
  To update a Squirrel simply click on the Unique Id displayed on the list of Squirrels of the Main Page
  Also accesible through /sightings/<Unique Id of the Squirrel>
  
## Group Name
Group Incognito

## Members

UNIs:[ed2911,nd2673,ne2323]

## Link to GitHub Repository 

https://github.com/EduardoDCRR/incognito-project.git




