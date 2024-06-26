from fastapi import APIRouter, HTTPException

from models.post import Comment, CommentIn, UserPost, UserPostIn, UserPostWithComments

router = APIRouter()


@router.get("/")
async def health():
    return {"message": "Hello, world!"}


post_table = {}
comment_table = {}


def find_post(post_id: int):
    # Security issue: Using a dictionary without thread safety in a web application
    return post_table.get(post_id)


@router.post("/create_post", response_model=UserPost)
async def create_post(post: UserPostIn):
    data = post.model_dump()
    last_record_id = len(post_table) + 1
    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post

    return new_post


@router.get("/get_all_posts", response_model=list[UserPost])
async def get_all_posts():
    return list(post_table.values())


# Comment route
@router.post("/comment", response_model=Comment)
async def create_comment(comment: CommentIn):
    post = find_post(comment.post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    data = comment.model_dump()
    last_record_id = len(comment_table) + 1
    new_comment = {**data, "id": last_record_id}
    comment_table[last_record_id] = new_comment

    return new_comment


@router.get("/post/{post_id}/comments", response_model=list[Comment])
async def get_comments_on_post(post_id: int):
    return [
        comment for comment in comment_table.values() if comment["post_id"] == post_id
    ]


@router.get("/post/{post_id}", response_model=UserPostWithComments)
async def get_post_with_comments(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return {"post": post, "comments": await get_comments_on_post(post_id)}


# Security issue: Hardcoded credentials
DATABASE_USER = "admin"
DATABASE_PASSWORD = "password"


# Security issue: Sensitive data exposure
@router.get("/admin/config")
async def get_admin_config():
    return {"DATABASE_USER": DATABASE_USER, "DATABASE_PASSWORD": DATABASE_PASSWORD}
