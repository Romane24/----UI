pipeline {
    agent any
    
    stages {
        stage('Checkout via SSH') {
            steps {
                echo '🚀 使用SSH协议拉取代码...'
                retry(3) {
                    git branch: 'main',
                       url: 'git@github.com:Romane24/----UI.git',
                       credentialsId: 'github-ssh-key',
                       timeout: 10
                }
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo '✅ 设置测试环境...'
                sh '''
                    echo "安装依赖..."
                    pip install -r requirements.txt || echo "没有requirements.txt"
                    
                    echo "环境信息:"
                    python --version
                    pip --version
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                echo '✅ 运行自动化测试...'
                sh 'python -m pytest tests/ --html=report.html || true'
            }
            post {
                always {
                    publishHTML(target: [
                        allowMissing: true,
                        reportDir: '.',
                        reportFiles: 'report.html',
                        reportName: '测试报告'
                    ])
                }
            }
        }
    }
    
    post {
        always {
            echo '🎯 构建完成'
        }
    }
}