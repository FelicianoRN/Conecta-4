# Conecta Cuatro

Este proyecto implementa el clásico juego **Conecta Cuatro**. Es un juego para dos personas que alternan turnos para colocar fichas en un tablero de 7x6.

## Requisitos

El juego cuenta con las siguientes características:

- **Tablero**: Dimensiones de 7 columnas (eje "x") por 6 filas (eje "y").
- **Fichas**: Dos tipos de fichas:
  - Rojas 🟥
  - Amarillas 🟨
- **Turnos**: 
  - La primera partida siempre la comienza la ficha Roja.
  - En las partidas siguientes, el turno inicial alterna (Amarilla en la segunda partida, Roja en la tercera, etc.).
- **Colocación de fichas**: 
  - Los jugadores seleccionan una columna, y la ficha cae hasta la posición más baja disponible.
- **Marcador**: 
  - Se guarda el número de partidas ganadas por cada equipo mientras la aplicación esté en ejecución.
- **Botones**:
  - **Reiniciar partida**: Permite reiniciar la partida en curso sin afectar al marcador.
  - **Resetear contador**: Restablece el marcador de victorias y derrotas.

## Funcionalidades Extra

Puedes añadir funcionalidades adicionales como:
- Indicador visual del jugador que tiene el turno actual.
- Animaciones al colocar fichas.
- Notificaciones al detectar un ganador o empate.

## Cómo jugar

1. Dos jugadores reales alternan turnos.
2. Selecciona una columna para colocar la ficha.
3. El objetivo es conectar cuatro fichas consecutivas en línea horizontal, vertical o diagonal.
4. ¡El primer jugador en lograrlo gana la partida!
