from fastapi import APIRouter, HTTPException, status

from models.post import Comment, CommentIn, UserPost, UserPostIn, UserPostWithComments

router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Health check endpoint",
    description="This endpoint serves as a health check to ensure the API is up and running. It returns a simple 'Hello, world!' message.",
    response_description="Output: A JSON object containing a greeting message.",
    tags=["HEALTH CHECK"],
)
async def health():
    return {"message": "Hello, world!"}


post_table = {}
comment_table = {}


def find_post(post_id: int):
    return post_table.get(post_id)


@router.post(
    "/create_post",
    response_model=UserPost,
    status_code=status.HTTP_200_OK,
    summary="Create a new user post",
    description="This endpoint allows the creation of a new user post. It accepts the post data and returns the created post with an assigned ID.",
    response_description="Output: A JSON object containing the created post details.",
    tags=["POST API COLLECTION"],
)
async def create_post(post: UserPostIn):
    data = post.model_dump()
    last_record_id = len(post_table) + 1
    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post

    return new_post


@router.get(
    "/get_all_posts",
    response_model=list[UserPost],
    status_code=status.HTTP_200_OK,
    summary="Retrieve all user posts",
    description="This endpoint retrieves all the user posts available in the system.",
    response_description="Output: A JSON array containing all user posts.",
    tags=["POST API COLLECTION"],
)
async def get_all_posts():
    return list(post_table.values())


# Comment route
@router.post(
    "/comment",
    response_model=Comment,
    status_code=status.HTTP_200_OK,
    summary="Create a comment on a post",
    description="This endpoint allows the creation of a comment on a specified user post. It accepts the comment data and returns the created comment with an assigned ID.",
    response_description="Output: A JSON object containing the created comment details.",
    tags=["COMMENT API COLLECTION"],
)
async def create_comment(comment: CommentIn):
    post = find_post(comment.post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    data = comment.model_dump()
    last_record_id = len(comment_table) + 1
    new_comment = {**data, "id": last_record_id}
    comment_table[last_record_id] = new_comment

    return new_comment


@router.get(
    "/post/{post_id}/comments",
    response_model=list[Comment],
    status_code=status.HTTP_200_OK,
    summary="Retrieve comments on a post",
    description="This endpoint retrieves all comments associated with a specific user post.",
    response_description="Output: A JSON array containing all comments for the specified post.",
    tags=["COMMENT API COLLECTION"],
)
async def get_comments_on_post(post_id: int):
    return [
        comment for comment in comment_table.values() if comment["post_id"] == post_id
    ]


@router.get(
    "/post/{post_id}",
    response_model=UserPostWithComments,
    status_code=status.HTTP_200_OK,
    summary="Retrieve a post with comments",
    description="This endpoint retrieves a specific user post along with all its associated comments.",
    response_description="Output: A JSON object containing the post details and a list of associated comments.",
    tags=["COMMENT API COLLECTION"],
)
async def get_post_with_comments(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return {"post": post, "comments": await get_comments_on_post(post_id)}
