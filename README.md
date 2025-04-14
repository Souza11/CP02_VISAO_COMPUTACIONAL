# 🔍 Detector de Dígitos Vermelhos em RG

Um detector simples que identifica dígitos vermelhos em documentos de RG brasileiro usando segmentação de cor HSV através da webcam.

![Demonstração](https://via.placeholder.com/800x400?text=Demo+Detecção+Dígitos+RG)

## 📋 Sobre

Este projeto usa visão computacional para detectar em tempo real os dígitos vermelhos presentes em documentos de identidade brasileiros. A técnica utilizada baseia-se na segmentação de cor no espaço HSV, permitindo isolar os caracteres de cor vermelha.

## ✨ Funcionalidades

- Detecção de dígitos vermelhos em tempo real
- Captura de imagem com a tecla 'c'
- Visualização da máscara de segmentação
- Análise detalhada da imagem capturada

## 🔧 Requisitos

- Python 3.6+
- OpenCV
- NumPy
- Matplotlib
- Webcam funcionando

## 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/detector-digitos-rg.git
cd detector-digitos-rg

# Instale as dependências
pip install opencv-python numpy matplotlib
```

## 🚀 Como usar

1. Execute o script:
   ```bash
   python segmentacao_rg_digitos_vermelhos.py
   ```

2. Posicione o RG em frente à webcam

3. Comandos:
   - `c`: Captura a imagem atual e mostra análise detalhada
   - `q`: Sai do programa

## 🔬 Como funciona

1. Captura frames da webcam
2. Converte a imagem para o espaço de cores HSV
3. Aplica duas máscaras para capturar toda a gama de vermelhos
4. Utiliza operações morfológicas para limpar ruídos
5. Detecta contornos nas regiões vermelhas
6. Filtra os contornos por tamanho e proporção para identificar dígitos

## ⚙️ Ajustes

Se precisar ajustar a detecção, modifique os parâmetros HSV no código:

```python
parametros_hsv = {
    'h_min1': 0, 's_min1': 50, 'v_min1': 50, 'h_max1': 15,
    'h_min2': 160, 's_min2': 50, 'v_min2': 50, 'h_max2': 179
}
```
