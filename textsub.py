import getopt, sys
from html.parser import HTMLParser
import hashlib
from yandex_translate import YandexTranslate

def usage():
    print("""\
    Usage:
    textsub.py [option] <argument>
    
    Options:
    --extract-text - extract text from the sample html file and generate a .properties file.
    --generate-resource <language-code> - genearate the translated .properties file in the language specified by "language-code".
    --display-html - create a translated HTML page.
    --help - display this help text.
    
    Supported language codes:
    {'et', 'ro', 'sq', 'da', 'sk', 'tr', 'sr', 'lt', 'el', 'sl', 'be', 'ru', 'es', 'en', 'pt', 'fr', 'no', 'mk', 'fi', 'hy'}""")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["extract-text", "generate-resource=", "display-html", "help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    (abc, b) = opts[0]
    class myparser(HTMLParser):
                    
        def handle_data(self, data):
            if abc == '--extract-text':
                data = data.lstrip();
                data = data.rstrip();
                if data != '':
                    hash_object = hashlib.md5(data.encode())
                    f1 = open('example.properties', mode='a')
                    f1.write(hash_object.hexdigest() + "=" + data + "\n")
            elif abc == '--display-html':
                data = data.lstrip();
                data = data.rstrip();
                if data != '':
                    hash_object = hashlib.md5(data.encode())
                    rep = tran_dict[hash_object.hexdigest()]
                    self.newdata = self.newdata.replace(data, rep)                
        
    for o, a in opts:
        if o == "--extract-text":
            data_dict = {}
            f1 = open('example.properties', mode='w')
                    
            parser = myparser()
            f = open('sample.html')
            data = f.read()
            parser.feed(data)

        elif o == "--generate-resource":
            translate = YandexTranslate('trnsl.1.1.20160607T100954Z.0329b17b7e667944.3b9682b4988dfe500b80d3d23a867954d107ed6c')
            lang = a
            name = a + ".properties"
            
            f = open('example.properties')
            f1 = open('selected_language', 'w')
            f2 = open(name, mode='w')
            f1.write(name)
            
            for line in f:
                (key, val) = str(line).split('=');
                
                f2 = open(name, mode='a');
                res = translate.translate(val, a)
                out = str(res['text'])
                out = out.strip('[]')
                out = out.lstrip("'")
                out = out.rstrip("'")
                out = out.strip("\\n")
                f2.write(key + "=" + str(out) + "\n")
                
        elif o == "--display-html":
            data_dict = {}
            with open('selected_language') as f3:
                name = f3.read()
            with open('example.properties') as f4:
                for line in f4:
                    (key, val) = line.split('=')
                    data_dict[key] = val
                      
            tran_dict = {}
            with open(name) as f5:
                for line in f5:
                    (key, val) = line.split('=')
                    tran_dict[key] = val
            
            infile = open('sample.html', 'r');
            
            olddata = infile.read()
            newdata = olddata
            
            parser = myparser();
            parser.newdata = newdata;
            parser.feed(olddata);
            
            with open('sample.translated.html', 'w') as file:
                file.write(parser.newdata)
                
        elif o == "--help":
            usage()
            
        else:
            assert False, "unhandled option"
            
if __name__ == "__main__":
    main()