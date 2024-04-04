import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here

        # ROW 1
        self._ddLanguage = ft.Dropdown(
            options=[
                ft.dropdown.Option("english"),
                ft.dropdown.Option("italian"),
                ft.dropdown.Option("spanish"),
            ],
            label="Select language",
            on_change=self.__controller.handleLanguage
        )

        # ROW 2
        self._ddModality = ft.Dropdown(
            options=[
                ft.dropdown.Option("Default"),
                ft.dropdown.Option("Linear"),
                ft.dropdown.Option("Dichotomic")
            ],
            width=200,
            label="Search modality",
            on_change=self.__controller.handleModality
        )
        self._tbText = ft.TextField(label="Add your sentence here", expand=True)
        self._btn = ft.ElevatedButton(text="Spell check", on_click=self.__controller.handleSpellCheck)
        row2 = ft.Row([self._ddModality, self._tbText, self._btn])

        # ROW 3
        self._lv = ft.ListView(expand=1, spacing=10, padding=20)

        self.page.add(self._ddLanguage, row2, self._lv)

        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
