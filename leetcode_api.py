from flask import Flask, jsonify
import requests
import re
import os
from flask_cors import *

app = Flask(__name__)
CORS(app)

@app.route('/api/leetcode/<username>')
def get_leetcode_stats(username):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/{username}/",
        "User-Agent": "Mozilla/5.0"
    }

    query = {
        "query": """
        query getUserProfile($username: String!) {
          matchedUser(username: $username) {
            username
            submitStatsGlobal {
              acSubmissionNum {
                difficulty
                count
                submissions
              }
            }
          }
        }
        """,
        "variables": {
            "username": username
        }
    }

    try:
        response = requests.post(url, json=query, headers=headers)
        if response.status_code != 200:
            return jsonify({"error": "API error"}), response.status_code

        data = response.json()
        stats = data.get("data", {}).get("matchedUser", {}).get("submitStatsGlobal", {}).get("acSubmissionNum", [])
        total = next((item["count"] for item in stats if item["difficulty"] == "All"), 0)

        return jsonify({
            "username": username,
            "totalSolved": total
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's PORT or default to 5000
    app.run(host='0.0.0.0', port=port)