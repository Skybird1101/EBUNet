from model.EBUNet import EBUNet

def build_model(model_name, num_classes):
    if model_name == 'EBUNet':
        return EBUNet(classes=num_classes)
