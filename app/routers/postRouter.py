from fastapi import APIRouter, Response
from database import db
from validators.postValidators import PostValidator
from models import Post

postRouter = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}}
)




@postRouter.post("/post")
def createPost(data: PostValidator):
    try:
        post = Post(title=data.title, content=data.content)
        db.save(post)
        return Response("Posted successfully", 200)
    except Exception as e:
        print(e)
        return Response("Please try again later...", 500)
    
@postRouter.put("/update-post/{title}")
def updatePost(title: str, data: PostValidator):
    updated_post, affected_rows =  db.update(Post, Post.title == title, {Post.content: data.content}) 
    if affected_rows < 1:
        return Response(f"There was a problem updating your post named {title}")
    else:
        return {
            "message": "Post updated",
            "data": updated_post 
        }

@postRouter.delete("/delete-post/{title}")
def deleteUser(title: str):
    deleted_post, affected_rows = db.delete(Post, Post.title == title)
    if affected_rows < 1:
        return Response(f"Something was wrong, please check the post named {title}")
    else:
        return {
            "message": "User deleted",
            "data": deleted_post
        }

@postRouter.put("/like-post/{title}")
def likePost(title: str):
    query = db.query(Post)
    post: Post = query.filter(Post.title == title).first()
    likes = post.likes
    if not likes:
        likes = 0

    likes += 1     

    updated_post, affected_rows =  db.update(Post, Post.title == title, {Post.likes: likes})
    if affected_rows < 1:
        return Response(f"There was a problem updating your post named {title}")
    else:
        return {
            "message": "Post updated",
            "data": updated_post 
        }