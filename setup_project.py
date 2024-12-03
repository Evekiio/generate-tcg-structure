import os

# Define the root directory of the project
project_root = 'dimensions-tcg'

# List of directories to create
directories = [
    os.path.join(project_root, 'data'),
    os.path.join(project_root, 'sessions'),
    os.path.join(project_root, 'public'),
    os.path.join(project_root, 'public', 'styles'),
    os.path.join(project_root, 'public', 'scripts'),
    os.path.join(project_root, 'public', 'assets'),
    os.path.join(project_root, 'public', 'assets', 'images'),
    os.path.join(project_root, 'public', 'assets', 'sounds'),
    os.path.join(project_root, 'public', 'assets', 'cards'),
]

# Dictionary of files to create with optional initial content
files = {
    os.path.join(project_root, 'server.go'): '// Go server code will go here',
    os.path.join(project_root, 'data', 'users.json'): '[]',
    os.path.join(project_root, 'data', 'cards.json'): '[]',
    os.path.join(project_root, 'data', 'messages.json'): '[]',
    os.path.join(project_root, 'public', 'index.html'): '<!-- index.html -->',
    os.path.join(project_root, 'public', 'login.html'): '<!-- login.html -->',
    os.path.join(project_root, 'public', 'register.html'): '<!-- register.html -->',
    os.path.join(project_root, 'public', 'game.html'): '<!-- game.html -->',
    os.path.join(project_root, 'public', 'inbox.html'): '<!-- inbox.html -->',
    os.path.join(project_root, 'public', 'styles', 'main.css'): '/* main.css */',
    os.path.join(project_root, 'public', 'scripts', 'main.js'): '// main.js',
    os.path.join(project_root, 'public', 'scripts', 'login.js'): '// login.js',
    os.path.join(project_root, 'public', 'scripts', 'register.js'): '// register.js',
    os.path.join(project_root, 'public', 'scripts', 'game.js'): '// game.js',
    os.path.join(project_root, 'public', 'scripts', 'inbox.js'): '// inbox.js',
}

# Create the directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)
    print(f'Created directory: {directory}')

# Create the files with initial content
for filepath, content in files.items():
    with open(filepath, 'w') as file:
        file.write(content)
    print(f'Created file: {filepath}')

print('\nProject folder structure has been generated successfully.')
