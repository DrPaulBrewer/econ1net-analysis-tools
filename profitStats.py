#!/usr/bin/env python
#
# profitStats.py
#  Copyright 2018 Paul Brewer Economic and Financial Technology Consulting LLC <drpaulbrewer@eaftc.com>
#  License: The MIT License
#
# This software currently takes a consolidated profit.csv file
# from the Econ1.Net simulator as input, along with the number
# of buyers and number of seller.
#
# It outputs to stdout a large text file that includes embedded CSV
# giving statistics for each buyer or seller's profit as caseid is varied
#
import pandas as pd
import sys
if len(sys.argv)!=4:
    sys.exit("usage: stats.py /path/to/profit.csv nBuyers nSellers")
[ pathToProfitCSV, buyers, sellers ] = sys.argv[1:];
nBuyers = int(buyers)
nSellers = int(sellers)
df = pd.read_csv(pathToProfitCSV)
print len(df.columns)
for a in range(1,nBuyers+nSellers+1):
    agentname = "Buyer "+str(a) if (a<=nBuyers) else "Seller "+str(a-20)
    colname = "y"+str(a)
    df2 = df.groupby("caseid")[colname]
    def stat(p):
        calculatedSeries = df2.apply(getattr(pd.Series,p))
        calculatedSeries.name = p
        return calculatedSeries
    props = ["min","median","mean","max","std","skew","kurt"]
    stats = map(stat, props)
    df3 = pd.concat(stats,axis=1)
    print agentname
    print
    print df3.to_csv(sep=",")
    print
    

