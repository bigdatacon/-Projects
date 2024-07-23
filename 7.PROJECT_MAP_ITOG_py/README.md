# File Navigation

Each file runs independently:

## Videos

- Video with voice comments: [Google Drive](https://drive.google.com/file/d/1fRyeMLP70qOgl5VZhP1F3z-b5AtoNp_e/view?usp=sharing) or [Yandex Disk](https://disk.yandex.ru/i/zwC327KjLXMUHw)
- Description video: `video.mp4`
- Additional video after adding information on houses: [Google Drive](https://drive.google.com/file/d/1MceXNvV3UfXCB7IJWkr5cHYAG0sO_dvF/view?usp=sharing)

## Project Folder Information

- **Folder `utils`:** Contains the main functions where all calculations are done (files do not need to be executed) and adding coordinates through the Google API.
- **Folder `parser`:** Contains site parsers and parsed files.
- **Folder `files`:** Contains files for the project obtained after running the files and project.
- **Folder `Flask`:** Contains wrappers for Flask.

## Project Root

### a) `1.Get_info_for_many_new_coords`

Generates a list containing both coordinates and information about existing trade points and newly obtained coordinates and information, which are then transferred to Tableau Desktop. Only the `func`, `csvj`, and `ostanovk` files are needed for this to work.

- Links to Tableau reports (interactive maps of new and existing businesses; maps can be zoomed in and out, and hovering over a point displays basic information):
  - [Report 1](https://public.tableau.com/views/Book16_16143677148020/Sheet1?:language=en&:display_count=y&publish=yes&:origin=viz_share_link)
  - [Report 2](https://public.tableau.com/views/Book16_16143677148020/Satellite?:language=en&:display_count=y&publish=yes&:origin=viz_share_link)
  - [Report 3](https://public.tableau.com/views/Book3_16145304458620/Sheet1?:language=en&:display_count=y&publish=yes&:origin=viz_share_link)
  - [Report 4](https://public.tableau.com/views/Book3_16145304458620/Street_size?:language=en&:display_count=y&publish=yes&:origin=viz_share_link)
  - [Report 5](https://public.tableau.com/views/Book3_16145304458620/Sattelite_size?:language=en&:display_count=y&publish=yes&:origin=viz_share_link)
  - [Report 6](https://public.tableau.com/views/Book3_16145304458620/Satellite?:language=en&:display_count=y&publish=yes&:origin=viz_share_link)
  - [Report 7](https://public.tableau.com/views/Book3_16145304458620/Streetv?:language=en&:display_count=y&publish=yes&:origin=viz_share_link)
  - [Report 8](https://public.tableau.com/views/Book3_16145304458620/Dashboard1?:language=en&:display_count=y&publish=yes&:origin=viz_share_link)
- Excel file with all information for new and existing businesses: `files/ITOGI_FOR_MANY_POINS.xlsx`

### b) `2.Get_inf_for_1_done`

The file receives coordinates of the address where the user wants to open a new trade point (coordinates obtained from Yandex Maps). This point is then analyzed relative to all existing points in the database. The output is a list with information about the new point and all existing points, which are then transferred to Tableau Desktop. The `2.Get_inf_for_1_done` file requires the `FOR_CHEK_SPISOK_TEK_KOORD_WITH_ALL_INFO` file (obtained after running the `3.ZAPIS_VSEH_COORD` file), as well as the `func`, `csvj`, and `ostanovk` files.

- Output:
  - Link to Tableau report: [Report](https://public.tableau.com/views/Project_test_16131009080200/NEWPOINT?:language=en&:display_count=y&publish=yes&:origin=viz_share_link)
  - Files with information about all points: `files/ALL_POINT_INFO.xlsx`
  - File with information about the requested point: `files/one_POINT_INFO.xlsx`

### c) `3.ZAPIS_VSEH_COORD`

An auxiliary file that preps a file with additional information about existing trade points. Only the `func` and `csvj` files are needed for this to work. This file does not need to be executed as the required file (`files/FOR_CHEK_SPISOK_TEK_KOORD_WITH_ALL_INFO.json`) is already prepared.

### d) `10.add_rating`

Script that adds a rating to new points.

### e) `11.ADD_CENTERS`

Script for adding data about shopping and office centers.

## Additional Comments

To start each file, the `csvjs` file is needed. All newly obtained JSON files from the programs are automatically updated in Tableau reports (if Tableau Desktop is available). Initially, the report format is created in Tableau Desktop, and then the data in the reports is automatically updated when the programs are run. However, only a registered user on the Tableau Online site can automatically update the link to Tableau Online.

To check a single address, use the `2.Get_inf_for_1_done` file, but mapping it automatically is not possible at this stage. Programs under points a-b) work independently of each other.

When any program is started, it asks for the object category: cheap, middle, expensive. You can press ENTER without entering anything - in this case, the suitability indicators of the point will be calculated without considering the "class" of the object.

### Key Metrics in Final Files for New Points (status = new):

- Distance to competitor (distance_to_closer_conquer)
- Distance to metro (distance_to_closer_metro)
- Population within radius to the nearest competitor (chisl)
- Population and number of competitors within a 2 km radius
- Number of shopping centers within a 1 km radius
- Other metrics

Given that data on the population in each house in Moscow was parsed, an additional calculation of the population within the radius to the competitor by the number of houses in the radius is provided.

Added information on the number of competitors within a 2 km radius, population within a 2 km radius, and population per competitor within a 2 km radius. The number of houses is lower than the population by density due to the fact that the gosjkh site provides information on houses with a total population of 6.5 million people, which is ~50% of the official population in Moscow.

Only points where all three of the above components are "good" (or where only the distance to the metro and public transport stops is "bad") are included in the final file for speed optimization. These points are then filtered in Tableau. The program's essence is to find points with good location indicators considering their class.

All new points receive a rating calculated as the sum of the logarithms of the main metrics (distance to the metro, population within the radius to the competitor, population within a 2 km radius, number of competitors within a 2 km radius, population per competitor). The final rating is adjusted for the presence of large (S>25,000 m2) shopping and office centers within a 1 km radius. On the map, points with the best rating are highlighted in color.

All final files are in the `files` folder. Flask scripts with wrappers are in the `Flask` folder.

### Main Project Description:

Application: Electronic consulting (initially based on Moscow).

Production deployment: Consulting service on the internet (selling reports in Tableau).

### Target Audience:

- Small and medium businesses (service sector)
- Those looking to start a new business (service sector)

### Working Principle:

Based on the location of a trade point and its operation time in one place, the influence of external factors on the success of the point is evaluated:

- Distance to the nearest competitor
- Proximity to the metro
- Proximity to large shopping and office centers
- Population density in the area and within the radius to the nearest competitor (determined by the average city population density within the radius to the nearest competitor)
- The segment in which the client plans to operate. The model works both with and without specifying the segment. If the segment is specified, the new trade point's indicators are analyzed based on the indicators of existing businesses in the corresponding segment.
- Revenue (in the Project, revenue is set synthetically; further development based on the legal entity can obtain the TIN and revenue from open sources)
- Operation time (initial statistics for the company) - in the absence of revenue, the operation time is the main profitability criterion. If >1.5 years, the business is likely profitable.

Visualization of potential new trade points on the map in Tableau Desktop.

### Application Description:

#### Initial Stage:

1. Accumulating data on:
   - Existing businesses from open sources. A Yandex parser is available, but only 10 companies can be parsed for free. Therefore, the 2GIS database is used.
   - Large shopping and office centers (parser included);
   - Public transport stops;
   - Population in each house in Moscow (parser included) - but the site from which the data was parsed has information on houses with a total population of 6.5 million people.

2. Generating new points with a specified step (distance between points).
3. Determining from the generated points those that meet the criteria (more criteria can be added later):
   - Distance to the metro <= (average for existing points)/1.2
   - Distance to the nearest competitor >= (average for existing points)*1.2
   - Population within the radius to the nearest competitor >= (average for existing points)*1.2
   - Adjustment coefficient for the proximity of large (area >25,000 m2) shopping centers within a 1 km radius.

The final rating for the trade point is calculated considering the sum of the logarithms of all the above metrics. If a segment is chosen, the analysis for existing points is conducted within the corresponding segment.

### Potential Improvements:

Exclude coordinates of rivers, major highways, and roads. Add features, if available, on clients, proximity to busy roads, etc., to more accurately determine the attractiveness of the point.
