pipeline {
    agent any

    environment {
        JIRA_CREDENTIALS = credentials('jira-qa-token') // ID da credencial que você adicionou
    }

    stages {
        stage('Instalar dependências') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Executar testes') {
            steps {
                bat 'pytest ./tests/test_login.py --html=relatorios/report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'relatorios/report.html', fingerprint: true
        }

        failure {
            script {
                echo "Notificando o Jira sobre falha..."

                bat """
                curl -X POST -u %JIRA_CREDENTIALS_USR%:%JIRA_CREDENTIALS_PSW% ^
                -H "Content-Type: application/json" ^
                --data "{
                    \\"fields\\": {
                        \\"project\\": { \\"key\\": \\"SCRUM\\" },
                        \\"summary\\": \\"Erro na pipeline Jenkins - Testes falharam\\",
                        \\"description\\": \\"Os testes automatizados falharam. Verificar o relatório anexado à build.\\",
                        \\"issuetype\\": { \\"name\\": \\"Bug\\" }
                    }
                }" ^
                https://machadomam10-1749597940310.atlassian.net/rest/api/2/issue/
                """
            }
        }
    }
}