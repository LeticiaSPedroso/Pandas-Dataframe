#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:16:14 2018

@author: leticia
"""
import pandas as pd 

df = pd.read_table('<path>/unesp_2018.txt',
                   error_bad_lines=False,
                   header=None,
                   index_col=None,
                   lineterminator= " ",
                   delimiter = '\n')

df[0]=df.dropna(subset=[0])[0].str.replace('[\W|0-9]', '')
#Regex 
df[0]=df.replace('(B$|A$|C$|D$|E$|F$|O$|NÚMERO|CURSO|Ecologi|diurno|VESTIBULAR|horário|até|feira|dia|hora|vaga|pela|constar|interesse|confirmar|verá|lista|contar|cujo|candidato|Odontologia|Ocupacional|Terapia|Zootecnia|Computação|Ciência|Ambiental|Biotecnologia|Bioprocessos|Produção|Mecânica|Telecomunicações|Elétrica|Química|em|Biológica|Médica|Geologia|Matemática|matutino|Meteorologia|Tecnológica|Informação|Administração|Arquivologia|Visuais|Artes|ArteTeatro|Biblioteconomia|Econômicas|Sociais|Jornalismo|Social|Comunicação|Radialismo|Relações|Produto|Gráfico|Design|Musical|História|Canto|Música|Regência|Composição|Instrumento|Cordas|Clarineta|Sopros|Pedagogia|Violão|APª|matutinovespertino|Internacionais|Serviço|Energia|harelado|Cênicas|Oboé|Doce|Flauta|Antigo|NOME|Chamada|Chama|Matrícula|Até|APrimeira|noturno|Botucatu|Rio|Claro|SRVEBP|mais|autoclara|Pretos|Par|Indígenas|PPI|Lista|Candidatos|Classificados|Vestibular|Ciências|Biológicas|Bac|Lic|integral|Bauru|class|nome|Sistema|de|Reserva|Vagas|para|Educação|Básica|Primeira|Pública|Agronomia)',
               '', regex=True)

df=df.drop_duplicates(subset=[0])#remove linhas duplicadas

df2= df[0]
df2.to_csv('unesp_2018_output.txt',index=None, header=None)



 


    
