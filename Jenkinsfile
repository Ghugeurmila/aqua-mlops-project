pipeline {
    agent any
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Infra (Terraform)') { steps { sh 'echo "Applying Terraform..." ' } }
        stage('Config (Ansible)') { steps { sh 'echo "Running Ansible..." ' } }
        stage('Build Docker') { steps { sh 'docker build -t water-backend ./backend' } }
        stage('Test (Selenium)') { steps { sh 'python3 tests/selenium_test.py' } }
        stage('Deploy (K8s)') { steps { sh 'kubectl apply -f k8s/deployment.yaml' } }
    }
    post { always { sh './scripts/check_aqua.sh' } }
}
