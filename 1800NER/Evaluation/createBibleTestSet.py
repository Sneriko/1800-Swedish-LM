with open('/home/sneriko/Dropbox/Riksarkivet/1800_ner/1800_dataset/bible/txt/svediakorp-rel122-bibel1873dalin.txt', 'r') as bible, open('valBible.txt', 'w+') as val:
    for line in bible:
        if not(line.startswith('#')):
            val.write(line)    