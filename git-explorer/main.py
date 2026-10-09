
import subprocess


def get_commits():
    result = subprocess.run(
        ["git", "log", "--format=%H|%an|%s"],
        capture_output=True,
        text=True
    )

    lines = result.stdout.strip().splitlines()
    commits = []

    for line in lines:
        parts = line.split("|", 2)

        commits.append({
            "hash": parts[0],
            "author": parts[1],
            "message": parts[2]
        })

    return commits


def get_branch():
    result = subprocess.run(
        ["git", "branch", "--show-current"],
        capture_output=True,
        text=True
    )

    return result.stdout.strip()


def create_commit_text(author, message):
    text = author + ": " + message
    return text


def main():
    print("=== GIT EXPLORER ===")

    branch = get_branch()
    print("Current branch:", branch)

    print("\n=== COMMIT HISTORY ===")

    commits = get_commits()

    for commit in commits:
        text = create_commit_text(
            commit["author"],
            commit["message"]
        )

        if "Merge" in commit["message"]:
            print("🔀 MERGE COMMIT:", text)
        else:
            print("📝 NORMAL COMMIT:", text)


main()
