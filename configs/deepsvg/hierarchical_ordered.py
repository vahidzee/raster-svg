from .default_icons import *


class ModelConfig(Hierarchical):
    def __init__(self):
        super().__init__()

        self.label_condition = False
        self.use_vae = False


class Config(Config):
    def __init__(self, num_gpus=2):
        super().__init__(num_gpus=num_gpus)

        self.model_cfg = ModelConfig()
        self.model_args = self.model_cfg.get_model_args()

        self.filter_category = None
        self.train_ratio = 1.0

        self.max_num_groups = 500
        self.max_seq_len = 30
        self.max_total_len = 15000



        # Dataloader
        self.loader_num_workers = 20 * num_gpus

        # Training
        self.num_epochs = 100
        self.val_every = 2000

        # Optimization
        self.learning_rate = 1e-3 * num_gpus
        self.train_batch_size = 32
        self.val_batch_size = 32

        self.val_every = 2000
        self.log_every = 50
        self.ckpt_every = 10

        self.val_num_steps = 5
        self.stats_to_print = {
            "train": ["lr", "time"],
            "val": ["time"]
        }

        self.val_idxs = None
        self.train_idxs = None
