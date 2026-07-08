import flet as ft
import urllib.parse

from sorteadorApp import sortearTimes


def main(page: ft.Page):
    page.title = "Sorteador Fut"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    titulo = ft.Text(
        "⚽ Sorteador Fut Inimigos da Bola",
        size=28,
        weight=ft.FontWeight.BOLD,
    )

    descricao = ft.Text(
        "Digite os jogadores separados por vírgula e os níveis separados por '/'."
    )

    entrada = ft.TextField(
        label="Jogadores",
        multiline=True,
        min_lines=8,
        max_lines=10,
        expand=True,
        border_radius=12,
        hint_text="João,Pedro,Carlos/Lucas,Rafael,Bruno/Felipe,Marcos,André",
    )

    resultado = ft.Text(
        selectable=True,
        size=16,
    )

    def sortear(e):
        if not entrada.value.strip():
            resultado.value = "Digite os jogadores."
            page.update()
            return

        try:
            resultado.value = sortearTimes(entrada.value)
        except Exception as ex:
            resultado.value = str(ex)

        page.update()

    def compartilhar(e):
        if not resultado.value:
            return

        texto = urllib.parse.quote(resultado.value)

        page.launch_url(
            f"https://wa.me/?text={texto}"
        )

    page.add(
        titulo,
        descricao,
        entrada,
        ft.Row(
            [
                ft.ElevatedButton(
                    "🎲 Sortear",
                    icon=ft.Icons.CASINO,
                    on_click=sortear,
                ),
                ft.ElevatedButton(
                    "📲 Compartilhar",
                    icon=ft.Icons.SHARE,
                    on_click=compartilhar,
                ),
            ]
        ),
        ft.Divider(),
        resultado,
    )


ft.app(main)
