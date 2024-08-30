# Flask Web Application

## Project Description

This is a simple web application built using Flask. It demonstrates basic functionalities such as:

- Serving a homepage with a random number and the current year.
- Guessing the gender and age of a person based on their name using external APIs.
- Displaying blog posts fetched from an API.

## Features

1. **Homepage (`/`):**
   - Displays the current year and a random number between 1 and 10.
   - Renders `index.html` template with these values.

2. **Guess (`/guess/<name>`):**
   - Uses external APIs to guess the gender and age of a person based on the provided name.
   - `https://api.genderize.io/` for gender prediction.
   - `https://api.agify.io/` for age prediction.
   - Renders `gender.html` template with the guessed gender, age, and probability.

3. **Blog (`/blog/<num>`):**
   - Fetches blog posts from an API (`https://api.npoint.io/c790b4d5cab58020d391`).
   - Displays the fetched posts in the `blog.html` template.
   - Note: The route currently prints the `num` parameter but does not filter posts based on it. It will display all posts.

## Installation

1. **Clone the Repository:**

   ```sh
   git clone <repository-url>
