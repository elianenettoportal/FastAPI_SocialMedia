'''
    Endpoint to create votes. The rules are defined /controlled here
    First find the post to vote, filter by post_id
    Second, find if the vote for that user exists
    if the vote is equal to 1 and the vote for the user exists just raise a message
    if vote equals 0 and the vote for the user DOES NOT exist just raise a message
    if vote is equal to 1 and the user did not vote yet just create a new vote
    if vote equals 0 and user voted just delete the vote

'''
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2


router = APIRouter(
    prefix="/vote",
    tags=['Vote'] # group name routers. In FastAPI docs you can see it grouped
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {vote.post_id} does not exist")

    vote_exits = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)

    found_vote = vote_exits.first()
    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {current_user.id} has alredy voted on post {vote.post_id}")
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist")

        vote_exits.delete(synchronize_session=False)
        db.commit()

        return {"message": "successfully deleted vote"}