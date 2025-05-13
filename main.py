def fetch_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    result = run_query(query)
    return result
