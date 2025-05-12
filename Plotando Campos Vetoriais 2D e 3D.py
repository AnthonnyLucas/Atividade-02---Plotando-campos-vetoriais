import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from mpl_toolkits.mplot3d import Axes3D

# --- Configurações iniciais ---
fig = plt.figure(figsize=(12, 7), facecolor='#1e1e1e')
plt.subplots_adjust(bottom=0.2)

ax2d = fig.add_subplot(121)
ax3d = fig.add_subplot(122, projection='3d')
ax3d.set_visible(False)

current_view = "2D"

# --- Estilização dos eixos ---
def estilizar_axes(ax):
    ax.set_facecolor('#1e1e1e')
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    if hasattr(ax, 'zaxis'):
        ax.zaxis.label.set_color('white')
        ax.zaxis.set_tick_params(colors='white')
    ax.title.set_color('white')
    ax.grid(True, color='gray', linestyle='--', alpha=0.4)

# --- Campo Vetorial 2D: F(x, y) = (y, sin(x)) ---
x2d, y2d = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))
u2d = y2d
v2d = np.sin(x2d)

# --- Campo Vetorial 3D: F(x, y, z) = (y/z, -x/z, z/4) ---
x3d, y3d, z3d = np.meshgrid(np.linspace(-2, 2, 6),
                            np.linspace(-2, 2, 6),
                            np.linspace(0.5, 4, 6))
u3d = y3d / z3d
v3d = -x3d / z3d
w3d = z3d / 4

# --- Configuração dos eixos ---
def configurar_eixos_2d():
    ax2d.clear()
    estilizar_axes(ax2d)
    ax2d.set_title('Campo Vetorial 2D: F(x,y) = (y, sen(x))')
    ax2d.set_xlabel('x')
    ax2d.set_ylabel('y')
    ax2d.set_xlim([-5, 5])
    ax2d.set_ylim([-5, 5])
    ax2d.quiver(x2d, y2d, u2d, v2d, color='cyan')
    fig.canvas.draw_idle()

def configurar_eixos_3d():
    ax3d.clear()
    estilizar_axes(ax3d)
    ax3d.set_title('Campo Vetorial 3D: F(x,y,z) = (y/z, -x/z, z/4)')
    ax3d.set_xlabel('x')
    ax3d.set_ylabel('y')
    ax3d.set_zlabel('z')
    ax3d.set_xlim([-2, 2])
    ax3d.set_ylim([-2, 2])
    ax3d.set_zlim([0, 5])
    ax3d.quiver(x3d, y3d, z3d, u3d, v3d, w3d, color='orange', length=0.2, normalize=True)
    fig.canvas.draw_idle()

# --- Botões e interações ---
def show_2d(event):
    global current_view
    current_view = "2D"
    ax3d.set_visible(False)
    ax2d.set_visible(True)
    configurar_eixos_2d()

def show_3d(event):
    global current_view
    current_view = "3D"
    ax2d.set_visible(False)
    ax3d.set_visible(True)
    configurar_eixos_3d()

# --- Widgets ---
ax_button_2d = plt.axes([0.1, 0.08, 0.2, 0.06], facecolor='#2e2e2e')
btn_2d = Button(ax_button_2d, 'Mostrar Campo 2D', color='#444', hovercolor='gray')
btn_2d.on_clicked(show_2d)

ax_button_3d = plt.axes([0.7, 0.08, 0.2, 0.06], facecolor='#2e2e2e')
btn_3d = Button(ax_button_3d, 'Mostrar Campo 3D', color='#444', hovercolor='gray')
btn_3d.on_clicked(show_3d)

# --- Início com campo 2D ---
configurar_eixos_2d()
plt.show()
