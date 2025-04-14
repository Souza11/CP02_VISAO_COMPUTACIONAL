# CP02_VISAO_COMPUTACIONAL
Detector de Dígitos Vermelhos em RG
Este projeto consiste em um sistema de visão computacional que detecta e identifica dígitos vermelhos em documentos de identidade brasileiros (RG) usando a webcam. O sistema utiliza técnicas de segmentação de cor no espaço HSV para isolar os caracteres vermelhos do documento.

Sobre o Projeto
Documentos de identidade brasileiros (RG) geralmente possuem o número do documento impresso em tinta vermelha. Este programa captura imagens da webcam em tempo real, identifica os dígitos vermelhos através de segmentação de cor HSV e os destaca com retângulos verdes.

Funcionalidades
Captura de vídeo em tempo real da webcam
Detecção de cor vermelha usando segmentação HSV
Filtragem e identificação dos dígitos vermelhos
Visualização da máscara de detecção
Captura de imagem com tecla 'c' para análise detalhada
Requisitos
Python 3.6 ou superior
OpenCV (cv2)
NumPy
Matplotlib
Webcam funcionando
Instalação
Clone o repositório ou baixe o arquivo Python:
bash
git clone https://github.com/seu-usuario/detector-digitos-rg.git
cd detector-digitos-rg
Instale as dependências necessárias:
bash
pip install opencv-python numpy matplotlib
Como Usar
Execute o script Python:
bash
python segmentacao_rg_digitos_vermelhos.py
Posicione seu documento RG em frente à webcam.
Os dígitos vermelhos detectados serão destacados com retângulos verdes em tempo real.
Pressione a tecla 'c' para capturar a imagem atual e visualizar uma análise detalhada com:
Imagem original
Máscara de detecção vermelha
Imagem com os dígitos destacados
Pressione 'q' a qualquer momento para sair do programa.
Como Funciona
O sistema utiliza os seguintes passos para detectar os dígitos vermelhos:

Captura de imagem: Obtém frames da webcam em tempo real.
Conversão para HSV: Converte a imagem do espaço de cor BGR para HSV, que é mais adequado para segmentação de cores.
Segmentação de cor: Cria duas máscaras para capturar toda a gama de vermelhos (que no espaço HSV está dividida entre os extremos do círculo de matiz).
Operações morfológicas: Aplica dilatação e erosão para limpar ruídos e melhorar a detecção.
Detecção de contornos: Identifica os contornos externos nas regiões vermelhas detectadas.
Filtragem: Analisa os contornos detectados por tamanho e proporção para identificar apenas aqueles que provavelmente correspondem a dígitos.
Ajustes (Se Necessário)
Se a detecção não estiver funcionando corretamente, você pode ajustar os parâmetros HSV no código:

python
# Valores HSV fixos para detecção da cor vermelha
parametros_hsv = {
    'h_min1': 0, 's_min1': 50, 'v_min1': 50, 'h_max1': 15,
    'h_min2': 160, 's_min2': 50, 'v_min2': 50, 'h_max2': 179
}
Para tons vermelhos mais claros: Reduza os valores de s_min1, s_min2, v_min1 e v_min2
Para vermelho mais escuro: Aumente os valores de s_min1 e s_min2
Para ajustar a faixa de matiz: Modifique h_min1, h_max1, h_min2 e h_max2
Limitações
O sistema funciona melhor em condições de iluminação adequada e uniforme
Documentos com danos, reflexos ou iluminação muito baixa podem gerar falsos positivos ou negativos
A qualidade da webcam pode afetar significativamente os resultados
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.


