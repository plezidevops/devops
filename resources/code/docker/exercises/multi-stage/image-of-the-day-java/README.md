What this app does?

```
This app fetches the details of today's picture from NASA.
```

Build and run the application

```
1. Go the folder where the app is
2. docker image build -t today-image
3. docker container run --name today-image -d -p 800:80 today-image
```

Access the application

```
http://localhost:800/image
```

Facade over NASA Astronomy Picture of the Day (APOD)

ENV for API_KEY

```
https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
```

Full returns:

```
{"copyright":"Michel Loic","date":"2019-06-28","explanation":"The night of June 21 was the shortest night for planet Earth's northern latitudes, so at latitude 48.9 degrees north, Paris was no exception. Still, the City of Light had an exceptionally luminous evening. Its skies were flooded with silvery night shining or noctilucent clouds after the solstice sunset. Hovering at the edge of space, the icy condensations on meteoric dust or volcanic ash are still in full sunlight at the extreme altitudes of the mesophere. Seen at high latitudes in summer months, stunning, wide spread displays of northern noctilucent clouds are now being reported.","hdurl":"https://apod.nasa.gov/apod/image/1906/D7X7411-2Loic.jpg","media_type":"image","service_version":"v1","title":"A Solstice Night in Paris","url":"https://apod.nasa.gov/apod/image/1906/D7X7411-2Loic_1024.jpg"}
```

facade returns:

```
{
    "url":""
    "caption":""
    "copyright":""
}
```
