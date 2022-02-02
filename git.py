# import git
import time
import subprocess


iter = 0
while 1:
    iter += 1

    with open("test.txt", 'a') as the_file:
        first = str(iter) + "\n"
        the_file.write(first)

    # repo = git.Repo('/Nlarseny/git_test')
    # repo.git.add('--all')  # to add all the working files.
    # repo.git.commit('-m', 'commit message from python script', author='test_user@test.com')
    # origin = repo.remote(name='origin')
    # origin.push()

    print(subprocess.run(["ls", "-l"]))
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "test"])
    subprocess.run(["git", "push"])


    time.sleep(5)