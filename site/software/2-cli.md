# Command-Line Installation

## A Minimalist Approach: Miniconda (Recommended for Long-Term Learning)

If you're looking for a more streamlined installation that includes only the essential components needed, the recommended approach is to install Miniconda. This will install a Python distribution natively along with the necessary libraries for this context.

To install Python and the required libraries, follow these steps:

1. Install Miniconda for your OS from the [official Miniconda page](https://docs.conda.io/en/latest/miniconda.html).

```{attention}
*To download Miniconda, follow these steps:*

1. Go to the [Download Page](https://docs.anaconda.com/miniconda/).
2. Choose the correct installer for your Windows version (32-bit or 64-bit).
3. Download the Miniconda installation file. Depending on your browser and setup, it will either download to a default location (e.g., Downloads) or prompt you to choose a location (Desktop is a good option).
```
---

### Setting Up a Virtual Environment

Once Miniconda is installed, we need to create an independent virtual environment that will isolate all the necessary functionalities.

But first, **what are environments, and why do you need them?**

Environments in Python function like isolated sandboxes that allow you to install different versions of Python and packages without affecting other projects. You can create, list, update, and remove environments easily, and switch between them by "activating" or "deactivating" as needed.

For this course, we will control the packages installed by creating an environment using a YAML file called [environment-gds24.yml](https://surfdrive.surf.nl/files/index.php/s/B3iEVHnRM4jRX8k/download).

> To learn more about virtual environments, visit [this page](environment.md).

### Creating an Environment from a `.yml` File

Open a terminal depending on your operating system:

- Windows: Open **Anaconda Command Prompt**
- macOS: Go to **Applications > Utilities > Terminal**
- Linux: Use **Ctrl + Alt + T** to open the terminal.

Next, follow these steps:

1. Download the [environment-gds24.yml file](https://surfdrive.surf.nl/files/index.php/s/B3iEVHnRM4jRX8k/download).
2. Navigate to the folder where the file is located (e.g., Downloads):

    ```bash
    cd /path/to/Downloads
    ```

3. Run the following command to create the environment (note that a stable internet connection is required, and it may take some time):

    ```bash
    conda env create -f environment-gds24.yml
    ```

```{tip}
Depending on your internet speed, this may take 15–20 minutes. Grab a *cuppa* and be patient!
```


### Activating and Verifying the Environment

Once the environment is created, you need to activate it:

```bash
conda activate gds24
```

You should now see the name of the environment (e.g., (gds24)) at the beginning of your command prompt.

To verify that the environment was set up correctly, list all installed packages:

    ```shell
    conda list
    ```

```{note}
This command will give you a list of the packages installed in this environment. For managing your environment or learning more about what environments are capable of, go to [Manage conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
```

### Launching Jupyter Lab

You can now start Jupyter Lab by running the following command:

    ```shell
    jupyter lab
    ```
