pipeline {
    agent any

    stages {
        stage('Instalar dependências') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Executar testes') {
            steps {
                bat 'mkdir relatorios && pytest ./tests/test_login.py --html=relatorios/report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'relatorios/report.html', fingerprint: true
        }
    }
}
