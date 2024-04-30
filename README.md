# Criando-desenhos-com-o-turtlesim

# Projeto TurtleDraw

Este projeto demonstra como controlar a tartaruga no ambiente `turtlesim` do ROS 2 para desenhar figuras geométricas. Utiliza serviços para criar e remover tartarugas e publica comandos de velocidade para controlar os movimentos da tartaruga.

## Pré-requisitos

Este projeto requer que o ROS 2 e o pacote `turtlesim` estejam instalados no seu sistema. As instruções assumem que você está usando o ROS 2 Foxy ou versões mais recentes.

## Instalação

Para instalar e configurar o projeto, siga estas etapas:

1. Clone o repositório para o seu workspace ROS 2:
   ```
   cd ~/your_ros_workspace/src
   git clone https://github.com/seu_usuario/turtle_draw.git
   ```
2. Construa o projeto usando colcon:
   ```
   cd ~/your_ros_workspace
   colcon build --packages-select turtle_draw
   source install/setup.bash
   ```

## Uso

Para usar o projeto, você precisa primeiro iniciar o turtlesim_node e depois executar o nó turtle_draw:

1. Inicie o turtlesim_node:
    ```
    Copy code
    ros2 run turtlesim turtlesim_node
    ```
2. Em um novo terminal, execute o nó turtle_draw para começar a desenhar:
   ```
   Copy code
   ros2 run turtle_draw draw
   ```
   
Este comando iniciará o processo de desenho no turtlesim, onde a tartaruga irá desenhar uma figura geométrica especificada no código.

## Demonstração
## Demonstração

Para uma demonstração completa do funcionamento do sistema, veja o vídeo neste link: [Vídeo Demonstrativo](https://drive.google.com/drive/u/0/folders/1Rm0VATMWQFxST1yjlcKmXPKAZ0auyAKW?q=type:video%20parent:1Rm0VATMWQFxST1yjlcKmXPKAZ0auyAKW%20sharedwith:public)
