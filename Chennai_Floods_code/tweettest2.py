import sys
import json
import argparse
import re
from datetime import datetime

# arguments
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', required=True,
    help = 'name of file with tweets in json format')
parser.add_argument('-oe', '--outputedges', default='edges.csv',
    help = 'name of file where list of edges will be saved')
parser.add_argument('-on', '--outputnodes', default='nodes.csv',
    help = 'name of file where list of nodes will be saved')
parser.add_argument('-et', '--edgetype',
    choices=['retweets', 'mentions'],
    help = 'type of edge to extract')
args = parser.parse_args()

# arguments, and opening files for output
tweetfile = args.file
edges = args.edgetype
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

def export_retweets(tweetfile, outputedges, outputnodes):
    fh = open(tweetfile, 'r',encoding="utf-8")
    oute = open(outputedges, 'w',encoding="utf-8")
    oute.write('Source,Target,Text,Time\n')
    outn = open(outputnodes, 'w')
    outn.write('Id,Label,Followers,Lang\n')
    user_data = {}
    nodeset=set()
    i=0
    for line in fh:
        i+=1
        print(i)
        try:
            tweet = json.loads(line)
        except:
            continue
        if 'retweeted_status' not in tweet:
            x=tweet['text'].translate(non_bmp_map)
            z = lambda x: re.compile('\n').sub(' ',re.compile(',').sub(' ',x).strip())
            lw = tweet['user']['screen_name'] + ',' + \
                tweet['user']['screen_name'] + \
                ',' + \
                z(x) + ',' + \
                str(datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
            oute.write(lw + "\n")
            user_data[tweet['user']['id_str']] = "{0},{1},{2},{3}".format(
                tweet['user']['id_str'],
                tweet['user']['screen_name'],
                tweet['user']['followers_count'],
                tweet['user']['lang'])
            user_data[tweet['user']['id_str']] = "{0},{1},{2},{3}".format(
                tweet['user']['id_str'],
                tweet['user']['screen_name'],
                tweet['user']['followers_count'],
                tweet['user']['lang'])
            for user, user_string in user_data.items():
                #print(nodeset)
                if user not in nodeset:
                    nodeset.add(user)
                    outn.write('{0}\n'.format(user_string))
            
        else:
            x=tweet['retweeted_status']['text'].translate(non_bmp_map)
            z = lambda x: re.compile('\n').sub(' ',re.compile(',').sub(' ',x).strip())
            lw = tweet['user']['screen_name'] + ',' + \
                tweet['retweeted_status']['user']['screen_name'] + \
                ',' + \
                z(x) + ',' + \
                str(datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
            oute.write(lw + "\n")
            user_data[tweet['user']['id_str']] = "{0},{1},{2},{3}".format(
                tweet['user']['id_str'],
                tweet['user']['screen_name'],
                tweet['user']['followers_count'],
                tweet['user']['lang'])
            user_data[tweet['retweeted_status']['user']['id_str']] = "{0},{1},{2},{3}".format(
                tweet['retweeted_status']['user']['id_str'],
                tweet['retweeted_status']['user']['screen_name'],
                tweet['retweeted_status']['user']['followers_count'],
                tweet['retweeted_status']['user']['lang'])
            for user, user_string in user_data.items():
                #print(nodeset)
                if user not in nodeset:
                    nodeset.add(user)
                    outn.write('{0}\n'.format(user_string))
    oute.close()
    outn.close()


def export_mentions(tweetfile, outputedges, outputnodes):
    fh = open(tweetfile, 'r')
    oute = open(outputedges, 'w')
    oute.write('Source,Target,Time\n')
    outn = open(outputnodes, 'w')
    outn.write('Id,Label,Followers,Lang\n')
    user_data = {}
    for line in fh:
        try:
            tweet = json.loads(line)
        except:
            continue
        if len(tweet['entities']['user_mentions']) == 0:
            continue
        for mention in tweet['entities']['user_mentions']:
            lw = tweet['user']['id_str'] + ',' + mention['id_str'] + \
                ',' + str(datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
            oute.write(lw + "\n")
            user_data[tweet['user']['id_str']] = "{0},{1},{2},{3}".format(
                tweet['user']['id_str'],
                tweet['user']['screen_name'],
                tweet['user']['followers_count'],
                tweet['user']['lang'])
            if mention['id_str'] not in user_data.keys():
                user_data[mention['id_str']] = "{0},{1},{2},{3}".format(
                    mention['id_str'],
                    mention['screen_name'],
                    'NA',
                    'NA')
    for user, user_string in user_data.items():
        outn.write('{0}\n'.format(user_string))
    oute.close()
    outn.close()


if args.edgetype == 'retweets':
    export_retweets(tweetfile, args.outputedges, args.outputnodes)

if args.edgetype == 'mentions':
    export_mentions(tweetfile, args.outputedges, args.outputnodes)
