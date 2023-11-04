import praw

# Reddit API credentials (replace with your own)
reddit = praw.Reddit(
    client_id="Mrj3rzczYMmWZdjLBTbmTw",
    client_secret="wlj_pj1vXCJ88aDRu6UleOhH09sOOA",
    user_agent="TypoWeeb",
)

def search_reddit(question):
    try:
        # Search Reddit for the question
        results = reddit.subreddit("all").search(question, limit=1)
        
        for submission in results:
            # Print the title and URL of the top search result
            print("Title:", submission.title)
            print("URL:", submission.url)
            print()
            
            # Get the top-upvoted comment in the submission
            submission.comments.replace_more(limit=0)  # Ensure all comments are loaded
            top_comment = max(submission.comments, key=lambda x: x.score)
            
            # Print the top comment's content and score
            print("Top Comment ({} points):".format(top_comment.score))
            print(top_comment.body)
            return
        
        print("No results found on Reddit for your question.")
    
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    user_question = input("Enter a question to search on Reddit: ")
    search_reddit(user_question)