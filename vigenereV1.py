# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 18:27:38 2018


"""

import string
import numpy as np
import sys


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
    
def frequence (fichier) :
    
    contenu = fichier 
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
    
    fusion = zip(liste,tab_freq)
    final = np.array(fusion)
    return tab_freq
    
def occurence (fichier):
    #monFichier = open(fichier, "r")
    contenu = fichier
    #monFichier.close()
    

    tab_carac = []    
    tab_occ = []
    texte_min = []
    liste = list(string.ascii_lowercase) # alphabet en minuscule
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
          
                nvtxt.append(texte[i])
                
           ic_texte = CalculerIC(nvtxt) #calculer  /§§§§§§§§§§§§§§
           
               
           if (ic_texte > 0.06) :
               if (icmax < ic_texte):
                   icmax = ic_texte
                   lgcle = n
             
              
    if icmax > 0 :        
        print("on a trouve un IC qui est bon")  
        print icmax
        return lgcle
    else :
        if icmax == 0:
           print("on n'a pas trouve un ic qui est bon")
    

def trouver_cle(fichier):
    
    monFichier = open(fichier, "r")
    texte = monFichier.read()
    monFichier.close()
    
    liste = list(string.ascii_lowercase)
    lg = len(texte)
    
    taillecle = lg_cle_IC(fichier)
   
    nvtxt = []
    tab_freq = []
    indfinal = []
    motfinal = []
    deb = 0 
    
    while deb < taillecle :
        nvtxt = []       
        for i in range (deb,lg,taillecle):
           
            nvtxt.append(texte[i])
           
        tab_freq = frequence(nvtxt)
        max_lettre = tab_freq.index(max(tab_freq))
        indfinal.append((max_lettre - 4) % 26)
        deb +=1
           
    for i in indfinal:
        motfinal.append(liste[i])
    vigenere_dechiff(motfinal,texte)
    
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
    
    monFichier = open('plain.txt', "w")
    for k in texte_fin :   
        monFichier.write(k)
    monFichier.close()
    
    myKey = open('my_key.txt', "w")
    for k in cle :   
        myKey.write(k)
    myKey.close()
      
    return texte_fin


################################## main ###################################
###########################################################################
                
tab ='txfr.txt'
#print (tab)
#print(CalculerIC('txfr.txt'))
      
         
#lg = lg_cle_IC('chiff.txt')
#print (lg_cle_IC('text1.cipher'))
#lg = trouver_cle('text1.cipher')
texte = sys.argv[1]
lg = trouver_cle(texte)
print ("la cle du texte est : ",lg)