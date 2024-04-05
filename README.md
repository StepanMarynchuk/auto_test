1. Чи була змога роботи з Paramiko, requests, якщо так - то що робив? Yes, I have experience with paramiko and requests.

Paramiko use cases: 
- Servers interaction (prepare client, in order to run commands and collect output from different servers)
- SFTP Client and Server: create a SFTP client for uploading/downloading files and to establish a SFTP server
- SSH key handling of RSA, DSS, ECDSA and Ed25519 SSH keys for creating secure SSH connections.

Requests use cases:
- Send all types of HTTP requests such as GET, POST, DELETE to REST based endpoints/web services

- Add and modify the default parameters in the URLs of GET requests

- Send custom headers with your HTTP requests

- Perform HTTP file uploads

- Use exception classes for managing HTTP related errors

- Make JSON response bodies parsing.

2. Чи використовували на проекті СІ, якщо так, як він був побудований? 
- Mostly it is integrated into CI/CD pipeline unit tests job and post-deployment functional tests job. In other cases, in Jenkins, it is separate downstream job with set of automated tests.

5. Які задачі робив з докер, чи піднімав тести/фреймворк проекту в докері?
- I have experience with creation docker image for test automation frameworks as pytest, Selenium (for amazonlinux)
- Almost all my test frameworks are dockerized.

4.	Які задачі виконував за допомогою написаних самостійно BASH скриптів?
- Performance tests support tools: Script for collected information about CPU, Memory/ Disk usage and GPU rendering, network on linux and android base OS.
- Automate backup for files
- Process text files
- Automated FTP/SFTP upload/download
- Use Bash scripting with cron jobs to execute tasks at specified times
- 
5. With using BDD framework on python, write an automated scenario and automate website (at least one feature file) and push you code in Docker image:
- Please check code base.

Instruction for Docker usage:
- Pre-condition: make sure docker is running in your environment.
- for build Dokcer: $ docker build -t scraping-behave-tests .

- for run docker: $ docker run scraping-behave-tests
