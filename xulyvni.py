def xuly_vni(df):
        from underthesea import word_tokenize, pos_tag, sent_tokenize
        import regex
        import re
        import demoji
        ##LOAD EMOJICON
        file = open('files/emojicon.txt', 'r', encoding="utf8")
        emoji_lst = file.read().split('\n')
        emoji_dict = {}
        for line in emoji_lst:
                key, value = line.split('\t')
                emoji_dict[key] = str(value)
        file.close()
        #################
        #LOAD TEENCODE
        file = open('files/teencode.txt', 'r', encoding="utf8")
        teen_lst = file.read().split('\n')
        teen_dict = {}
        for line in teen_lst:
            key, value = line.split('\t')
            teen_dict[key] = str(value)
        file.close()
        ###############
        #LOAD wrong words
        file = open('files/wrong-word.txt', 'r', encoding="utf8")
        wrong_lst = file.read().split('\n')
        file.close()
        #################
        #LOAD STOPWORDS
        file = open('files/vietnamese-stopwords.txt', 'r', encoding="utf8")
        stopwords_lst = file.read().split('\n')
        file.close()


        ###
        def clean_text(text):
            text_clean = str(text).lower()
            if "Danh Mục\n" in text_clean:
                text_clean = text_clean[text_clean.index("Danh Mục\n"):]
            elif "Shopee\n" in text_clean:
                text_clean = text_clean[text_clean.index("Shopee\n"):]
            elif "\n\n" in text_clean:
                text_clean = text_clean[text_clean.index("\n\n") + 4:]
            elif "Gửi từ\n" in text_clean:
                text_clean = text_clean[text_clean.index("Gửi từ\n") + len("Gửi từ\n"):]
    
            ### exlucde size
            text_clean = re.sub(r"\nsize[^\n]*", " ", text_clean)
            # hastag
            text_clean = re.sub(r"#[^#]*", " ", text_clean)
            ###
            text_clean = re.sub(r"\n", " ", text_clean)
            text_clean = re.sub('[\.\:\,\-\+\d\!\%\...\"\*\>\<\^\&\/\[\]\(\)\=\~\#]', ' ', text_clean)
    
            ### words
            text_clean = re.sub('\ss\s|\sm\s|\sl\s|\sxl|xs|xl|xxl|xxxl|xxxxl|2xl|3xl|4xl|size|\smm\s|\sm\s|\sg\s|\skg\s', ' ', text_clean)
    
            ### space
            #text_clean = re.sub('\s+', ' ', text_clean)
    
            return text_clean
        
        df['description'] = df['description'].apply(lambda x: clean_text(x))
        ###

        def process_text(text, emoji_dict, teen_dict, wrong_lst):
            document = text.lower()
            document = document.replace("'",' ')
            document = regex.sub(r'\.+', " ", document)
            
            #document = regex.sub(r'none', " ", document)
            new_sentence =''
            for sentence in sent_tokenize(document):
                # if not(sentence.isascii()):
                ###### CONVERT EMOJICON
                sentence = ''.join(emoji_dict[word] + ' ' if word in emoji_dict else word for word in list(sentence))
                ###### CONVERT TEENCODE
                sentence = ' '.join(teen_dict[word] if word in teen_dict else word for word in sentence.split())
                ###### DEL Punctuation & Numbers
                pattern = r'(?i)\b[a-záàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ]+\b'
                sentence = ' '.join(regex.findall(pattern,sentence))
                ###### DEL wrong words   
                sentence = ' '.join('' if word in wrong_lst else word for word in sentence.split())
                new_sentence = new_sentence+ sentence + ' '                    
            document = new_sentence  
            #print(document)
            ###### DEL excess blank space
            document = regex.sub(r'none$', " ", document)
            
            ###space    
            document = regex.sub(r'\s+', ' ', document).strip()
            #...
            return document
        df['description'] = df['description'].apply(lambda x: process_text(x, emoji_dict, teen_dict, wrong_lst))

        # Remove HTTP links
        #df['processed_text'] = df['processed_text'].replace(
        #r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*', '',
        #regex=True)
        
        # Chuẩn hóa unicode tiếng việt
        def loaddicchar():
            uniChars = "àáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệđìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵÀÁẢÃẠÂẦẤẨẪẬĂẰẮẲẴẶÈÉẺẼẸÊỀẾỂỄỆĐÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴÂĂĐÔƠƯ"
            unsignChars = "aaaaaaaaaaaaaaaaaeeeeeeeeeeediiiiiooooooooooooooooouuuuuuuuuuuyyyyyAAAAAAAAAAAAAAAAAEEEEEEEEEEEDIIIOOOOOOOOOOOOOOOOOOOUUUUUUUUUUUYYYYYAADOOU"

            dic = {}
            char1252 = 'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ'.split(
                '|')
            charutf8 = "à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ".split(
                '|')
            for i in range(len(char1252)):
                dic[char1252[i]] = charutf8[i]
            return dic
         
        # Đưa toàn bộ dữ liệu qua hàm này để chuẩn hóa lại
        def covert_unicode(txt):
            dicchar = loaddicchar()
            return regex.sub(
                r'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ',
                lambda x: dicchar[x.group()], txt)
                
        df['description'] = df['description'].apply(lambda x: covert_unicode(x))
                        

        #loai bo stopwords
        def remove_stopword(text, stopwords):
            ###### REMOVE stop words
            document = ' '.join('' if word in stopwords else word for word in text.split())
            #print(document)
            ###### DEL excess blank space
            document = regex.sub(r'\s+', ' ', document).strip()
            return document
        df['description'] = df['description'].apply(lambda x: remove_stopword(x,stopwords_lst))

        
        return df
