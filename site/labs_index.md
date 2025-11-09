---
updated: November 9, 2025
---

# 💻 Labs

```{admonition} Table of Contents! 👇🏽
:class: dropdown
1. [Lab 0: Tools](#lab-0)
2. [Lab 1: Tidy Data](#lab-1)
3. [Lab 2: Data Engineering](#lab-2)
4. [Lab 3: Geo-Visualisation](#lab-3)
```

***

(lab-0)=
## Lab 0 - Tools

#### Resources

- **Download Materials:** [Lab 0 & Homework 0 Notebooks + Data (ZIP)](https://surfdrive.surf.nl/files/index.php/s/qv637XJ3TiHHxWt/download)

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

#### Data

This session uses two datasets which are provided in the zipped lab files above.

1. A dataset about wines from different countries, download from **Kaggle**.
2. A dataset scraped and collected from **Goodreads**.


***

(lab-3)=
## Lab 3 - Geo-Visualisation

#### Resources

- **Download Materials:** [Lab 3 Notebooks + Data (ZIP)](https://surfdrive.surf.nl/files/index.php/s/JoKvDXxL6Hb15zD/download)

The homework exercises are embedded within the lab files itself. You have to complete the exercises as you go along understanding the rest of the code. There are two files for this lab, ``geovis`` and ``eda``. Since this geocomputational lab is not as straightforward as other python code, a **solution set** is also provided for questions indicated in the lab.

#### Data

This session uses multiple datasets which are provided in the zipped lab files above.

1. A **"Census socio-demographics"** dataset from the Municipality of the city of Cape Town from the Open Data Portal for the City of the Cape Town. [Source](https://odp-cctegis.opendata.arcgis.com/).
2. Shape files for the city of Cape Town from Media Monitoring Africa (MMA) which is an independent watchdog for ethical and fair journalism that upholds human rights. [Source](https://wazimap.co.za/profiles/municipality-CPT-city-of-cape-town/).
3. Simple datasets on ``heart diseases``, ``titanic`` and a ``mystery`` are also provided.

#### Extra Material

* A good introduction to the `geopandas` project is provided by Kelsey Jordahl, the project's founder in this [set of slides](http://kjordahl.github.io/SciPy-Tutorial-2015/#1) from a 2015 talk and the companion [repository](https://github.com/kjordahl/SciPy-Tutorial-2015).
* An additional great resource is this 4h. [workshop](https://github.com/carsonfarmer/python_geospatial) by Carson Farmer.
