"""
recommender.py
Sistema de recomendação simples baseado em similaridade do cosseno.

Este arquivo demonstra:
1. Carregamento dos dados (CSV)
2. Normalização dos dados (boa prática para sistemas reais)
3. Cálculo da matriz de similaridade
4. Função de recomendação simples baseada no usuário mais parecido

Este é o exemplo avançado do repositório, porém ainda didático.
"""

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import joblib


def carregar_dados(caminho="dataset_example.csv"):
    """
    Carrega o dataset de notas dos usuários.
    O CSV deve conter uma coluna 'Usuario' e colunas de produtos.
    """
    df = pd.read_csv(caminho).set_index("Usuario")
    return df


def treinar_modelo(df):
    """
    Normaliza os dados e calcula a matriz de similaridade entre usuários.
    A normalização evita que usuários que dão notas mais altas por padrão
    distorçam o cálculo da similaridade.
    """
    scaler = StandardScaler()
    dados_norm = scaler.fit_transform(df.values)

    sim_matrix = cosine_similarity(dados_norm)

    # Salvamos como ferramenta opcional
    joblib.dump(scaler, "scaler.joblib")
    joblib.dump(sim_matrix, "similarity_matrix.joblib")

    return sim_matrix, scaler


def recomendar_para(usuario, df, sim_matrix, top_n=2):
    """
    Recomenda usuários mais parecidos com o usuário informado.
    (Versão simples — apenas identifica perfis similares.)

    Em sistemas reais, a partir desse ponto você recomendaria produtos
    consumidos pelos usuários similares que o usuário-alvo ainda não consumiu.
    """
    if usuario not in df.index:
        raise ValueError(f"Usuário '{usuario}' não encontrado no dataset.")

    idx = list(df.index).index(usuario)
    scores = sim_matrix[idx]

    # Ordena por similaridade (maior → menor)
    idxs_ordenados = scores.argsort()[::-1]

    # Remove o próprio usuário da lista
    similares = [df.index[i] for i in idxs_ordenados if i != idx]

    return similares[:top_n]


def main():
    print("Carregando dados...")
    df = carregar_dados()

    print("Treinando modelo...")
    sim_matrix, scaler = treinar_modelo(df)

    print("\nMatriz de similaridade:")
    print(pd.DataFrame(sim_matrix, index=df.index, columns=df.index))

    print("\nExemplo de recomendação:")
    recomendados = recomendar_para("A", df, sim_matrix)
    print(f"Usuários mais parecidos com 'A': {recomendados}")


if __name__ == "__main__":
    main()

