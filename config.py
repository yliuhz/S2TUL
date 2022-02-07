from dataclasses import dataclass


@dataclass
class FoursquareConfig:

    seed: int = 2021
    #datadir: str = "../foursquare/foursquare_TKY/processed_allday_norec/108/"
    # datadir: str = "../foursquare/foursquare_TKY/processed_allday_norec/209/"
    datadir: str = "../foursquare/foursquare_NYC/processed_allday_norec/108/"
    # datadir: str = "../foursquare/foursquare_NYC/processed_allday_norec/209/"
    #datadir: str = "../gowalla/gowalla/processed_allday_norec/209/"
    #datadir: str = "../gowalla/gowalla/processed_allday_norec/108/"
    # datadir: str = "../brightkite/brightkite/processed_allday_norec/108/"
    #datadir: str = "../brightkite/brightkite/processed_allday_norec/209/"
    # datadir: str = "/data/shgpu/TUL/processed/gowalla/300/"
    #datadir: str = "../gowalla/processed_allday/1000_randomly/"
    #datadir: str = "../gowalla/processed_allday/2000_randomly/"
    pretrain_loc_path: str = "./pretrain/word2vec/foursquare_32_108users.txt"
    # model parameters
    hidden_size: int = 32
    dropout: float = 0.1
    # training parameters
    device: str = "cuda:2"
    epochs: int = 200
    lr: float = 1e-3        # for batched_main, we should set smaller lr
    weight_decay: float = 1e-4
    log_every_n_steps: int = 10
    alpha_t: float = 0.8
    tau: float = 1
    gamma: float = 0.9
    steps: int = 30
    # for batched_main
    batch_size: int = 64
    # To demonstrate the effectiveness for data sparsity
    m: float = 1
    # for TULLSTM_main
    model_type: str = "BiLSTM"
    # spatial threshold, meters
    # spatio: float = 1500        # gowalla
    # spatio: float = 700      # brightkite
    spatio: float = 500        # foursquare
    # within 1 hour
    temporal: float = 1
