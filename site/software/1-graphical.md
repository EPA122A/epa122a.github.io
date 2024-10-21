# Graphical Installation

## A graphical approach: `anaconda` installer (easiest to work with)

Follow the instructions on the [Anaconda](https://www.anaconda.com/products/distribution) website and install a distribution which contains Python 3.9. Once the software is installed, double click on it, and confirm that you have something called JupyterLab already installed within it. You are done!

- Once you have anaconda installed, we need to set up an independent virtual environment that isolates all the functionality we need.

```{important}
But first, **what are environments and do you need them?**
```

Environments in Python are like sandboxes that have different versions of Python and/or packages installed in them. You can create, export, list, remove, and update environments. Switching or moving between environments is called activating the environment. When you are done with an environment, you may deactivate it.

For this course, we want to have a bit more control on the packages that will be installed with the environment so we will create an environment with a so-called YAML file.

To learn more about virtual environments, you can also go [here](environment.md).

### Creating an environment from an environment.yml file

Get the `environment-gds24.yml` file from [here](https://surfdrive.surf.nl/files/index.php/s/B3iEVHnRM4jRX8k/download).

1. Open Anaconda Navigator.
2. Go to the Environments tab.
3. Click on the Import button.
4. Select your `environment-gds24.yml` file.
5. Follow the prompts to create the environment.


```{tip}
Depending on the speed of your connection, this step will take a while (but no less than 15-30 minutes). Grab a *cuppa* and be patient!
```

This has created the `gds24` environment, congratulations! We are _almost_ there. Now we need to _activate_ the environment. For this, just  select the right environment and open a jupyter lab notebook.
