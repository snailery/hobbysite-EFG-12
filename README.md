## Some Quick Links
* [Django Documentation](https://docs.djangoproject.com/en/5.1/)
* [Final Project Specs](https://docs.google.com/document/d/1fdo4qsts2FMcZatLKYAP0l6aarfT3h_XZyYdUccRU8I/edit?tab=t.0)
* [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [Template Documentation](https://preview.keenthemes.com/html/metronic/docs/index)

## New Changes!
> [!IMPORTANT]
> Since the `master` branch has been renamed to `midterm`, it needs to be updated locally. Please run the following commands:
>```
git branch -m master midterm
git fetch origin
git branch -u origin/midterm midterm
git remote set-head origin -a
git checkout [name]/[app]
git branch -d master
```

* The previous default branch `master` has been changed to `midterm`. This branch serves as our archive for the project at the time of midterm submission (just in case of emergencies).
    * The new default branch is `final/dev`.
    * This branch is the *development* branch and has been locked.
    * To make any changes to this branch, please submit a **pull request**!
* The production branch to be used for deployment is `final/prod`.
    * This should be directly connected (eventually) to DigitalOcean once our project is ready to deploy.
    * It is also locked and requires a pull request.
* The workflow would be as follows: 
`[name]/[app]` &rarr; `final/dev` &rarr; `final/prod`.

## Some Group Conventions
Please work in your branches. 
* Use `git status` to check which branch you are on.
* Use `git checkout [yourname]/[yourapp]` to switch to the correct branch.

Pull before push!
* Use `git pull` to update your local branch!
* Use `git pull origin final/dev` to bring your branch up-to-date with master.
* Use `git push origin [yourname]/[yourapp]` only after staging and committing all changes.

Commits must be atomic.
* Means you have to commit after small changes, don't commit all at once.
* Use `git add .` to stage all changes or `git add file1.py file2.py` to stage only specific files.
* Use `git commit -m [your message]` to write your commit message.

#### NEVER PUSH TO MASTER!!
* Master now refers the branches `final/prod` and `final/dev`.
    * These are now locked anyways.
* Always make sure you're doing `git push origin [yourname]/[yourapp]` to push to your branch instead of master.
* If you want to merge, submit a pull request instead!
    * if there's ever any conflicts, let's arrange a group meeting to discuss it :^)
