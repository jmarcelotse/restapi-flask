# Flask App - CI/CD com GitHub + Jenkins

## 📋 Descrição
Aplicação Flask de exemplo para testar pipeline CI/CD completo usando:
- **GitHub** como repositório
- **Jenkins** para CI/CD
- **Harbor** como registry
- **SonarQube** para análise de código
- **ArgoCD** para GitOps

## 🚀 Pipeline Stages

### 1. 🔍 Checkout
- Baixa código do GitHub
- Mostra informações do commit

### 2. 🔨 Build
- Instala dependências Python
- Prepara aplicação para deploy

### 3. 🧪 Test
- Executa testes unitários
- Gera relatório de cobertura

### 4. 🐳 Docker Build
- Constrói imagem Docker
- Prepara para push no Harbor

### 5. 📊 Quality Check
- Análise SonarQube
- Verifica quality gates

### 6. 🚀 Deploy
- Deploy automático via ArgoCD
- Atualiza ambiente

## 🔧 Como Testar

### Teste Manual:
```bash
# Executar aplicação
python app.py

# Executar testes
pytest test_app.py -v
```

### Teste Pipeline:
1. Faça commit neste repositório
2. Webhook dispara Jenkins automaticamente
3. Acompanhe execução em: http://jenkins.localhost.com

## 📊 URLs de Acesso

- **Jenkins:** http://jenkins.localhost.com
- **Harbor:** http://harbor.localhost.com  
- **SonarQube:** http://sonarqube.localhost.com
- **ArgoCD:** http://argocd.localhost.com

## 📈 Status do Último Build

- **Build:** #${BUILD_NUMBER}
- **Status:** ✅ SUCCESS
- **Data:** $(date)
- **Branch:** main

## 🔍 Endpoints da API

- `GET /` - Informações principais
- `GET /health` - Health check
- `GET /info` - Detalhes da aplicação

## 🏗️ Estrutura do Projeto

```
app/
├── app.py              # Aplicação Flask principal
├── test_app.py         # Testes unitários
├── Jenkinsfile         # Pipeline CI/CD
├── Dockerfile          # Container da aplicação
├── requirements.txt    # Dependências Python
└── README.md          # Esta documentação
```

---
**Última atualização:** $(date)  
**Versão:** 1.0.0
