# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 18:27:38 2018



"""
import string
import numpy as np
import sys

def frequence (fichier) :
    
    # lecture du fichier #    
    #monFichier = open(fichier, "r")
    contenu = fichier 
    #monFichier.close()
    

    tab_carac = []    
    tab_freq = []
    texte_min = []
    liste = list(string.ascii_lowercase) # alphabet en majuscule
    tab_carac.append(liste)
     
    
    for k in contenu :
     
       texte_min.append(k.lower())
       
    lg_liste = len(liste)
    lg_contenu = len(texte_min)
   
    i = 0
    j = 0 
    nb_occ = 0
   
    while (i < lg_liste) :
        carac = liste[i]    
        j = 0
        nb_occ = 0
        while( j < lg_contenu) :   
            if (carac == texte_min[j]) :
                nb_occ +=1 
            j = j+1
        tab_freq.append(float (nb_occ) /lg_contenu)
        i+=1
    return tab_freq

def vigenere_chiff_txt(cle,fichier):

    monFichier = open(fichier, "r")
    texte = monFichier.read()
    monFichier.close()
    
    alphabet = list(string.ascii_uppercase)
    cle_maj = []
    cle_ind = []
    lgc = len(cle)
    for k in cle:
        cle_maj.append(k.upper())

    for k in cle_maj : 
        cle_ind.append(alphabet.index(k))

    texte_maj = []
    texte_fin = []

    for k in texte :
       texte_maj.append(k.upper())
    j = 0   
    for i in texte_maj:
        ind = alphabet.index(i)
        vg = (ind + cle_ind[j%lgc]) % 26
        j+=1
        texte_fin.append(alphabet[vg])
   
   
    monFichier = open('chiff.txt', "w")
    for k in texte_fin :   
        monFichier.write(k)
    monFichier.close()
    
    return texte_fin
    
    
def CalculerIC(texte):
    
    tab_occurence = occurence(texte)
    taille_texte = sum(occurence(texte))
    calcul = 0
    for k in tab_occurence:
        calcul += (float(k*(k-1)))/(taille_texte*(taille_texte-1))
    
    return calcul

def  CalculerICM(texte1,texte2):
    
    tab_occ1 = occurence(texte1)
    taille_texte1 = sum(occurence(texte1))
    tab_occ2 = occurence(texte2)
    taille_texte2 = sum(occurence(texte2))
    
    calcul = 0
    for k in range(0,len(tab_occ1)):
        calcul += (float(tab_occ1[k])*tab_occ2[k])/(taille_texte1*taille_texte2)
    
    return calcul
    
def occurence (fichier):
    #monFichier = open(fichier, "r")
    contenu = fichier
    #monFichier.close()
    

    tab_carac = []    
    tab_occ = []
    texte_min = []
    liste = list(string.ascii_uppercase) # alphabet en minuscule
    tab_carac.append(liste)
     
    
    for k in contenu :
     
       texte_min.append(k.upper())
       
    lg_liste = len(liste)
    lg_contenu = len(texte_min)
   
    i = 0
    j = 0 
    nb_occ = 0
   
    while (i < lg_liste) :
        carac = liste[i]    
        j = 0
        nb_occ = 0
        while( j < lg_contenu) :   
            if (carac == texte_min[j]) :
                nb_occ +=1 
            j = j+1
        tab_occ.append(nb_occ)
        i+=1
    return tab_occ

def lg_cle_formule(fichier):
    
    monFichier = open(fichier, "r")
    texte = monFichier.read()
    monFichier.close()
    
    ic_texte = CalculerIC(texte)
    ic_fr = 0.074
    ic_alea = 0.038
    lgtxt = len(texte)
    
    lg_cle = ((ic_fr - ic_alea)*lgtxt)/((lgtxt - 1)*ic_texte - (lgtxt*ic_alea) + ic_fr)
    
    return lg_cle
    
    
    


def lg_cle_IC(fichier):
    
    monFichier = open(fichier, "r")
    texte = monFichier.read()
    monFichier.close()
    icmax = 0
    lgcle = 0
    lg = len(texte)
    
    ic_texte = 0
    
    for n in range (4 , 20): 
              
           nvtxt = []
           for i in range (0,lg,n):
          
                nvtxt.append(texte[i])  #rajouter une boucle pour faire la moyenne des IC pour avoir un meilleure résultat
                
           ic_texte = CalculerIC(nvtxt)
           print(ic_texte)
           
               
           #if (ic_texte > 0.06) :
           if (icmax < ic_texte):
               icmax = ic_texte
               lgcle = n
             
              
    if icmax > 0 :        
        print("on a trouve un ic qui est bon")  
        print icmax
        print lgcle
        return lgcle
    else :
        if icmax == 0:
           
           print("on n'a pas trouve un ic qui est bon")  

def cesar_chiff(cle, texte) :

    
    alphabet = list(string.ascii_uppercase)
    cle_maj=cle.upper()
    c = (alphabet.index(cle_maj))
    texte_maj = []
    texte_fin = []
    for k in texte :
     
       texte_maj.append(k.upper())     
      
    for i in texte_maj[0:len(texte_maj)-1] :
        ind = alphabet.index(i)
        ind2 = (ind+c) % 26
        texte_fin.append(alphabet[ind2])
    
    return texte_fin
    
    
def trouver_cle(fichier):
    
    monFichier = open(fichier, "r")
    texte = monFichier.read()
    monFichier.close()
    liste = list(string.ascii_uppercase)
    lg = len(texte)
    
    
    taillecle = lg_cle_IC(fichier)


    nvtxt = []
    colonne = []
    tab_icfin = []
    motfinal = []
    deb = 0
    while deb < taillecle :
        nvtxt = []       
        for i in range (deb,lg,taillecle):
                  
                nvtxt.append(texte[i])
                         
        colonne.append(nvtxt)
        deb +=1  
        
    print taillecle  
   
    
    col_act = 0
    nvtxt = [] # texte avec tous les decalages par rapport a S0
    nvtxt2 = []
   
    while (col_act < taillecle-1):
        i = col_act+1
        if col_act == 0:
            nvtxt2+=colonne[0]
        while (i < taillecle):
           
            tab_ic = []
            maxi = 0
            q = 0
                      
            listact = []
            texteact = []
            for l in liste :
                
                nvtxt_chiff = cesar_chiff(l,colonne[i])               
                n = (CalculerICM(colonne[col_act],nvtxt_chiff))
                if n > 0.06 and maxi < n :
                    if q == 0:
                        
                        tab_ic.append(col_act)
                        tab_ic.append(i)
                        tab_ic.append(liste.index(l))
                        tab_ic.append(round(n,3))                   ########### tout en colonne ###############
                        tab_icfin.append(tab_ic)
                        texteact = nvtxt_chiff
                        
                        nvtxt.append(texteact)
                        q+=1
                        maxi = n
                        listact = tab_ic
                        tab_ic = []
                    
                    if q > 0:
                        tab_icfin.remove(listact)
                        nvtxt.remove(texteact)
                        tab_ic.append(col_act)
                        tab_ic.append(i)
                        tab_ic.append(liste.index(l))
                        tab_ic.append(round(n,3))                   ########### tout en colonne ###############
                        tab_icfin.append(tab_ic)
                        listact = tab_ic
                        texteact = nvtxt_chiff
                        nvtxt.append(texteact)
                        maxi = n
                        tab_ic = []
   
            i+=1     
        col_act+=1
    tabtrc = [] 
    
    #print np.array(tab_icfin)
    print len(nvtxt2)
    for lis in tab_icfin :
       
        if lis[0] == 0:
            tabtrc.append(lis)
            nvtxt2+=nvtxt[tab_icfin.index(lis)]
           
            
   
    print np.array(tabtrc)  
    tab_freq = frequence(nvtxt2) #calculer la frequence /§§§§§§§§§§§§§§             #####################"tronquer le tableau #########
    max_lettre = tab_freq.index(max(tab_freq))
    s0 =(max_lettre - 4) % 26
    print s0
                     #####################" reecrire en forme equation le tableau #########
                     
                     
    l_map = [] 
    for i in range(len(tabtrc)+1):
         l_map.append([0] * taillecle) 
   
    tabval = []
   
    for i in range(0,len(tabtrc)) :
        
        l_map[i][tab_icfin[i][0]] = 1
        l_map[i][tab_icfin[i][1]] = -1
        tabval.append(tab_icfin[i][2])
    
    l_map[len(tabtrc)][0] = 1
    tabval.append(s0)
    a = np.array(l_map)
    b = np.array(tabval)
    print a
    print b
    x = np.linalg.lstsq(a, b)   
   # print x
    indice = []
    for i in range (0,(taillecle)):
       indice.append((int)(round(x[0][i])%26))
    print indice
        
    for i in indice:
        motfinal.append(liste[i])
    vigenere_dechiff(motfinal,texte) 
    print motfinal
    return motfinal   
    
def vigenere_dechiff(cle,texte):
    
    alphabet = list(string.ascii_uppercase)
    cle_maj = []
    cle_ind = []
    lgc = len(cle)
    for k in cle:
        cle_maj.append(k.upper())

    for k in cle_maj : 
        cle_ind.append(alphabet.index(k))

    texte_maj = []
    texte_fin = []

    for k in texte :
       texte_maj.append(k.upper())
    j = 0   
    for i in texte_maj[0:len(texte)-1]:
        ind = alphabet.index(i)
        vg = (ind - cle_ind[j%lgc]) % 26
        j+=1
        texte_fin.append(alphabet[vg])
    
    monFichier = open('dechiffv2text2.txt', "w")
    for k in texte_fin :   
        monFichier.write(k)
    monFichier.close()
        
    return texte_fin


################################## main ###################################
###########################################################################
                
tab ='txfr.txt'
#print (tab)
#print(CalculerIC('txfr.txt'))

cle = 'anisrty'             
#vigenere_chiff_txt(cle,tab)             
#lg = lg_cle_IC('chiff.txt')
#print (lg_cle_IC('text1.cipher'))
texte = sys.argv[1]
lg = trouver_cle(texte)
#print('la cle est : ', lg)