import tkinter as tk
from tkinter import messagebox
import instaloader
import subprocess
import os

# 계정 정보를 저장할 딕셔너리
main_account = {"username": None, "password": None}
sub_account = {"username": None, "password": None}

not_following_back = []

def account_login(account_type):
    """
    본계정 또는 가계정의 로그인 정보를 입력받는 Tkinter UI
    """
    account = {"username": None, "password": None}

    def submit():
        account["username"] = username_var.get()
        account["password"] = password_var.get()

        if not account["username"] or not account["password"]:
            messagebox.showerror("오류", "모든 필드를 입력하세요.")
            return

        # 로그인 검증
        try:
            loader = instaloader.Instaloader()
            loader.login(account["username"], account["password"])
            messagebox.showinfo("성공", f"{account_type} 로그인 성공!")
            root.destroy()

            # 본계정 로그인 후 fetch_data.py 실행
            if account_type == "본계정":
                subprocess.run(["python3", "fetch_data.py"], check=True)
                load_not_following_back()  # 결과 로드
                display_not_following_ui()  # 체크박스 UI 표시

            # 가계정 로그인 후 migrate_follow.py 실행
            elif account_type == "가계정":
                subprocess.run(["python3", "migrate_follow.py"], check=True)

        except instaloader.exceptions.BadCredentialsException:
            messagebox.showerror("로그인 실패", "아이디 또는 비밀번호가 잘못되었습니다. 다시 시도하세요.")
        except instaloader.exceptions.ConnectionException:
            messagebox.showerror("연결 실패", "Instagram 서버에 연결할 수 없습니다. 인터넷 연결을 확인하세요.")
        except Exception as e:
            messagebox.showerror("오류", f"예기치 않은 오류가 발생했습니다: {str(e)}")

    root = tk.Tk()
    root.title(f"{account_type} 로그인")

    tk.Label(root, text=f"{account_type} 로그인", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

    # 사용자 ID 입력
    tk.Label(root, text="아이디:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    username_var = tk.StringVar()
    tk.Entry(root, textvariable=username_var).grid(row=1, column=1, padx=10, pady=5)

    # 비밀번호 입력
    tk.Label(root, text="비밀번호:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    password_var = tk.StringVar()
    tk.Entry(root, textvariable=password_var, show="*").grid(row=2, column=1, padx=10, pady=5)

    # 확인 버튼
    tk.Button(root, text="로그인", command=submit).grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()

    return account

def load_not_following_back():
    """not_following_back.txt 파일을 읽어 리스트에 저장."""
    global not_following_back
    if os.path.exists("not_following_back.txt"):
        with open("not_following_back.txt", "r") as file:
            not_following_back = [line.strip() for line in file.readlines()]

def display_not_following_ui():
    """not_following_back 리스트를 체크박스로 표시하는 UI."""
    selected_accounts = []

    def submit_selection():
        for var, account in zip(check_vars, not_following_back):
            if var.get():
                selected_accounts.append(account)
        root.destroy()
        save_selected_accounts(selected_accounts)
        subprocess.run(["python3", "migrate_follow.py"], check=True)  # 가계정으로 팔로우 실행

    root = tk.Tk()
    root.title("선택된 계정")

    tk.Label(root, text="나를 팔로우하지 않는 계정을 선택하세요:", font=("Arial", 12)).pack(pady=10)

    check_vars = []
    for account in not_following_back:
        var = tk.BooleanVar()
        tk.Checkbutton(root, text=account, variable=var).pack(anchor="w")
        check_vars.append(var)

    tk.Button(root, text="확인", command=submit_selection).pack(pady=10)
    root.mainloop()

def save_selected_accounts(selected_accounts):
    """선택된 계정을 별도 파일로 저장."""
    with open("selected_accounts.txt", "w") as file:
        file.writelines(f"{account}\n" for account in selected_accounts)

if __name__ == "__main__":
    print("본계정 로그인 시작")
    main_account = account_login("본계정")
    print(f"본계정 로그인 완료: {main_account}")

    print("가계정 로그인 시작")
    sub_account = account_login("가계정")
    print(f"가계정 로그인 완료: {sub_account}")
