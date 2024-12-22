# Photography Website - Django Project

This is my first Django project: a photography-themed website. The website allows users to showcase their resume, display photos with descriptions, write blog posts, and access contact and about sections. It is a simple and functional platform designed to highlight creative work and connect with others.

### A demo of website

https://github.com/user-attachments/assets/2ce2e671-a0b4-46c6-ac60-b8d4680c2576

## Features

### 1. **Photography Showcase**
   - Upload and display your pictures.
   - Add descriptions to your photos to provide context or tell a story.

### 2. **Resume Section**
   - Present your professional resume and share details about your photography journey.

### 3. **Blog**
   - Write and publish blog posts.
   - Include images within your blog posts to enhance storytelling.

### 4. **About Section**
   - Share information about yourself or your photography business.

### 5. **Contact Section**
   - View the contact details.
   - Send emails or share ideas directly through the website.

## Installation

Follow these steps to set up and run the project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/` to view the website.

## Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS (and optionally JavaScript for enhanced interactivity)
- **Database:** SQLite (default for Django projects)

## How to Contribute

If you'd like to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- Thanks to Django for being a great framework for beginners and professionals.
- Inspired by the love of photography and the desire to learn web development.

