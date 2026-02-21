# ==============================
# QUIZ: QUAL POKÉMON VOCÊ É?
# ==============================

print("🔥 Bem-vindo ao Quiz Pokémon! 🔥")
print("Responda com A, B, C ou D\n")

pontos_fogo = 0
pontos_agua = 0
pontos_planta = 0
pontos_eletrico = 0

# ------------------------------
# PERGUNTA 1
# ------------------------------
print("1) Você se considera:")
print("A) Calmo")
print("B) Agressivo")
print("C) Inteligente")
print("D) Alegre")

resposta = input("Resposta: ").upper()

if resposta == "A":
    pontos_agua += 1
elif resposta == "B":
    pontos_fogo += 1
elif resposta == "C":
    pontos_planta += 1
elif resposta == "D":
    pontos_eletrico += 1


# ------------------------------
# PERGUNTA 2
# ------------------------------
print("\n2) Qual elemento você prefere?")
print("A) Fogo")
print("B) Água")
print("C) Planta")
print("D) Elétrico")

resposta = input("Resposta: ").upper()

if resposta == "A":
    pontos_fogo += 1
elif resposta == "B":
    pontos_agua += 1
elif resposta == "C":
    pontos_planta += 1
elif resposta == "D":
    pontos_eletrico += 1


# ------------------------------
# PERGUNTA 3
# ------------------------------
print("\n3) Como você resolve problemas?")
print("A) Agindo rapidamente")
print("B) Pensando com calma")
print("C) Criando estratégias")
print("D) Esperando o melhor momento")

resposta = input("Resposta: ").upper()

if resposta == "A":
    pontos_fogo += 1
elif resposta == "B":
    pontos_agua += 1
elif resposta == "C":
    pontos_planta += 1
elif resposta == "D":
    pontos_eletrico += 1


# ------------------------------
# PERGUNTA 4
# ------------------------------
print("\n4) O que você mais valoriza?")
print("A) Coragem")
print("B) Lealdade")
print("C) Sabedoria")
print("D) Energia")

resposta = input("Resposta: ").upper()

if resposta == "A":
    pontos_fogo += 1
elif resposta == "B":
    pontos_agua += 1
elif resposta == "C":
    pontos_planta += 1
elif resposta == "D":
    pontos_eletrico += 1


# ------------------------------
# PERGUNTA 5
# ------------------------------
print("\n5) Em um grupo você é:")
print("A) O líder impulsivo")
print("B) O equilibrado")
print("C) O planejador")
print("D) O animador")

resposta = input("Resposta: ").upper()

if resposta == "A":
    pontos_fogo += 1
elif resposta == "B":
    pontos_agua += 1
elif resposta == "C":
    pontos_planta += 1
elif resposta == "D":
    pontos_eletrico += 1


# ------------------------------
# RESULTADO FINAL
# ------------------------------

print("\n🎉 Resultado Final 🎉")

if pontos_fogo >= pontos_agua and pontos_fogo >= pontos_planta and pontos_fogo >= pontos_eletrico:
    print("🔥 Você é o CHARMANDER!")
elif pontos_agua >= pontos_fogo and pontos_agua >= pontos_planta and pontos_agua >= pontos_eletrico:
    print("💧 Você é o SQUIRTLE!")
elif pontos_planta >= pontos_fogo and pontos_planta >= pontos_agua and pontos_planta >= pontos_eletrico:
    print("🌿 Você é o BULBASAUR!")
else:
    print("⚡ Você é o PIKACHU!")

print("\nObrigado por jogar! 🕹️")