jogador =  {
    "nome": "Cristiano",
    "gols": 760,
    "partidas": 1040
}

print( "\n-----Dados do Jogador-----")
print(f"nome: {jogador['nome']}")
print(f"gols: {jogador['gols']}")
print(f"partidas: {jogador['partidas']}")
media_gols = jogador['gols'] / jogador['partidas']
print(f"Média de gols por partida: {media_gols:.2f}")