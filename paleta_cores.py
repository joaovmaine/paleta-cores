import tkinter as tk  # Importa o módulo tkinter para criar interfaces gráficas
from tkinter import colorchooser, font  # Importa funções adicionais de tkinter para escolher cores e configurar fontes
import pyperclip  # Importa a biblioteca pyperclip para copiar textos para a área de transferência
import os  # Importa o módulo os para manipulação de caminhos de arquivos

class ColorPaletteApp:
    def __init__(self, root):
        self.root = root  # Define a janela principal
        self.root.title("Paleta de Cores")  # Define o título da janela
        self.root.geometry("600x500")  # Define o tamanho inicial da janela
        self.root.resizable(True, True)  # Permite que a janela seja redimensionada

        # Define o caminho do ícone
        icon_path = os.path.join(os.path.dirname(__file__), 'favicon.ico')
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)  # Define o ícone da janela e da barra de tarefas
        else:
            print("Ícone não encontrado:", icon_path)

        # Define os temas com diferentes cores
        self.themes = {
            "claro": {
                "bg": "#F5F5F5",  # Cor de fundo da janela para o tema claro
                "button_bg": "#009688",  # Cor de fundo dos botões para o tema claro
                "button_fg": "#FFFFFF",  # Cor do texto dos botões para o tema claro
                "button_hover_bg": "#00796B",  # Cor de fundo dos botões ao passar o mouse para o tema claro
                "label_bg": "#E0E0E0",  # Cor de fundo dos rótulos para o tema claro
                "label_fg": "#333333",  # Cor do texto dos rótulos para o tema claro
                "status_fg": "#009688",  # Cor do texto de status para o tema claro
            },
            "escuro": {
                "bg": "#2E2E2E",  # Cor de fundo da janela para o tema escuro
                "button_bg": "#FF9800",  # Cor de fundo dos botões para o tema escuro
                "button_fg": "#FFFFFF",  # Cor do texto dos botões para o tema escuro
                "button_hover_bg": "#F57C00",  # Cor de fundo dos botões ao passar o mouse para o tema escuro
                "label_bg": "#424242",  # Cor de fundo dos rótulos para o tema escuro
                "label_fg": "#E0E0E0",  # Cor do texto dos rótulos para o tema escuro
                "status_fg": "#FF9800",  # Cor do texto de status para o tema escuro
            }
        }
        
        self.current_theme = "claro"  # Define o tema inicial como claro
        self.color_code = None  # Inicializa a variável para armazenar o código da cor escolhida

        self.custom_font = font.Font(family="Arial", size=12)  # Define uma fonte personalizada

        self.create_widgets()  # Cria os componentes da interface gráfica
        
        # Aplica o tema atual após a criação dos widgets
        self.apply_theme()

    def apply_theme(self):
        """Aplica as cores do tema atual a todos os widgets."""
        theme = self.themes[self.current_theme]
        self.root.configure(bg=theme["bg"])  # Aplica a cor de fundo da janela
        # Aplica as cores aos botões
        self.choose_button.configure(bg=theme["button_bg"], fg=theme["button_fg"])
        self.copy_button.configure(bg=theme["button_bg"], fg=theme["button_fg"])
        self.clear_button.configure(bg=theme["button_bg"], fg=theme["button_fg"])
        # Mantém o fundo do rótulo de cor branco independentemente do tema
        self.color_display.configure(bg="white")
        # Aplica as cores aos rótulos de código hexadecimal e status
        self.code_label.configure(bg=theme["label_bg"], fg=theme["label_fg"])
        self.status_label.configure(fg=theme["status_fg"])

        # Aplica o tema aos botões com hover
        self.apply_button_theme(self.choose_button)
        self.apply_button_theme(self.copy_button)
        self.apply_button_theme(self.clear_button)
        self.apply_button_theme(self.theme_button)

    def create_widgets(self):
        """Cria todos os widgets da interface gráfica e os organiza na janela."""
        # Cria um frame principal para os widgets
        main_frame = tk.Frame(self.root, bg=self.themes[self.current_theme]["bg"])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Botão para escolher uma cor
        self.choose_button = tk.Button(main_frame, text="Escolher Cor", command=self.show_color,
                                       font=self.custom_font, padx=10, pady=5, relief="raised")
        self.choose_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        # Botão para copiar o código hexadecimal da cor escolhida
        self.copy_button = tk.Button(main_frame, text="Copiar Código", command=self.copy_to_clipboard,
                                     font=self.custom_font, padx=10, pady=5, relief="raised")
        self.copy_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Rótulo para exibir a cor escolhida
        self.color_display = tk.Label(main_frame, text="Cor", width=30, height=10, bg="white", relief="solid", borderwidth=2)
        self.color_display.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        
        # Rótulo para exibir o código hexadecimal da cor
        self.code_label = tk.Label(main_frame, text="Cor: #ffffff", font=self.custom_font)
        self.code_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")
        
        # Rótulo de status para mensagens de feedback ao usuário
        self.status_label = tk.Label(main_frame, text="", font=self.custom_font)
        self.status_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        # Botão para limpar a cor escolhida
        self.clear_button = tk.Button(main_frame, text="Limpar", command=self.clear_color,
                                      font=self.custom_font, padx=10, pady=5, relief="raised")
        self.clear_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # Botão para trocar o tema
        self.theme_button = tk.Button(main_frame, text="Trocar Tema", command=self.toggle_theme,
                                      font=self.custom_font, padx=10, pady=5, relief="raised")
        self.theme_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # Ajusta a grid para expandir corretamente
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

    def apply_button_theme(self, button):
        """Aplica as cores de fundo e texto do tema atual aos botões, e configura eventos de hover."""
        theme = self.themes[self.current_theme]
        button.configure(bg=theme["button_bg"], fg=theme["button_fg"])
        button.bind("<Enter>", self.on_hover)  # Evento quando o cursor passa sobre o botão
        button.bind("<Leave>", self.on_hover_leave)  # Evento quando o cursor sai do botão

    def on_hover(self, event):
        """Muda a cor de fundo do botão quando o cursor passa sobre ele."""
        widget = event.widget
        theme = self.themes[self.current_theme]
        widget.configure(bg=theme["button_hover_bg"])

    def on_hover_leave(self, event):
        """Restaura a cor de fundo original do botão quando o cursor sai."""
        widget = event.widget
        self.apply_button_theme(widget)  # Reaplica o tema ao botão

    def show_color(self):
        """Abre uma caixa de diálogo para escolher uma cor e atualiza a interface com a cor escolhida."""
        color = colorchooser.askcolor()  # Abre o seletor de cores
        self.color_code = color[1] if color else None  # Armazena o código hexadecimal da cor
        
        if self.color_code:
            self.color_display.config(bg=self.color_code)  # Atualiza a cor de fundo do rótulo de cor
            self.code_label.config(text=f"Cor: {self.color_code}")  # Atualiza o texto com o código da cor
            self.status_label.config(text="Cor escolhida.")  # Mensagem de status
        else:
            self.status_label.config(text="Nenhuma cor escolhida.")  # Mensagem de status

    def copy_to_clipboard(self):
        """Copia o código hexadecimal da cor escolhida para a área de transferência."""
        if self.color_code:
            pyperclip.copy(self.color_code)  # Copia o código da cor
            self.status_label.config(text="Código copiado para a área de transferência!")  # Mensagem de status
        else:
            self.status_label.config(text="Nenhuma cor para copiar.")  # Mensagem de status
    
    def clear_color(self):
        """Limpa a cor escolhida e redefine os rótulos para o estado inicial."""
        self.color_display.config(bg="white")  # Mantém o fundo do rótulo de cor branco
        self.code_label.config(text="Cor: #ffffff")  # Redefine o texto do código da cor
        self.color_code = None  # Limpa o código da cor
        self.status_label.config(text="Cor limpa.")  # Mensagem de status

    def toggle_theme(self):
        """Alterna entre o tema claro e escuro."""
        self.current_theme = "escuro" if self.current_theme == "claro" else "claro"  # Alterna o tema
        self.apply_theme()  # Aplica o novo tema

if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal
    app = ColorPaletteApp(root)  # Cria uma instância da aplicação
    root.mainloop()  # Inicia o loop principal da interface gráfica
