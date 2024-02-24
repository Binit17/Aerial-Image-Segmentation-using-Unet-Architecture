1. **Clone the Project**: 

    ```bash
    git clone <project_url>
    ```

2. **Create a Virtual Environment**:

    ```bash
    python3 -m venv myenv
    ```

    This will create a virtual environment named `myenv`.

3. **Activate the Virtual Environment**:

    On Windows:
    ```bash
    myenv\Scripts\activate
    ```

    On Unix or MacOS:
    ```bash
    source myenv/bin/activate
    ```

4. **Install Dependencies from Pipfile**:

    ```bash
    pip install -r Pipfile
    ```

    This command will install all the packages listed in the `Pipfile` and its corresponding `Pipfile.lock`.

5. **Install Additional Packages**:

    ```bash
    python -m pip install Pillow
    pip install django-cors-headers
    ```

    These commands will install additional packages not listed in the `Pipfile`.
