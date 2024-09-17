from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template for the portfolio website
template = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>My Portfolio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background: #333;
            color: #fff;
            padding: 10px 0;
            text-align: center;
        }
        .container {
            width: 80%;
            margin: 0 auto;
        }
        .section {
            padding: 20px;
            margin: 10px 0;
            background: #fff;
            border-radius: 5px;
        }
        h2 {
            border-bottom: 2px solid #333;
            padding-bottom: 10px;
        }
        footer {
            background: #333;
            color: #fff;
            text-align: center;
            padding: 10px 0;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>My Portfolio</h1>
    </header>
    <div class="container">
        <div class="section">
            <h2>About Me</h2>
            <p>Hello! I'm a web developer with a passion for creating beautiful and functional websites. I have experience with various web technologies and enjoy working on challenging projects.</p>
        </div>
        <div class="section">
            <h2>Projects</h2>
            <ul>
                <li>Project 1: A web application for tracking tasks.</li>
                <li>Project 2: A personal blog built with Flask.</li>
                <li>Project 3: An e-commerce site with Django.</li>
            </ul>
        </div>
        <div class="section">
            <h2>Contact</h2>
            <p>You can reach me via email at <a href="mailto:example@example.com">example@example.com</a>.</p>
        </div>
    </div>
    <footer>
        <p>&copy; 2024 My Portfolio</p>
    </footer>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)
