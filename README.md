<div id="readme-top">
  <h3 align="center"> ZoeziAI </h3>

  <p align="center">
    Get personalized fitness programs
    <br />
  </p>
  <p align="center">
    Completed: April 2022
    <br />
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

ZoeziAI is a system that provides users with a personalized fitness program based on criteria that they specify.
Admins can:
* add users
* add exercises and workout programs

Users can:
* enter personal information
* get personalized programs based on the info

### Built With

* Django
* SQLite


<!-- GETTING STARTED -->
## Getting Started

To get this app running on your machine, simply clone the repository and ensure the following prerequisites are all installed.

### Prerequisites

Have the following prerequisites:
* Python (version 3.9)
* Pip (latest version)
* Django (version 4.0.2)
* Bootstrap 4

### Installation

1. Clone the repository
   ```
   git clone https://github.com/GituMbugua/zoeziAI.git
   ```
2. Create a virtual environment

3. Install requirements
    ```
    (venv)$ pip install requirements.txt
    ```
4. Add your keys and secrets to a .env file
    ```
    DATABASE_NAME=<dbname>
    DATABASE_USER=<username>
    DATABASE_PASS=<password>
    EMAIL_HOST_USER=<email>
    EMAIL_HOST_PASSWORD=<email_password>
    ```
    
5. Run the server
    ```
    (venv)$ python manage.py runserver
    ```
   

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

Gitu Mbugua - gmbugua38@gmail.com

Project Link: [https://github.com/GituMbugua/zoeziAI](https://github.com/GituMbugua/zoeziAI)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
