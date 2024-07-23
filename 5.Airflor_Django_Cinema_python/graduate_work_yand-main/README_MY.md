# Final Project: Movie Converter and Yandex Alice Integration

The final project was completed in a group, which included another participant with a significantly higher proficiency in Python than mine. Therefore, I have uploaded my implementation to reflect my understanding of the material. 

## Project Description

The service downloads movies from the database, converts them to a smaller size, and writes them back to the database (into a new table). All of this is implemented using Airflow. Additionally, I have added functionality for Yandex Alice to search for information about movies/actors through Alice's text search.

### Issues and Workarounds

In my implementation of Alice, there is an unresolved issue: the functions for Alice are loaded and run through the cloud (instructions here: [YouTube Video](https://www.youtube.com/watch?v=-6Ik2DUWaqI&t=6s)), but access to the movie database API (1000+ movies) implemented with Click here is only possible through deploying the API service in Yandex Cloud or through Alice interacting with the API service on a local machine. I was unable to achieve either. However, to demonstrate Alice's capabilities, I added a test database, which is deployed within the functions in the cloud.

## Running the Converter

1. Rename the `env.example` files to remove the `.example` suffix.
2. In the `myconverter` folder:
    ```sh
    docker-compose build
    docker-compose up
    ```
3. After this, the Airflow management panel will be available at `http://127.0.0.1:8080/` where you can run the DAG by clicking the green play button. If Airflow asks for a login and password, use `admin` and `admin`.

## Demonstration of Alice

- Video demonstration: `docs/АЛИСА ДЕМО.mp4`
- Yandex Disk link: `ALICE DEMO`
