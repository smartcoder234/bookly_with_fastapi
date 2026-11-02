from pydantic import BaseModel, Field, EmailStr

# Model for incoming request data
# class UserCreateSchema(BaseModel):
#     username: str = Field(min_length=3, max_length=50)
#     email: EmailStr
#     password: str = Field(min_length=8)

# # Model for outgoing data
# class UserResponseSchema(BaseModel):
#     id: int
#     username: str
#     email: str
# # user created response
# class UserCreatedResponse(BaseModel):
#     message: str
#     user: UserResponseSchema

# # Model for a list of users
# class UserListResponse(BaseModel):
#     message: str
#     users: list[UserResponseSchema]

# # Model for udating user data
# class UpdateUserSchema(BaseModel):
#     username: str|None=None
#     email: str|None=None
#     password: str|None=None

# -----------------------------
# 1. Pydantic schemas
# -----------------------------

# Data required when creating a user
class UserCreateSchema(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: str
    password: str = Field(min_length=8)


# Data returned to clients
class UserResponseSchema(BaseModel):
    id: int
    username: str
    email: str


# Response returned after creating a user
class UserCreatedResponse(BaseModel):
    message: str
    user: UserResponseSchema


# Response returned when listing users
class UserListResponse(BaseModel):
    message: str
    users: list[UserResponseSchema]


# Fields that may be updated
class UpdateUserSchema(BaseModel):
    username: str | None = Field(default=None, min_length=3, max_length=50)
    email: str | None = None
    password: str | None = Field(default=None, min_length=8)

