import os, re #, csv, json, sys, string
import numpy as np
import pandas as pd
#import spacy as sp
#from collections import defaultdict, Counter

#import gzip

from tqdm import tqdm

#import pickle as pkl
from argparse import ArgumentParser
import logging
import alsatian_tokeniser as als_t

tqdm.pandas()
#nlp_fr = sp.load("fr_core_news_sm")

parser = ArgumentParser()
parser.add_argument('--dataPath', help='path to CSV data file with texts')
parser.add_argument('--lexPath', help='path to lexicon. CSV with columns "word" plus emotion columns')
parser.add_argument('--lexNames', nargs="*", type=str, help='Names of the lexicons/column names in the lexicon CSV')
parser.add_argument('--savePath', help='path to save folder')

def read_lexicon(path, LEXNAMES):
    df = pd.read_csv(path)
    df = df[~df['word'].isna()]
    df = df[['word']+LEXNAMES]
    df['word'] = [x.lower() for x in df['word']]
    return df
    # df = df[~df['val'].isna()]

def prep_dim_lexicon(df, dim):
    ldf = df[['word']+[dim]]
    ldf = ldf[~ldf[dim].isna()]
    ldf.drop_duplicates(subset=['word'], keep='first', inplace=True)
    ldf[dim] = [float(x) for x in ldf[dim]]
    ldf.rename({dim: 'val'}, axis='columns', inplace=True)
    ldf.set_index('word', inplace=True)
    return ldf

def get_alpha(token):
    return token.isalpha()


def get_vals(twt, lexdf, idf_coeff):
    ret = als_t.RegExpTokeniser()
    phrase = (ret.tokenise(twt.lower())).get_contents()
    tt = re.split("[,|.| |?|!|\n|\"|…|;|:]", phrase)
    
    #tt = twt.lower().split(" ") # maybe use spacy to tokenize here
    at = [w for w in tt if w != ""] # compter num de tokens

    pw = [x for x in tt if x in lexdf.index] # contient tous les mots parcourus
    pv_ori = [lexdf.loc[w]['val'] for w in pw]
    pv = [lexdf.loc[w]['val']*idf_coeff[w]*10 for w in pw if w in idf_coeff] # contient coeffs de chaque mots
    #print(pv_ori)
    #print(pv)


    numTokens = len(at)
    numLexTokens = len(pw)
    
    avgLexVal = np.mean(pv)  # nan for 0 tokens

    return [numTokens, numLexTokens, avgLexVal]


def process_df(df, lexdf, idf_coeff):
    logging.info("Number of rows: " + str(len(df)))

    
    resrows = [get_vals(x, lexdf, idf_coeff) for x in df['text']] # tokenisation
    resrows = [x + y for x,y in zip(df.values.tolist(), resrows)]

    resdf = pd.DataFrame(resrows, columns=df.columns.tolist() + ['numTokens', 'numLexTokens', 'avgLexVal'])
    resdf = resdf[resdf['numLexTokens']>=1]
    
    resdf['lexRatio'] = resdf['numLexTokens']/resdf['numTokens']
    return resdf

def main(dataPath, LEXICON, LEXNAMES, savePath):

    os.makedirs(savePath, exist_ok=True)

    logfile = os.path.join(savePath, 'log.txt')

    logging.basicConfig(filename=logfile, format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
    
    df = pd.read_csv(dataPath)

    idf_df = pd.read_csv("idf_info.csv", index_col=0, encoding="utf-8")
    idf_coeff = idf_df.loc[savePath+".txt"][:]
    #print(idf_coeff.loc['uff'])

    for LEXNAME in LEXNAMES:

        lexdf = prep_dim_lexicon(LEXICON, LEXNAME)
        logging.info(LEXNAME + " lexicon length: " + str(len(lexdf)))
        resdf = process_df(df, lexdf, idf_coeff)
    
        resdf.to_csv(os.path.join(savePath, LEXNAME+'.csv'), index=False)

if __name__=='__main__':
    args = parser.parse_args()

    dataPath = args.dataPath
    lexPath = args.lexPath

    LEXNAMES = args.lexNames
    LEXICON = read_lexicon(lexPath, LEXNAMES)

    savePath = args.savePath

    main(dataPath, LEXICON, LEXNAMES, savePath)