# 💻 Labs

```{admonition} Table of Contents! 👇🏽
:class: dropdown
1. [Lab 0: Tools](lab-0)
2. [Lab 1: Tidy Data](lab-1)
3. [Lab 2: Data Engineering](lab-2)
4. [Lab 3: Geo-Visualisation](lab-3)
5. [Lab 4: Networks and Spatial Weights](lab-4)
6. [Lab 5: Linear Regression](lab-5)
7. [Lab 6: Clustering](lab-6)
8. [Lab 7: Points](lab-7)
```

***

(lab-0)=
## Lab 0 - Tools

#### Resources

- **Download Materials:** [Lab 0 & Homework 0 Notebooks + Data (ZIP)](https://surfdrive.surf.nl/files/index.php/s/qv637XJ3TiHHxWt/download)

#### Notebooks

- [Lab 0](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-00/lab-00.ipynb)
- [Homework 0](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-00/hw-00.ipynb)

#### Notes

**IMPORTANT** This is a supplementary notebook that covers many basics of the tools we will use in the course but does not explain anything directly related to Spatial Data Science.

Students are encouraged to read it before getting started with the other notebooks and then keep it as a reference throughout the rest of the course. There are some basic Python operations in there that act as a refresher, practice or learning material, if you may need it.

#### Extra Material

If you want to explore further by yourself the contents presented in this tutorial, the following pointers are good places to start:

* Gallery of [interesting notebooks](https://github.com/jupyter/jupyter/wiki): a wealth of examples of Jupyter (formerly called IPython) notebooks.
* (Downey, 2012): very good general introduction to Python as a programming language and to the algorithmic way of thinking. The book is freely available in [HTML](http://www.greenteapress.com/thinkpython/html/index.html) and [PDF](http://www.greenteapress.com/thinkpython/thinkpython.pdf).

***

(lab-1)=
## Lab 1 - Tidy Data

#### Resources

- **Download Materials:** [Lab 1 & Homework 1 Notebooks + Data (ZIP)](https://surfdrive.surf.nl/files/index.php/s/UJBpIa4V6CecvOQ/download)

#### Notebooks

- [Lab 1 - Part 1](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-01/lab-01-part-01.ipynb)
- [Lab 1 - Part 2](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-01/lab-01-part-02.ipynb)
- [Lab 1 - Part 3](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-01/lab-01-part-02.ipynb)
- [Homework 1](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-01/hw-01.ipynb)

#### Data

This session uses the **"Census socio-demographics"** dataset of The Hague, Netherlands and Liverpool, United Kingdom in two parts. The dataset for this lab is provided in the zipped lab files above.

1. Table of neighbourhoods called Buurten areas in The Hague with population counts by World region and Age groups. The table is derived from the denhaagcijfers dataset.
2. Table of LSOA areas in Liverpool with population counts by World region. The table is derived from the CDRC Census data pack.
3. Collection of socio-demographic characteristics from the 2011 Census for the city of Liverpool.

#### Extra Material

* **[Visualization]** Python library `seaborn` [tutorial](http://stanford.edu/~mwaskom/software/seaborn/tutorial.html).
* [NY Times article](http://www.nytimes.com/2014/08/18/technology/for-big-data-scientists-hurdle-to-insights-is-janitor-work.html?_r=0) about the importance of cleaning data.


***

(lab-2)=
## Lab 2 - Data Engineering

#### Resources

- **Download Materials:** [Lab 2 & Homework 2 Notebooks + Data (ZIP)](https://surfdrive.surf.nl/files/index.php/s/XK6UdKXfB9vAT9h/download)

#### Notebooks

- [Lab 2 - Part 1](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-02/lab-02-part-01.ipynb)
- [Lab 2 - Part 2](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-02/lab-02-part-02.ipynb)
- [Homework 2](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-02/hw-02.ipynb)

#### Data

This session uses two datasets which are provided in the zipped lab files above.

1. A dataset about wines from different countries, download from **Kaggle**.
2. A dataset scraped and collected from **Goodreads**.


***

(lab-3)=
## Lab 3 - Geo-Visualisation

#### Resources

- **Download Materials:** [Lab 3 Notebooks + Data (ZIP)](https://surfdrive.surf.nl/files/index.php/s/JoKvDXxL6Hb15zD/download)

#### Notebooks

- [Lab 3 - Part 1](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-03/lab-03-part-01.ipynb)
- [Lab 3 - Part 2](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-03/lab-03-part-02.ipynb)

The homework exercises are embedded within the lab files itself. You have to complete the exercises as you go along understanding the rest of the code. There are two files for this lab, ``geovis`` and ``eda``. Since this geocomputational lab is not as straightforward as other python code, a **solution set** is also provided for questions indicated in the lab.

#### Data

This session uses multiple datasets which are provided in the zipped lab files above.

1. A **"Census socio-demographics"** dataset from the Municipality of the city of Cape Town from the Open Data Portal for the City of the Cape Town. [Source](https://odp-cctegis.opendata.arcgis.com/).
2. Shape files for the city of Cape Town from Media Monitoring Africa (MMA) which is an independent watchdog for ethical and fair journalism that upholds human rights. [Source](https://wazimap.co.za/profiles/municipality-CPT-city-of-cape-town/).
3. Simple datasets on ``heart diseases``, ``titanic`` and a ``mystery`` are also provided.

#### Extra Material

* A good introduction to the `geopandas` project is provided by Kelsey Jordahl, the project's founder in this [set of slides](http://kjordahl.github.io/SciPy-Tutorial-2015/#1) from a 2015 talk and the companion [repository](https://github.com/kjordahl/SciPy-Tutorial-2015).
* An additional great resource is this 4h. [workshop](https://github.com/carsonfarmer/python_geospatial) by Carson Farmer.


***

(lab-4)=
## Lab 4 - Networks and Spatial Weights

#### Resources

- **Download Materials:** [Lab 4 & Homework 4 Notebooks + Data (ZIP)](https://surfdrive.surf.nl/files/index.php/s/PD3aIcAr9DBcTMT/download)

#### Notebooks

- [Lab 4 - Part 1](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-04/lab-04-part-01.ipynb)
- [Lab 4 - Part 2](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-04/lab-04-part-02.ipynb)
- [Homework 4](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-04/hw-04.ipynb)

#### Data

This session uses multiple datasets which are all provided in the zipped lab files above.

This session uses multiple datasets which are provided in the zipped lab files above.

1. An **"Index of Multiple Deprivation""** dataset as well as the Ordnance Survey **(OS) Geodata Pack**.
Scores, ranks, and components of the 2015 Index of Multiple Deprivation (IMD).
**Source**: [CDRC](http://cdrc.ac.uk/)'s English Indices of Deprivation 2015 Geodata Pack for the city of Liverpool (UK).
2. Additionally, you will need the raster file for the basemap of Liverpool. This has been assembled by [Dani Arribas-Bel](http://darribas.org) from the [OS VectorMap District (Backdrop Raster)](https://www.ordnancesurvey.co.uk/business-and-government/products/vectormap-district.html), and it is licensed as OpenData.
3. A **Brexit** dataset.

The Brexit dataset is of the results of the 2016 referendum vote to leave the EU, at the local authority level. All the necessary data have been assembled for convenience in a single file that contains geographic information about each local authority in England, Wales and Scotland, as well as the vote attributes. The file is in the modern geospatial format [GeoPackage](http://www.geopackage.org/), which presents several advantages over the more traditional shapefile (chief among them, the need of a single file instead of several).

The source data used to compile the file linked above include:

- Electoral Commission data on the EU referendum results ([`url`](https://www.electoralcommission.org.uk/find-information-by-subject/elections-and-referendums/past-elections-and-referendums/eu-referendum/electorate-and-count-information))
- Local Authority District boundaries (archived, not available online anymore)


***

(lab-5)=
## Lab 5 - Linear Regression

#### Resources

- **Download Materials:** [Lab 5 & Homework 5 Notebooks + Data (ZIP)](https://surfdrive.surf.nl/files/index.php/s/tvNqOlvMw6q4a7A/download)

#### Notebooks

- [Lab 5 - Part 1](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-05/lab-05-part-01.ipynb)
- [Lab 5 - Part 2](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-05/lab-05-part-02.ipynb)
- [Homework 5](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-05/hw-05.ipynb)

Since this lab is not as straightforward as other python code, a **solution set** is provided for questions indicated in the lab and homework. It is better if you try yourself and get feedback from your peers, and then look at the solutions.

#### Data

This session uses multiple data files.

1. A dataset downloaded from Kaggle on stats about the premiere league.
2. A Boston housing dataset and its training set companion.
3. An IMDB cast dataset.
4. A car dataset.
5. A cab dataset.

These sets are not that relevant to global urban issues but simple to work with on small regression practice sets.


***

(lab-6)=
## Lab 6 - Clustering

#### Resources

- **Download Materials:** [Lab 6 & Homework 6 Notebooks + Data (ZIP)](https://surfdrive.surf.nl/files/index.php/s/QRxW7MgfT42F0KW/download)

#### Notebooks

- [Lab 6](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-06/lab-06_Rio.ipynb)
- [Homework 6](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-06/hw-06.ipynb)

#### Data

This session uses the **"AirBnb listing for Inner London - MSOA level"** dataset.

This dataset contains information for [AirBnb](https://www.airbnb.com) properties for the area of Inner London aggregated at the MSOA level. It has been prepared by Dani Arribas-Bel using as the original source the full listing of AirBnb locations for London provided by [Inside AirBnb](http://insideairbnb.com/). Same as the source, the dataset is released under a [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) License.

For every polygon, the following variables are provided:

* `id`: MSOA unique identifier.
* `accommodates`: average property capacity in the MSOA.
* `bathrooms`: average number of bathrooms in the properties within the MSOA.
* `bedrooms`: average number of bedrooms in the properties within the MSOA.
* `beds`: average number of beds in the properties within the MSOA.
* `number_of_reviews`: average number of reviews received by the properties within the MSOA.
* `reviews_per_month`: average number of reviews per month received by the properties within the MSOA.
* `review_scores_ratings`: average rating score received by the properties within the MSOA.
* `review_scores_accuracy`: average accuracy score received by the properties within the MSOA.
* `review_scores_cleanliness`: average cleanliness score received by the properties within the MSOA.
* `review_scores_checkin`: average checkin score received by the properties within the MSOA.
* `review_scores_communication`: average communication score received by the properties within the MSOA.
* `review_scores_location`: average location score received by the properties within the MSOA.
* `review_scores_value`: average value score received by the properties within the MSOA.
* `property_count`: total number of AirBnb properties listed withing the MSOA.

The lab also uses an additional file that contains the boundary lines of the London boroughs provided in the data folder as well.

#### Extra Material

* The documentation for [`scikit-learn`](http://scikit-learn.org), a world-class Python library for machine learning, is excellent and includes many examples that cover the entire functionality set of the library.

***

(lab-7)=
## Lab 7 - Points

#### Resources

- **Download Materials:** [Lab 7 & Homework 7 Notebooks + Data (ZIP)](https://surfdrive.surf.nl/files/index.php/s/9mJDjRSuIVd7HeL/download)

#### Notebooks

- [Lab 7](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-07/lab-07.ipynb)
- [Homework 7](https://github.com/EPA122A/epa122a-2024/blob/main/labs/lab-07/hw-07.ipynb)

#### Data

This lab uses a sample of geo-referenced locations of photographs taken in Tokyo.

#### Extra Material

* A very good resource for kernel density estimation in Python is provided in [this blog post](https://jakevdp.github.io/blog/2013/12/01/kernel-density-estimation/) by Jake Vanderplas.
