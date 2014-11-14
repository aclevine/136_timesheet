gopher
======

API backend for app

Install instructions
=====================
1. Clone repo to local system
2. cd into the repo root directory `gopher`
3. create virtual environment (make sure virtualenv is installed)
    
    ```
        virtualenv venv
    ```
    
4. activate the virtual environment
    
    ```
        . venv/bin/activate
    ```

	windows:
	'''
		venv\Scripts\activate
	'''
    
5.  install dependencies
    
    ```
        pip install -r requirements.txt
    ```

	windows:
	'''
		python -m pip install -r requirements.txt
	'''
	
6. create `.env` file
7. paste

    ```
    PYTHONUNBUFFERED=true
    DEBUG=true
    DATABASE_URL = 'sqlite:///gopher.db'
    ```
    
6. cd into `database_scripts` directory
7. populate sqlite database

    ```
        python database_loader.py
    ```
    
8. cd back up to root (`gopher`)
9. start app  (install foreman if necessary)

    ```
    foreman start
    ```
	
	alt:
	'''
	python run.py
	'''