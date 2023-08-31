""" Nif Utilities, for bones mapping """

from collections import defaultdict


class BonesMapper:
    """A simple class for bones mapping."""  
    
    # List of possible DAOC bones 
    bone_names = ["Bip01","Bip01 Pelvis","Bip01 Spine","Bip01 Spine1","Bip01 Spine2","Bip01 Spine3","Bip01 Neck","Bip01 Neck1","Bip01 Neck2","Bip01 Neck3","Bip01 Neck4","Bip01 Head","Bip01 Ponytail1","Bip01 Ponytail11","Bip01 Ponytail12","Bip01 Ponytail13","Bip01 Ponytail14","Bip01 Ponytail2","Bip01 Ponytail21","Bip01 Ponytail22","Bip01 Ponytail23","Bip01 Ponytail24","Bip01 L Clavicle","Bip01 L UpperArm","Bip01 L Forearm","Bip01 L Hand","Bip01 L Finger0","Bip01 L Finger01","Bip01 L Finger02","Bip01 L Finger1","Bip01 L Finger11","Bip01 L Finger12","Bip01 L Finger2","Bip01 L Finger21","Bip01 L Finger22","Bip01 R Clavicle","Bip01 R UpperArm","Bip01 R Forearm","Bip01 R Hand","Bip01 R Finger0","Bip01 R Finger01","Bip01 R Finger02","Bip01 R Finger1","Bip01 R Finger11","Bip01 R Finger12","Bip01 R Finger2","Bip01 R Finger21","Bip01 R Finger22","Bip01 L Thigh","Bip01 L Calf","Bip01 L HorseLink","Bip01 L Foot","Bip01 L Toe0","Bip01 L Toe01","Bip01 R Thigh","Bip01 R Calf","Bip01 R HorseLink","Bip01 R Foot","Bip01 R Toe0","Bip01 R Toe01","Bip01 Tail","Bip01 Tail1","Bip01 Tail2","Bip01 Tail3","Bip01 Tail4","Bip01 L Shield","Bip01 R Shield","Bip01 L Held","Bip01 R Held","Bip01 L Belt","Bip01 R Belt","Bip01 L Back","Bip01 R Back","Bip01 Helm","Bip01 Ext01","Bip01 Ext02","Bip01 Ext03","Bip01 Ext04","Bip01 Ext05","Bip01 Ext06","Bip01 Ext07","Bip01 Ext08","Bip01 Ext09","Bip01 Ext10","Bip01 Ext11","Bip01 Ext12","Bip01 Ext13","Bip01 Ext14","Bip01 Ext15","Bip01 Ext16","Bip01 Ext17","Bip01 Ext18","Bip01 Ext19","Bip01 Ext20","Bip01 L Finger3","Bip01 L Finger31","Bip01 L Finger32","Bip01 L Finger4","Bip01 L Finger41","Bip01 L Finger42","Bip01 R Finger3","Bip01 R Finger31","Bip01 R Finger32","Bip01 R Finger4","Bip01 R Finger41","Bip01 R Finger42","Bip01 L Toe02","Bip01 L Toe03","Bip01 L Toe1","Bip01 L Toe11","Bip01 L Toe12","Bip01 L Toe2","Bip01 L Toe21","Bip01 L Toe22","Bip01 R Toe02","Bip01 R Toe03","Bip01 R Toe1","Bip01 R Toe11","Bip01 R Toe12","Bip01 R Toe2","Bip01 R Toe21","Bip01 R Toe22","Bip01 L ForeTwist","Bip01 L ForeTwist1","Bip01 R ForeTwist","Bip01 R ForeTwist1","Bip01 EyeLids","Bip01 L BicepTwist","Bip01 R BicepTwist","Bip01 L Pauldron","Bip01 R Pauldron","Bip01 Beard1","Bip01 Beard2","Bip01 FrontRobe1","Bip01 FrontRobe2","Bip01 BackRobe1","Bip01 BackRobe2","Bip01 C Cloak01","Bip01 C Cloak02","Bip01 C Cloak03","Bip01 C Cloak04","Bip01 C Cloak05","Bip01 L Cloak01","Bip01 L Cloak02","Bip01 L Cloak03","Bip01 L Cloak04","Bip01 L Cloak05","Bip01 R Cloak01","Bip01 R Cloak02","Bip01 R Cloak03","Bip01 R Cloak04","Bip01 R Cloak05","Bip01 C CloakIKChain","Bip01 L CloakIKChain","Bip01 R CloakIKChain","Bip01 L ThighTwist","Bip01 R ThighTwist","R Cloak Control01","L Cloak Control01","C Cloak Control01","C Cloak Control02","C Cloak Control03","C Cloak Control04","C Cloak Control05","C Cloak Control06","L Cloak Control02","L Cloak Control03","L Cloak Control04","L Cloak Control05","L Cloak Control06","R Cloak Control02","R Cloak Control03","R Cloak Control04","R Cloak Control05","R Cloak Control06"]

    # Dictionnary to map bones names to id
    bonename_dict = defaultdict(int)
    id = 0
    for x in bone_names:
        if not bonename_dict[x]:
            bonename_dict[x] = id
            id+=1
        


