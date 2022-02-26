from googletrans import Translator

t = Translator()

out = t.translate("stomach", dest = "hi", src = "en")
print(out.text)