***What are runners?***
Runners are the amchines that executes jobs in github actions workflow.

There are 2 types of Runners:-

a) Github runners:- is a type pf vitual machine (VM) hosted by github with runner application with Ubuntu Linux, Windows or macOS operating system.

b) Self-hosted runners:- is a system that you deploy and manage to execute jobs from github actions on github.com


***Differences between GitHub-hosted and self-hosted runners***

GitHub-hosted runners offer a quicker, simpler way to run your workflows, while self-hosted runners are a highly configurable way to run workflows in your own custom environment.

GitHub-hosted runners:

Receive automatic updates for the operating system, preinstalled packages and tools, and the self-hosted runner application.
Are managed and maintained by GitHub.
Provide a clean instance for every job execution.
Use free minutes on your GitHub plan, with per-minute rates applied after surpassing the free minutes.

Self-hosted runners:

Receive automatic updates for the self-hosted runner application only, though you may disable automatic updates of the runner. For more information about controlling runner software updates on self-hosted runners, see Autoscaling with self-hosted runners. You are responsible for updating the operating system and all other software.
Can use cloud services or local machines that you already pay for.
Are customizable to your hardware, operating system, software, and security requirements.
Don't need to have a clean instance for every job execution.
Are free to use with GitHub Actions, but you are responsible for the cost of maintaining your runner machines.
