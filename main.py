# from fastapi import FastAPI, status, HTTPException
# from pydantic import BaseModel, Field, EmailStr
# from uuid import uuid4


# app = FastAPI(title="User Management API")

# @app.get('/')
# def read_root():
#     return {'hello': 'FastAPI World'}

# # Path Parameters
# @app.get('/greet/{username}')
# def greet(username:str|None=None):
#     return {'message': f'Hi, good day {username}'}

# # Query parameter:  In FastAPI, any parameter passed to a route handler, like search_for_user, and is not provided in the path as a path param is treated as a query parameter.
# @app.get('/search')
# def search(username:str):
#     users = ['Ezekiel', 'ade', 'John']
#     if username in users:
#         return {'msg': f'Username {username} was found'}
#     else:
#         return {'msg': f'User {username} not found'}

# # Optional parameter
# @app.get('/sayhi')
# async def sayhi(username:str|None =None):
#     if username:
#         return {'message': f'Hi, good day {username}'}
    
#     return {'message': f'Hi, good day guest'}

# # Request body: Create a new user
# @app.post('/users', response_model=UserCreatedResponse, status_code=status.HTTP_201_CREATED)
# def create_user(user_data: UserCreateSchema):
#     for user in users:
#         if user['username'] == user_data.username:
#             raise HTTPException(
#                 status_code = status.HTTP_409_CONFLICT,
#                 detail='Username already taken'
#             )

#         if user['email'] == user_data.email:
#             raise HTTPException(
#                 status_code = status.HTTP_409_CONFLICT,
#                 detail='Email already taken'
#             )
        
#     global next_id

#     new_user = {
#         'id': next_id,
#         'username': user_data.username,
#         'email': user_data.email,
#         'password': user_data.password
#     }

#     users.append(new_user)
#     next_id += 1

#     return {"message": "User Created successfully", "user": new_user}

    

# @app.get('/users', status_code=status.HTTP_200_OK, response_model=UserListResponse)
# def get_users():
#     if users:
#         return {
#             "message": f'{len(users)} total user(s) found', "users": users
#         }
#     else:
#         return {
#                 "message": f'{len(users)} total user(s) found', "users": []
#             }

# # get user by id
# @app.get('/users/{user_id}', response_model=UserResponseSchema,status_code=status.HTTP_200_OK)
# def get_user(user_id:int):
#     for user in users:
#         if user['id'] == user_id:
#             return user

#     raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User not found"
#         )

# # Update user by id
# @app.patch('/users/{user_id}', response_model=UserResponseSchema,status_code=status.HTTP_200_OK)
# def update_user(user_id:int, update_user_data : UpdateUserSchema):
#     # Convert to dictionary
#     update_data = update_user_data.model_dump(exclude_unset=True)
#     for user in users:
#         if user['id'] == user_id:

#             user['username'] = update_data.get('username', user['username'])
#             user['email'] = update_data.get('email', user['email'])
#             user['password'] = update_data.get('password', user['password'])

#             # user['username'] = update_user_data.username or user['username']
#             # user['email'] = update_user_data.email or user['email']
#             # user['password'] = update_user_data.password or user['password']
#             return user

#     raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User not found"
#         )

# # Delete user
# @app.delete('/users/{user_id}', status_code=status.HTTP_200_OK)
# def delete_user(user_id:int):
#     for user in users:
#         if user['id'] == user_id:
#             users.remove(user)
#             return {'message': 'User deleted successfully'}

#     raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User not found"
#         )