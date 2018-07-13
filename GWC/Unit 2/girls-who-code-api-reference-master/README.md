# girls-who-code-api-reference

## Giphy 
![Giphy Api](https://developers.giphy.com/static/img/api.c99e353f761d.gif)

**API Key** - `VU0MWvV9PyOQln4z3PtKGbHUDiwfZAtm`

**Endpoint** - http://api.giphy.com/v1/gifs/search

**Example** - http://api.giphy.com/v1/gifs/search?api_key=VU0MWvV9PyOQln4z3PtKGbHUDiwfZAtm&q=tracer&limit=5&rating=pg

| Query Parameter  | Type | Value | Description |
| ------------- | ------------- |------------ | --- |
| api_key  | string  | any string | API application key
| q | string  | any string | Search query
| limit  | number  | any number | limit how many images are returned
| rating | string  | g or pg | filter results based on MPAA rating

## Youtube
![Youtube Logo](https://png.icons8.com/color/260/youtube.png)

**API Key** - `AIzaSyC-bOTKR-WG8jNw__TKfMQl9WO-0AnsSpc`

**Endpoint** -  https://www.googleapis.com/youtube/v3/search

**Example** - https://www.googleapis.com/youtube/v3/search?key=AIzaSyC-bOTKR-WG8jNw__TKfMQl9WO-0AnsSpc&q=tracer&safeSearch=strict&type=video&videoEmbeddable=true&part=snippet

| Query Parameter  | Type | Value | Description |
| ------------- | ------------- |------------ | --- |
| key  | string  | any string | API application key
| q | string  | any string | Search query
| safeSearch  | string  | strict | safe search settings
| type | string  | video or playlist or channel | Video type to return
| videoEmbeddable | string | any or true | Only return videos that are embeddable
| part | string | snippet | common delimited list of fields to include in response

### How to Embed Youtube videos based on response
TODO

## Flickr 
![Flickr Logo](http://icons.iconarchive.com/icons/uiconstock/socialmedia/256/Flickr-icon.png)

**API Key** - `3baa8586f9b7202d3b0e80662c880403`

**Endpoint** - https://api.flickr.com/services/rest/

**Example** - https://api.flickr.com/services/rest/?api_key=3baa8586f9b7202d3b0e80662c880403&text=tracer&safe_search=1&method=flickr.photos.search&format=json&nojsoncallback=1

| Query Parameter  | Type | Value | Description |
| ------------- | ------------- |------------ | --- |
| api_key  | string  | any string | API application key
| text | string  | any string | Search query
| safe_search  | number  | 1 | safe search settings
| method | string  | flickr.photos.search | name of flickr API method
| format | string | json | format of HTTP response
| nojsoncallback | number | 1 | whether or not to return the response as [JSONP](https://en.wikipedia.org/wiki/JSONP)

## How to convert response into image URLS
You can construct image urls by taking the response fields and creating URLs with the following pattern https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg
TODO
