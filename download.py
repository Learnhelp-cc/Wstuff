from flask import Flask, redirect

app = Flask(__name__)

# Replace these URLs with the actual raw GitHub URLs of your files
file_mapping = {
    '0000001': 'https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY/main/test.txt',
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
