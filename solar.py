import pygame
import math
pygame.init()

WIDTH , HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH,  HEIGHT))
pygame.display.set_caption("Simulacion de sistema solar")

amarillo = (242,207,35)
marron = (75,29,6)
beige = (246,242,137)
azul = (10,120,233)
naranja = (245,51,12)
blanco = (255, 255, 255)
marron_claro = (241,163, 89)

fuente = pygame.font.SysFont("arial", 16)

class Planeta:
    AU = (149.6e6*1000)
    G = 6.67428e-11
    ESCALA = 75 / AU #1AU = 100px
    VEL = 18600 # 1 dia

    def __init__(self,x ,y, radio, color, masa):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.masa = masa

        self.orbita = []
        self.sol = False
        self.distancia_sol = 0

        self.x_vel = 0
        self.y_vel = 0
    
    def dibujo(self, win):
        x = self.x * self.ESCALA + WIDTH / 2
        y = self.y * self.ESCALA + HEIGHT /2

        if len(self.orbita) > 2:
            actualizar_pun = []
            for punto in self.orbita:
                x, y = punto
                x = x * self.ESCALA + WIDTH / 2
                y = y * self.ESCALA + WIDTH / 2
                actualizar_pun.append((x, y))
        
            pygame.draw.lines(win, self.color, False, actualizar_pun, 1)

        pygame.draw.circle(win, self.color, (x, y), self.radio)
        
        if not self.sol:
            texto_distancia = fuente.render(f"{round(self.distancia_sol/1000, 1)}km", 1, blanco)
            WIN.blit(texto_distancia, (x - texto_distancia.get_width()/2, y - texto_distancia.get_width()/2))
            
    def Fa(self, other):
        other_x, other_y = other.x, other.y
        distancia_x = other.x - self.x
        distancia_y = other.y - self.y
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)

        if other.sol:
            self.distancia_sol = distancia
        
        fuerza = self.G * self.masa * other.masa / distancia**2 
        tita = math.atan2(distancia_y, distancia_x)
        fuerza_x = fuerza * math.cos(tita)
        fuerza_y = fuerza * math.sin(tita)
        return fuerza_x, fuerza_y

    def actualizar_posicion(self, planetas):
        fx_total = fy_total = 0
        for planeta in planetas:
            if self == planeta:
                continue
            fx, fy = self.Fa(planeta)
            fx_total += fx
            fy_total += fy
        
        self.x_vel += fx_total / self.masa * self.VEL
        self.y_vel += fy_total / self.masa * self.VEL

        self.x += self.x_vel * self.VEL
        self.y += self.y_vel * self.VEL
        self.orbita.append((self.x, self.y))

def main():
    on = True
    reloj = pygame.time.Clock()

    sol = Planeta(0, 0, 10, amarillo, 1.98892 * 10**30)
    sol.sol = True

    mercurio = Planeta(-0.387 * Planeta.AU, 0, 2, marron, 0.33010 * 10**24)
    mercurio.y_vel = 47.4 * 1000

    venus = Planeta(-0.723 * Planeta.AU, 0, 5, beige, 4.8673 * 10**24)
    venus.y_vel = 35.02 * 1000

    tierra = Planeta(-1 * Planeta.AU, 0, 5, azul, 5.9722 * 10**24 )
    tierra.y_vel = 29.783 * 1000
    
    marte = Planeta(-1.524 * Planeta.AU, 0, 2.5, naranja, 0.64169 * 10**24)
    marte.y_vel = 24.1 * 1000

    jupiter = Planeta(-5.20 * Planeta.AU, 0, 8, marron_claro, 1898.13 * 10**24)
    jupiter.y_vel = 13.1*1000
    
    planetas = [sol, mercurio, venus, tierra, marte, jupiter]
    
    while on:
        reloj.tick(60)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
        
        for planeta in planetas:
            planeta.actualizar_posicion(planetas)
            planeta.dibujo(WIN)

        pygame.display.update()

    pygame.quit()

main()