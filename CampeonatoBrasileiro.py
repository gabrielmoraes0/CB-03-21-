import pandas as pd

def csv(path):
    ler = pd.read_csv(path)
    return ler

def renomeado(dados):
    dados = dados.rename(columns={'estado_vencedor': 'vencedor_estado', 'ID':'#',
    'mandante_placar': 'casa', 'visitante_placar':'fora'
                                  })
    return dados

def placarmandante(dados):
    dados = dados['mandante_placar'].mean()
    return dados

def placarvisitante(dados):
    dados = dados['visitante_placar'].mean()
    return dados

def concatena(dados):
    dados['soma'] = dados['mandante_placar'] + dados['visitante_placar']
    return dados

def maioresvencedores(dados):
    dados = dados['vencedor'].value_counts()
    return dados

def estadovencedor(dados):
    dados = dados['estado_vencedor'].value_counts()
    return dados

def goleadasmandantes(dados):
    dados = dados[['mandante', 'mandante_placar', 'visitante', 'visitante_placar']]
    dados = dados.sort_values(by='mandante_placar', ascending=False)
    return dados

def goleadasvisitantes(dados):
    dados = dados[['visitante', 'visitante_placar', 'mandante', 'mandante_placar']]
    dados = dados.sort_values(by='visitante_placar', ascending=False)
    return dados

def formacao(dados):
    conca = pd.concat([dados['formacao_visitante'], dados['formacao_mandante']]).value_counts()
    return conca

def tecnicos(dados):
    conca = pd.concat([dados['tecnico_visitante'], dados['tecnico_mandante']]).value_counts()
    return conca

def rodadamandante(dados):
    dados = dados[['rodada', 'mandante', 'mandante_placar', 'visitante', 'visitante_placar']]
    n3 = dados.loc[df['rodada'] == 1]
    n3 = n3.sort_values(by='mandante_placar', ascending=False)
    return n3

def todostimes(dados):
    n1 = dados['mandante'].unique()
    return n1

def horarios_jogados(dados):
    dados = dados['hora'].value_counts()
    return dados

def soma_gols(dados):
    n1 = dados['mandante_placar'] + dados['visitante_placar']
    dados = n1.sum()
    return dados

def empate(dados):
    empatec = dados[['mandante', 'mandante_placar', 'visitante', 'visitante_placar']]
    empatec = empatec.loc[empatec['mandante_placar'] == empatec['visitante_placar']]
    return empatec


if __name__ == '__main__':
    df = csv('campeonato-brasileiro-full.csv')

    print(f'DF PURO \n {df}')

    #info das indices, tipos, informações gerais sobre os dados
    print(df.info())

    df_renomeado = renomeado(df)
    print(f'DF Renomeado\n {df_renomeado}')

    mediamandante = placarmandante(df)
    print(f'Media de gols mandante\n {mediamandante}')

    mediavisitante = placarvisitante(df)
    print(f'Media de gols visitante\n {mediavisitante}')

    soma = concatena(df)
    soma = soma['soma'].mean()
    print(f'Media de gols do campeonato por partida\n {soma}')

    rankingvencedores = maioresvencedores(df)
    print(f'Times que mais venceram entre o BR 03 até o BR 21\n{rankingvencedores}')

    rankingestado = estadovencedor(df)
    print(f'Estados com mais vitórias \n{rankingestado}')

    placarmand = goleadasmandantes(df)
    print(placarmand)

    placavisi = goleadasvisitantes(df)
    print(placavisi)

    tatica = formacao(df)
    print(f'Formaçoes mais usadas durante o campeonato\n{tatica}')

    tecni = tecnicos(df)
    print(f'Tecnicos que mais dirigiram times durante o campeonato \n{tecni}')

    rodam = rodadamandante(df)
    print(f'Maior goleada da rodada 1 \n{rodam}')

    times = todostimes(df)
    print(f'Todos os times que participaram do BR \n{times}')

    horario = horarios_jogados(df)
    print(f'Horarios que mais ocorreram jogos \n{horario}')

    gols = soma_gols(df)
    print(f'Quantidade de gols que ocorreram ao todo \n{gols}')

    empatecasa = empate(df)
    empatecasa = empatecasa.value_counts(['mandante'])
    print(f'Maior quantidade de empate como {empatecasa} \n')

    empatefora = empate(df)
    empatefora = empatefora.value_counts(['visitante'])
    print(f'Maior quantidade de empate como {empatefora}')







    






























