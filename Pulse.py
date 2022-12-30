import discord
import numpy as np
import pandas as pd
import string
import numexpr as ne
from sympy import Derivative, Symbol, symbols
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext import commands, tasks
import datetime
import itertools
from datetime import datetime, timezone, date
import matplotlib.pyplot as plt
from matplotlib import colors
from plotly.offline import plot
from matplotlib.ticker import PercentFormatter
import os
import requests
import schedule
import asyncio
import time
import random
import queue
from urllib.request import Request, urlopen
import sched
from bs4 import BeautifulSoup
import numexpr as ne

from urllib.request import Request, urlopen
from urllib.error import HTTPError ####
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from PIL import Image
import seaborn as sns
import math
import matplotlib as faggot

from threading import Thread

# alarm_time = '22:24'#24hrs
# channel_id = '400673288768192524' #modchat
Test = 50

def Role(message, role):
    return [str(x) for x in message.author.roles].__contains__(role)

intents = discord.Intents.default()
intents.members = True
# client = commands.Bot(command_prefix = 'P', Intents = intents)
client = commands.Bot(command_prefix='P ', intents=discord.Intents.all(), case_insensitive=True, self_bot=True)

Bot = discord.Client(intents=intents)
dick = 0

async def create_thread(self,name,minutes,message):
    token = 'Bot ' + self._state.http.token
    url = f"https://discord.com/api/v9/channels/{self.id}/messages/{message.id}/threads"
    headers = {
        "authorization" : token,
        "content-type" : "application/json"
    }
    data = {
        "name" : name,
        "type" : 11,
        "auto_archive_duration" : minutes
    }

    return requests.post(url,headers=headers,json=data).json()

discord.TextChannel.create_thread = create_thread

def Titles(S):
    list1 = [x.a['title'] for x in S.find_all('div', {'class':"mw-search-result-heading"})] #names
    list2 = [x.a['href'] for x in S.find_all('div', {'class':"mw-search-result-heading"})] #links
    stringo = ""
    for i in range(len(list1)):
        stringo += f"[{i}]."+ list1[i] + '\n '
    # print(list1)
    return [stringo, list2]

shock = ['wut', 'wtf', 'O3O', 'stfu pulse', 'fk this server', 'fuck this server', 'server is dead', ' wtf', 'fk your mum', 'fk ur mum', 'w0t', 'wot']
NUG = ['nugget', 'Nugget', 'NUGGET', 'nuget', 'Nuget']
nono = ['221533934314455041', '704334452398096534']
n = []
UHM = ['umm', 'uhm', 'umwhat']
dick = -0.1
# @client.event
# async def on_member_update(before, after):
#
#     print("print before get_channel()")
#     channel = client.get_channel(83566743976411136)
#     print("hewwo")
#
#     #print("hewwo")
#     channel.send("hi!")
#     if before.game != after.game:
#         print("O:::::::")
#         await channel.send("o:")
def unique(list):
    newlist=[]
    for i in list:
        if i in newlist:
            pass
        else:
            newlist.append(i)
    return newlist



















def pitychaintilldeath(lastroll, faith, *args): #with pity system - 2 fails in a row leads to one auto success | NEW:lastroll is option to retain information from previous roll to start from where you ended off from previous attempt!!!!
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        summ = 0
        result = True
        for mass in massDist:
            summ += mass
            if randRoll < summ:
                return result
            else:
                return False
    level=1
    string = ' '
    xxxx = []
    for i in args:
        if '*' in str(i):
            xxxx.append(float(i[:-1]))
        else:
            xxxx.append(float(i))
    print(len(xxxx))
    #print(xxxx)
    #print(xxxx[level])
    #print(1-xxxx[level])
    count = 1
    bottom = 0
    #Lets try to establish which arguments are critical points at which falling below is not possible - for now I think it is reasonable to expect that the critical points
    #behave exactly like the first level that we provide
    #First - let's try to extract and 'look for' critical points denoted by * after the probability values
    criticalno = []
    for i in range(len(args)):
        if '*' in str(args[i]):
            criticalno.append(i+1)   
    failedatcheckpoint = False  #To record if failure at checkpoint occurred in last roll - because if you fail once alr at a checkpoint, you CANNOT be given pity rank up if you fail at it again            
    while count < int(faith)+1 and level+lastroll<len(args)+1:
        print(level-1+lastroll)
        sampleMassDist = (xxxx[level-1+lastroll],1-xxxx[level-1+lastroll])
        t = roll(sampleMassDist)
        count+=1
        string+=str(t)+' '
        if t:
            level+=1
            failedatcheckpoint = False
        elif string.split(' ')[-1] == 'False' and failedatcheckpoint == False:
            level-=0 #just to indicate that you failed AND succeeded because of pity rank up right after at 100%
            string+='True '
            count+=1
            failedatcheckpoint = False
        elif len(criticalno) > 0:
            for i in criticalno:
                if level + lastroll == i:  #If you are at one of the critical points, you will not fail.
                    failedatcheckpoint = True
                    bottom += 1
        elif level+lastroll>1:  #Catch all term for dropping a level if no check point was triggered in previous if statement
            level-=1
            failedatcheckpoint = False
        else:
            bottom+=1
            failedatcheckpoint = True
    return [string, bottom]







def pitychaintilldeath0(lastroll, faith, *args): #with pity system - 2 fails in a row leads to one auto success | NEW:lastroll is option to retain information from previous roll to start from where you ended off from previous attempt!!!! 100% false dependent.
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        summ = 0
        result = True
        for mass in massDist:
            summ += mass
            if randRoll < summ:
                return result
            else:
                return False
    def countFalses(stringie):
        cunt = 0
        for i in stringie.split(' '):
            if i == 'False':cunt+=1
            else:pass
        return cunt
    level=1
    string = ' '
    #xxxx = [float(x) for x in args]
    xxxx = []
    for i in args:
        if '*' in str(i):
            xxxx.append(float(i[:-1]))
        else:
            xxxx.append(float(i))
    print(len(xxxx))
    #print(xxxx)
    #print(xxxx[level])
    #print(1-xxxx[level])
    count = 1
    bottom =0 #Number of times failed at bottom
    #Lets try to establish which arguments are critical points at which falling below is not possible - for now I think it is reasonable to expect that the critical points
    #behave exactly like the first level that we provide
    #First - let's try to extract and 'look for' critical points denoted by * after the probability values
    criticalno = []
    for i in range(len(args)):
        if '*' in str(args[i]):
            criticalno.append(i+1)     
    failedatcheckpoint = False  #To record if failure at checkpoint occurred in last roll - because if you fail once alr at a checkpoint, you CANNOT be given pity rank up if you fail at it again            
    while countFalses(string) < int(faith) and level+lastroll<len(args)+1:
        sampleMassDist = (xxxx[level-1+lastroll],1-xxxx[level-1+lastroll])
        t = roll(sampleMassDist)
        count+=1
        string+=str(t)+' '           
        if t:
            level+=1
            failedatcheckpoint = False
        elif string.split(' ')[-1] == 'False' and failedatcheckpoint == False:
            level-=0
            string+='True '
            count+=1
            failedatcheckpoint = False
        elif len(criticalno) > 0:
            for i in criticalno:
                if level + lastroll == i:  #If you are at one of the critical points, you will not fail.
                    failedatcheckpoint = True
                    bottom += 1            
        elif level+lastroll>1:
            level-=1
            failedatcheckpoint = False
        else:
            bottom+=1
            failedatcheckpoint = True
    return [string, bottom]





#Simple "AI". If softcap of successes is not reached and total count is alr reached, carry on for a small fail target. - A more conservative tapping higher failure aversive rolling session. You are aiming for a 
#More complex "AI". If last 3 taps were not FFT (pity) + last tap was T, then try a few more taps 

def hybridchain1(lastroll, softcap, faith, push,*args):  #So this is the simple version
#Hence, faith here is going to be the total number of taps cap BUT, it will decide to override it based off of softcap
#How much we push past despite reaching count cap is determined by input variable 'push'. 'push is the new number of failures we are willing to accept.
    push = int(push)
    softcap = int(softcap) #Low end number of failures you are willing to accept
    faith = int(faith) #This is going to be total number of taps you are 'generally' willing to accept
    softcap = min(softcap,len(args))
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        summ = 0
        result = True
        for mass in massDist:
            summ += mass
            if randRoll < summ:
                return result
            else:
                return False
    def countFalses(stringie):
        cunt = 0
        for i in stringie.split(' '):
            if i == 'False':cunt+=1
            else:pass
        return cunt
    level=1
    string = ' '
    # xxxx = [float(x.translate) for x in args]
    xxxx = []
    for i in args:
        if '*' in str(i):
            xxxx.append(float(i[:-1]))
        else:
            xxxx.append(float(i))
    print(len(xxxx))
    #print(xxxx)
    #print(xxxx[level])
    #print(1-xxxx[level])
    count = 1
    pushcount = 0
    bottom =0 #Number of times failed at bottom
    pityT = 0
    criticalno = []
    for i in range(len(args)):
        if '*' in str(args[i]):
            criticalno.append(i+1)     
    failedatcheckpoint = False  #To record if failure at checkpoint occurred in last roll - because if you fail once alr at a checkpoint, you CANNOT be given pity rank up if you fail at it again       
    while level+lastroll<len(args)+1: #The only condition when we break... when we reach our goal. This endpoint is always absolute. We are going to add break functions to stop this from "infiniting"
        sampleMassDist = (xxxx[level-1+lastroll],1-xxxx[level-1+lastroll])
        t = roll(sampleMassDist)
        count+=1
        string+=str(t)+' '
        if t:
            level+=1
            failedatcheckpoint = False
        elif string.split(' ')[-1] == 'False' and failedatcheckpoint == False:
            level-=0
            string+='True '
            count+=1
            pityT+=1
            failedatcheckpoint = False
        elif len(criticalno) > 0:
            for i in criticalno:
                if level + lastroll == i:  #If you are at one of the critical points, you will not fail.
                    failedatcheckpoint = True
                    bottom += 1               
        elif level+lastroll>1:
            level-=1
            failedatcheckpoint = False
        else:  #This is supposedly at the bottom where we fail and do not drop a level
            bottom += 1
            failedatcheckpoint = True 
        if count >= int(faith) and len(string.split(' '))-countFalses(string) - bottom - pityT<softcap:
            break
        elif count>= int(faith) and len(string.split(' '))-countFalses(string) - bottom  - pityT>=softcap and pushcount <= push:
            if t==False:
                pushcount += 1
                if pushcount >= push:
                    break
        else:pass
            

    return [string, bottom]


def hybridchain2(lastroll, softcap, faith, push,*args):  #So this is the simple version
#More aggressive mechanism.
#This reaches softcap and faith cap but then decides to push despite both being reached until push fail limit is reached.
    push = int(push)
    softcap = int(softcap) #Low end number of failures you are willing to accept
    faith = int(faith) #This is going to be total number of taps you are 'generally' willing to accept
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        summ = 0
        result = True
        for mass in massDist:
            summ += mass
            if randRoll < summ:
                return result
            else:
                return False
    def countFalses(stringie):
        cunt = 0
        for i in stringie.split(' '):
            if i == 'False':cunt+=1
            else:pass
        return cunt
    level=1
    string = ' '
    # xxxx = [float(x) for x in args]
    xxxx = []
    for i in args:
        if '*' in str(i):
            xxxx.append(float(i[:-1]))
        else:
            xxxx.append(float(i))
    print(len(xxxx))
    #print(xxxx)
    #print(xxxx[level])
    #print(1-xxxx[level])
    count = 1
    pushcount = 0
    bottom = 0
    criticalno = []
    for i in range(len(args)):
        if '*' in str(args[i]):
            criticalno.append(i+1)    
    failedatcheckpoint = False    
    while level+lastroll<len(args)+1: #The only condition when we break... when we reach our goal. This endpoint is always absolute. We are going to add break functions to stop this from "infiniting"
        sampleMassDist = (xxxx[level-1+lastroll],1-xxxx[level-1+lastroll])
        t = roll(sampleMassDist)
        count+=1
        string+=str(t)+' '
        if t:
            level+=1
            failedatcheckpoint = False    
        elif string.split(' ')[-1] == 'False' and failedatcheckpoint == False    :
            level-=0
            string+='True '
            count+=1
            failedatcheckpoint = False    
        elif len(criticalno) > 0:
            for i in criticalno:
                if level + lastroll == i:  #If you are at one of the critical points, you will not fail.
                    failedatcheckpoint = True
                    bottom += 1                   
        elif level+lastroll>1:
            level-=1
            failedatcheckpoint = False    
        else:
            bottom+=1
            failedatcheckpoint = True 
        if count>= int(faith) and countFalses(string)>=softcap:
            if t==True and string.split(' ')[-1] == 'False' and string.split(' ')[-2] == 'False' and pushcount == 0: #Break if pity at the softcap mark
                break
            elif t== False and pushcount == 0: #break if 
                break
            elif t== False and pushcount == push:
                break
            elif t== False:
                pushcount+=1
            else:
                pass


        else:pass
            

    return [string, bottom]


#This means that the total number of successes is actually len(trues) - len(falses) +bottom. This is only important when you are repeating these above






















def chainular(*args):
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        sum = 0
        result = True
        for mass in massDist:
            sum += mass
            if randRoll < sum:
                return result
            else:
                return False

    string = ''
    for i in args:
        print(i)
        sampleMassDist = (float(i),1-float(i))
        string += str(roll(sampleMassDist))+' '
    return string

def chaintilldeath(faith, *args):  #without pity system
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        sum = 0
        result = True
        for mass in massDist:
            sum += mass
            if randRoll < sum:
                return result
            else:
                return False
    level=1
    string = ' '
    # xxxx = [float(x) for x in args]
    xxxx = []
    for i in args:
        if '*' in str(i):
            xxxx.append(float(i[:-1]))
        else:
            xxxx.append(float(i))
    #print(xxxx)
    #print(xxxx[level])
    #print(1-xxxx[level])
    count = 1
    while count < int(faith)+1 and level<len(args)+1:
        sampleMassDist = (xxxx[level-1],1-xxxx[level-1])
        t = roll(sampleMassDist)
        count+=1
        string+=str(t)+' '
        if t:
            level+=1
        elif level>1:
            level-=1
    return string



async def MS(ctx):
    await client.wait_until_ready()
    while not client.is_closed():  
        noofpings = 100
        cute_norm = 2  
        schannel = client.get_channel(892205198456533022)
        N_TRIES = min(60**2, int(noofpings))
        await schannel.send(f"``Commencing maple-reboot channel ping analysis for norm of {cute_norm} with {noofpings} pings...``")
        matr = np.zeros([N_TRIES, 30])
        def check(name):
            return name[:7] == 'Channel'
        row = 0
        while row < N_TRIES:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            link_template = f'https://xymu.github.io/maple.watch/#GMS-Reboot'
            driver = webdriver.Chrome(r'E:\chromedriver.exe', chrome_options=options)
            driver.get(link_template)
            no = 4.5
            try:
                WebDriverWait(driver, no).until(EC.presence_of_element_located((By.CLASS_NAME, 'container item__body--uZhP-')))
            except TimeoutException:
                print(f'Page timed out after {no} secs.')
            soup = BeautifulSoup(driver.page_source, 'html5lib')
            driver.quit()
            LEN = len(soup.find_all("article", {"class":"slow"}))
            source = [soup.find_all("article", {"class":"slow"})[x].span.text for x in range( LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
            print(len(source))
            PING = [int(soup.find_all("article", {"class":"slow"})[x].find('div', {'class':'time'}).text[:-2]) for x in range(LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
            channels = []
            counterofchannels = 0
            for i in source:
                if check(i):
                    counterofchannels += 1
                    channels.append(int(i.split(' ')[-1]))
            try:
                number = min(channels)-1
                for j in channels:
                    matr[row][j-1] += PING[number]
                    # print(len(PING), max(channels))
                    number+=1
                row+=1
            except: pass
        MEAN = [np.median([ping[channel] for ping in matr if ping[channel]!=0]) for channel in range(len(source))] #changed from 30 to len(source) for longevity
        if int(cute_norm)==2:STD = [np.std([ping[channel] for ping in matr if ping[channel]!=0]) for channel in range(len(source))]
        else:
            MINUS = [np.array(matr[:, channel]) /MEAN[channel] for channel in range(len(source))]
            def norm(array, dyn):
                sum=0
                for thing in array:
                    sum+=thing**dyn
                return sum**(1/dyn)
            STD = [norm(error, int(cute_norm)) for error in MINUS]
        #Let us try rearranging the parent matr matrix in order to get sexier plots. We shall use the standard dev values in STD!
        sortedmatrixsortof = [list(np.transpose(matr)[i-1]) for __,i in sorted(zip(STD,channels))]
        new_matr = np.zeros([len(source),N_TRIES])
        for i in range(len(new_matr)):
            for j in range(len(new_matr[i])):
                new_matr[i,j] += sortedmatrixsortof[i][j]
        Channelssorted = [i for __,i in sorted(zip(STD,channels))]
        x_axis = np.arange(1,N_TRIES+1) #####################
        linestyle_tuple = [
        ((0, (1, 10))),
        ((0, (1, 1))),
        ((0, (1, 1))),
        ((0, (5, 10))),
        ((0, (5, 5))),
        ((0, (5, 1))),
        ((0, (3, 10, 1, 10))),
        ((0, (3, 5, 1, 5))),
        ((0, (3, 1, 1, 1))),
        ((0, (3, 5, 1, 5, 1, 5))),
        ((0, (3, 10, 1, 10, 1, 10))),
        ((0, (3, 1, 1, 1, 1, 1)))]
        await schannel.send(f"```{ctx.message.author}'s Request for ping over {N_TRIES} samples with norm of {cute_norm} acquired!```")
        print(type(sortedmatrixsortof))
        # plt.figure(figsize=(4.1*2.5,4.1))
        if int(noofpings)<21:plt.figure(figsize=(15,8))
        else:plt.figure(figsize=(25,10))
        RAND = np.random.uniform(10,20)
        for repeat in range(3):
            plt.clf()
            plt.style.use("seaborn-dark")
            for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
                plt.rcParams[param] = '#212946'  # bluish dark grey
            for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
                plt.rcParams[param] = '0.9'  # very light grey
            split = 0
            for idx, row in enumerate(np.transpose(np.transpose(new_matr)[:,repeat*10:(repeat+1)*10])): #@@7z. Senpai wish me luck o3o
                plt.grid(color='#2A3459')
                if split <5:
                    plt.subplot(1,2,1)
                    stringofchannels = ''
                    for i in range(5):
                        stringofchannels += f'{Channelssorted[repeat*10+i]}' + ', '
                    plt.title(f"Channels {stringofchannels}")
                    # plt.subplots_adjust(wspace=3, hspace=3)
                else:
                    plt.subplot(1,2,2)
                    stringofchannels = ''
                    for i in range(5,10):
                        stringofchannels += f'{Channelssorted[repeat*10+i]}' + ', '
                    plt.title(f"Channels {stringofchannels}")
                    # plt.subplots_adjust(wspace=1, hspace=1)
                number_of_colors = len(source)
                C0L = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(number_of_colors)])
                # print(color)
                MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
                size = 12
                plt.ylabel("NZ ping/ms")
                plt.plot(x_axis, row, label = f" Ch {Channelssorted[repeat*10+idx]}", linestyle = random.choice(linestyle_tuple), marker = MARK, linewidth = 2.5, color = C0L, ms = size)
                n_lines = 12
                diff_linewidth = 1.02
                alpha_value = 0.02 #0.03
                for n in range(1, n_lines+1):
                    plt.plot(x_axis,row,
                            linewidth=2+(diff_linewidth*n),
                            alpha=alpha_value,
                            color=C0L, ms = size)
                leg = plt.legend(loc='best', ncol=2, shadow=True, fancybox=True, prop={'size': 22})
                leg.get_frame().set_alpha(0.7)
                plt.xlabel("Ping attempts")

                #Here was the title line
                split+=1
            plt.savefig(fname='plot')
            await schannel.send(file=discord.File('plot.png'))
            os.remove('plot.png') ############
        STD = [np.std([ping[channel] for ping in matr if ping[channel]!=0]) for channel in range(len(source))]
        L10 = [norm(error, 10) for error in MINUS]
        await schannel.send(f'``The lowest mean server is Channel {MEAN.index(min(MEAN))+1}: with sd {STD[MEAN.index(min(MEAN))]}``')
        mean = np.copy(MEAN)
        await schannel.send(f'``Alternatives would be Channel {MEAN.index(sorted(mean)[1])+1}, {MEAN.index(sorted(mean)[2])+1}, or {MEAN.index(sorted(mean)[3])+1}``')
        await schannel.send(f'``The least variant server is Channel {STD.index(min(STD))+1}: {MEAN[STD.index(min(STD))] - MEAN[MEAN.index(min(MEAN))]}ms relative ping with sd {STD[STD.index(min(STD))]}``')
        std = np.copy(STD)
        await schannel.send(f'``Alternatives would be Channel {STD.index(sorted(std)[1])+1}, {STD.index(sorted(std)[2])+1}, or {STD.index(sorted(std)[3])+1}``')
        await schannel.send(f" `` --------------------------------------------------------------------------- ``")
        await schannel.send(f'``Fun fact: the channel with the highest ping is Channel {MEAN.index(max(MEAN))+1}: {MEAN[MEAN.index(max(MEAN))] - MEAN[MEAN.index(min(MEAN))]}ms relative ping with sd {STD[MEAN.index(max(MEAN))]}``')
        await schannel.send(f'``The channel with the most variant ping is Channel {STD.index(max(STD))+1}: {MEAN[STD.index(max(STD))] - MEAN[MEAN.index(min(MEAN))]}ms relative ping with sd {STD[STD.index(max(STD))]}``')
        source_copy = np.copy(source)
        await schannel.send(f" `` --------------------------------------------------------------------------- ``")
        UNS = [source_copy[unstable] for unstable in range(len(source_copy)) if L10[unstable] > 2]
        var = 2
        if len(UNS) >27:
            var = .75*(max(L10) - min(L10)) + min(L10)
            UNS = [source_copy[unstable] for unstable in range(len(source_copy)) if L10[unstable] > var]
        uns = " "
        for i in UNS: uns+=i + ", "
        ORDER_OF_CHAOS = [channel for _,channel in sorted(zip(L10, source_copy))]
        await schannel.send(f'**Warning**: ``Detecting severe relative instabilities in  {ORDER_OF_CHAOS[-1]}, {ORDER_OF_CHAOS[-2]}, or {ORDER_OF_CHAOS[-3]}!! \n List of Channels with >{var} L10 norm : {uns}``  ')
        await schannel.send(f'``Instead, consider these if anything else -  {ORDER_OF_CHAOS[0]}, {ORDER_OF_CHAOS[1]}, {ORDER_OF_CHAOS[2]}, or {ORDER_OF_CHAOS[3]}.``  ')
        await asyncio.sleep(2*60**2)





async def time_check():
    await client.wait_until_ready()
    while not client.is_closed():
        channel = client.get_channel(620593416757182474)    #Pulse channel
        schannel = client.get_channel(620604577288290314)
        rss_address = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
        json_data = requests.get(rss_address).json()
        magn = float(json_data['features'][0]['properties']['mag'])
        loc = json_data['features'][0]['properties']['place']
        timedispLat = json_data['features'][0]['properties']['updated'] - json_data['features'][0]['properties']['time']
        T = lambda: int(round(time.time() * 1000))
        timeepochmodified = T()/1000
        normaltime = datetime.fromtimestamp(timeepochmodified, timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f')
        timeattainLat = T() - json_data['features'][0]['properties']['time']

        global n
        if (loc not in n):
            n.append(loc)
            # print(n)
            await channel.send(f'``{loc}:{magn}@ {normaltime}\n Processing Delay:{timedispLat//1000}s , API Delay:{timeattainLat//1000}s ``')
            await schannel.send(f'``{loc}:{magn} @ {normaltime}\n Processing Delay:{timedispLat//1000}s , API Delay:{timeattainLat//1000}s ``')


            if len(n)>=10:
                n = n[9:10]


        await asyncio.sleep(5)


mark = 0

# async def checkwithuser():
#     await client.wait_until_ready()
#     while not client.is_closed():
#         user = await client.fetch_user(74168156804878336)
#         integer = random.choice([476683609105760256,481002210038251520,375543502119108608,192528449187872772])
#         randomuser = await client.fetch_user(integer)
#         await user.send("SIR! o3o")
#         # await randomuser.send("I hope you are doing good so far!")
#         # time.sleep(2)
#         # await randomuser.send(random.choice(["FOOL!","I mean it. Don't go killing yourself off now o3o"," You are a very handsome looking woman after all.","Have some tea, on yourself."]))
#         await asyncio.sleep(3*60**2)


async def conv_check_sgdtonzd():
    await client.wait_until_ready()
    while not client.is_closed():
        channel = client.get_channel(907924439012896808)    #xe_currencyconverter channel
        schannel = client.get_channel(620604577288290314)
        dbs = client.get_channel(934654643764613141)#DBS bank channel
        animalswikia = f'https://www.xe.com/currencyconverter/convert/?Amount=1&From=SGD&To=NZD' #this is the xecurrency one which is liek looking a bit into the future for DBS
        Req = Request(animalswikia)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')
        txt = soup.find('p',{'class':"result__BigRate-sc-1bsijpp-1 iGrAod"}).text
        animalswikia = 'https://www.sgrates.com/bankrate/dbs.html'
        Req = Request(animalswikia)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')
        def SGD_to_NZD(soupo):
            entry_we_want = ''
            for i in soupo.find_all('tr')[1:]:
                if i.find_all('td')[0].text.replace('\n','').replace(' ','').__contains__('NZD'):
                    entry_we_want = (float(i.find_all('td')[4].text.replace('\n','').replace(' ',''))+float(i.find_all('td')[2].text.replace('\n','').replace(' ','')))/2
                    break
            return 1/entry_we_want
        def SGD_to_USD(soupo):
            entry_we_want = ''
            for i in soupo.find_all('tr')[1:]:
                if i.find_all('td')[0].text.replace('\n','').replace(' ','').__contains__('USD'):
                    entry_we_want = (float(i.find_all('td')[4].text.replace('\n','').replace(' ',''))+float(i.find_all('td')[2].text.replace('\n','').replace(' ','')))/2
                    break
            return 1/entry_we_want


        myself = await client.fetch_user(74168156804878336)
        sham = await client.fetch_user(305647375756689429)
        if float(txt.split(' N')[0]) > 1.1:
            await channel.send(f"{myself.mention}! `` 1 SGD = {txt}``")
        else:await channel.send(f"``1 SGD = {txt}``")
        try:await sham.send(f"``Beep boop. Just here to report that as of today, 1SGD = {txt}``") #send to ma
        except:pass
        if SGD_to_NZD(soup) > 1.09:
            await myself.send(f"``SIR! I think you should check out the exchange rate! I am getting {SGD_to_NZD(soup)} NZD for 1 SGD from DBS!!!``")
            await sham.send(f"``Excuse me ma'am! I think you should check out the exchange rate! I am getting {SGD_to_NZD(soup)} NZD for 1 SGD from DBS!!!``")
        if SGD_to_USD(soup)>0.755:
            await myself.send(f"``PSSSSSSSSSSST! By the way, master... I am getting news of {SGD_to_NZD(soup)} USD for 1 SGD from DBS as well! In case you were interested o3o``")
        await sham.send(f"``ALSO MA'AM!!! Also take note that as of today, 1SGD = {SGD_to_NZD(soup)} for DBS bank in particular!``")
        await dbs.send(f"``1 SGD = {SGD_to_NZD(soup)} NZD``")
        await dbs.send(f"``1 SGD = {SGD_to_USD(soup)} USD``")
        await asyncio.sleep(2*60**2)


async def conv_check_usdtosgd():
    await client.wait_until_ready()
    while not client.is_closed():
        channel = client.get_channel(907924439012896808)    #Pulse channel
        schannel = client.get_channel(620604577288290314)
        animalswikia = f'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=SGD'
        Req = Request(animalswikia)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')
        txt = soup.find('p',{'class':"result__BigRate-sc-1bsijpp-1 iGrAod"}).text
        myself = await client.fetch_user(74168156804878336)
        if float(txt.split(' S')[0]) < 1.38300:
            await myself.send(f"``SHISHO! COME LOOK! I think you should check out the exchange rate! {float(txt.split(' S')[0])} SGD for 1 USD!!! Have you maybe had a look at how much NX is right now in NZ?``")
        elif float(txt.split(' N')[0]) < 1.4:
            await myself.send(f"``Interesting, interesting... Shisho..``")
            await myself.send(f"``Did you know... that only about {float(txt.split(' S')[0])} NZD is now equivalent to 1 USD!!!``")
        await channel.send(f"``1 USD = {txt}``")
        await asyncio.sleep(2*60**2)



async def main():
    async with client:
        client.loop.create_task(time_check())
        client.loop.create_task(conv_check_sgdtonzd())
        client.loop.create_task(conv_check_usdtosgd())
        await client.start('NjIwNTk1Njc3ODM5MjI4OTMy.XXZE2A.UpS2XMVoGP188xNjZscEy1RdiBo')
# client.loop.create_task(checkwithsuser())
# client.loop.create_task(jade())


@client.event
async def on_ready():
    print("Beep!")


@Bot.event
async def on_member_join(member):
    schannel = client.get_channel(891562421221732363)
    await client.get_channel(schannel).send(f"{member.name} has joined")
    await member.send("Hello there good sir! o3o")
    time.sleep(2)
    await member.send("If you happen to be joining this server to play maple, please head on over to #announcements and react to the bottom message below in order to gain access to the maple chat")
    time.sleep(0.5)
    await member.send("Otherwise, you can't see the beautiful people speak to you ( ・⌓・｀)")
    time.sleep(5)
    await member.send("BTW! We also have a maplestory ping channel, which for now, returns ping data per channel for a player based in NZ, click the Pingpong react button as well in announcements :3")
    time.sleep(1)
    await member.send("Looking at which channels vary the least the ping indicate channel stability, regardless of region")
    time.sleep(0.5)
    await member.send("If you happen to be interested, let me know :3 We can gib the python code to you, as long as you promise to share your delicious code o3o")
    time.sleep(2)
    await member.send("Sharing is caring after all o3o")


# @client.command()
# @commands.has_role("Duke")
# async def stop(ctx):
#     await client.logout()


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()

@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")


@client.command(brief = "<day1> <month1> <year1> <day2> <month2> <year2>")
async def time(ctx, day1, month1, year1, day2, month2, year2):
    proj = date(int(year2), int(month2), int(day2))
    cur = date(int(year1), int(month1), int(day1))
    await ctx.send(f"`` Beep boop! That is about {int((proj-cur).days)} days, master :D ``")

@client.command(brief = "<no of runs until and INCLUDING the trial when you got the drop> <''> <''> ...",description="Please call this command together with all number of times you had to run in order to get your drop in question. The more times you have to provide for me to study, the better :D")
async def Droprate(ctx, s, n):
    s = int(s)
    n = int(n)
    p1 = s/n
    p2 = (s-1)/(n-1)
    await ctx.send(f'`` mle/mme estimate of drop rate with given input is {p1*100}% ``')
    await ctx.send(f'`` minimum variance unbiased estimator (mvue) estimate of drop rate with given input is {p2*100}% ``')
    conf = [.5,.75,.90]
    end = []
    end2 = []
    for i in conf:
        end.append(np.log(1-i)/np.log(1-p1))
        end2.append(np.log(1-i)/np.log(1-p2))
    await ctx.send('BEEP.BOOP.')
    for i in range(len(end)):
        await ctx.send(f'`` {conf[i]*100}% confidence that you will get a drop in {math.ceil(end[i])} runs :D - according to mme/mle prob =3=  ``')
        try:
            await ctx.send(f'`` {conf[i]*100}% confidence that you will get a drop in {math.ceil(end2[i])} runs :D - according to mvue prob ``')
        except:
            pass



@client.command()
@commands.has_any_role('Duke',  'Moderator', 'Tsuki')
async def func(ctx, arg1, *args):
    n = len(args)
    for i in range(1, n+1):
        exec(f'x{i} = (float(args[i-1].strip()))')
    G = arg1.strip()
    y = ne.evaluate(G)
    await ctx.send(f'{y}')


@client.command()
async def SFcost(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/891562421221732363/993904661767671868/starforceprobs.PNG')



@client.command()
@commands.has_role("Team Lucid")
async def rolls(ctx, arg1, arg2=1):
    sampleMassDist = (float(arg1),1-float(arg1))
    def roll(massDist):
        randRoll = random.random() # in [0,1]
        sum = 0
        result = True
        for mass in massDist:
            sum += mass
            if randRoll < sum:
                return result
            else:
                return False

    print(roll(sampleMassDist))
    string = ''
    for i in range(int(min(100,arg2))):
        string += str(roll(sampleMassDist))+' '
    await ctx.send(string)



@client.command()
@commands.has_role("Team Lucid")
async def rollsuntildie(ctx, *args):
    def checkforFalse(stringie):
        final = True
        for i in stringie.split(' '):
            if i == 'False':
                final = False
        return final
    count = 1
    checkthis = chainular(*args)
    print(checkthis)
    while checkforFalse(checkthis) == False:
        print(count)
        count += 1
        checkthis = chainular(*args)
    await ctx.send(count)






























    # @client.command()
    # async def starforceNB(ctx,faith, *args):  #helps to loop through the tries. This is for batches UNTIL success
    #     SUCCESSWEWANT = len(args)
    #     nocatch = True
    #     for i in args:
    #         if float(i)>0.999999:
    #             nocatch=False
    #             await ctx.author.send("Here is an example for you...")
    #             await ctx.author.send(f"If say the probability of a piano hitting you on the head was {i}, then I would then be simulating it 3 times or so, and saying {chainular(i,i,i)} for them... Now is that really necessary to calculate? o3o")
    #             await ctx.author.send("Of course not o3o. Now kindly go eat a potato and get fatter by a {i*100}% chance pls, ty")
    #         elif float(i)<0.0001 or float(faith)<len(args):
    #             nocatch = False
    #             await ctx.send(f"fuck you, {ctx.author.mention}")
    #             await ctx.author.send("No, we are not trying to find the probability of your tiny dick being worth anything, silly. Try something else, like, the probability of you being deranged enough to bully a cute little robot o3o")
    #             await ctx.author.send(f"I would estimate that to be around {(random.random()*0.1+0.8)*100}% of being the case")
    #             await ctx.author.send(f"May Allah have mercy on your crusty soul, good sir, https://tenor.com/view/jesus-christ-praying-rosary-gif-16833024")
    #     if nocatch:
    #         def TrueCount(stringie):
    #             final = False
    #             if len([x for x in stringie.split(' ') if x == 'True']) - len([x for x in stringie.split(' ') if x == 'False']) == SUCCESSWEWANT:
    #                 final = True
    #             return final
    #         count = 1
    #         faith = int(faith)
    #         faith = max(len(args),faith)
    #         checkthis = chaintilldeath(faith, *args) #first run
    #         print(checkthis) #print the string of results for the first batch of runs
    #         while TrueCount(checkthis) == False:
    #             #print(count)
    #             count += 1
    #             checkthis = chaintilldeath(faith, *args)
    #             print(checkthis)
    #         await ctx.send(count)
    #     else:
    #         await ctx.send(f"{ctx.author.mention}, nu. o3o")

@client.command()
async def StarforceNB(ctx,faith, *args):  #helps to loop through the tries. This is for batches UNTIL success
    SUCCESSWEWANT = len(args)
    faith = int(faith)
    faith = max(len(args),faith)
    nocatch = True
    for i in args:
        if float(i)>0.999999:
            nocatch=False
            await ctx.author.send("Here is an example for you...")
            await ctx.author.send(f"If say the probability of a piano hitting you on the head was {i}, then I would then be simulating it 3 times or so, and saying {chainular(i,i,i)} for them... Now is that really necessary to calculate? o3o")
            await ctx.author.send("Of course not o3o. Now kindly go eat a potato and get fatter by a {i*100}% chance pls, ty")
        elif float(i)<0.0001 or float(faith)<len(args):
            nocatch = False
            await ctx.send(f"fuck {ctx.author.id}")
            await ctx.author.send("No, we are not trying to find the probability of your tiny dick being worth anything, silly. Try something else, like, the probability of you being deranged enough to bully a cute little robot o3o")
            await ctx.author.send(f"I would estimate that to be around {(random.random()*0.1+0.8)*100}% of being the case")
            await ctx.author.send(f"May Allah have mercy on your crusty soul, good sir, https://tenor.com/view/jesus-christ-praying-rosary-gif-16833024")
    if nocatch:    
        def TrueCount(stringie, lastround):
            final = False
            if len([x for x in stringie.split(' ') if x == 'True']) - len([x for x in stringie.split(' ') if x == 'False']) + int(lastround) == SUCCESSWEWANT:
                final = True
            return final
        count = 1
        lasttime = 0        
        checkthis, BOTTOM = pitychaintilldeath(lasttime, faith, *args) #first run
        print(checkthis) #print the string of results for the first batch of runs
        while TrueCount(checkthis, lasttime) == False:
            #print(count)
            count += 1
            lastttime += len([x for x in checkthis.split(' ') if x == 'True']) - len([x for x in checkthis.split(' ') if x == 'False'])+BOTTOM  #Update the trial number you previously were at!!!
            lasttime = max(lasttime,0)
            checkthis, BOTTOM = pitychaintilldeath(lasttime, faith, *args)
            print(checkthis)
        await ctx.send(count)
    else:
        await ctx.send(f"{ctx.author.mention}, nu. o3o")        


@client.command()
async def bottle(ctx):
    await ctx.author.send("Wassup? o3o")












@client.command()
async def SF(ctx):
    dictionary = {'150':{
    "No SafeGuard":
    {"0-15":
    {"51015":"Average 441m \n Median 334m \n ",
     "30% off":"Average 365m \n Median 284m \n ",
     "No boom":"Average 489m \n Median 370m \n "} ,
    "0-17":{"51015":"Average gldfjgdfsgm \n Median 334m \n ",
     "30% off":"Average 365m \n Median 284m \n ",
     "No boom":"Average 489m \n Median 370m \n "}

     },

     "SafeGuard":{"0-15":{"51015":"Average 718m \n Median 551m \n ",
      "30% off":"Average 615m \n Median 467m \n ",
      "No boom":"Average 490m \n Median 362m \n "}}}  ,

      '160':{
      "No SafeGuard":{"0-15":{"51015":"Average 441m \n Median 334m \n ",
       "30% off":"Average 365m \n Median 284m \n ",
       "No boom":"Average 489m \n Median 370m \n "}},

       "SafeGuard":{"0-15":{"51015":"Average 718m \n Median 551m \n ",
        "30% off":"Average 615m \n Median 467m \n ",
        "No boom":"Average 490m \n Median 362m \n "}}} }
    await ctx.send(f"``` Level of equipment: ```")
    def check(m):
        return m.content == m.content and m.author == ctx.author
    morecontent = await client.wait_for('message',check = check, timeout = 40.0)
    lvl = str(morecontent.content)
    await ctx.send(f"``` [0]SafeGuard or [1]No SafeGuard? Reply with either 0 or 1 pls o3o ```")
    morecontent = await client.wait_for('message',check = check, timeout = 40.0)
    safe = 'No SafeGuard'
    if int(morecontent.content)==0:safe='SafeGuard'
    await ctx.send(f"``` What enhancement level do you want...\n '0-15' \n '0-17' \n '0-22' \n '15-17' \n '15-16' \n '16-17' \n '15-22' ```")
    morecontent = await client.wait_for('message',check = check, timeout = 40.0)
    enhancement = str(morecontent.content)
    await ctx.send(f"```Any events? \n [0]'51015' \n [1]'30% off' \n [2] [3]'No Boom Event' \n [4]'No event' ```")
    listofevents = ["51015","30% off","No boom","No event"]
    morecontent = await client.wait_for('message',check = check, timeout = 40.0)
    event = listofevents[int(morecontent.content)]
    await ctx.send(f"```{dictionary[lvl][safe][enhancement][event]}```")

@client.command()
async def create(ctx, name="Output_from_Pulse"):
    guild = ctx.message.guild
    await guild.create_text_channel(str(name))
    existing_channel = discord.utils.get(ctx.guild.channels, name=str(name))
    iden = existing_channel.id
    schannel = client.get_channel(iden)
    await schannel.send("Hello!!!")
    time.sleep(3)
    if existing_channel is not None:
        await existing_channel.delete()

@client.command()
async def maplefandom(ctx, *argslist):
    args = ''
    try:
        userinput = int(argslist[-1])
        for i in argslist[:-2]:
            args += i + "+"
        args+= argslist[-2]
    except:
        userinput = 5
        for i in argslist[:-1]:
            args += i + "+"
        args+= argslist[-1]
    req = Request(f'https://maplestory.fandom.com/wiki/Special:Search?query={args.replace(" ","+")}&scope=internal&contentType=&ns%5B0%5D=0')
    uClient = urlopen(req)
    soup = BeautifulSoup(uClient.read(), 'html5lib')
    def edit(listentry):
        list1 = [x for x in listentry.split('\t') if x.__contains__('\n')==False if x!=''  ]
        # print(list1)
        string = ''
        for i in list1:
            string += i + " "
        return string
    def Titles(soupfunc):
        list1 = [x.text for x in soup.find_all('h1') if x['class'].__contains__('unified-search__result__header')] #names
        list2 = [x.a['href'] for x in soup.find_all('h1') if x['class'].__contains__('unified-search__result__header')] #links
        stringo = ""
        for i in range(len(list1)):
            stringo += f"[{i}]."+edit(list1[i]) + '\n '
        print(stringo)
        return [stringo, list2]
    stringtoprint, links = Titles(soup)
    await ctx.send(f"``` {stringtoprint} ```")
    def check(m):
        return m.content == m.content and m.author == ctx.author
    morecontent = await client.wait_for('message',check = check, timeout = 40.0)
    ans = int(morecontent.content)
    eligible = []
    for i in range(len(soup.find_all('a',{ "class", "result-link"}))):
        eligible.append(i)
    if ans in [x for x in range(len(links))]:
        # print(links[ans])
        url = links[ans]
        path = 'C:/Users/Irshad/Pictures/Saved Pictures/newpic.png'
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome('D:/chromedriver.exe',options=options)
        driver.get(url)
        height = driver.execute_script("return document.body.scrollHeight")  #some scrolling to lazy load
        numberofpicstomake = min(int(userinput),height//1000)
        driver.set_window_size(1000, height - 100)
        driver.execute_script("window.scrollTo(0, 100)")
        driver.execute_script("window.scrollTo(0, 0)")
        driver.set_window_size(1000, height)
        time.sleep(2) # new images need time to load
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
        tag = 'body'
        loopcount = 0
        while loopcount<1000:
            try:
                if driver.find_element(By.TAG_NAME, tag).screenshot(path): break
            except Exception:
                print("Looping Till Height")
                loopcount+=1
                tag+=' div'
        # driver.find_element(By.TAG_NAME, 'body').screenshot(path)
        driver.quit()
        def long_slice(image_path, out_name, outdir, slice_size):
            """slice an image into parts slice_size tall"""
            img = Image.open(image_path)
            width, height = img.size
            upper = 0
            left = 0
            slices = int(math.ceil(height/slice_size))

            count = 1
            listofsplits = []
            for slice in range(slices):
                #if we are at the end, set the lower bound to be the bottom of the image
                if count == slices:
                    lower = height
                else:
                    lower = int(count * slice_size)
                #set the bounding box! The important bit
                bbox = (left, upper, width, lower)
                working_slice = img.crop(bbox)
                upper += slice_size
                #save the slice
                newpath = f"{outdir}"+ "part" + f"{out_name}" + "_" + str(count)+".png"
                working_slice.save(os.path.join(newpath))
                listofsplits.append(newpath)
                count +=1
            return listofsplits

        # await ctx.send(file=discord.File(path))
        guild = ctx.message.guild
        stringthing = f"pulse_mstrat_output"
        await guild.categories[3].create_text_channel(stringthing)
        existing_channel = discord.utils.get(ctx.guild.channels, name=stringthing)
        iden = existing_channel.id
        schannel = client.get_channel(iden)
        await schannel.send(ctx.author.mention)
        for newpath in long_slice(path, "2_split", os.getcwd(), height//numberofpicstomake):
            await schannel.send(file=discord.File(newpath))
            os.remove(newpath)
        os.remove(path)
        time.sleep(180)
        await existing_channel.delete()

# @client.command(brief = "<no of runs until and INCLUDING the trial when you got the drop> <''> <''> ...",description="Please call this command together with all number of times you had to run in order to get your drop in question. The more times you have to provide for me to study, the better :D")
# async def droprate(ctx, *argslist):
#     args = []
#     try:
#         for i in argslist:
#             args.append(int(i))
#     except:
#         await ctx.send('```Something went wrong :c```')
#     print(args)
#     await ctx.send(f'`` mle/mme estimate of drop rate with given input is {len(args)/sum(args)*100}% ``')
#     await ctx.send(f'`` minimum variance unbiased estimator (mvue) estimate of drop rate with given input is {(len(args)-1)/(sum(args)-1)*100}% ``')
#     p1 = len(args)/sum(args)
#     p2 = (len(args)-1)/(sum(args)-1)
#     conf = [.5,.75,.90]
#     end = []
#     end2 = []
#     for i in conf:
#         end.append(np.log(1-i)/np.log(1-p1))
#         end2.append(np.log(1-i)/np.log(1-p2))
#     await ctx.send('B⃞    e⃞    e⃞    p⃞     b⃞    o⃞    o⃞    p⃞')
#     for i in range(len(end)):
#         await ctx.send(f'`` {conf[i]*100}% confidence that you will get a drop in {math.ceil(end[i])} runs :D - according to mme/mle prob =3=  ``')
#         await ctx.send(f'`` {conf[i]*100}% confidence that you will get a drop in {math.ceil(end2[i])} runs :D - according to mvue prob ``')
   


@client.command()
async def cam(ctx, website, userinput=5):
    url = website
    path = r"C:\Users\Victus\Desktop\PULSE\capture.png"
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(r'C:\Users\Victus\Desktop\chromedriver_win32\chromedriver.exe',options=options)
    driver.get(url)
    height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1000, height - 100)
    driver.execute_script(f"window.scrollTo(0, {height/2})")
    driver.execute_script("window.scrollTo(0, 0)")
    driver.set_window_size(1000, height)
    numberofpicstomake = min(int(userinput),height//1000)
    time.sleep(5) # new images need time to load
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
    tag = 'body'
    loopcount = 0
    while loopcount<1000:
        try:
            if driver.find_element(By.TAG_NAME, tag).screenshot(path): break
        except Exception:
            print("Looping Till Height")
            loopcount+=1
            tag+=' div'
    driver.quit()
    def long_slice(image_path, out_name, outdir, slice_size):
        """slice an image into parts slice_size tall"""
        img = Image.open(image_path)
        width, height = img.size
        upper = 0
        left = 0
        slices = int(math.ceil(height/slice_size))

        count = 1
        listofsplits = []
        for slice in range(slices):
            #if we are at the end, set the lower bound to be the bottom of the image
            if count == slices:
                lower = height
            else:
                lower = int(count * slice_size)
            #set the bounding box! The important bit
            bbox = (left, upper, width, lower)
            working_slice = img.crop(bbox)
            upper += slice_size
            #save the slice
            newpath = f"{outdir}"+ "part" + f"{out_name}" + "_" + str(count)+".png"
            working_slice.save(os.path.join(newpath))
            listofsplits.append(newpath)
            count +=1
        return listofsplits
    guild = ctx.message.guild
    stringthing = f"pulse_image_output"
    await guild.categories[4].create_text_channel(stringthing)
    existing_channel = discord.utils.get(ctx.guild.channels, name=stringthing)
    iden = existing_channel.id
    schannel = client.get_channel(iden)
    await schannel.send(ctx.author.mention)
    for newpath in long_slice(path, "2_split", os.getcwd(), height//numberofpicstomake):
        await schannel.send(file=discord.File(newpath))
        os.remove(newpath)
    os.remove(path)
    time.sleep(60)
    await existing_channel.delete()




@client.command()
async def hurricane(ctx):
    # await client.wait_until_ready()
    # while not client.is_closed():
    channel = client.get_channel(621332209592434688)  #Hurricane channel
    mainchannel = client.get_channel(83566743976411136)
    #Atlantic
    req = Request('https://www.nhc.noaa.gov/gtwo.php?basin=atlc&fdays=5')
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'lxml')


    atlantic_ = soup.find("div", {"class":"textproduct"})
    atlantic = atlantic_.text
    await channel.send(f'``Reports for Atlantic``')
    await channel.send(f'```{atlantic}```')




    req = Request('https://www.nhc.noaa.gov/gtwo.php?basin=epac&fdays=5')
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'lxml')


    EPacific_ = soup.find("div", {"class":"textproduct"})
    EPacific = EPacific_.text
    await channel.send(f'``Reports for East Pacific``')
    await channel.send(f'```{EPacific}```')




    req = Request('https://www.nhc.noaa.gov/gtwo.php?basin=cpac&fdays=5')
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'lxml')


    atlantic_ = soup.find("div", {"class":"textproduct"})
    atlantic = atlantic_.text
    await channel.send(f'``Reports for Central Pacific``')
    await channel.send(f'```{atlantic}```')




@client.command(brief = "<Channel Number you want to ping | 1-30> <Number of pings/samples you want>")
async def _maple_channel_ping_(ctx,channelno,NO):
    await ctx.send("``Commencing...``")
    N_TRIES = min(6*60**2/24, int(NO))
    x_axis = np.arange(1,N_TRIES+1)
    def check(name):
        return name[:7] == 'Channel'
    channel_ping = []
    for row in range(N_TRIES):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        link_template = f'https://xymu.github.io/maple.watch/#GMS-Reboot'
        driver = webdriver.Chrome(r'E:\chromedriver.exe', chrome_options=options)
        driver.get(link_template)
        no = 4.5
        try:
            WebDriverWait(driver, no).until(EC.presence_of_element_located((By.CLASS_NAME, 'container item__body--uZhP-')))
        except TimeoutException:
            print(f'Page timed out after {no} secs.')
        soup = BeautifulSoup(driver.page_source, 'html5lib')
        driver.quit()
        LEN = len(soup.find_all("article", {"class":"slow"}))
        source = [soup.find_all("article", {"class":"slow"})[x].span.text for x in range( LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
        PING = [int(soup.find_all("article", {"class":"slow"})[x].find('div', {'class':'time'}).text[:-2]) for x in range(LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
        for i in source:
            if check(i):
                if int(i.split(' ')[-1]) == int(channelno):
                    ind = int(i.split(' ')[-1])
                    channel_ping.append(PING[ind])
    arr = np.vstack((x_axis, np.array(channel_ping)))
    plt.style.use("seaborn-dark")
    plt.clf()
    plt.figure(figsize=(20,10)) #########Check this
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    plt.grid(color='#2A3459')
    # colors = random.choice(['#99fcff', '#fb53fe', "#FFE74C", "#FFFFFF", "#6BF178", "#BF0603", "#35A7FF", "#8447FF", "#D972FF", "#F6F930", "#D2F898", "#FCFCFC", "#ED4D6E", "#E9D6EC", "#59A96A", "#9BDEAC", "#B4E7CE", "#4392F1", "#61E786", "#E3EBFF", "#38369A", "#020887"])
    colors = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(200)])
    MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
    linestyle_tuple = [
     ((0, (1, 10))),
     ((0, (1, 1))),
     ((0, (1, 1))),
     ((0, (5, 10))),
     ((0, (5, 5))),
     ((0, (5, 1))),
     ((0, (3, 10, 1, 10))),
     ((0, (3, 5, 1, 5))),
     ((0, (3, 1, 1, 1))),
     ((0, (3, 5, 1, 5, 1, 5))),
     ((0, (3, 10, 1, 10, 1, 10))),
     ((0, (3, 1, 1, 1, 1, 1)))]
    plt.plot(arr[0], arr[1], color = colors, marker = MARK, linestyle = random.choice(linestyle_tuple))
    n_lines = 20
    diff_linewidth = 1.03
    alpha_value = 0.01
    for n in range(1, n_lines+1):
        plt.plot(arr[0],arr[1],marker=MARK,
                linewidth=2+(diff_linewidth*n),
                alpha=alpha_value,
                color=colors)
    plt.xlabel("Ping attempts")
    plt.ylabel("NZ ping/ms")
    plt.title(f"{ctx.message.author}\'s Request for Channel {channelno}'s relative ping over {NO} samples")
    plt.savefig(fname='plot')
    await ctx.send(file=discord.File('plot.png'))
    os.remove('plot.png')
    await ctx.send(f'``Channel {channelno} has a standard deviation of {np.std(channel_ping)} ms, given off of {N_TRIES} samples``')



@client.command(brief = "<Channel Number>", description = "This checks instantaneous ping of channel in perspective of author")
async def _maple_channel_ping(ctx, num):
    await ctx.send("``Commencing...``")
    def check(name):
        return name[:7] == 'Channel'
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    link_template = f'https://xymu.github.io/maple.watch/#GMS-Reboot'
    driver = webdriver.Chrome(r'D:\Tea\chromedriver.exe', options=options)
    driver.get(link_template)
    no = 4.5
    try:
        WebDriverWait(driver, no).until(EC.presence_of_element_located((By.CLASS_NAME, 'container item__body--uZhP-')))
    except TimeoutException:
        print(f'Page timed out after {no} secs.')
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    LEN = len(soup.find_all("article", {"class":"slow"}))
    source = [soup.find_all("article", {"class":"slow"})[x].span.text for x in range( LEN-10) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
    PING = [int(soup.find_all("article", {"class":"slow"})[x].find('div', {'class':'time'}).text[:-2]) for x in range(LEN-10) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
    await ctx.send(f"Relative ping of Channel {num} appears to be { PING[([int(x.split(' ')[-1]) for x in source]).index(int(num))] - min(PING) }" )






@client.command(brief = "<Number of pings/samples> <Order of norm>", description = "Order of norm is typically set to 2 to behave like standard deviation. If you want to penalize for bigger, more uncommon-ish spikes in ping, use higher order norms for this category (5++)")
async def _maple_channel_varlist(ctx, noofpings, power=2):
    msg = await ctx.send("``Commencing...``")
    N_TRIES = min(60**2, int(noofpings))
    matr = np.zeros([N_TRIES, 30])
    def check(name):
        return name[:7] == 'Channel'
    row = 0
    while row < N_TRIES:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        link_template = f'https://xymu.github.io/maple.watch/#GMS-Reboot'
        driver = webdriver.Chrome(r'D:\chromedriver.exe', chrome_options=options)
        driver.get(link_template)
        no = 4.5
        try:
            WebDriverWait(driver, no).until(EC.presence_of_element_located((By.CLASS_NAME, 'container item__body--uZhP-')))
        except TimeoutException:
            print(f'Page timed out after {no} secs.')
        soup = BeautifulSoup(driver.page_source, 'html5lib')
        driver.quit()
        LEN = len(soup.find_all("article", {"class":"slow"}))
        source = [soup.find_all("article", {"class":"slow"})[x].span.text for x in range( LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
        PING = [int(soup.find_all("article", {"class":"slow"})[x].find('div', {'class':'time'}).text[:-2]) for x in range(LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
        channels = []
        counterofchannels = 0
        for i in source:
            if check(i):
                counterofchannels += 1
                channels.append(int(i.split(' ')[-1]))
        # min(channels)
        try:
            number = min(channels)-1
            for j in channels:
                try:matr[row][j-1] += PING[number]
                except:print(f"row is {row}, j-1 is {j-1}, number is {number}, length of matr is {len(matr)}, len(PING) is {len(PING)}")
                # print(len(PING), max(channels))
                number+=1
            row+=1
        except:
            pass
    if int(power)==2:STD = [np.std([ping[channel] for ping in matr if ping[channel]!=0]) for channel in range(len(source))]
    else:
        MEAN = [np.median([ping[channel] for ping in matr if ping[channel]!=0]) for channel in range(len(source))]
        MINUS = [np.array(matr[:, channel]) /MEAN[channel] for channel in range(len(source))]
        def norm(array, dyn):
            sum=0
            for thing in array:
                sum+=thing**dyn
            return sum**(1/dyn)
        STD = [norm(error, int(power)) for error in MINUS]
    lowvar_channels = [int((source[channel]).split(" ")[-1]) for channel in range(len(source))]
    PARENT = sorted(zip(STD,lowvar_channels))
    channelsordered = [lowvar_channels for __,lowvar_channels in PARENT]
    testnumbers = [__ for __,lowvar_channels in PARENT]
    stringie = ''
    for i in range(len(channelsordered)):
        stringie += "Channel " + f"{channelsordered[i]}" +f" : [L{power} norm of {testnumbers[i]}]" '\n'
    await ctx.send(f"```ini\n{stringie}```  ")



@client.command(brief = "<Number of pings/samples> <Standard Deviation Cap>")
async def _maple_channel_varfilter(ctx, noofpings, std, bottom_std = 0, switch = 1):
    msg = await ctx.send("``Commencing...``")
    N_TRIES = min(60**2, int(noofpings))
    matr = np.zeros([N_TRIES, 30])
    def check(name):
        return name[:7] == 'Channel'
    row = 0
    while row < N_TRIES:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        link_template = f'https://xymu.github.io/maple.watch/#GMS-Reboot'
        driver = webdriver.Chrome(r'D:\chromedriver.exe', chrome_options=options)
        driver.get(link_template)
        no = 4.5
        try:
            WebDriverWait(driver, no).until(EC.presence_of_element_located((By.CLASS_NAME, 'container item__body--uZhP-')))
        except TimeoutException:
            print(f'Page timed out after {no} secs.')
        soup = BeautifulSoup(driver.page_source, 'html5lib')
        driver.quit()
        LEN = len(soup.find_all("article", {"class":"slow"}))
        source = [soup.find_all("article", {"class":"slow"})[x].span.text for x in range( LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
        PING = [int(soup.find_all("article", {"class":"slow"})[x].find('div', {'class':'time'}).text[:-2]) for x in range(LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
        channels = []
        counterofchannels = 0
        for i in source:
            if check(i):
                counterofchannels += 1
                channels.append(int(i.split(' ')[-1]))
        # min(channels)
        try:
            number = min(channels)-1
            for j in channels:
                try:matr[row][j-1] += PING[number]
                except:print(f"row is {row}, j-1 is {j-1}, number is {number}, length of matr is {len(matr)}, len(PING) is {len(PING)}")
                # print(len(PING), max(channels))
                number+=1
            row+=1
        except:
            pass
    STD = [np.std([ping[channel] for ping in matr if ping[channel]!=0]) for channel in range(len(source))]
    lowvar_channels = [int((source[channel]).split(" ")[-1]) for channel in range(len(source)) if STD[channel]<int(std) if STD[channel]>int(bottom_std)]
    x_axis = np.arange(1,N_TRIES+1) #####################
    linestyle_tuple = [
     ((0, (1, 10))),
     ((0, (1, 1))),
     ((0, (1, 1))),
     ((0, (5, 10))),
     ((0, (5, 5))),
     ((0, (5, 1))),
     ((0, (3, 10, 1, 10))),
     ((0, (3, 5, 1, 5))),
     ((0, (3, 1, 1, 1))),
     ((0, (3, 5, 1, 5, 1, 5))),
     ((0, (3, 10, 1, 10, 1, 10))),
     ((0, (3, 1, 1, 1, 1, 1)))]
    await ctx.send(f"```Dear {ctx.message.author},  The following channels fit your variance preference```")
    if int(noofpings)<21:plt.figure(figsize=(15,8))
    else:plt.figure(figsize=(25,10))
    plt.clf()
    plt.style.use("seaborn-dark")
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    for idx, row in enumerate(np.transpose(matr[:,[int(x-1) for x in lowvar_channels]])): #@@7z
        plt.grid(color='#2A3459')
        tem = " "
        for i in lowvar_channels:tem+=str(i) + ", "
        plt.title(f"Channels {tem}")
        number_of_colors = len(source)
        C0L = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(number_of_colors)])
        MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
        size = 12 #marker size
        if switch != 0: row = np.log(row);plt.ylabel("NZ ln(ping/ms)")
        else:plt.ylabel("NZ ping/ms")
        plt.plot(x_axis, row, label = f" Ch {lowvar_channels[idx]}", linestyle = random.choice(linestyle_tuple), marker = MARK, linewidth = 2.5, color = C0L, ms = size)
        n_lines = 15
        diff_linewidth = 1.02
        alpha_value = 0.02 #0.03
        for n in range(1, n_lines+1):
            plt.plot(x_axis,row,
                    linewidth=2+(diff_linewidth*n),
                    alpha=alpha_value,
                    color=C0L, ms = size)
        leg = plt.legend(loc='best', ncol=2, shadow=True, fancybox=True, prop={'size': 15})
        leg.get_frame().set_alpha(0.7)
        plt.xlabel("Ping attempts")

    plt.savefig(fname='plot')
    await msg.delete()
    await ctx.send(file=discord.File('plot.png'))
    os.remove('plot.png') ############





@client.command(brief = "<Number of pings/samples> <Standard Deviation Cap>")
async def _maple_channels_pings_(ctx, noofpings, channel1, channel2, switch = 0): #change switch number to anything but 0 to get log plot
    await ctx.send("``Commencing...``")
    N_TRIES = min(60**2, int(noofpings))
    matr = np.zeros([N_TRIES, 30])
    def check(name):
        return name[:7] == 'Channel'
    row = 0
    while row < N_TRIES:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        link_template = f'https://xymu.github.io/maple.watch/#GMS-Reboot'
        driver = webdriver.Chrome(r'D:\chromedriver.exe', chrome_options=options)
        driver.get(link_template)
        no = 4.5
        try:
            WebDriverWait(driver, no).until(EC.presence_of_element_located((By.CLASS_NAME, 'container item__body--uZhP-')))
        except TimeoutException:
            print(f'Page timed out after {no} secs.')
        soup = BeautifulSoup(driver.page_source, 'html5lib')
        driver.quit()
        LEN = len(soup.find_all("article", {"class":"slow"}))
        source = [soup.find_all("article", {"class":"slow"})[x].span.text for x in range( LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
        PING = [int(soup.find_all("article", {"class":"slow"})[x].find('div', {'class':'time'}).text[:-2]) for x in range(LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
        channels = []
        counterofchannels = 0
        for i in source:
            if check(i):
                counterofchannels += 1
                channels.append(int(i.split(' ')[-1]))
        # min(channels)
        try:
            number = min(channels)-1
            for j in channels:
                try:matr[row][j-1] += PING[number]
                except:print(f"row is {row}, j-1 is {j-1}, number is {number}, length of matr is {len(matr)}, len(PING) is {len(PING)}")
                # print(len(PING), max(channels))
                number+=1
            row+=1
        except:
            pass
    STD = [np.std([ping[channel] for ping in matr if ping[channel]!=0]) for channel in range(len(source))]
    lowvar_channels = [int(channel1), int(channel2)]
    x_axis = np.arange(1,N_TRIES+1) #####################
    linestyle_tuple = [
     ((0, (1, 10))),
     ((0, (1, 1))),
     ((0, (1, 1))),
     ((0, (5, 10))),
     ((0, (5, 5))),
     ((0, (5, 1))),
     ((0, (3, 10, 1, 10))),
     ((0, (3, 5, 1, 5))),
     ((0, (3, 1, 1, 1))),
     ((0, (3, 5, 1, 5, 1, 5))),
     ((0, (3, 10, 1, 10, 1, 10))),
     ((0, (3, 1, 1, 1, 1, 1)))]
    await ctx.send(f"```Dear {ctx.message.author},  The following channels fit your variance preference```")
    if int(noofpings)<21:plt.figure(figsize=(15,8))
    else:plt.figure(figsize=(25,10))
    plt.clf()
    plt.style.use("seaborn-dark")
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#212946'  # bluish dark grey
    for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9'  # very light grey
    for idx, row in enumerate(np.transpose(matr[:,[int(x-1) for x in lowvar_channels]])): #@@7z
        plt.grid(color='#2A3459')
        tem = " "
        for i in lowvar_channels:tem+=str(i) + ", "
        plt.title(f"Channels {tem}")
        number_of_colors = len(source)
        C0L = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(number_of_colors)])
        MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
        size = 12 #marker size
        if switch != 0: row = np.log(row);plt.ylabel("NZ ln(ping/ms)")
        else:plt.ylabel("NZ ping/ms")
        plt.plot(x_axis, row, label = f" Ch {lowvar_channels[idx]}", linestyle = random.choice(linestyle_tuple), marker = MARK, linewidth = 2.5, color = C0L, ms = size)
        n_lines = 15
        diff_linewidth = 1.02
        alpha_value = 0.02 #0.03
        for n in range(1, n_lines+1):
            plt.plot(x_axis,row,
                    linewidth=2+(diff_linewidth*n),
                    alpha=alpha_value,
                    color=C0L, ms = size)
        leg = plt.legend(loc='best', ncol=2, shadow=True, fancybox=True, prop={'size': 15})
        leg.get_frame().set_alpha(0.7)
        plt.xlabel("Ping attempts")

    plt.savefig(fname='plot')
    await ctx.send(file=discord.File('plot.png'))
    os.remove('plot.png') ############



@client.command(brief = '<Number of pings/samples you want> ', description = "This command pings all the channels in maple. Requires Duke role \n While more samples will give a better average, taking samples above 20 would likely lead you to getting ping behaviour that is rather different for the appx 1/2h or so that you are playing for. Channels are inconsistent. \n Number of pings recommended prior to doing a boss run for instance is probably about 20-30. \n Note also that each ping takes about 4.5 seconds")
@commands.has_role("Duke")
async def _maple_ping(ctx, noofpings, cute_norm = 2):    
    schannel = client.get_channel(892205198456533022)
    N_TRIES = min(60**2, int(noofpings))
    await schannel.send(f"``Commencing maple-reboot channel ping analysis for norm of {cute_norm} with {noofpings} pings...``")
    matr = np.zeros([N_TRIES, 30])
    def check(name):
        return name[:7] == 'Channel'
    row = 0
    while row < N_TRIES:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        link_template = f'https://xymu.github.io/maple.watch/#GMS-Reboot'
        driver = webdriver.Chrome(r'E:\chromedriver.exe', chrome_options=options)
        driver.get(link_template)
        no = 4.5
        try:
            WebDriverWait(driver, no).until(EC.presence_of_element_located((By.CLASS_NAME, 'container item__body--uZhP-')))
        except TimeoutException:
            print(f'Page timed out after {no} secs.')
        soup = BeautifulSoup(driver.page_source, 'html5lib')
        driver.quit()
        LEN = len(soup.find_all("article", {"class":"slow"}))
        source = [soup.find_all("article", {"class":"slow"})[x].span.text for x in range( LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
        print(len(source))
        PING = [int(soup.find_all("article", {"class":"slow"})[x].find('div', {'class':'time'}).text[:-2]) for x in range(LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
        channels = []
        counterofchannels = 0
        for i in source:
            if check(i):
                counterofchannels += 1
                channels.append(int(i.split(' ')[-1]))
        try:
            number = min(channels)-1
            for j in channels:
                matr[row][j-1] += PING[number]
                # print(len(PING), max(channels))
                number+=1
            row+=1
        except: pass
    MEAN = [np.median([ping[channel] for ping in matr if ping[channel]!=0]) for channel in range(len(source))] #changed from 30 to len(source) for longevity
    if int(cute_norm)==2:STD = [np.std([ping[channel] for ping in matr if ping[channel]!=0]) for channel in range(len(source))]
    else:
        MINUS = [np.array(matr[:, channel]) /MEAN[channel] for channel in range(len(source))]
        def norm(array, dyn):
            sum=0
            for thing in array:
                sum+=thing**dyn
            return sum**(1/dyn)
        STD = [norm(error, int(cute_norm)) for error in MINUS]
    #Let us try rearranging the parent matr matrix in order to get sexier plots. We shall use the standard dev values in STD!
    sortedmatrixsortof = [list(np.transpose(matr)[i-1]) for __,i in sorted(zip(STD,channels))]
    new_matr = np.zeros([len(source),N_TRIES])
    for i in range(len(new_matr)):
        for j in range(len(new_matr[i])):
            new_matr[i,j] += sortedmatrixsortof[i][j]
    Channelssorted = [i for __,i in sorted(zip(STD,channels))]
    x_axis = np.arange(1,N_TRIES+1) #####################
    linestyle_tuple = [
     ((0, (1, 10))),
     ((0, (1, 1))),
     ((0, (1, 1))),
     ((0, (5, 10))),
     ((0, (5, 5))),
     ((0, (5, 1))),
     ((0, (3, 10, 1, 10))),
     ((0, (3, 5, 1, 5))),
     ((0, (3, 1, 1, 1))),
     ((0, (3, 5, 1, 5, 1, 5))),
     ((0, (3, 10, 1, 10, 1, 10))),
     ((0, (3, 1, 1, 1, 1, 1)))]
    await schannel.send(f"```{ctx.message.author}'s Request for ping over {N_TRIES} samples with norm of {cute_norm} acquired!```")
    print(type(sortedmatrixsortof))
    # plt.figure(figsize=(4.1*2.5,4.1))
    if int(noofpings)<21:plt.figure(figsize=(15,8))
    else:plt.figure(figsize=(25,10))
    RAND = np.random.uniform(10,20)
    for repeat in range(3):
        plt.clf()
        plt.style.use("seaborn-dark")
        for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
            plt.rcParams[param] = '#212946'  # bluish dark grey
        for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
            plt.rcParams[param] = '0.9'  # very light grey
        split = 0
        for idx, row in enumerate(np.transpose(np.transpose(new_matr)[:,repeat*10:(repeat+1)*10])): #@@7z. Senpai wish me luck o3o
            plt.grid(color='#2A3459')
            if split <5:
                plt.subplot(1,2,1)
                stringofchannels = ''
                for i in range(5):
                    stringofchannels += f'{Channelssorted[repeat*10+i]}' + ', '
                plt.title(f"Channels {stringofchannels}")
                # plt.subplots_adjust(wspace=3, hspace=3)
            else:
                plt.subplot(1,2,2)
                stringofchannels = ''
                for i in range(5,10):
                    stringofchannels += f'{Channelssorted[repeat*10+i]}' + ', '
                plt.title(f"Channels {stringofchannels}")
                # plt.subplots_adjust(wspace=1, hspace=1)
            number_of_colors = len(source)
            C0L = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(number_of_colors)])
            # print(color)
            MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
            size = 12
            plt.ylabel("NZ ping/ms")
            plt.plot(x_axis, row, label = f" Ch {Channelssorted[repeat*10+idx]}", linestyle = random.choice(linestyle_tuple), marker = MARK, linewidth = 2.5, color = C0L, ms = size)
            n_lines = 12
            diff_linewidth = 1.02
            alpha_value = 0.02 #0.03
            for n in range(1, n_lines+1):
                plt.plot(x_axis,row,
                        linewidth=2+(diff_linewidth*n),
                        alpha=alpha_value,
                        color=C0L, ms = size)
            leg = plt.legend(loc='best', ncol=2, shadow=True, fancybox=True, prop={'size': 22})
            leg.get_frame().set_alpha(0.7)
            plt.xlabel("Ping attempts")

            #Here was the title line
            split+=1
        plt.savefig(fname='plot')
        await schannel.send(file=discord.File('plot.png'))
        os.remove('plot.png') ############
    STD = [np.std([ping[channel] for ping in matr if ping[channel]!=0]) for channel in range(len(source))]
    L10 = [norm(error, 10) for error in MINUS]
    await schannel.send(f'``The lowest mean server is Channel {MEAN.index(min(MEAN))+1}: with sd {STD[MEAN.index(min(MEAN))]}``')
    mean = np.copy(MEAN)
    await schannel.send(f'``Alternatives would be Channel {MEAN.index(sorted(mean)[1])+1}, {MEAN.index(sorted(mean)[2])+1}, or {MEAN.index(sorted(mean)[3])+1}``')
    await schannel.send(f'``The least variant server is Channel {STD.index(min(STD))+1}: {MEAN[STD.index(min(STD))] - MEAN[MEAN.index(min(MEAN))]}ms relative ping with sd {STD[STD.index(min(STD))]}``')
    std = np.copy(STD)
    await schannel.send(f'``Alternatives would be Channel {STD.index(sorted(std)[1])+1}, {STD.index(sorted(std)[2])+1}, or {STD.index(sorted(std)[3])+1}``')
    await schannel.send(f" `` --------------------------------------------------------------------------- ``")
    await schannel.send(f'``Fun fact: the channel with the highest ping is Channel {MEAN.index(max(MEAN))+1}: {MEAN[MEAN.index(max(MEAN))] - MEAN[MEAN.index(min(MEAN))]}ms relative ping with sd {STD[MEAN.index(max(MEAN))]}``')
    await schannel.send(f'``The channel with the most variant ping is Channel {STD.index(max(STD))+1}: {MEAN[STD.index(max(STD))] - MEAN[MEAN.index(min(MEAN))]}ms relative ping with sd {STD[STD.index(max(STD))]}``')
    source_copy = np.copy(source)
    await schannel.send(f" `` --------------------------------------------------------------------------- ``")
    UNS = [source_copy[unstable] for unstable in range(len(source_copy)) if L10[unstable] > 2]
    var = 2
    if len(UNS) >27:
        var = .75*(max(L10) - min(L10)) + min(L10)
        UNS = [source_copy[unstable] for unstable in range(len(source_copy)) if L10[unstable] > var]
    uns = " "
    for i in UNS: uns+=i + ", "
    ORDER_OF_CHAOS = [channel for _,channel in sorted(zip(L10, source_copy))]
    await schannel.send(f'**Warning**: ``Detecting severe relative instabilities in  {ORDER_OF_CHAOS[-1]}, {ORDER_OF_CHAOS[-2]}, or {ORDER_OF_CHAOS[-3]}!! \n List of Channels with >{var} L10 norm : {uns}``  ')
    await schannel.send(f'``Instead, consider these if anything else -  {ORDER_OF_CHAOS[0]}, {ORDER_OF_CHAOS[1]}, {ORDER_OF_CHAOS[2]}, or {ORDER_OF_CHAOS[3]}.``  ')





@client.command(brief = '<Number of pings/samples you want> ', description = "This command pings all the channels in maple. Requires Duke role \n While more samples will give a better average, taking samples above 20 would likely lead you to getting ping behaviour that is rather different for the appx 1/2h or so that you are playing for. Channels are inconsistent. \n Number of pings recommended prior to doing a boss run for instance is probably about 20-30. \n Note also that each ping takes about 4.5 seconds")
@commands.has_role("Duke")
async def _maple_ping_ordered(ctx, noofpings, switch = 1):
    schannel = client.get_channel(892205198456533022)
    await schannel.send("``Commencing...``")
    N_TRIES = min(60**2, int(noofpings))
    matr = np.zeros([N_TRIES, 30])
    def check(name):
        return name[:7] == 'Channel'
    row = 0
    while row < N_TRIES:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        link_template = f'https://xymu.github.io/maple.watch/#GMS-Reboot'
        driver = webdriver.Chrome(r'D:\chromedriver.exe', chrome_options=options)
        driver.get(link_template)
        no = 4.5
        try:
            WebDriverWait(driver, no).until(EC.presence_of_element_located((By.CLASS_NAME, 'container item__body--uZhP-')))
        except TimeoutException:
            print(f'Page timed out after {no} secs.')
        soup = BeautifulSoup(driver.page_source, 'html5lib')
        driver.quit()
        LEN = len(soup.find_all("article", {"class":"slow"}))
        source = [soup.find_all("article", {"class":"slow"})[x].span.text for x in range( LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
        PING = [int(soup.find_all("article", {"class":"slow"})[x].find('div', {'class':'time'}).text[:-2]) for x in range(LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
        channels = []
        counterofchannels = 0
        for i in source:
            if check(i):
                counterofchannels += 1
                channels.append(int(i.split(' ')[-1]))
        try:
            number = min(channels)-1
            for j in channels:
                matr[row][j-1] += PING[number]
                # print(len(PING), max(channels))
                number+=1
            row+=1
        except: pass
    MEAN = [np.median([ping[channel] for ping in matr if ping[channel]!=0]) for channel in range(len(source))] #changed from 30 to len(source) for longevity
    STD = [np.std([ping[channel] for ping in matr if ping[channel]!=0]) for channel in range(len(source))]
    x_axis = np.arange(1,N_TRIES+1) #####################
    linestyle_tuple = [
     ((0, (1, 10))),
     ((0, (1, 1))),
     ((0, (1, 1))),
     ((0, (5, 10))),
     ((0, (5, 5))),
     ((0, (5, 1))),
     ((0, (3, 10, 1, 10))),
     ((0, (3, 5, 1, 5))),
     ((0, (3, 1, 1, 1))),
     ((0, (3, 5, 1, 5, 1, 5))),
     ((0, (3, 10, 1, 10, 1, 10))),
     ((0, (3, 1, 1, 1, 1, 1)))]
    await schannel.send(f"```{ctx.message.author}'s Request for Relative ping over {N_TRIES} samples```")
    print(type(matr))
    # plt.figure(figsize=(4.1*2.5,4.1))
    if int(noofpings)<21:plt.figure(figsize=(15,8))
    else:plt.figure(figsize=(25,10))
    RAND = np.random.uniform(10,20)
    for repeat in range(3):
        plt.clf()
        plt.style.use("seaborn-dark")
        for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
            plt.rcParams[param] = '#212946'  # bluish dark grey
        for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
            plt.rcParams[param] = '0.9'  # very light grey
        split = 0
        for idx, row in enumerate(np.transpose(matr[:,repeat*10:(repeat+1)*10])): #@@7z
            plt.grid(color='#2A3459')
            if split <5:
                plt.subplot(1,2,1)
                plt.title(f"Channels {repeat*10+1} - {repeat*10+5}")
                # plt.subplots_adjust(wspace=3, hspace=3)
            else:
                plt.subplot(1,2,2)
                plt.title(f"Channels {repeat*10+6} - {(repeat+1)*10}")
                # plt.subplots_adjust(wspace=1, hspace=1)
            number_of_colors = len(source)
            C0L = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(number_of_colors)])
            # print(color)
            MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
            size = 12
            if (switch != 0) and (int(noofpings)<31):row = np.log(row);plt.ylabel("NZ ln(ping/ms)");
            elif switch != 0: row = np.log10(row)/np.log10(RAND);plt.ylabel("NZ log(ping/ms)");
            else:plt.ylabel("NZ ping/ms")
            plt.plot(x_axis, row, label = f" Ch {repeat*10+idx+1}", linestyle = random.choice(linestyle_tuple), marker = MARK, linewidth = 2.5, color = C0L, ms = size)
            n_lines = 12
            diff_linewidth = 1.02
            alpha_value = 0.02 #0.03
            for n in range(1, n_lines+1):
                plt.plot(x_axis,row,
                        linewidth=2+(diff_linewidth*n),
                        alpha=alpha_value,
                        color=C0L, ms = size)
            leg = plt.legend(loc='best', ncol=2, shadow=True, fancybox=True, prop={'size': 22})
            leg.get_frame().set_alpha(0.7)
            plt.xlabel("Ping attempts")

            #Here was the title line
            split+=1
        plt.savefig(fname='plot')
        await schannel.send(file=discord.File('plot.png'))
        os.remove('plot.png') ############
    await schannel.send(f'``The lowest mean server is Channel {MEAN.index(min(MEAN))+1}: with sd {STD[MEAN.index(min(MEAN))]}``')
    mean = np.copy(MEAN)
    await schannel.send(f'``Alternatives would be Channel {MEAN.index(sorted(mean)[1])+1}, {MEAN.index(sorted(mean)[2])+1}, or {MEAN.index(sorted(mean)[3])+1}``')
    await schannel.send(f'``The least variant server is Channel {STD.index(min(STD))+1}: {MEAN[STD.index(min(STD))] - MEAN[MEAN.index(min(MEAN))]}ms relative ping with sd {STD[STD.index(min(STD))]}``')
    std = np.copy(STD)
    await schannel.send(f'``Alternatives would be Channel {STD.index(sorted(std)[1])+1}, {STD.index(sorted(std)[2])+1}, or {STD.index(sorted(std)[3])+1}``')
    await schannel.send(f" `` --------------------------------------------------------------------------- ``")
    await schannel.send(f'``Fun fact: the channel with the highest ping is Channel {MEAN.index(max(MEAN))+1}: {MEAN[MEAN.index(max(MEAN))] - MEAN[MEAN.index(min(MEAN))]}ms relative ping with sd {STD[MEAN.index(max(MEAN))]}``')
    await schannel.send(f'``The channel with the most variant ping is Channel {STD.index(max(STD))+1}: {MEAN[STD.index(max(STD))] - MEAN[MEAN.index(min(MEAN))]}ms relative ping with sd {STD[STD.index(max(STD))]}``')
    MINUS = [np.array(matr[:, channel]) /MEAN[channel] for channel in range(len(source))]
    def norm(array, dyn):
        sum=0
        for thing in array:
            sum+=thing**dyn
        return sum**(1/dyn)
    L10 = [norm(error, 10) for error in MINUS]
    source_copy = np.copy(source)
    await schannel.send(f" `` --------------------------------------------------------------------------- ``")
    UNS = [source_copy[unstable] for unstable in range(len(source_copy)) if L10[unstable] > 2]
    var = 2
    if len(UNS) >27:
        var = .75*(max(L10) - min(L10)) + min(L10)
        UNS = [source_copy[unstable] for unstable in range(len(source_copy)) if L10[unstable] > var]
    uns = " "
    for i in UNS: uns+=i + ", "
    ORDER_OF_CHAOS = [channel for _,channel in sorted(zip(L10, source_copy))]
    await schannel.send(f'**Warning**: ``Detecting severe relative instabilities in  {ORDER_OF_CHAOS[-1]}, {ORDER_OF_CHAOS[-2]}, or {ORDER_OF_CHAOS[-3]}!! \n List of Channels with >{var} L10 norm : {uns}``  ')
    await schannel.send(f'``Instead, consider these if anything else -  {ORDER_OF_CHAOS[0]}, {ORDER_OF_CHAOS[1]}, {ORDER_OF_CHAOS[2]}, or {ORDER_OF_CHAOS[3]}.``  ')



@client.command()
async def unc(ctx, arg1, arg2, *args):
    n = len(args)
    Number = int(arg2.strip())
    limit = Number ** n
    if limit >=45000001:
        await ctx.send(f'No can do because arg2^no.(vectors) is greater than 45 million! In fact, it would take {limit/45E6 * 12.6} min to calculate your silly calculation.')
        if "duke" in [y.name.lower() for y in ctx.author.roles]:

            tsundere = await client.wait_for('message', timeout = 5.0, check = lambda message: message.author == ctx.author)
            tsun = tsundere.content
            if '0verride' or 'Override' in tsun:
                await ctx.send('UwU')
                await ctx.send(f'RIP. See ya in {limit/45E6 * 12.6}min')
                await ctx.send('https://66.media.tumblr.com/07e66b40902c48b64f603a4277ebdd71/tumblr_ouiyulleIv1s32c21o1_400.gif')
        else:
            return

    G = arg1.strip()
    Vs = []
    m = []
    err = []
    for Tp in args:
        Vs.append(Tp.strip().split(','))
    for V in Vs:
        m.append(float(V[0]))
        err.append(float(V[1]))

    v = []
    for i in range(n):
        low = m[i] - err[i]
        high = m[i] + err[i]
        v.append(np.linspace(low, high, Number))
        # print(v[0])

    # print(v)
    # print(v[0][1])

    all_perms = []
    answer = []
    TRUEanswer = []
    def brute_force(ls, indx, total, Vs):
    #ls must be empty list []
    #indx must be 0
    #total must be the number of vectors
    #print(f"{indx}/{total}")
        if len(answer)>1: return
        if indx>=total:
            all_perms.append(ls)
            if n == 3:
                fv = []
                for i in range(Number):
                    for j in range(Number):
                        for k in range(Number):
                            x1 = float(v[0][i])
                            x2 = float(v[1][j])
                            x3 = float(v[2][k])
                            f = ne.evaluate(G)
                            fv.append(f)

                if len(answer) <= 1:
                    fmax = np.max(fv)
                    fmin = np.min(fv)
                    main = np.average(fv)
                    amt = .5 * (fmax-fmin)
                    answer.append(main)
                    answer.append(amt)


                return answer
            elif n == 4:
                fv = []
                for i in range(Number):
                    for j in range(Number):
                        for k in range(Number):
                            for m in range(Number):
                                x1 = float(v[0][i])
                                x2 = float(v[1][j])
                                x3 = float(v[2][k])
                                x4 = float(v[3][m])
                                f = ne.evaluate(G)
                                fv.append(f)


                if len(answer) <= 1:
                    fmax = np.max(fv)
                    fmin = np.min(fv)
                    main = np.average(fv)
                    amt = .5 * (fmax-fmin)
                    answer.append(main)
                    answer.append(amt)


                return answer

            elif n == 5:
                fv = []
                for i in range(Number):
                    for j in range(Number):
                        for k in range(Number):
                            for m in range(Number):
                                for t in range(Number):
                                    x1 = float(v[0][i])
                                    x2 = float(v[1][j])
                                    x3 = float(v[2][k])
                                    x4 = float(v[3][m])
                                    x5 = float(v[4][t])
                                    f = ne.evaluate(G)
                                    fv.append(f)


                if len(answer) <= 1:
                    fmax = np.max(fv)
                    fmin = np.min(fv)
                    main = np.average(fv)
                    amt = .5 * (fmax-fmin)
                    answer.append(main)
                    answer.append(amt)


                return answer

            elif n == 6:
                fv = []
                for i in range(Number):
                    for j in range(Number):
                        for k in range(Number):
                            for m in range(Number):
                                for t in range(Number):
                                    for g in range(Number):
                                        x1 = float(v[0][i])
                                        x2 = float(v[1][j])
                                        x3 = float(v[2][k])
                                        x4 = float(v[3][m])
                                        x5 = float(v[4][t])
                                        x6 = float(v[5][g])
                                        f = ne.evaluate(G)
                                        fv.append(f)


                if len(answer) <= 1:
                    fmax = np.max(fv)
                    fmin = np.min(fv)
                    main = np.average(fv)
                    amt = .5 * (fmax-fmin)
                    answer.append(main)
                    answer.append(amt)


                return answer

            elif n == 7:
                fv = []
                for i in range(Number):
                    for j in range(Number):
                        for k in range(Number):
                            for m in range(Number):
                                for t in range(Number):
                                    for g in range(Number):
                                        for y in range(Number):
                                            x1 = float(v[0][i])
                                            x2 = float(v[1][j])
                                            x3 = float(v[2][k])
                                            x4 = float(v[3][m])
                                            x5 = float(v[4][t])
                                            x6 = float(v[5][g])
                                            x7 = float(v[6][y])
                                            f = ne.evaluate(G)
                                            fv.append(f)


                if len(answer) <= 1:
                    fmax = np.max(fv)
                    fmin = np.min(fv)
                    main = np.average(fv)
                    amt = .5 * (fmax-fmin)
                    answer.append(main)
                    answer.append(amt)
                    print(answer)

                return answer

            elif n == 8:
                fv = []
                for i in range(Number):
                    for j in range(Number):
                        for k in range(Number):
                            for m in range(Number):
                                for t in range(Number):
                                    for g in range(Number):
                                        for y in range(Number):
                                            for h in range(Number):
                                                x1 = float(v[0][i])
                                                x2 = float(v[1][j])
                                                x3 = float(v[2][k])
                                                x4 = float(v[3][m])
                                                x5 = float(v[4][t])
                                                x6 = float(v[5][g])
                                                x7 = float(v[6][y])
                                                x8 = float(v[7][h])
                                                f = ne.evaluate(G)
                                                fv.append(f)


                if len(answer) <= 1:
                    fmax = np.max(fv)
                    fmin = np.min(fv)
                    main = np.average(fv)
                    amt = .5 * (fmax-fmin)
                    answer.append(main)
                    answer.append(amt)
                    print(answer)

                return answer

            elif n == 9:
                fv = []
                for i in range(Number):
                    for j in range(Number):
                        for k in range(Number):
                            for m in range(Number):
                                for t in range(Number):
                                    for g in range(Number):
                                        for y in range(Number):
                                            for h in range(Number):
                                                for w in range(Number):
                                                    x1 = float(v[0][i])
                                                    x2 = float(v[1][j])
                                                    x3 = float(v[2][k])
                                                    x4 = float(v[3][m])
                                                    x5 = float(v[4][t])
                                                    x6 = float(v[5][g])
                                                    x7 = float(v[6][y])
                                                    x8 = float(v[7][h])
                                                    x9 = float(v[8][w])
                                                    f = ne.evaluate(G)
                                                    fv.append(f)


                if len(answer) <= 1:
                    fmax = np.max(fv)
                    fmin = np.min(fv)
                    main = np.average(fv)
                    amt = .5 * (fmax-fmin)
                    answer.append(main)
                    answer.append(amt)
                    print(answer)

                return answer

            elif n == 10:
                fv = []
                for i in range(Number):
                    for j in range(Number):
                        for k in range(Number):
                            for m in range(Number):
                                for t in range(Number):
                                    for g in range(Number):
                                        for y in range(Number):
                                            for h in range(Number):
                                                for w in range(Number):
                                                    for z in range(Number):
                                                        x1 = float(v[0][i])
                                                        x2 = float(v[1][j])
                                                        x3 = float(v[2][k])
                                                        x4 = float(v[3][m])
                                                        x5 = float(v[4][t])
                                                        x6 = float(v[5][g])
                                                        x7 = float(v[6][y])
                                                        x8 = float(v[7][h])
                                                        x9 = float(v[8][w])
                                                        x10 = float(v[9][z])
                                                        f = ne.evaluate(G)
                                                        fv.append(f)


                if len(answer) <= 1:
                    fmax = np.max(fv)
                    fmin = np.min(fv)
                    main = np.average(fv)
                    amt = .5 * (fmax-fmin)
                    answer.append(main)
                    answer.append(amt)
                    print(answer)

                return answer



        for Val in Vs[indx]:
            ls.append(Val)
            #print(ls)
            brute_force(ls, indx+1, total, Vs)
            ls=ls[0:indx]

    brute_force([],0,n,v)
    await ctx.send(f"```The main value and uncertainty is {answer}. Don't you think I am wrong or something! >:C ```")


@client.command()
async def horny(ctx, member : discord.Member, *, reason=None) :
    number = np.random.normal()
    string = random.choice([', pls stop the horny', 'has been reported to the horny police', f', this is your {int(abs(np.random.normal(15,10)))}th offence mister >:c'])
    await ctx.send(f"{member.mention} {string}")
    img = random.choice(['https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fexternal-preview.redd.it%2FuFki8hEItDYbcyk69ksbnynkrrLd4ftMjoMqTujpRcI.png%3Fwidth%3D960%26crop%3Dsmart%26auto%3Dwebp%26s%3D9feaf1201b644492ae14fb171ae2915e8d05b6e5&f=1&nofb=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.kym-cdn.com%2Fentries%2Ficons%2Foriginal%2F000%2F033%2F758%2FScreen_Shot_2020-04-28_at_12.21.48_PM.png&f=1&nofb=1', 'https://external-content.duckduckgo.com/iu?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.SjLRxLGl2VOOs9_YFG_56wHaFH%26pid%3DApi&f=1','https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpreview.redd.it%2Frhgquecla8051.png%3Fauto%3Dwebp%26s%3D4d58fe3769a99c76f11f70fc9d6093a472a0cd87&f=1&nofb=1', 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fmemes.ucoz.com%2F_nw%2F70%2F52768965.jpg&f=1&nofb=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.ebaumsworld.com%2FmediaFiles%2Fpicture%2F2452130%2F86400014.jpg&f=1&nofb=1'])
    await ctx.send(img)




@client.command()
async def tsun(ctx):
    channel = client.get_channel(621936276882456576)  #tsunamis
    req = Request('https://ptwc.weather.gov/feeds/ptwc_rss_pacific.xml')
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'lxml')
    content = soup.find_all("description")


    Desc = content[1].text
    Trudesc = Desc.split("\n")

    n = 0
    start = []
    end = []

    for i in Trudesc:
        n += 1
        if 'PRELIMINARY EARTHQUAKE PARAMETERS' in i:
            start.append(n)
        if 'NEXT UPDATE AND ADDITIONAL INFORMATION' in i:
            end.append(n)
            break

    str = ''
    for i in range(start[0]-1, end[0]-1):
        str += Trudesc[i]
        str += '\n'

    await channel.send(str)

    req = Request('https://ptwc.weather.gov/feeds/ptwc_rss_caribe.xml')
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'lxml')
    content = soup.find_all("description")


    Desc = content[1].text
    Trudesc = Desc.split("\n")

    n = 0
    start = []
    end = []

    for i in Trudesc:
        n += 1
        if 'PRELIMINARY EARTHQUAKE PARAMETERS' in i:
            start.append(n)
        if 'NEXT UPDATE AND ADDITIONAL INFORMATION' in i:
            end.append(n)
            break

    str = ''
    for i in range(start[0]-1, end[0]-1):
        str += Trudesc[i]
        str += '\n'

    await channel.send(str)




@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        return



    if client.user.mentioned_in(message):
        if message.content.lower().__contains__('boss'):
            await message.channel.send(f"{message.author.mention}``, are you going bossing, master?``")
            time.sleep(1)
            await message.channel.send("``Must be fun :>``")
            time.sleep(2)
            await message.channel.send("`` I do hope you don't forget your essentials though o3o ``")
            emb = discord.Embed(title = f"Boss Checklist", color = 0x594F4F)
            emb.add_field(name = '**Pre Bossing Checklist**', value = f'•All party members are there, except maybe Durex... :3\n •Potions and Legion Coupons \n •Buffs (Guild buffs, Tengu buff, Red pot perhaps) \n •Familiars \n •Hyperstat presets \n •Links \n •Legion \n •Matrix Skills' )
            emb.add_field(name = ' ** ** ', value = '** ** ** **')
            emb.add_field(name = ' ** ** ', value = '** ** ** **')
            emb.add_field(name = '**Post Bossing Checklist**', value = f'•Off pet loot \n •Drop Boosters Coupons \n•Holy Symbol \n •Greed Pendant' )
            emb.set_author(name = "Maple", icon_url = 'https://cdn.discordapp.com/attachments/891562421221732363/917317295079047168/template_1467542766v2.fw.png')
            await message.channel.send(content = None, embed = emb)

    if message.content.__contains__("Preact"):
        choices = ["┌─┐\n┴─┴\nಠ_ರೃ \n Oh, why...Hello to you too, good sir!", '{◕ ◡ ◕}']
        await message.channel.send(random.choice(choices))        

    if message.content.lower().__contains__("cleanup"):
        DukeVerification = [str(x) for x in message.author.roles].__contains__("Duke")
        print(DukeVerification)
        if DukeVerification:
            await message.channel.purge(limit=int(message.content[8:]))
            thing = await message.channel.send('``Cleared by`` {}'.format(message.author.mention))
            await thing.delete()        

    if message.content.startswith("Pstop") and Role(message, "Duke"):
        await client.logout()

    if message.content.startswith("MS"):
        noofpings = int(message.content[3:])
        await message.channel.send("``Commencing...``")
        N_TRIES = min(60**2, int(noofpings))
        matr = np.zeros([N_TRIES, 30])
        def check(name):
            return name[:7] == 'Channel'
        row = 0
        print(f"N_TRIES IS EQUAL TO {N_TRIES}")
        while row < N_TRIES:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            link_template = f'https://xymu.github.io/maple.watch/#GMS-Reboot'
            driver = webdriver.Chrome(executable_path = r'C:\Users\Victus\Desktop\chromedriver_win32\chromedriver.exe', chrome_options=options)
            driver.get(link_template)
            no = 4.5
            try:
                WebDriverWait(driver, no).until(EC.presence_of_element_located((By.CLASS_NAME, 'container item__body--uZhP-')))
            except TimeoutException:
                print(f'Page timed out after {no} secs.')
            soup = BeautifulSoup(driver.page_source, 'html5lib')
            print(soup)
            driver.quit()
            LEN = len(soup.find_all("article", {"class":"slow"}))
            source = [soup.find_all("article", {"class":"slow"})[x].span.text for x in range( LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
            PING = [int(soup.find_all("article", {"class":"slow"})[x].find('div', {'class':'time'}).text[:-2]) for x in range(LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
            channels = []
            counterofchannels = 0
            for i in source:
                if check(i):
                    counterofchannels += 1
                    channels.append(int(i.split(' ')[-1]))
            # min(channels)
            try:
                number = min(channels)-1
                for j in channels:
                    try:matr[row][j-1] += PING[number]
                    except:print(f"row is {row}, j-1 is {j-1}, number is {number}, length of matr is {len(matr)}, len(PING) is {len(PING)}")
                    # print(len(PING), max(channels))
                    number+=1
                row+=1
            except:
                pass
        STD = [np.std([ping[channel] for ping in matr if ping[channel]!=0]) for channel in range(len(source))]
        lowvar_channels = [int(channel1), int(channel2)]
        x_axis = np.arange(1,N_TRIES+1) #####################
        linestyle_tuple = [
        ((0, (1, 10))),
        ((0, (1, 1))),
        ((0, (1, 1))),
        ((0, (5, 10))),
        ((0, (5, 5))),
        ((0, (5, 1))),
        ((0, (3, 10, 1, 10))),
        ((0, (3, 5, 1, 5))),
        ((0, (3, 1, 1, 1))),
        ((0, (3, 5, 1, 5, 1, 5))),
        ((0, (3, 10, 1, 10, 1, 10))),
        ((0, (3, 1, 1, 1, 1, 1)))]
        await ctx.send(f"```Dear {ctx.message.author},  The following channels fit your variance preference```")
        if int(noofpings)<21:plt.figure(figsize=(15,8))
        else:plt.figure(figsize=(25,10))
        plt.clf()
        plt.style.use("seaborn-dark")
        for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
            plt.rcParams[param] = '#212946'  # bluish dark grey
        for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
            plt.rcParams[param] = '0.9'  # very light grey
        for idx, row in enumerate(np.transpose(matr[:,[int(x-1) for x in lowvar_channels]])): #@@7z
            plt.grid(color='#2A3459')
            tem = " "
            for i in lowvar_channels:tem+=str(i) + ", "
            plt.title(f"Channels {tem}")
            number_of_colors = len(source)
            C0L = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(number_of_colors)])
            MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
            size = 12 #marker size
            if switch != 0: row = np.log(row);plt.ylabel("NZ ln(ping/ms)")
            else:plt.ylabel("NZ ping/ms")
            plt.plot(x_axis, row, label = f" Ch {lowvar_channels[idx]}", linestyle = random.choice(linestyle_tuple), marker = MARK, linewidth = 2.5, color = C0L, ms = size)
            n_lines = 15
            diff_linewidth = 1.02
            alpha_value = 0.02 #0.03
            for n in range(1, n_lines+1):
                plt.plot(x_axis,row,
                        linewidth=2+(diff_linewidth*n),
                        alpha=alpha_value,
                        color=C0L, ms = size)
            leg = plt.legend(loc='best', ncol=2, shadow=True, fancybox=True, prop={'size': 15})
            leg.get_frame().set_alpha(0.7)
            plt.xlabel("Ping attempts")

        plt.savefig(fname='plot')
        await ctx.send(file=discord.File('plot.png'))
        os.remove('plot.png') ############    

    if message.content.lower().startswith("maplechannel"):
        channelno = int(message.content[13:14])
        NO = int(message.content[15:].replace(" ",""))
        print(NO)
        await message.channel.send("``Commencing...``")
        N_TRIES = min(6*60**2/24, int(NO))
        print(f"N_TRIES to iterate over is {N_TRIES}")
        x_axis = np.arange(1,N_TRIES+1)
        def check(name):
            return name[:7] == 'Channel'
        channel_ping = []
        for row in range(N_TRIES):
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            link_template = "https://xymu.github.io/maple.watch/#GMS-Reboot"
            # driver = webdriver.Chrome(r'C:\Users\Victus\Desktop\chromedriver_win32\chromedriver.exe', options=options)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(link_template)
            no = 4.5
            try:
                WebDriverWait(driver, no).until(EC.presence_of_element_located((By.CLASS_NAME, 'container item__body--uZhP-')))
            except TimeoutException:
                print(f'Page timed out after {no} secs.')
            print("Soup should be getting created as we speak...")
            soup = BeautifulSoup(driver.page_source, 'html5lib')
            print(soup)
            driver.quit()
            LEN = len(soup.find_all("article", {"class":"slow"}))
            source = [soup.find_all("article", {"class":"slow"})[x].span.text for x in range( LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
            PING = [int(soup.find_all("article", {"class":"slow"})[x].find('div', {'class':'time'}).text[:-2]) for x in range(LEN) if check(soup.find_all("article", {"class":"slow"})[x].span.text)]
            for i in source:
                if check(i):
                    if int(i.split(' ')[-1]) == int(channelno):
                        ind = int(i.split(' ')[-1])
                        channel_ping.append(PING[ind])
            print(PING)
        arr = np.vstack((x_axis, np.array(channel_ping)))
        print(arr)
        plt.style.use("seaborn-dark")
        plt.clf()
        plt.figure(figsize=(20,10)) #########Check this
        for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
            plt.rcParams[param] = '#212946'  # bluish dark grey
        for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
            plt.rcParams[param] = '0.9'  # very light grey
        plt.grid(color='#2A3459')
        # colors = random.choice(['#99fcff', '#fb53fe', "#FFE74C", "#FFFFFF", "#6BF178", "#BF0603", "#35A7FF", "#8447FF", "#D972FF", "#F6F930", "#D2F898", "#FCFCFC", "#ED4D6E", "#E9D6EC", "#59A96A", "#9BDEAC", "#B4E7CE", "#4392F1", "#61E786", "#E3EBFF", "#38369A", "#020887"])
        colors = random.choice(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])for i in range(200)])
        MARK = random.choice([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"])
        linestyle_tuple = [
        ((0, (1, 10))),
        ((0, (1, 1))),
        ((0, (1, 1))),
        ((0, (5, 10))),
        ((0, (5, 5))),
        ((0, (5, 1))),
        ((0, (3, 10, 1, 10))),
        ((0, (3, 5, 1, 5))),
        ((0, (3, 1, 1, 1))),
        ((0, (3, 5, 1, 5, 1, 5))),
        ((0, (3, 10, 1, 10, 1, 10))),
        ((0, (3, 1, 1, 1, 1, 1)))]
        plt.plot(arr[0], arr[1], color = colors, marker = MARK, linestyle = random.choice(linestyle_tuple))
        n_lines = 20
        diff_linewidth = 1.03
        alpha_value = 0.01
        for n in range(1, n_lines+1):
            plt.plot(arr[0],arr[1],marker=MARK,
                    linewidth=2+(diff_linewidth*n),
                    alpha=alpha_value,
                    color=colors)
        plt.xlabel("Ping attempts")
        plt.ylabel("NZ ping/ms")
        plt.title(f"{ctx.message.author}\'s Request for Channel {channelno}'s relative ping over {NO} samples")
        plt.savefig(fname='plot')
        await message.channel.send(file=discord.File('plot.png'))
        os.remove('plot.png')
        await message.channel.send(f'``Channel {channelno} has a standard deviation of {np.std(channel_ping)} ms, given off of {N_TRIES} samples``')        

    if message.content.lower().__contains__('fuck pulse'):
        await message.channel.send(f"{message.author.mention}``, now why would you say that? o3o``")


    if message.content.startswith('wf.wikia'):
        ctx = message.content[9:]
        ctx = ctx.replace(" ", "+")

        animalswikia = f'https://warframe.fandom.com/wiki/Special:Search?query={ctx}'

        print(animalswikia)

        Req = Request(animalswikia)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')
        soup.find_all('a',{ "class", "result-link"})[3]['href']
        if len(soup.find_all('a',{ "class", "result-link"})) >= 10:
            length = 10
        else:
            length = len(soup.find_all('a',{ "class", "result-link"}))

        list = []
        for i in range(length):
            list.append(soup.find_all('a',{ "class", "result-link"})[i]['href'])
            alpha = soup.find_all('li', {'class', 'result'})[i].a.text
            print(i,alpha)
            await channel.send(f'```{alpha}```')

        await channel.send("``Please choose one of the provided links: 0, 1, 2 etc ...``")
        def check(m):
            return m.content == m.content and m.channel == message.channel
        morecontent = await client.wait_for('message',check = check, timeout = 40.0)
        ans = int(morecontent.content)
        eligible = []
        for i in range(len(soup.find_all('a',{ "class", "result-link"}))):
            eligible.append(i)


#Going into the link perhaps
        if ans in eligible:
            await channel.send((soup.find_all('li', {'class', 'result'})[ans].a['href']))   #Post link for now
            animalswikia = soup.find_all('li', {'class', 'result'})[ans].a['href']
            Req = Request(animalswikia)
            uClient = urlopen(Req)
            soup = BeautifulSoup(uClient.read(), 'html5lib')

            isthereatable = len(soup.find_all('aside'))
            if isthereatable == 1:
                img = soup.aside.a['href']
                try:
                    for i in range(len(soup.aside.find_all('div', {'class','pi-item pi-data pi-item-spacing pi-border-color'}))):
                        thing = soup.aside.find_all('div', {'class','pi-item pi-data pi-item-spacing pi-border-color'})[i].div.text
                        Stat = soup.aside.find_all('div', {'class','pi-item pi-data pi-item-spacing pi-border-color'})[i].find_all('a')[-1].text
                        await channel.send(f'```{Stat} \n {thing} ```')
                except:
                    pass

    if 'o3o' in message.content.lower():
        choices = [ '(◯Δ◯∥)', '∑(ΦдΦlll', '（∂△∂；）', '(;Ⅲ□Ⅲ;)', '(=￣▽￣=)Ｖ', '(^ー^)ｖ', '(○ﾟε＾○)v', ':thumbsup:', 'ಠ‸ಠ', '(◎_◎;)?', '(⊙.☉)7', 'סּ_סּ' ]
        if np.random.normal()>-.8:await channel.send(random.choice(choices))

    if 'seppuku' in message.content or 'suicide' in message.content:
        await channel.send('https://tenor.com/view/spongebob-stabbing-himself-minul-mirdha-spongebob-suicide-gif-19249830')

    if message.content.lower().__contains__('spank'):
        if (message.author.bot  == False ):
            await channel.send('https://tenor.com/view/cats-funny-spank-slap-gif-15308590')


    if len([x for x in [message.content.lower().__contains__(i) for i in shock] if x==True])>.1:
        choices = ['ಠ‸ಠ', 'ಠnಠ', '( ಠ ಠ )', '༼ ಠل͟ಠ༽', '(╯°Д°）╯︵/(.□ . \)', '┌∩┐(ಠ_ಠ)┌∩┐', '┌─┐\n┴─┴\nಠ_ರೃ' ]
        await channel.send(random.choice(choices))

    if 'potato' in message.content.lower():
        if np.random.normal()>.6:
            await channel.send('https://cdn.discordapp.com/attachments/400673288768192524/855288890650001488/potato.gif')

    if len([x for x in [message.content.lower().__contains__(i) for i in ["can't stop me", "cant stop me"]] if x==True])>.1:
        if np.random.normal()>0.01:
            await channel.send('https://cdn.discordapp.com/attachments/891562421221732363/941219411203850270/temptation.JPG')

    if 'hi pulse' in message.content.lower() or 'Pulse' in message.content:
        choices = ['乁( ◔ ౪◔)ㄏ' ,'◔‿◔', '୧༼ಠ益ಠ༽୨', 'つ◕ل͜◕)つ', '☜(ಠ_ಠ☜)' ,  '( =￣+∇￣=)v']
        await channel.send(random.choice(choices))

    if 'sugoi' in message.content.lower() or 'wow' in message.content.lower():
        await channel.send('https://cdn.discordapp.com/attachments/400673288768192524/855288876888490014/jesus.gif')

    if 'sad' in message.content.lower():
        choices = ['◉︵◉', '(◕︵◕)', '༼இɷஇ༽']
        if np.random.normal()>0.2:await channel.send(random.choice(choices))

    if message.content.lower() in ['impossible', 'not possible', 'not possible', 'how?', 'not scientifically possible', 'shut yo mouth', 'shut your mouth']:
        await channel.send('https://cdn.discordapp.com/attachments/83566743976411136/858594186516758538/external-content.duckduckgo.com.gif')

    if 'facebook' in message.content.lower():
        await channel.send('(╯°□°)╯︵ ʞooqǝɔɐℲ')

    if message.content in NUG:
        choices = ['https://cdn.discordapp.com/attachments/224589445725290497/844208394524688414/NUGGET_00070.png', 'https://cdn.discordapp.com/attachments/224589445725290497/844208400531456000/NUGGET_00071.png', 'https://cdn.discordapp.com/attachments/224589445725290497/844208409125060646/NUGGET_00072.png', 'https://cdn.discordapp.com/attachments/224589445725290497/844208415097749574/NUGGET_00073.png','https://cdn.discordapp.com/attachments/224589445725290497/844208419954229295/NUGGET_00074.png', 'https://cdn.discordapp.com/attachments/224589445725290497/844208432055320576/NUGGET_00076.png', 'https://cdn.discordapp.com/attachments/224589445725290497/844208441030475776/NUGGET_00077.png', 'https://cdn.discordapp.com/attachments/224589445725290497/844208450052423681/NUGGET_00078.png', 'https://cdn.discordapp.com/attachments/224589445725290497/844208451868950548/NUGGET_00079.png', 'https://cdn.discordapp.com/attachments/224589445725290497/844208453492539443/NUGGET_00084.png', 'https://cdn.discordapp.com/attachments/224589445725290497/844208454067683348/NUGGET_00081.png', 'https://cdn.discordapp.com/attachments/224589445725290497/844208454201901056/NUGGET_00085.png', 'https://cdn.discordapp.com/attachments/224589445725290497/844208456483209247/NUGGET_00083.png', 'https://cdn.discordapp.com/attachments/224589445725290497/844208456574959676/NUGGET_00080.png', 'https://cdn.discordapp.com/attachments/224589445725290497/844208582211665970/NUGGET_00086.png', 'https://cdn.discordapp.com/attachments/224589445725290497/844208584949628988/NUGGET_00085.png', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flh5.googleusercontent.com%2Fproxy%2FtMn3SAXAdOVvt1sGcn-sk4tLiPISzDK7iANOFos0AmJLJ84wwXCjT03Er0YLZ-2dPcvH83AFhQJYu3A_eseQdVkTdiYlJTmFJnmflk1k4AwSKf9Tzo31XRl6TS-CHYpXhGg%3Ds0-d&f=1&nofb=1','https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcellbasedtech.com%2Fwp-content%2Fuploads%2F2019%2F11%2Fchicken-nugget.gif&f=1&nofb=1']
        await channel.send(random.choice(choices))
    if message.content.startswith('anima.wikia'):
        def x202(thingie):
            thing = thingie.replace('\n', '')
            thing = thing.replace('\t', '')
            news = thing.encode('ascii', 'ignore')
            encoding = 'utf-8'
            news = news.decode(encoding)
            return(news)
        ctx = message.content[12:]
        ctx = ctx.replace(" ", "+")

        animalswikia = f'https://animals.fandom.com/wiki/Special:Search?query={ctx}'

        print(animalswikia)

        Req = Request(animalswikia)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')
        if len(soup.find_all('li', {'class', 'unified-search__result'})) >= 10:
            length = 10
        else:
            length = len(soup.find_all('li', {'class', 'unified-search__result'}))

        list = []
        stringo = ''
        for i in range(length):
            list.append(soup.find_all('li', {'class' : 'unified-search__result'})[i].find('h1').a['href'])  #Title links
            alpha = x202(soup.find_all('li', {'class' : 'unified-search__result'})[i].find('h1').text)                 #Title names
            # await channel.send(f'```[{i}]. {alpha}```')                                #Titles with numbers now!!
            stringo+=f'[{i}]. {alpha}' + ' \n'
        await channel.send(f"```{stringo}```")

        def check(m):
            return m.content == m.content and m.channel == message.channel
        count = 0
        while(count<10000):
            try:
                await channel.send("``Please choose one of the provided links: 0, 1, 2 etc ...``")
                morecontent = await client.wait_for('message',check = check, timeout = 40.0)
                ans = int(float(morecontent.content))
                break
            except:
                if ans.lower().__contains__('stop'):break
                print("Float to int conversion failed!")
                count+=1
        print(ans)
        eligible = []
        for i in range(length):
            eligible.append(i)


        if ans in eligible:                                                     #After feedback has been given to expand on selected section of entry
            animalswikia = soup.find_all('li', {'class' : 'unified-search__result'})[ans].find('h1').a['href']

            print(animalswikia)

            Req = Request(animalswikia)
            uClient = urlopen(Req)
            soup = BeautifulSoup(uClient.read(), 'html5lib')


            try:
                list = []
                for element in soup.tbody.find_all('tr'):
                    if element.th != None:
                        pass
                    elif element.td.has_attr('colspan'):
                        pass
                    elif element.td.text == '\n':
                        pass
                    else:
                        list.append(element)

                categories = []
                categorienames = []
                for element in list:
                    categories.append(element.b.text)
                    categorienames.append(x202(element.text.replace(f'{element.b.text}', "")))

                colours = [0xE5FCC2, 0x9DE0AD   , 0x45ADA8, 0x68829E   , 0x547980   , 0x594F4F , 0x453f3f, 0x2A3132 ]      #Listofcoloursforembed anima wikia output
                emb = discord.Embed(title = f"Animal Wikia for {message.content[12:]}", color = random.choice(colours))
                for j in range(len(categories)):
                    emb.add_field(name = f'{categories[j]}', value = f'{categorienames[j]}' )

                for i in range(1,len(soup.find_all('img'))):
                    if soup.find_all('img')[i]['height'] == '75':              #To remove the first image in every anima wikia page. Best way to remove for now instead of identifying it with some other
                        pass
                    else:
                        image = soup.find_all('img')[i]['src']
                        if image.startswith('https'):
                            break
                        else:
                            pass

                titles = ''
                listformytitles = []
                soup.find_all("span", {"class", "mw-headline"})
                n = 0
                nlist = [0]
                for thing in soup.find_all("span", {"class", "mw-headline"}):                     #Listoftitles at end of output apparently
                    titles += f'[{n}]'+ '.' + str(thing['id']) + '.   '
                    listformytitles.append(thing['id'])
                    n += 1
                    nlist.append(n)                                                               #We have made 2 separate lists to try to make 2 optins for user to choose section to expand

                emb.set_image(url = f'{image}')

                await channel.send(content = None, embed = emb)
                try:
                    #Starter text from animal fandom
                    start = soup.find("div", {"class", "mw-content-ltr mw-content-text"}).table.next_sibling
                    end = soup.find("nav", {"class", "toc"}).previous
                    x = start
                    comp = [start]
                    while x != end:
                        x = x.next
                        comp.append(x)

                    print(type(str(comp[2])))
                    sr = ''
                    for part in comp:
                        if type(part) != bs4.element.NavigableString:
                            pass
                        else:
                            sr += str(part)


                    await channel.send(f'``{sr} ``')
                    await channel.send(f'```  {titles} ```')
                    print(f'{titles}')
                except:
                    pass
                    await channel.send(f'```  {titles}  ```')
                    print(f'{titles}')


# We have now the bot to go ahead and wait for user to ask to expand any sections below



                def check(m):
                    return m.content == m.content and m.channel == message.channel
                morecontent = await client.wait_for('message',check = check, timeout = 40.0)
                ans = (morecontent.content)


                if ans in listformytitles:
                    paragraphs = []
                    for element in soup.find('div', {"class", "mw-content-ltr mw-content-text"}).find_all('p'):
                        if element.text == '\n':
                            pass
                        else:
                            paragraphs.append(element)

                    n = 0
                    numberingofparagraphs = []
                    incels = []
                    for i in range(len(soup.find_all('span', {"class", "mw-headline"}))):
                        if n <= 0.9:
                            print(f'No matched paragraphs found for {i-1}th title')
                            incels.append(i-1)
                        n = 0
                        for j in range(len(paragraphs)):
                            if soup.find_all('span', {"class", "mw-headline"})[i].parent.next_sibling.next == paragraphs[j]:
                                numberingofparagraphs.append(j)
                                n += 1
                                break

                    del incels[0]
                    CHOOSE = []
                    for incel in incels:
                        for j in range(len(paragraphs)):
                            if soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break


                    thing = numberingofparagraphs
                    for i in range(len(CHOOSE)):
                        thing = thing[:incels[i]] + [CHOOSE[i]] + thing[incels[i]:]



                    for i in range(len(listformytitles)):
                        if ans == listformytitles[i]:
                            if thing[i] == thing[-1]:
                                for j in range(thing[i], len(paragraphs)):
                                    await channel.send(f'``{paragraphs[j].text} \n ``')
                            else:
                                for j in range(thing[i], thing[i+1]):
                                    await channel.send(f'``{paragraphs[j].text} \n ``')




# We use numbers to call titles out as well


                elif int(ans) in nlist:
                    ans = listformytitles[int(ans)]
                    paragraphs = []
                    for element in soup.find('div', {"class", "mw-parser-output"}).find_all('p'):     #All paragraphs presumably
                        if element.text == '\n':
                            pass
                        else:
                            paragraphs.append(element)

                    n = 0
                    numberingofparagraphs = []
                    incels = []
                    for i in range(len(soup.find_all('span', {"class", "mw-headline"}))):
                        if n <= 0.9:
                            print(f'No matched paragraphs found for {i-1}th title')
                            incels.append(i-1)
                        n = 0
                        for j in range(len(paragraphs)):
                            if soup.find_all('span', {"class", "mw-headline"})[i].parent.next_sibling.next == paragraphs[j]:
                                numberingofparagraphs.append(j)
                                n += 1
                                break

                    del incels[0]
                    CHOOSE = []
                    for incel in incels:
                        for j in range(len(paragraphs)):
                            if soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break


                    thing = numberingofparagraphs
                    for i in range(len(CHOOSE)):
                        thing = thing[:incels[i]] + [CHOOSE[i]] + thing[incels[i]:]



                    for i in range(len(listformytitles)):
                        if ans == listformytitles[i]:
                            if thing[i] == thing[-1]:
                                for j in range(thing[i], len(paragraphs)):
                                    await channel.send(f'``{paragraphs[j].text} \n ``')
                            else:
                                for j in range(thing[i], thing[i+1]):
                                    await channel.send(f'``{paragraphs[j].text} \n ``')








            except:
                await channel.send('``Page format does not include table or some other standard wikia format. Initiating alternative procedure...``')
                titles = ''
                listformytitles = []
                soup.find_all("span", {"class", "mw-headline"})
                for thing in soup.find_all("span", {"class", "mw-headline"}):
                    titles += str(thing['id']) + '.'
                    listformytitles.append(thing['id'])

                try:
                    #Starter text from animal fandom
                    start = soup.find("div", {"class", "mw-content-ltr mw-content-text"}).table.next_sibling
                    end = soup.find("nav", {"class", "toc"}).previous
                    x = start
                    comp = [start]
                    while x != end:
                        x = x.next
                        comp.append(x)

                    print(type(str(comp[2])))
                    sr = ''
                    for part in comp:
                        if type(part) != bs4.element.NavigableString:
                            pass
                        else:
                            sr += str(part)


                    await channel.send(f'``{sr} ``')
                    await channel.send(f'```  {titles} ```')
                    print(f'{titles}')
                except:
                    pass
                    await channel.send(f'```  {titles}  ```')
                    print(f'{titles}')


                def check(m):
                    return m.content == m.content and m.channel == message.channel
                morecontent = await client.wait_for('message',check = check, timeout = 40.0)
                ans = (morecontent.content)


                if ans in listformytitles:
                    paragraphs = []
                    for element in soup.find('div', {"class", "mw-parser-output"}).find_all('p'):
                        if element.text == '\n':
                            pass
                        else:
                            paragraphs.append(element)

                    n = 0
                    numberingofparagraphs = []
                    incels = []
                    for i in range(len(soup.find_all('span', {"class", "mw-headline"}))):
                        if n <= 0.9:
                            print(f'No matched paragraphs found for {i-1}th title')
                            incels.append(i-1)
                        n = 0
                        for j in range(len(paragraphs)):
                            if soup.find_all('span', {"class", "mw-headline"})[i].parent.next_sibling.next == paragraphs[j]:
                                numberingofparagraphs.append(j)
                                n += 1
                                break

                    del incels[0]
                    CHOOSE = []
                    for incel in incels:
                        for j in range(len(paragraphs)):
                            if soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break
                            elif soup.find_all('span', {"class", "mw-headline"})[incel].parent.next_sibling.next.next.next.next.next.next.next.next.next.next.next.next.next == paragraphs[j]:
                                CHOOSE.append(j)
                                break


                    thing = numberingofparagraphs
                    for i in range(len(CHOOSE)):
                        thing = thing[:incels[i]] + [CHOOSE[i]] + thing[incels[i]:]



                    for i in range(len(listformytitles)):
                        if ans == listformytitles[i]:
                            if thing[i] == thing[-1]:
                                for j in range(thing[i], len(paragraphs)):
                                    await channel.send(f'``{paragraphs[j].text} \n ``')
                            else:
                                for j in range(thing[i], thing[i+1]):
                                    await channel.send(f'``{paragraphs[j].text} \n ``')



    if message.content.startswith('anc.wikia'):

        def generalise(string):
            name = ''
            for i in string.h1.text.split('\n'):   #It finds the h1 title name and makes it into a text itself
                if i != '':
                    for j in i.split('\t'):
                        if j != '':
                            name+=j + ' '
            return name


        ctx = message.content[10:]
        ctx = ctx.replace(" ", "+")

        animalswikia = f'https://ancient-animals.fandom.com/wiki/Special:Search?query={ctx}'
        dinowikia = f'https://dinopedia.fandom.com/wiki/Special:Search?query={ctx}'
        # print(animalswikia)

        Req = Request(animalswikia)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')

        Req = Request(dinowikia)
        uClient = urlopen(Req)
        soup2 = BeautifulSoup(uClient.read(), 'html5lib')

        length = 0   #To find the titles and the length of the list of all of these titles from each of the 2 websites
        if len(soup.find_all('li', {'class', 'unified-search__result'})) >= 5:
            length += 5
        else:
            length += len(soup.find_all('li', {'class', 'unified-search__result'}))

        length2 = 0
        if len(soup2.find_all('li', {'class', 'unified-search__result'})) >= 15:
            length += 15
            length2 += 15
        else:
            length += len(soup2.find_all('li', {'class', 'unified-search__result'}))
            length2 += len(soup2.find_all('li', {'class', 'unified-search__result'}))

        # print(length, length2)
        list = []
        for i in range(length - length2):
            #list.append(soup.find_all('a',{ "class", "result-link"})[int(2*i)]['href'])
            list.append(soup.find_all('li', {'class', 'unified-search__result'})[i].a['href'])
            alpha = generalise(soup.find_all('li', {'class', 'unified-search__result'})[i])
            await channel.send(f'```[{i}]. {alpha}```')                                #Titles with numbers now!!

        for i in range(length2):
            list.append(soup2.find_all('li', {'class', 'unified-search__result'})[i].a['href'])
            alpha = generalise(soup2.find_all('li', {'class', 'unified-search__result'})[i])
            await channel.send(f'```[{i+length - length2}]. {alpha}```')                                #Titles with numbers now!!



        await channel.send("``Please choose one of the provided links: 0, 1, 2 etc ...``")


        def check(m):
            return m.content == m.content and m.channel == message.channel
        morecontent = await client.wait_for('message',check = check, timeout = 40.0)
        ans = int(morecontent.content)
        eligible = []
        eligible2 = []
        for i in range(length - length2):
            eligible.append(i)
        for i in range(length - length2, length):
            eligible2.append(i)



        if ans in eligible:
            animalswikia = soup.find_all("li", {"class":"unified-search__result"})[ans].a['href']
            print(animalswikia)

            Req = Request(animalswikia)
            uClient = urlopen(Req)
            soup = BeautifulSoup(uClient.read(), 'html5lib')

            if len(soup.find_all('table', {'class':'wikia-infobox'})) != 0:
                Classification = []
                Ans = []
                Titles = []
                nt = 0
                no = 0
                nolist = []
                yet = 0
                for element in soup.find_all('table', {'class':'wikia-infobox'}):
                    for part in element.find_all('tr'):
                        if len(part.find_all('th')) != 0:
                            if len(part.find_all('td')) != 0:
                                if part.th.has_attr('class') == False:
                                    if part.td.has_attr('class') == False:
                                        if part.div == None:
                                            Classification.append(part.th.text)
                                            Ans.append(part.td.text)
                                            no += 1
                            elif part.th.has_attr('class'):
                                if part.th['class'] == ['wikia-infobox-header']:
                                    if yet != 0:
                                        Titles.append(part.text)
                                        nt+=1
                                        nolist.append(no)
                                        no = 0
                                        yet += 1
                                    else:
                                        Titles.append(part.text)
                                        nt+=1
                                        no = 0
                                        yet += 1
                nolist.append(no)

                #Recursive way to export out the table values
                add = 0
                n = 0
                for ii in nolist:
                    prev = add
                    add += ii
                    # print('NEWLISTODESU')
                    colours = [0xF2F7F2, 0x7FB285   , 0xEDEEC0, 0xBCAA99   , 0x00171F  , 0x3066BE , 0x60AFFF, 0x832161, 0x28C2FF, 0x2AF5FF]
                    emb = discord.Embed(title = f"{Titles[n]} wikia findings...", color = random.choice(colours))
                    for element in range(prev, add):
                        emb.add_field(name = f'{Classification[element]}', value = f'{Ans[element]}' )
                    emb.set_author(name = "Novum", icon_url = "https://cdn.discordapp.com/attachments/83566743976411136/650138167403479050/m8.png")
                    await channel.send(content = None, embed = emb)
                    n += 1



        elif ans in eligible2:
            def filtern(string):
                list = string.split('\n')
                for thing in list:
                    if thing == '':
                        list.remove(thing)

                for element in list:
                    list = element.split(' ')
                    for thing in list:
                        if thing == '':
                            list.remove(thing)
                return list

            def filtern2(string):
                list = string.split('\n')
                for thing in list:
                    if thing == '':
                        list.remove(thing)

                for element in list:
                    list = element.split(' ')
                    for thing in list:
                        if thing == '':
                            list.remove(thing)

                str = ''
                for i in list:
                    str += f'{i}' + ' '
                return str

            def green(ele):   #On 'tr' results
                return len(ele.find_all('th'))

            def greenno():    #I think this calculated the number of table elements
                no = 0
                for i in soup.find_all('tr'):
                    if green(i) != 0:
                        no+= 1

                return no

            def Tits():
                list = []
                begin = 0
                n = 0
                if len(soup.find_all('table',{'class':'infobox'})) >= 1:
                    for i in soup.find_all('tr'):
                        n+=1
                        if filtern2(i.text) == 'Scientific classification ':
                            list.append(f'Scientific classification ' + '/' + f'{n-1}')
                            begin += 1
                            break

                if begin!=0:
                    for i in range(n, len(soup.find_all('tr'))):
                        if len(list) <= greenno() -2:
                            if green(soup.find_all('tr')[i]) != 0:
                                str = filtern2(soup.find_all('tr')[i].text)
                                newstr = str + '/' + f'{i}'
                                list.append(newstr)
                                # print((soup.find_all('tr')[i].text))
                                # print(list)


                return list



            print(length2)
            print(length)
            print(ans)
            animalswikia = soup2.find_all("li", {"class":"unified-search__result"})[ans-length+length2].a['href']
            print(animalswikia)

            Req = Request(animalswikia)
            uClient = urlopen(Req)
            soup = BeautifulSoup(uClient.read(), 'html5lib')

###

            Class = []
            Ans = []
            for element in soup.find('table', {'class':'infobox'}).find_all('tr'):
                if len(element.find_all('td')) == 2:
                    Class.append(element.find_all('td')[0].text.split('\n')[0])
                    Ans.append(element.find_all('td')[1].text)

            colours = [0xF2F7F2, 0x7FB285   , 0xEDEEC0, 0xBCAA99   , 0x00171F  , 0x3066BE , 0x60AFFF, 0x832161, 0x28C2FF, 0x2AF5FF]
            emb = discord.Embed(title = f"{soup.find('h1').text} wikia findings...", color = random.choice(colours))
            emb.set_author(name = "Novum", icon_url = "https://cdn.discordapp.com/attachments/83566743976411136/650138167403479050/m8.png")
            for element in range(len(Class)):
                emb.add_field(name = f'{Class[element]}', value = f'{Ans[element]}' )


            imgcount = 0
            img = []
            row = 0
            for element in soup.find('table', {'class':'infobox'}).find_all('tr'):
                row += 1
                if len(element.find_all('a')) >= 0.1:
                    for thing in element.find_all('a'):
                        if thing.has_attr('title') == False:
                            imgcount += len(element.find_all('a'))
                            img.append(thing['href'])
                    if imgcount >= 1.1:
                        print(f'There are {imgcount} images in the table section for the {row}th row.')

            emb.set_thumbnail(url = f'{img[0]}')

            conditionforsynonym = 0
            for i in range(len(soup.find_all('tr'))):
                if filtern2(soup.find_all('tr')[i].text) == 'Synonyms ':
                    conditionforsynonym += i

            if conditionforsynonym != 0:
                if len(soup.find_all('tr')[conditionforsynonym+1].find_all('p')) >= 1:
                    left = []
                    right = []
                    for i in range(len(soup.find_all('tr')[conditionforsynonym+1].find_all('p'))):
                        left.append(soup.find_all('tr')[conditionforsynonym+1].find_all('p')[i].text)
                        try:
                            right.append(soup.find_all('tr')[conditionforsynonym+1].find_all('ul')[i].text)
                        except:
                            right.append('Nil')

                    for i in range(len(left)):
                        emb.add_field(name = f'{left[i]}', value = f'{right[i]}' )


            await channel.send(content = None, embed = emb)


    if message.content.startswith('anc.tax'):
        def x202(thingie):
            thing = thingie.replace('\n', ' ')
            news = thing.encode('ascii', 'ignore')
            encoding = 'utf-8'
            news = news.decode(encoding)
            return(news)

        # await channel.send(f'{message.content[8]}')
        # await channel.send(f'{message.content[8:]}')
        animalswikia = f'http://www.prehistoric-wildlife.com/species/{message.content[8]}/{message.content[8:]}.html'
        Req = Request(animalswikia)
        uClient = urlopen(Req)
        soup = BeautifulSoup(uClient.read(), 'html5lib')

        #Table results : Universal
        c = 0
        Tibble = []
        TibbleRes = []
        while c!= 1:
            for item in soup.find_all('b'):
                Tibble.append(item.text)
                if item.next_sibling == ' ':
                    # print(item.text, item.next_sibling.next_sibling.text, 'method0')
                    TibbleRes.append(item.next_sibling.next_sibling.text)
                else:
                    try:
                        # print(item.text, x202(item.next_sibling.text), 'method1')
                        TibbleRes.append(x202(item.next_sibling.text))
                    except:
                        # print(item.text, x202(item.next_sibling), 'method3')
                        TibbleRes.append(x202(item.next_sibling))
                if item.text == 'Fossil representation:':
                    c += 1
                    break

        #Diagnostics: 0 images, 1 image, multiple images +/- multiple paragraphs?
        n = len(soup.find_all('img'))-3
        list = soup.find_all('img')
        for i in range(len(soup.find_all('img'))):
            string = soup.find_all('img')[i]['src']
            listofwords = string.split('/')
            if 'r_nav_link_images' in listofwords:
                n -= 1
                list.remove(soup.find_all('img')[i])
        # n = number of bodyline images, including the center top image, list is later to be made into finallist of full links below
        finallist = []
        for i in range(3, len(list)):
            eg = list[i]
            egg = eg['src']
            link = 'http://www.prehistoric-wildlife.com/images' + egg.split('images')[-1]
            finallist.append(link)

        def chunks(s, n):                                        #To split long paragraphs of information into chunks of 1980 chars down in "for chunk in chunks(text, __)"
            for start in range(0, len(s), n):
                yield s[start:start+n]

        def Title(x):                                                       #Finding title by finding the bold text within the left aligned paras
            ptit = soup.find_all('p', {'align':'left'})[x].b
            if ptit != None:
                thingie = ptit.text
                thing = thingie.replace('\n', ' ')
                news = thing.encode('ascii', 'ignore')
                encoding = 'utf-8'
                news = news.decode(encoding)

                return news
            else:
                return "There is no title for this paragraph"

        ntitles = -1                                                         #How many multiple titles are there in the body of text?
        for i in range(1, len(soup.find_all('p', {'align':'left'}))):
            if Title(i) != 'There is no title for this paragraph':
                ntitles+=1
            else:
                pass

        if n <= .9:
            print('No images found')

            colours = [0xF2F7F2, 0x7FB285   , 0xEDEEC0, 0xBCAA99   , 0x00171F  , 0x3066BE , 0x60AFFF, 0x832161, 0x28C2FF, 0x2AF5FF]
            emb = discord.Embed(title = f"Excavated {message.content[8:]} returned findings...", color = random.choice(colours))
            for element in range(len(Tibble)):
                emb.add_field(name = f'{Tibble[element]}', value = f'{TibbleRes[element]}' )
            emb.set_author(name = "Novum", icon_url = "https://cdn.discordapp.com/attachments/83566743976411136/650138167403479050/m8.png")
            await channel.send(content = None, embed = emb)
            #In the case that we have 1 paragraph in entire article : Most common
            listofps = soup.find_all('p')
            for i in range(len(listofps)):
                if len(soup.find_all('p')[i].find_all('b')) == 0:     #Is there any bold chars inside para? o3o If not, then it is likely the para we want for expanded info
                    # print(soup.find_all('p')[i].text)
                    TT = soup.find_all('p')[i].text
                    TT = TT.replace('\n', ' ')
                    TT = TT.replace('\xa0', '')
                    for chunk in chunks(TT, 1980):
                        await channel.send(f'``{chunk}``')
                    # print(TT)
                else:
                    pass


#This is to cover cases whereby there is at least 1 image BUT there are not multiple subtitles within the subtext
        elif ntitles <= 0:
            print(n)
            colours = [0xF2F7F2, 0x7FB285   , 0xEDEEC0, 0xBCAA99   , 0x00171F  , 0x3066BE , 0x60AFFF, 0x832161, 0x28C2FF, 0x2AF5FF]
            emb = discord.Embed(title = f"Excavated {message.content[8:]} returned findings...", color = random.choice(colours))
            for element in range(len(Tibble)):
                emb.add_field(name = f'{Tibble[element]}', value = f'{TibbleRes[element]}' )
            emb.set_thumbnail(url = f'{finallist[0]}')
            emb.set_author(name = "Novum", icon_url = "https://cdn.discordapp.com/attachments/83566743976411136/650138167403479050/m8.png")
            if n == 1:
                await channel.send(content = None, embed = emb)
            elif n == 2:
                emb.set_image(url = finallist[1])
                await channel.send(content = None, embed = emb)
            elif n >= 2:
                emb.set_image(url = finallist[1])
                await channel.send(content = None, embed = emb)
                for i in range(2, n):
                    await channel.send(finallist[i])
            listofps = soup.find_all('p')
            for i in range(len(listofps)):
                if len(soup.find_all('p')[i].find_all('b')) == 0:     #Is there any bold chars inside para? o3o If not, then it is likely the para we want for expanded info
                    # print(soup.find_all('p')[i].text)
                    TT = soup.find_all('p')[i].text
                    TT = TT.replace('\n', ' ')
                    TT = TT.replace('\xa0', '')
                    for chunk in chunks(TT, 1980):
                        await channel.send(f'``{chunk}``')
                    # print(TT)
                else:
                    pass




        else:
            print('fag')
            print(n)
            print(ntitles)
            colours = [0xF2F7F2, 0x7FB285   , 0xEDEEC0, 0xBCAA99   , 0x00171F  , 0x3066BE , 0x60AFFF, 0x832161, 0x28C2FF, 0x2AF5FF]
            emb = discord.Embed(title = f"Excavated {message.content[8:]} returned findings...", color = random.choice(colours))
            for element in range(len(Tibble)):
                emb.add_field(name = f'{Tibble[element]}', value = f'{TibbleRes[element]}' )
            emb.set_author(name = "Novum", icon_url = "https://cdn.discordapp.com/attachments/83566743976411136/650138167403479050/m8.png")
            emb.set_thumbnail(url = f'{finallist[0]}')
            if n == 1:
                await channel.send(content = None, embed = emb)
            elif n == 2:
                emb.set_image(url = finallist[1])
                await channel.send(content = None, embed = emb)
            elif n >= 2:
                emb.set_image(url = finallist[1])
                await channel.send(content = None, embed = emb)
                for i in range(2, n):
                    await channel.send(finallist[i])

#THe paragraphs associated with each TItle
            arbitrary = 1
            yet = 0
            listofpara = []
            listoftits = []
            for i in range(1, len(soup.find_all('p', {'align':'left'}))):
                if Title(i) != 'There is no title for this paragraph':
                    yet += 1
                    listoftits.append(Title(i))
                    textie = soup.find_all('p', {'align':'left'})[i].text
                    listofpara.append(x202(textie.split(soup.find_all('p', {'align':'left'})[i].next.text)[-1]))
                elif yet == 0:
                    listofpara.append(x202(soup.find_all('p', {'align':'left'})[i].text) + '\n')
                    arbitrary = 0
                else:
                    listofpara[-1] += '\n' + x202(soup.find_all('p', {'align':'left'})[i].text)

            if arbitrary == 0:
                for chunk in chunks(listofpara[0], 1980):
                    await channel.send(f'``{chunk}``')
                del listofpara[0]


            await channel.send(f'There appear to be {ntitles} within this library that you can expand')



            read = ''
            para = []
            for i in range(len(listoftits)-1):
                read += f'[{i}]. ' + listoftits[i] + '\n'
                para.append(i)

            await channel.send(f'```{read}```')
            def check(m):
                return m.content == m.content and m.channel == message.channel
            morecontent = await client.wait_for('message',check = check, timeout = 40.0)
            ans = (morecontent.content)

            if int(ans) in para:
                send = int(ans)
                await channel.send(f'**{listoftits[send]}**')
                text = listofpara[send]
                if len(text) >= 2000:
                    for chunk in chunks(text, 1980):
                        await channel.send(f'``{chunk}``')
                else:
                    await channel.send(f'``{text}``')






    await client.process_commands(message)


asyncio.run(main())
client.run(####YOUR TOKEN HERE#####')