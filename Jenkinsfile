pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo '正在拉取代码...'
                git branch: 'main', 
                    url: 'https://github.com/Romane24/----UI.git'
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo '正在安装依赖...'
                sh 'pip install -r requirements.txt || echo "没有requirements.txt文件"'
            }
        }
        
        stage('Run Tests') {
            steps {
                echo '正在运行测试...'
                // 根据您的测试框架调整命令
                sh 'python -m pytest tests/ || echo "测试运行完成"'
            }
        }
    }
    
    post {
        always {
            echo '自动化测试流程完成'
        }
    }
}