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
                bat 'pytest ./tests/test_login.py --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'relatorios/report.html', fingerprint: true
        }
    }
}
