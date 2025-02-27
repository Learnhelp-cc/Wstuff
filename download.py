from flask import Flask, redirect

app = Flask(__name__)

# File mapping with the GitHub URL you provided
file_mapping = {
    '0000001': 'https://raw.githubusercontent.com/Learnhelp-cc/Wstuff/cce96fd3c1fea62bec2023c7d67c072c0f52f26e/hostedfiles/test.txt',
    # Add more mappings as needed
}

@app.route('/<file_id>')
def download_file(file_id):
    github_url = file_mapping.get(file_id)
    if github_url:
        return redirect(github_url)
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)
