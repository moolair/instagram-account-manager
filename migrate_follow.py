import instaloader

def follow_accounts(username, password, accounts_to_follow):
    """
    선택된 계정을 가계정으로 팔로우합니다.
    """
    loader = instaloader.Instaloader()
    loader.login(username, password)

    for user in accounts_to_follow:
        try:
            profile = instaloader.Profile.from_username(loader.context, user)
            profile.follow()
            print(f"Followed {user}")
        except Exception as e:
            print(f"Failed to follow {user}: {e}")

if __name__ == "__main__":
    from login_ui import sub_account
    from fetch_data import not_following_back

    # 팔로우할 계정 필터링
    selected_accounts = list(not_following_back)  # 여기서 모든 계정을 선택했다고 가정

    # 가계정으로 팔로우 실행
    follow_accounts(sub_account["username"], sub_account["password"], selected_accounts)
