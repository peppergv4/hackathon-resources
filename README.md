# Hackathon Resources

## Useful Links

- [Sign up to Mayhem!](https://mayhem.forallsecure.com/)

- [Mayhem Documentation](https://mayhem.forallsecure.com/docs/)

- [Mayhem Tutorials](https://mayhem.forallsecure.com/docs/tutorial/choose-your-path/)

- [Mayhem Community](https://community.forallsecure.com/)

- [Discord Invite](https://discord.gg/KhSGZnrEpp)

## Exercises

1. [lighttpd exercise](lighttpd-example.md)
2. [Docker + Mayhem Exercise](docker-intro.md)
3. [CMake Exercise](cmake-exercise.md)
4. [libFuzzer Exercise](libfuzzer-exercise.md)
5. [Mayhem GitHub Action Exercise](gh-actions.md)

## Mayhem Heroes Workflow

1. Select a repository for integration.

    See the target requirements for more information on what qualifies for integration.

2. Create a fork of the repo you want to integrate. (Please make sure you create a fork of the _mayhemheroes_ repo, NOT the upstream!)

3. Add additional harnessing or improve existing harnesses on the fork. You'll want to integrate your changes and ensure a successful action run _before_ submitting.

4. Submit [this form](https://dydbdnwi0qu.typeform.com/to/YYJdU5wd).

5. Once ForAllSecure validates your target and elligiblity, you'll be asked to submit a pull request to the repository under github.com/mayhemheroes. If requested during the review, make changes.

6. Once your changes have been approved and merged, you'll be eligible for **up to $1000 for new integrations and $5000 for existing integrations!**

## Target Checklist

Looking for a target to start working with? Start here!

* Repos eligible for improvement have already been forked under github.com/mayhemheroes

* You **must** add new harnessing or improve existing harnessing to these repositories

* Submissions will be graded on increased testsuite size, improved speed, added code coverage and defects found

If in doubt, ask in Discord or on the Mayhem Community.

_ForAllSecure reserves the right to reject any submission at its sole discretion._

## Troubleshooting Checklist

There are several small configuration steps that you'll need to take on your repo in order to properly integrate a repo with Mayhem. They are easy to miss, so here is a list for your reference:

* Package has public visibility.

* Repo has been linked and has read+write access to the package.

You can check the reply to [this community post](https://community.forallsecure.com/t/error-buildx-call-failed-with-error-denied-installation-not-allowed-to-write-organization-package/354/3) for more troubleshooting tips.

## Other Resources

## Resources

* [Linux CLI Reference](assets/Linux_Useful_Commands.pdf)
* [Linux CLI for Beginners](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)
