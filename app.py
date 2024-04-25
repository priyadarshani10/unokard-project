from flask import Flask, render_template, request

app = Flask(__name__)

# University data
universities = [
    {
        "name": "Harvard University",
        "location": "Cambridge, MA",
        "gre_score": 320,
        "gmat_score": 700,
        "toefl_score": 100,
        "fee": "$50,000 per year",
        "opportunities": ["Research opportunities", "Internship programs"]
    },
    {
        "name": "Stanford University",
        "location": "Stanford, CA",
        "gre_score": 310,
        "gmat_score": 720,
        "toefl_score": 105,
        "fee": "$55,000 per year",
        "opportunities": ["Tech industry connections", "Start-up incubator programs"]
    },
    {
        "name": "University of Oxford",
        "location": "Oxford, UK",
        "gre_score": 325,
        "gmat_score": 680,
        "toefl_score": 95,
        "fee": "£25,000 per year",
        "opportunities": ["International study programs", "Networking events"]
    }
]

@app.route('/')
def index():
    return render_template('index.html', universities=universities)

@app.route('/submit_scores', methods=['POST'])
def submit_scores():
    gre_score = int(request.form['gre_score'])
    gmat_score = int(request.form['gmat_score'])
    toefl_score = int(request.form['toefl_score'])
    eligible_universities = []
    other_eligible_universities = []
    for uni in universities:
        if gre_score >= uni['gre_score'] and gmat_score >= uni['gmat_score'] and toefl_score >= uni['toefl_score']:
            eligible_universities.append(uni)
        else:
            other_eligible_universities.append(uni)
    return render_template('submission.html', gre_score=gre_score, gmat_score=gmat_score, toefl_score=toefl_score, eligible_universities=eligible_universities, other_eligible_universities=other_eligible_universities)

if __name__ == '__main__':
    app.run(debug=True)
