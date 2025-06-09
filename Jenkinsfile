pipeline {
    agent any

    stages {
        stage('Instalar dependências') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Executar testes') {
            steps {
                sh 'pytest ./tests/test_login.py --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}
