## Newshiglight API specification

Modified on 16th April 2019

Version: **1.0 **

This is the first work out of my specification and would like to get a feedback from you

##Table of Contents
Introduction
System Overview
Usage
Future Directions and Open Questions
1. Introduction
1.1. Scope

This document describes a News Website App that is primarily concerned with making its users get information and updates about latest happenings around the world. The app is entirely updated/powered by the News API.

1.2. Archivements

Give information to the public-political,sports, entertainment, technology.
Instant and latest news fro all over the globe.
Easier accessibility.
Pictures of articles resective of news source
1.2.1 Goals for implementation
```
  The process by which the API push updates to the app must be simple.

 The app must be secure to use in environments that lack support for Security. This is by use of SECRET_KEY which will prevent CrossSiteOriginForgery
```
2. System overview
The News Web ultimately provides a comfortable and friendly method of obtaining trusted news around the world. This app targets everyone around the world since it is easy to use.

2.1 How the system works
The following are the steps on how The News Web app works, (This is an error-free case.)
```
   Fetching data:
        Periodically, the News app gets updates from The News Web API using the defined Base_URL and an API_KEY, with the use of a context manager, the data from the API gets read, then converted into json format and stored in an object.

  Processing data:
        The Json data then gets processed while applying a filter by the key value assigned to a variable
        i.e
        urlToImage = item.get('urlToImage)
        if urlToImage:
            create object, then instantiate it respective class.
  Displaying data:
        Processed data then get passed into the template(html), where it gets iterated through and displayed

```
2.2. Usage

Minimum Requirements(if working on a local environment)
1. Good internet connection. 
2. Before Running this Project i. run > pip install -r requirements.txt.

You can also choose to use the live link Steps
1. With a browser of your choice, Visit https://rotichnews.herokuapp.com/
2. Onload, the page displays news sources. 
3. Click on any channel you woud like to read news from.
4. You will be presented with various articles from the news source.
5. Click any that you find interesting.

Disclaimer The data contained is not filtered by contents, hence the news app won't be responsible for any rude or unfriendly wordings or images.

Compatibility issues

The app is works as expected across all platforms, incase you face any compatibility issue feel free to reach out.

2.3. Future Directions and Open Questions

For future modifications and directions ,immportantly first understand that this is from a news API and no disclaime issues