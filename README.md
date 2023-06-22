# Desktop Anime Wallpaper API Documentation

## Index
This endpoint provides a list of available API endpoints with their descriptions and links.

### Endpoint:
- **URL:** /
- **Method:** GET

## Get Wallpaper
This endpoint retrieves wallpapers based on the provided search criteria or randomly.

### Endpoint:
- **URL:** /api/wallpapers/name
- **Method:** GET
- **Description:** Get wallpaper by character name

### Parameters:
- `<name>` (required): The name of the wallpaper to search for. It can also be set to "random" to get a random wallpaper.

### Query Parameters:
- `limit` (optional): The maximum number of wallpapers to retrieve. Default value is 1.
- `width` (optional): The desired width of the wallpaper in pixels. Default value is 1920.
- `height` (optional): The desired height of the wallpaper in pixels. Default value is 1080.

### Successful Response:
- Status Code: 200 (OK)
- Body: A JSON array of wallpaper objects. Each object contains the following fields:
  - `name`: The title of the wallpaper.
  - `url`: The URL of the wallpaper image.

### Error Responses:
- Status Code: 400 (Bad Request)
- Body: A JSON object with an error field indicating the error message.

### Examples:
1. **Retrieve a wallpaper by name:**
   - URL: /api/wallpapers/nature
   - Method: GET
   - Response:
     ```json
     [
         {
             "title": "Nature Wallpaper",
             "url": "https://example.com/nature.jpg"
         }
     ]
     ```

2. **Retrieve a random wallpaper:**
   - URL: /api/wallpapers/random
   - Method: GET
   - Response:
     ```json
     [
         {
             "title": "Random Wallpaper",
             "url": "https://example.com/random.jpg"
         }
     ]
     ```

3. **Retrieve multiple wallpapers by name and set limit, width, and height:**
   - URL: /api/wallpapers/cars
   - Get Data Parameters:
     - limit: 5
     - width: 1280
     - height: 720
   - Method: GET
   - Response:
     ```json
     [
         {
             "title": "Car Wallpaper 1",
             "url": "https://example.com/car1.jpg"
         },
         {
             "title": "Car Wallpaper 2",
             "url": "https://example.com/car2.jpg"
         }
         // ...
     ]
     ```

## Footer
APIs are build by scraping [Wallhaven](https://wallhaven.cc/).

Developed by [@Ritin Tiwari](https://www.github.com/ritin0204).
