pipeline {
    agent {
        kubernetes {
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: python
    image: python:3.9.12-alpine3.15
    command:
    - sleep
    args:
    - infinity
    securityContext:
      runAsUser: 1000
    env:
    - name: HOME
      value: "/tmp/jenkins"
    - name: PIP_USER
      value: "1"
'''
        }
    }
    stages {
        stage('Unit tests') {
            steps {
                container('python') {
                    sh '''
                        mkdir -p $HOME/.local/bin
                        export PATH="$HOME/.local/bin:$PATH"
                        
                        pip install --user --upgrade pip
                        pip install --user -r requirements.txt
                        pip install --user setuptools

                        bandit -r . -x './venv/,./tests/'
                        black .
                        pytest -v --disable-warnings
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
