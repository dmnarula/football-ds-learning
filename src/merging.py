import pandas as pd

# URL function
def get_gw_urls(gw: int):
  gw_path = "https://raw.githubusercontent.com/olbauday/FPL-Elo-Insights/refs/heads/main/data/2025-2026/By%20Gameweek/GW"
  url_stats = f"{gw_path}{gw}/playermatchstats.csv"
  url_players = f"{gw_path}{gw}/players.csv"
  url_teams = f"{gw_path}{gw}/teams.csv"
  url_matches = f"{gw_path}{gw}/matches.csv"
  return url_stats, url_players, url_teams, url_matches

# Merging data function
def build_match_df(url_stats, url_players, url_teams, url_matches):
    df_stats   = pd.read_csv(url_stats)
    df_players = pd.read_csv(url_players)
    df_teams   = pd.read_csv(url_teams)
    df_matches = pd.read_csv(url_matches)

    player_cols = ["player_code", "player_id", "web_name", "team_code", "position"]
    team_cols   = ["code", "name", "short_name"]
    match_cols  = ["gameweek", "home_team", "away_team",
                   "match_id", "home_score", "away_score"]

    df_players = df_players[player_cols].copy()
    df_teams   = df_teams[team_cols].copy()
    df_matches = df_matches[match_cols].copy()

    df_matches["home_team"] = pd.to_numeric(df_matches["home_team"], errors="coerce").astype("Int64")
    df_matches["away_team"] = pd.to_numeric(df_matches["away_team"], errors="coerce").astype("Int64")
    df_teams["code"]        = pd.to_numeric(df_teams["code"], errors="coerce").astype("Int64")

    df_sp = df_stats.merge(df_players, on="player_id", how="left")
    df_spm = df_sp.merge(df_matches, on="match_id", how="left")

    df_spmh = df_spm.merge(df_teams, left_on="home_team", right_on="code", how="left") \
        .rename(columns={"name": "home_team_name", "short_name": "home_team_short_name"}) \
        .drop(columns=["code"])

    df_spmha = df_spmh.merge(df_teams, left_on="away_team", right_on="code", how="left") \
        .rename(columns={"name": "away_team_name", "short_name": "away_team_short_name"}) \
        .drop(columns=["code"])

    df_final = df_spmha.merge(df_teams, left_on="team_code", right_on="code", how="left") \
        .rename(columns={"name": "team_name", "short_name": "team_short_name"}) \
        .drop(columns=["code"])

    return df_final
