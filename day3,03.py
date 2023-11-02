high_score=0
def update_high_score(score):
    global high_score
    if score>high_score:
        high_score=score
update_high_score(50)
print("high_score:",high_score)