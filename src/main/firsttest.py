# -*- coding: UTF-8 -*-

# Pygame-Modul importieren.
import pygame

from main.ship import Ship

if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')
if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')


def main():
    # Initialisieren aller Pygame-Module und    
    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.
    pygame.display.set_caption("Pygame-Tutorial: Grundlagen")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)

    # Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.
    clock = pygame.time.Clock()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    ship1 = Ship((400, 300))

    # Die Schleife, und damit unser Spiel, läuft solange running == True.
    running = True
    while running:
        # Framerate auf 30 Frames pro Sekunde beschränken.
        # Pygame wartet, falls das Programm schneller läuft.
        clock.tick(60)

        # screen-Surface mit Schwarz (RGB = 0, 0, 0) füllen.
        screen.fill((32, 32, 32))

        # Alle aufgelaufenen Events holen und abarbeiten.
        for event in pygame.event.get():
            # Spiel beenden, wenn wir ein QUIT-Event finden.
            if event.type == pygame.QUIT:
                running = False

            # Wir interessieren uns auch für "Taste gedrückt"-Events.
            if event.type == pygame.KEYDOWN:
                # Wenn Escape gedrückt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                elif event.key == pygame.K_RIGHT:
                    ship1.rotate(-10)
                elif event.key == pygame.K_LEFT:
                    ship1.rotate(10)

        #ship1.update()
        screen.blit(ship1.image, ship1.rect)

        # Inhalt von screen anzeigen.
        pygame.display.update()


# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__main__':
    # Unsere Main-Funktion aufrufen.
    main()
