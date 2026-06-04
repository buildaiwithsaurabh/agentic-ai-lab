# ==========================================
# PATH PARAMETERS IN FASTAPI
# ==========================================

# Definition:
# Path Parameters are values passed directly inside the URL path.
#
# They are used to identify a specific resource.
#
# Example:
#
# /users/10
#
# Here:
# 10 is the Path Parameter.


from fastapi import FastAPI

app = FastAPI()


# Example 1: Single Path Parameter

@app.get("/users/{user_id}")
def get_user(user_id: int):

    return {
        "user_id": user_id
    }


# Test URL:
#
# http://127.0.0.1:8000/users/10
#
# Output:
#
# {
#     "user_id": 10
# }


# ==========================================
# MULTIPLE PATH PARAMETERS
# ==========================================

@app.get("/users/{user_id}/posts/{post_id}")
def get_post(user_id: int, post_id: int):

    return {
        "user_id": user_id,
        "post_id": post_id
    }


# Test URL:
#
# http://127.0.0.1:8000/users/5/posts/20
#
# Output:
#
# {
#     "user_id": 5,
#     "post_id": 20
# }


# Common Use Cases:
#
# /users/1
# /products/50
# /orders/100
# /posts/25
#
# Used when retrieving a specific item.