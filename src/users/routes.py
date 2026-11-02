from fastapi import APIRouter, status, HTTPException
from src.users.schemas import UserCreatedResponse, UserListResponse, UpdateUserSchema, UserResponseSchema, UserCreateSchema

user_router = APIRouter()

# Temporary in-memory storage
users = []
next_id = 1

@user_router.post(
    "/users",
    response_model=UserCreatedResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(user_data: UserCreateSchema):
    global next_id

    # Prevent duplicate usernames and emails
    for user in users:
        if user["username"].casefold() == user_data.username.casefold():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username already exists"
            )

        if user["email"].casefold() == user_data.email.casefold():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists"
            )

    new_user = {
        "id": next_id,
        "username": user_data.username,
        "email": user_data.email,
        "password": user_data.password
    }

    users.append(new_user)
    next_id += 1

    return {
        "message": "User created successfully",
        "user": new_user
    }


# -----------------------------
# 5. READ: Get all users
# -----------------------------

@user_router.get(
    "/users",
    response_model=UserListResponse,
    status_code=status.HTTP_200_OK
)
def get_users():
    return {
        "message": f"{len(users)} total user(s) found",
        "users": users
    }

# READ: Get one user by ID
@user_router.get(
    "/users/{user_id}",
    response_model=UserResponseSchema,
    status_code=status.HTTP_200_OK
)
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

# UPDATE: Partially update a user
@user_router.patch(
    "/users/{user_id}",
    response_model=UserResponseSchema,
    status_code=status.HTTP_200_OK
)
def update_user(user_id: int, update_user_data: UpdateUserSchema):
    # Only include supplied fields; ignore explicit null values
    update_data = update_user_data.model_dump(
        exclude_unset=True,
        exclude_none=True
    )

    for user in users:
        if user["id"] == user_id:

            # Check uniqueness before changing username or email
            for other_user in users:
                if other_user["id"] == user_id:
                    continue

                if (
                    "username" in update_data
                    and other_user["username"].casefold()
                    == update_data["username"].casefold()
                ):
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT,
                        detail="Username already exists"
                    )

                if (
                    "email" in update_data
                    and other_user["email"].casefold()
                    == update_data["email"].casefold()
                ):
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT,
                        detail="Email already exists"
                    )

            # Apply only the fields supplied
            user.update(update_data)

            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )


#DELETE: Remove a user
@user_router.delete(
    "/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return None

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )
