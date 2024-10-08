import torch.nn as nn
import torch.nn.functional as F
from core.Losses.builder import LOSSES
from core.Losses.utils import weighted_loss


@weighted_loss
def l1_loss(pred, target):
    """Warpper of mse loss."""
    return F.l1_loss(pred, target, reduction='none')

@weighted_loss
def mse_loss(pred, target):
    """Warpper of mse loss."""
    return F.mse_loss(pred, target, reduction='none')



@LOSSES.register_module()
class L1Loss(nn.Module):
    def __init__(self, reduction='mean', loss_weight=1.0):
        super().__init__()
        self.reduction = reduction
        self.loss_weight = loss_weight

    def forward(self, pred, target, weight=None):
        loss = self.loss_weight * \
               l1_loss(pred,
                       target,
                       weight,
                       reduction=self.reduction)
        return loss

@LOSSES.register_module()
class MSELoss(nn.Module):
    def __init__(self, reduction='mean', loss_weight=1.0):
        super().__init__()
        self.reduction = reduction
        self.loss_weight = loss_weight

    def forward(self, pred, target, weight=None, avg_factor=None):
        loss = self.loss_weight * mse_loss(
            pred,
            target,
            weight,
            reduction=self.reduction,
            avg_factor=avg_factor)
        return loss


