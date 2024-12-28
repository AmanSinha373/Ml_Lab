echo pipeline { > Jenkinsfile
echo     agent any >> Jenkinsfile
echo     stages { >> Jenkinsfile
echo         stage('Clone Repo') { >> Jenkinsfile
echo             steps { >> Jenkinsfile
echo                 git url: 'https://github.com/AmanSinha373/Ml_Lab.git', branch: 'main' >> Jenkinsfile
echo             } >> Jenkinsfile
echo         } >> Jenkinsfile
echo         stage('Build Docker Image') { >> Jenkinsfile
echo             steps { >> Jenkinsfile
echo                 script { >> Jenkinsfile
echo                     bat 'docker build -t ml_project .' >> Jenkinsfile
echo                 } >> Jenkinsfile
echo             } >> Jenkinsfile
echo         } >> Jenkinsfile
echo         stage('Run Docker Container') { >> Jenkinsfile
echo             steps { >> Jenkinsfile
echo                 script { >> Jenkinsfile
echo                     bat 'docker run -d --name ml_container ml_project' >> Jenkinsfile
echo                 } >> Jenkinsfile
echo             } >> Jenkinsfile
echo         } >> Jenkinsfile
echo         stage('Clean Up') { >> Jenkinsfile
echo             steps { >> Jenkinsfile
echo                 script { >> Jenkinsfile
echo                     bat 'docker rm -f ml_container' >> Jenkinsfile
echo                     bat 'docker rmi ml_project' >> Jenkinsfile
echo                 } >> Jenkinsfile
echo             } >> Jenkinsfile
echo         } >> Jenkinsfile
echo     } >> Jenkinsfile
echo     post { >> Jenkinsfile
echo         always { >> Jenkinsfile
echo             echo 'Cleaning up...' >> Jenkinsfile
echo         } >> Jenkinsfile
