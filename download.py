from flask import Flask, redirect, render_template

app = Flask(__name__)

# File mapping with the GitHub URLs you provided
file_mapping = {
    '0000001': 'https://raw.githubusercontent.com/Learnhelp-cc/Wstuff/cce96fd3c1fea62bec2023c7d67c072c0f52f26e/hostedfiles/test.txt',
    '0000002': 'https://raw.githubusercontent.com/Learnhelp-cc/Wstuff/7f83c17e4966aaf772aee25e25a4437b6961bca1/P-Diddy%20with%20fur%20%23animation%20%23alvinandthechipmunks%20%23pdiddy%20%23diddy.mp3',
    '0000003': 'https://raw.githubusercontent.com/Learnhelp-cc/Wstuff/60f5a018ae3df6f4f487daf9571e0efcaed183b3/hostedfiles/oilup.html',
    '0000004': 'https://github.com/Learnhelp-cc/Wstuff/raw/refs/heads/main/hostedfiles/Eaglercraft_1.12_Offline_Download.zip',
}

@app.route('/<file_id>')
def download_file(file_id):
    github_url = file_mapping.get(file_id)
    if github_url:
        return redirect(github_url)
    else:
        return render_template('404.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
