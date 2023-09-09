from flask import Flask, request, jsonify
import datetime
import pytz
import os

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    current_day = datetime.datetime.now(pytz.utc).strftime('%A')
    current_time_utc = datetime.datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    github_url_file = "https://github.com/JesusBoi007/Zuri-Internship/blob/main/app.py"
    github_repo_url = "https://github.com/JesusBoi007/Zuri-Internship"

    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'current_utc_time': current_time_utc,
        'track': track,
        'github_url_file': github_url_file,
        'github_repo_url': github_repo_url,
        'status_code': 200
    }

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
