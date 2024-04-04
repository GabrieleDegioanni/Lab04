import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleLanguage(self, e):
        self._view._lv.controls.append(ft.Text(f"Language changed to {self._view._ddLanguage.value}", color="green"))
        self._view.page.update()
        return

    def handleModality(self, e):
        self._view._lv.controls.append(ft.Text(f"Modality changed to {self._view._ddModality.value}", color="green"))
        self._view.page.update()
        return

    def handleSpellCheck(self, e):

        language = self._view._ddLanguage.value
        modality = self._view._ddModality.value
        if language is None:
            self._view._lv.controls.append(ft.Text("Language must be selected!", color="red"))
            self._view.page.update()
            return
        if modality is None:
            self._view._lv.controls.append(ft.Text("Modality must be selected!", color="red"))
            self._view.page.update()
            return

        txtIn = self._view._tbText.value
        txtOut, time = self.handleSentence(txtIn, language, modality)
        self._view._lv.controls.append(ft.Text(f"Sentence: {self._view._tbText.value}"))
        self._view._lv.controls.append(ft.Text(f"Uncorrect words: {txtOut}"))
        self._view._lv.controls.append(ft.Text(f"Time: {time}"))
        self._view._tbText.value = ""
        self._view.page.update()



    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn)

        words = txtIn.lower().split()
        paroleErrate = ""

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text