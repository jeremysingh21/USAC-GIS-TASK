The following repo contains files that construct two maps using the E-Rate data API from the Scroata API.

## Data
The data was acquired from the [E-rate Request for Discount on Services: Basic Information](https://opendata.usac.org/E-rate/E-rate-Request-for-Discount-on-Services-Basic-Info/9s6i-myen)
dataset. Using the [USAC_Data.py](https://github.com/jeremysingh21/USAC-GIS-TASK/blob/master/USAC_Data.ipynb), the socarata api was accessed to pull the requested data.
## Web Maps
Two web maps were constructed using MapboxGL and Mapbox studio. The maps is [hosted here](https://jeremysingh21.github.io/USAC-GIS-TASK/index.html)

The page contains two tabs-

**Map 1: Funding by Organization**: Points in the web map represent organizations that requested e-rate funding in 2018. The requested funding amount shown is aggregated at the organization leveland will be shown in the pop-up when point is clicked. The html/js code for this can be found under [index.html](https://github.com/jeremysingh21/USAC-GIS-TASK/blob/master/index.html)

**Map 2: Funding by State** This web map represents the total funding request amount in 2018 by state. The funding information can be accessed in the information box on the right by hovering mouse-pointer over a desired state. [states_total.html](https://github.com/jeremysingh21/USAC-GIS-TASK/blob/master/states_total.html)

The css code for the page can be found in [styles.css](https://github.com/jeremysingh21/USAC-GIS-TASK/blob/master/styles.css)
