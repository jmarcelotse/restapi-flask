pipeline {
    agent {
        kubernetes {
            yamlFile 'jenkins-pod.yaml'
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

                        bandit -r . -x './venv/,./tests/' -ll || true
                        black .
                        pytest -v --disable-warnings
                    '''
                }
            }
            when {
                anyOf {
                    branch pattern: "feature-*"
                    branch pattern: "develop"
                    branch pattern: "hotfix-*"
                    branch pattern: "release-*"
                    branch pattern: "v"
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
