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
'''
        }
    }
    stages {
        stage('Unit tests') {
            steps {
                container('python') {
                    sh '''
                        pip install -r requirements.txt

                        bandit -r . -x './.venv/','./tests/'
                        black .
                        pytest -v --disable-warnings
                    '''
                }
            }
        }
    }
}
