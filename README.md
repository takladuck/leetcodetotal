# LeetCode Tracker API

A simple Flask API to fetch total solved questions count from LeetCode profiles. Built for tracking progress with my friends using Excel spreadsheets.

## Features

- Fetch total solved questions count for any LeetCode username
- Deployed on Render for reliable hosting

## API Endpoint

### Get LeetCode Stats

```
GET /api/leetcode/<username>
```

**Parameters:**
- `username` (string): LeetCode username

**Response:**
```json
{
  "username": "example_user",
  "totalSolved": 157
}
```

**Error Response:**
```json
{
  "error": "API error"
}
```


## Deployment on Render

This API is configured to deploy on Render with the following setup:

1. **Environment**: Python 3
2. **Build Command**: `pip install -r requirements.txt`
3. **Start Command**: `python app.py`
4. **Port**: Automatically detected from `PORT` environment variable


## How It Works

The API uses LeetCode's GraphQL endpoint to fetch user statistics:

1. Sends a GraphQL query to `https://leetcode.com/graphql`
2. Retrieves the `acSubmissionNum` data for the user
3. Filters for the "All" difficulty level to get total solved count
4. Returns a clean JSON response with username and total solved questions


## Disclaimer

This API uses LeetCode's public GraphQL endpoint. Please be respectful of their service and avoid excessive requests.
