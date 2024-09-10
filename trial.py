import cv2,torch,torchvision,torchinfo
if __name__ =="__main__":
    ckpt="/home/muahmmad/projects/Image_enhancement/UWEnhancement/checkpoints/UIEC2Net.pth"
    state_dict=torch.load(f=ckpt,weights_only=True)
    print(state_dict["state_dict"].keys())