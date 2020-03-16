# coding: utf-8
# center = centre en pixel relevé via ImageJ
# deltat = intervalle de temps entre 2 panos. J'ai pris 1040 secondes pour les acquisitions sans log
# milieu = milieu de culture
# operateur = personnes qui a fait la manip
# Light = WHITE ou FLUO

# pour utiliser:
# import DictManips as DM
# DictKeys, lst = DM.ManipList() retourne la liste de toutes les manips et les keys disponibles
# PARAMS =  DM.MANIPS(manip) retourne les parametres de la manip 'manip'



def MANIPS(manip):

    DictKeys, lst = ManipList()
    PARAMS = dict.fromkeys(DictKeys, None) 

    if manip == '2019_04_09_P_S_M2':
        update = {'name' : manip ,
                  'center' : (2883,3337),
                  'deltat' : 1040,
                  'milieu' : 'M2',
                  'operateur' : 'sabrina'}

    elif manip == '2019_04_11_P_S_M2':
        update = {'name' : manip ,
                  'center' : (2970,3324),
                  'deltat': 1040,
                  'milieu' : 'M2',
                  'operateur' : 'sabrina' }

    elif manip == '2019_03_27_P_S_M0':
        update = {'name' : manip ,
                  'center' : (3005,3336),
                  'deltat': 1040,
                  'milieu' : 'M0',
                  'operateur' : 'sabrina' }

    elif manip == '2019_04_10_P_S_M0':
        update = {'name' : manip ,
                  'center' : (2950,3510),
                  'deltat': 1040,
                  'milieu' : 'M0',
                  'operateur' : 'sabrina' }
    else:
        PARAMS = ' ERROR  '
        print( '--\n\t -- PAS DE MANIP À CE NOM \n\t --')


    PARAMS.update( update)

    return PARAMS

def ManipList():

    lst = [ '2019_04_09_P_S_M2',
            '2019_04_11_P_S_M2',
            '2019_03_27_P_S_M0',
            '2019_04_10_P_S_M0']

    DictKeys = {'name',
                'center',
                'deltat',
                'milieu' ,
                'operateur',
                'ImageSize',
                'Light',
                'FrameNumber'}

    print(' -- ')
    print(' -- Liste des manips disponibles :')
    print(' -- ')
    print(lst)

    return DictKeys, lst


def main():

    DictKeys, lst = ManipList()

    fname = lst[0] # '2019_04_09_P_S_M2'
    PARAMS = MANIPS(fname)

if __name__ == "__main__":
    main()
