import flet as ft
import urllib.parse
from sorteadorApp import sortearTimes


def main(page: ft.Page):
    page.title = "Sorteador Fut"
    page.window.width = 450
    page.window.height = 750
    page.scroll = ft.ScrollMode.AUTO

    entrada = ft.TextField(
        label="Jogadores por nível",
        hint_text="João,Pedro,Carlos/Lucas,Rafael,Bruno/Felipe,Marcos,André",
        multiline=True,
        min_lines=8,
        max_lines=12,
        expand=True,
    )

    resultado = ft.Text(
        selectable=True,
        size=16,
    )

    def sortear(e):
        if entrada.value.strip() == "":
            resultado.value = "Digite os jogadores."
            page.update()
            return

        try:
            resultado.value = sortearTimes(entrada.value)
        except Exception as ex:
            resultado.value = f"Erro:\n{ex}"

        page.update()

    def compartilhar_whatsapp(e):
        if not resultado.value:
            return

        texto = urllib.parse.quote(resultado.value)

        page.launch_url(f"https://wa.me/?text={texto}")

    
    page.add(
        ft.Text(
            "⚽ Sorteador Fut Inimigos da Bola",
            size=24,
            weight=ft.FontWeight.BOLD,
        ),

        ft.Text(
            "Separe os níveis com / e os jogadores com vírgula."
        ),

        entrada,

        ft.Row(
            [
                ft.ElevatedButton(
                    "🎲 Sortear",
                    on_click=sortear,
                ),
                ft.ElevatedButton("📲 Compartilhar",
                                  icon=ft.Icons.SHARE,
                                  on_click=compartilhar_whatsapp,
                                  ),
            ]
        ),

        ft.Divider(),

        resultado,
    )


ft.app(target=main)
