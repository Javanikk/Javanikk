print("Select 1")
print("1.Español\n2.English\n3.Deutsch\n4.日本語\n5.Potuguês\n")
idioma = int(input())
# Se detecta el idioma

match idioma:
    case 1:
        print("¡Bienvenido a mi página!\n")
        print("Esta página sirve para mis proyectos públicos, por lo que aquí\nverás, probablemente, de todo un poco lo que te puedas imaginar")
    case 2:
        print("Welcome to my page!\n")
        print("This page is for my public projects, so here you'll probably see\na bit of everything you can imagine")
    case 3:
        print("Willkommen auf meiner Website!\n")
        print("Diese Seite ist für meine öffenlichten Projekte gedacht,\n also werden Sie hier wahrscheinlich ein bisschen von allem sehen, was Sie sich vorstellen können")
    case 4:
        print("僕のウエブサイトへようこそ！\n")
        print("このページは私の公開プロジェクトのためのものなので、おそらくここで、\nあなたが想像できるあらゆるものを少し見ることができるだろう")
    case 5:
        print("¡Bem-vindo na minha página!\n")
        print("Esta página é para meus projetos públicos, portanto, aqui você provavelmente verá\num pouco de tudo que possa imaginar")
    case _:
        print("ERROR: NON-VALID OPTION")

# El programa reacciona al número dado por el usuario

# Traducciones para alemán y japonés hechas gracias a DeepL
