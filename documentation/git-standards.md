# Git standards

## Purpose
The purpose of this document is to establish a shared standard for git usage.
This will make any operations involving git easier and it will allow for greater version control.

## General workflow
1. Create issue
	1. Describe the problem to the best of your abilities.
	2. Tag the issue properly
	3. Assign the issue to the person you think it regards. If it's a major issue, talk to the person before assigning it.
	4. Message the person assigned to the issue
2. The assignee creates a branch associated with the issue.
3. The assignee is responsible for solving it. Either by him- or herself or in collaboration with other team members.
4. When the assignee considers the issue solved they create a merge request.
5. If the merge request is denied the assignee is responsible for fixing the problems and creating a new merge request. If it is accepted the issue can be marked as 'solved' and the branch can be removed.

## Commit standards
* Commits should generally be as atomic as possible. They should include as few changes (not changes as in lines of code, but addition of feaures) as possible. This makes it easy to add and remove features in case a commit needs to be revised. It also makes tracking changes easy.
* Never push a commit used for 'saving' or 'sharing' your work. Commits should be made often, but only when you have a finished unit of work. Not when you log off and realize that others might want to view your changes. 
* If you do find yourself in a situation where you forgot to commit for a long time, do split the commits up into units as well as you can.

### A few rules of thumb:
* Non-specific commits that could contain a header such as `Todays work`, `Update` or `njasdfsdfasdf` should be avoided.
* Commits should contain finished features. Commits such as `Started work on x` or `Continued work on y` should be avoided. Commiting drafts is however okay, since that is a piece of finished work.
* Commits containing ONE specific change (a unit) are good. Such commits could contain a header such as `Update readme for clarity`, `Remove unreachable code in file x` or `Add feature x to y`. 
* Use more rather than less commits.
* Try to avoid commands such as `git add -A` or `git add *` unless you are really sure that all changes in your working directory belongs to the next commit.

## Issues
Issues in this project should be the main way of communicating that something should be done. 

## Branching
All major features should be created on a separate branch to facilitate paralell development. Branches should generally be created from an existing issue and they should solve said issue. When a branch is verified to be working it should be merged into master.

The master branch is protected and should never be pushed directly to. This allows the developers to ensure that all features that get merged into master are tested and working. 

## Commit messages
This section will describe how commit messages should be written for readability and consistensy.

A good practise is to always write the messages using a text editor rather than using the command `git commit -m "Message goes here"`.
This promotes well written messages.

### Header
The commit message header should:
* Be short (preferably under 50 characters)
* Be descriptive.
* Not comment changes in code. Commands like `git diff` and just looking at the commit changes tells the user what changed. As a rule of thumb, comment what and why things have changed and not the specific changes in code.
* Be written in imperative mood. The commit header (and message) should be written as a command. eg. `Add x for usage in y` should be used instead of `Added x for usage in y`.
A good way to test this is to say: If applied, this commit will *your subject line here*
A good commit messages should always fit into that sentence.
* Start with a capital letter.
* Not contain a period.

Some examples of good and bad headings and why

`Refactor file x for better readability` 
Is a good commit message. It tells the user what the change is and why things changed. It's short and easy to read. The message is written in an imperative mood.

`replaced the if statement with a case statement` 
Is a bad commit message. It only tells the user things they could have concluded themselves by just looking at the diffs between versions. It tells us nothing about why the change occured and what differences it really made. The header is also not written in an imperative mood.

### Body
The message body should:
* Be separated from the header with a blank line.
* Be wrapped at 72 characters wide.
* Contain information that did not fit inside of the header.
* Like the header, the body should explain why and what, not how. Well written code is generally self explanatory (With the help of a few comments).

An example of how a full message could be formated.
> Refactor file x for better readability
> 
> This would contain more text about why the refactoring occured, what
> improvements it makes and more detailed information that did not fit
> inside of the header.

