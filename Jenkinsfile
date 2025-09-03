pipeline {
    agent {
        kubernetes {
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: python
    image: python:3.12-alpine
    command:
    - sleep
    args:
    - infinity
    securityContext:
      runAsUser: 1000
    env:
    - name: PIP_USER
      value: "1"
    - name: PATH
      value: "/home/jenkins/.local/bin:$PATH"
'''
        }
    }
    stages {
        stage('Setup') {
            steps {
                container('python') {
                    sh '''
                        pip install --user --upgrade pip
                        pip install --user -r requirements.txt
                        pip install --user setuptools
                    '''
                }
            }
        }
        
        stage('Unit Tests') {
            steps {
                container('python') {
                    sh '''
                        python -m pytest -v --disable-warnings
                    '''
                }
            }
        }
        
        stage('Security Analysis') {
            steps {
                container('python') {
                    sh '''
                        python -m bandit -r . -x './venv/,./tests/'
                    '''
                }
            }
        }
        
        stage('Code Formatting') {
            steps {
                container('python') {
                    sh '''
                        python -m black --check .
                    '''
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                container('python') {
                    sh '''
                        echo "Building Docker image..."
                        # Docker build seria executado aqui
                    '''
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed!'
        }
        success {
            echo 'All quality gates passed!'
        }
        failure {
            echo 'Pipeline failed - check quality gates'
        }
    }
}
