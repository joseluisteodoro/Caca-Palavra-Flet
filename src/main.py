import flet as ft
import requests

# def verificar_conexão():
#     endereco_API = "https://api.dicionario-aberto.net/"
#     return "conectado" if requests.get(endereco_API).status_code == 200 else "Desconectado"

# print(verificar_conexão())


def palavra_aleatoria():
    url = "https://api.dicionario-aberto.net/random"
    acentos = "áàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ"
    while True:
        resposta = requests.get(url)
        dados = resposta.json()
        palavra_API = dados.get("word")
        
        if not any(acento in acentos for acento in palavra_API):
            return palavra_API
            




def main(page: ft.Page):
    page.title = "Caça Palavras"
    page.theme_mode = ft.ThemeMode.DARK
    page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.PURPLE)

    if page.web == False:
        page.window.width = 400
        page.window.height = 600
        page.window.center()

  








    palavra_descobrir = ft.Text("",size=30)
    palavra_resultado = ""
    letras_digitadas = []
    letras_reveladas = []
    exibir_letras_digitadas = ft.Text(f"Letras digitadas: {', '.join(letras_digitadas)}")
    
    def clean_textfild_alerts():
        escreva.error_text = None
        escreva.helper_text = None
        escreva.helper_style = None




    def atualizar_palavra(e):
        nonlocal palavra_resultado, letras_reveladas
        buscar_palavra_aleatoria.text = "⏳ Buscando..."
        buscar_palavra_aleatoria.disabled = True
        page.update()

        nova_palavra = palavra_aleatoria() #Busca palavra na API
        palavra_resultado = nova_palavra
        letras_digitadas.clear()
        letras_reveladas = ["_" for _ in nova_palavra]


        #limpeza e foco no campo de texto
        clean_textfild_alerts()
        escreva.value = ""
        escreva.focus()
        
        exibir_letras_digitadas.value = f"Letras digitadas: {', '.join(letras_digitadas)}"
        oculta = "".join(["_" for _ in nova_palavra])
        palavra_descobrir.value = f"{oculta}"
 
        buscar_palavra_aleatoria.text = "🔄 Gerar palavra"
        buscar_palavra_aleatoria.disabled = False
        page.update()


    def tentativa(e):
        clean_textfild_alerts()
    
        letra = str(escreva.value)

        if len(letra) !=1 or not letra.isalpha():
            escreva.error_text = "⛔Digite somente letras!"
            
            

        elif letra in letras_digitadas:
            escreva.error_text = f"❌A letra {letra} já foi digitada"
            

        else:
            letras_digitadas.append(escreva.value)
            exibir_letras_digitadas.value = f"Letras digitadas: {', '.join(letras_digitadas)}"
            if letra in palavra_resultado.lower():
                escreva.helper_text = "✅Você acertou a letra"
                escreva.helper_style = ft.TextStyle(color=ft.Colors.GREEN, weight=ft.FontWeight.BOLD)
                for i, caractere in enumerate (palavra_resultado):
                    if caractere.lower() == letra:
                        letras_reveladas[i] = caractere
                        palavra_descobrir.value = " ".join(letras_reveladas)
                
                

            else:
                escreva.helper_text = f"❌A letra {letra} não está na palavra secreta"
                escreva.helper_style = ft.TextStyle(color=ft.Colors.RED, weight=ft.FontWeight.BOLD)
                
            
            
        
        escreva.value = ""
        escreva.focus()
        page.update()


    escreva = ft.TextField(label="Digite uma letra",max_length=1,on_submit=tentativa,width=300)
   

    buscar_palavra_aleatoria = ft.ElevatedButton("🔄 Gerar palavra",on_click=atualizar_palavra)

    

    page.add(ft.SafeArea(
        ft.Container(
        ft.Column(
            [
                buscar_palavra_aleatoria,
                escreva,
                exibir_letras_digitadas,
                palavra_descobrir
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),alignment=ft.alignment.center,expand=True)))




# ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER)