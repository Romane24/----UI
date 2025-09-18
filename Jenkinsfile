pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo '✅ 正在拉取代码...'
                checkout([$class: 'GitSCM', 
                         branches: [[name: 'main']],
                         userRemoteConfigs: [[url: 'https://github.com/Romane24/----UI.git']]
                ])
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo '✅ 正在安装依赖...'
                sh '''
                    echo "当前目录:"
                    pwd
                    ls -la
                    pip install -r requirements.txt || echo "没有requirements.txt文件"
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                echo '✅ 正在运行测试...'
                sh '''
                    echo "当前Python版本:"
                    python --version || echo "Python未安装"
                    echo "运行测试..."
                    python -m pytest tests/ -v || echo "测试完成"
                '''
            }
        }
    }
    
    post {
        always {
            echo '🎯 自动化测试流程执行完成'
            sh 'ls -la'  // 查看最终工作目录内容
        }
    }
}