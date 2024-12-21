import instaloader

def get_following_and_followers(username, password):
    """
    본계정의 팔로잉 및 팔로워 목록을 가져옵니다.
    """
    loader = instaloader.Instaloader()
    loader.login(username, password)

    profile = instaloader.Profile.from_username(loader.context, username)

    following = {follow.username for follow in profile.get_followees()}
    followers = {follower.username for follower in profile.get_followers()}
    
    return following, followers

if __name__ == "__main__":
    from login_ui import main_account  # 로그인 정보를 가져옴

    # 팔로잉 및 팔로워 목록 가져오기
    following, followers = get_following_and_followers(main_account["username"], main_account["password"])
    not_following_back = following - followers  # 나를 팔로우하지 않는 계정

    print(f"나를 팔로우하지 않는 계정: {not_following_back}")

    # 데이터 저장 (필요 시)
    with open("not_following_back.txt", "w") as f:
        f.writelines("\n".join(not_following_back))
