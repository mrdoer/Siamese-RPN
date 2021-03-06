import numpy as np


class Config:
    # dataset related
    exemplar_size = 127                    # exemplar size
    instance_size = 255                    # instance size
    context_amount = 0.5                   # context amount
    sample_type = 'uniform'

    # training related
    num_per_epoch = 4 * 53200              # num of samples per epoch
    train_ratio = 0.95                     # training ratio of VID dataset
    frame_range = 100                      # frame range of choosing the instance
    train_batch_size = 64                  # training batch size
    valid_batch_size = 8                   # validation batch size
    train_num_workers = 4                  # number of workers of train dataloader
    valid_num_workers = 4                  # number of workers of validation dataloader

    start_lr = 3e-4
    end_lr = 1e-6
    warm_epoch = 0
    warm_lr = 1e-3
    warm_scale = warm_lr/start_lr
    epoch = 50
    lr = np.logspace(np.log10(start_lr), np.log10(end_lr), num=epoch)[0]
    gamma = np.logspace(np.log10(start_lr), np.log10(end_lr), num=epoch)[1] / \
            np.logspace(np.log10(start_lr), np.log10(end_lr), num=epoch)[0]
                                           # decay rate of LR_Schedular
    step_size = 1                          # step size of LR_Schedular
    momentum = 0.9                         # momentum of SGD
    weight_decay = 0.0005                  # weight decay of optimizator

    seed = 1234                            # seed to sample training videos
    log_dir = './models/logs'              # log dirs
    max_translate = 12                     # max translation of random shift
    scale_resize = 0.15                    # scale step of instance image
    total_stride = 8                       # total stride of backbone
    valid_scope = int((instance_size - exemplar_size) / total_stride / 2)
    anchor_scales = np.array([8, ])
    anchor_ratios = np.array([0.33, 0.5, 1, 2, 3])
    anchor_num = len(anchor_scales) * len(anchor_ratios)
    anchor_base_size = 8
    pos_threshold = 0.6
    neg_threshold = 0.3
    num_pos = 16
    num_neg = 48
    lamb = 100
    save_interval = 1
    show_interval = 100
    pretrained_model = '/mnt/usershare/zrq/pytorch/lab/model/zhangruiqi/finaltry/sharedata/alexnet.pth'

    # tracking related
    gray_ratio = 0.25
    blur_ratio = 0.15
    score_size = int((instance_size - exemplar_size) / 8 + 1)
    penalty_k = 0.35
    window_influence = 0.10
    lr_box = 0.3
    min_scale = 0.1
    max_scale = 10


config = Config()
