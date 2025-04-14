import cv2
import numpy as np
import matplotlib.pyplot as plt

def segmentar_RG():
    # Inicializar a webcam
    cap = cv2.VideoCapture(0)
    
    print("Webcam iniciada. Posicione o RG na frente da câmera.")
    print("Pressione 'c' para capturar imagem ou 'q' para sair.")
    
    # Valores HSV fixos para detecção da cor vermelha
    parametros_hsv = {
        'h_min1': 0, 's_min1': 50, 'v_min1': 50, 'h_max1': 15,
        'h_min2': 160, 's_min2': 50, 'v_min2': 50, 'h_max2': 179
    }
    
    while True:
        # Capturar frame da webcam
        ret, frame = cap.read()
        
        if not ret:
            print("Erro ao capturar frame da webcam!")
            break
        
        resultado_frame, mascara_vermelha = processar_frame(frame, parametros_hsv)
        
        # Mostrar resultados
        cv2.imshow('Webcam - Pressione c para capturar ou q para sair', resultado_frame)
        cv2.imshow('Máscara Vermelha', mascara_vermelha)
        
        # Detectar tecla pressionada
        key = cv2.waitKey(1) & 0xFF
        
        # Se 'q' for pressionado, sair do loop
        if key == ord('q'):
            break
        
        # Se 'c' for pressionado, capturar a imagem e processar
        if key == ord('c'):
            imagem = frame.copy()
            print("Imagem capturada! Processando...")
            
            # Processar imagem capturada
            processar_imagem_capturada(imagem, parametros_hsv)
    
    # Liberar recursos
    cap.release()
    cv2.destroyAllWindows()
    return None

def processar_frame(frame, parametros_hsv):
    """Processa um frame para visualização em tempo real"""
    # Converter para HSV
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Definir intervalos para a cor vermelha em HSV
    vermelho_baixo1 = np.array([parametros_hsv['h_min1'], parametros_hsv['s_min1'], parametros_hsv['v_min1']])
    vermelho_alto1 = np.array([parametros_hsv['h_max1'], 255, 255])
    
    vermelho_baixo2 = np.array([parametros_hsv['h_min2'], parametros_hsv['s_min2'], parametros_hsv['v_min2']])
    vermelho_alto2 = np.array([parametros_hsv['h_max2'], 255, 255])
    
    # Criar as máscaras
    mascara1 = cv2.inRange(frame_hsv, vermelho_baixo1, vermelho_alto1)
    mascara2 = cv2.inRange(frame_hsv, vermelho_baixo2, vermelho_alto2)
    
    # Combinar as máscaras
    mascara_vermelha = cv2.bitwise_or(mascara1, mascara2)
    
    # Aplicar operações morfológicas para limpar a máscara
    kernel = np.ones((5, 5), np.uint8)
    mascara_vermelha = cv2.morphologyEx(mascara_vermelha, cv2.MORPH_CLOSE, kernel)
    mascara_vermelha = cv2.dilate(mascara_vermelha, kernel, iterations=1)
    mascara_vermelha = cv2.erode(mascara_vermelha, np.ones((3, 3), np.uint8), iterations=1)
    
    # Encontrar contornos na máscara
    contornos, _ = cv2.findContours(mascara_vermelha, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Desenhar retângulos ao redor dos contornos detectados
    resultado_frame = frame.copy()
    contagem_digitos = 0
    
    for contorno in contornos:
        area = cv2.contourArea(contorno)
        if area > 30 and area < 5000:
            x, y, w, h = cv2.boundingRect(contorno)
            aspect_ratio = float(w) / h
            if 0.1 < aspect_ratio < 3.0:
                cv2.rectangle(resultado_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                contagem_digitos += 1
    
    # Mostrar informações na tela
    contornos_info = f"Dígitos detectados: {contagem_digitos}"
    cv2.putText(resultado_frame, contornos_info, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    return resultado_frame, mascara_vermelha

def processar_imagem_capturada(imagem, parametros_hsv):
    """Processa a imagem capturada para visualização estática"""
    # Converter para RGB para visualização
    imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    
    # Converter para HSV para segmentação
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    
    # Definir intervalos para a cor vermelha em HSV
    vermelho_baixo1 = np.array([parametros_hsv['h_min1'], parametros_hsv['s_min1'], parametros_hsv['v_min1']])
    vermelho_alto1 = np.array([parametros_hsv['h_max1'], 255, 255])
    
    vermelho_baixo2 = np.array([parametros_hsv['h_min2'], parametros_hsv['s_min2'], parametros_hsv['v_min2']])
    vermelho_alto2 = np.array([parametros_hsv['h_max2'], 255, 255])
    
    # Criar as máscaras
    mascara1 = cv2.inRange(imagem_hsv, vermelho_baixo1, vermelho_alto1)
    mascara2 = cv2.inRange(imagem_hsv, vermelho_baixo2, vermelho_alto2)
    
    # Combinar as máscaras
    mascara_vermelha = cv2.bitwise_or(mascara1, mascara2)
    
    # Aplicar operações morfológicas para limpar a máscara
    kernel = np.ones((5, 5), np.uint8)
    mascara_vermelha = cv2.morphologyEx(mascara_vermelha, cv2.MORPH_CLOSE, kernel)
    mascara_vermelha = cv2.dilate(mascara_vermelha, kernel, iterations=1)
    mascara_vermelha = cv2.erode(mascara_vermelha, np.ones((3, 3), np.uint8), iterations=1)
    
    # Encontrar contornos na máscara
    contornos, _ = cv2.findContours(mascara_vermelha, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Criar uma cópia da imagem original para desenhar os contornos
    imagem_contornos = imagem_rgb.copy()
    
    # Desenhar os contornos encontrados
    for contorno in contornos:
        area = cv2.contourArea(contorno)
        if area > 30 and area < 5000:
            x, y, w, h = cv2.boundingRect(contorno)
            aspect_ratio = float(w) / h
            if 0.1 < aspect_ratio < 3.0:
                cv2.rectangle(imagem_contornos, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Visualizar os resultados
    plt.figure(figsize=(15, 10))
    
    plt.subplot(2, 2, 1)
    plt.title("Imagem Original")
    plt.imshow(imagem_rgb)
    
    plt.subplot(2, 2, 2)
    plt.title("Máscara Vermelha")
    plt.imshow(mascara_vermelha, cmap='gray')
    
    plt.subplot(2, 2, 3)
    plt.title("Dígitos Detectados")
    plt.imshow(imagem_contornos)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    segmentar_RG()