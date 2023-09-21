# Function to calculate similarity between two users based on their interests
def calculate_similarity(user, other_user):
    common_interests = set(user['interests']).intersection(set(other_user['interests']))
    similarity = sum(user['interests'][interest] * other_user['interests'][interest] for interest in common_interests)
    return similarity

# Function to get top N friends based on interests
def get_top_friends(users, user_id, top_n=5):
    target_user = None
    for user in users:
        if user['id'] == user_id:
            target_user = user
            break

    if target_user is None:
        return f"User with id {user_id} not found."

    similarities = {}
    for user in users:
        if user['id'] != user_id:
            similarities[user['name']] = calculate_similarity(target_user, user)

    top_friends = sorted(similarities, key=similarities.get, reverse=True)[:top_n]
    
    return top_friends

# Function to get online users

