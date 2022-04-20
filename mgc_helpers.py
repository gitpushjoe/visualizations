import pickle

def readtxt(txtfile: str, return_str = False, rem_blank = False, rem_comment = True): #will return textfile as list if not string
    with open(txtfile, encoding='utf8') as f:
        if return_str:
            txt = f.read()
        else:
            txt = f.readlines()
            if rem_blank:
                txt = filter(lambda s: not s, txt)
            if rem_comment: #will remove all lines that begin with "#"
                txt = filter(lambda s: s[0] != '#', txt)
        f.close()
        return txt

def save_to_file(datum, location):
	pickle.dump(datum, open(location, "wb"))

def read_from_file(location):
	with open(location, "rb") as f:
		return pickle.load(f)