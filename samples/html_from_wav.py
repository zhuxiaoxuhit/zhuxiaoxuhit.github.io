import re,glob,os,sys

def generate_html(path,mode):
	wav = glob.glob(path+"/*.wav")
	wav = sorted(wav)
	print(re.split(r"[\/]",path))
	title = re.split(r"[\/]",path)[-1]
	f = open(path+"/"+re.split(r"[\/]",path)[-1]+'.html','w')
	if mode == "0": # tts wav + alignments
		f.write('<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title></title></head><body>\
				<h1 align=\"center\">'+title+'</h1>\
				<ol><table border=\"2\" bordercolor=\"black\" width=\"300\" cellspacing=\"0\" cellpadding=\"5\" style=\"margin:auto\">\
				<tr>    <td>utter_ID</td>    <td>tts_audio</td>    <td>aligments</td> </tr>\n')
		for w in wav:
			n = re.split(r"[\/\.]",w)[-2] 
			p = re.split(r"[\/\.]",w)[1]+'/'+ re.split(r"[\/\.]",w)[2]
			f.write('<tr>    <td>'+n+'</td>    \
					<td><audio controls><source src=\"'+n+'.wav\"></audio></td>    \
					<td><div align=\"center\"><img src=\"'+n+'.png \" height=\"60\" width=\"80\" /></div></td>    </tr>\n')
		f.write('</table></br></ol></body></html>\n')
		f.close()
	elif mode == "1": # tts wav + origin wav + aligments
		f.write('<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title></title></head><body>\
				<h1 align=\"center\">'+title+'</h1> \
				<ol><table border=\"2\" bordercolor=\"black\" width=\"300\" cellspacing=\"0\" cellpadding=\"5\" style=\"margin:auto\">\
				<tr>    <td>utter_ID</td>    <td>tts_audio</td>    <td>origin_audio</td>    <td>aligments</td> </tr>\n')
		for w in wav:
			n = re.split(r"[\/\.]",w)[-2] 
			p = re.split(r"[\/\.]",w)[1]+'/'+ re.split(r"[\/\.]",w)[2]
			f.write('<tr>    <td>'+n+'</td>    <td><audio controls><source src=\"'+n+'.wav\"></audio></td>    \
					<td><audio controls><source src=\"'+n+'_origin.wav\"></audio></td>    \
					<td><div align=\"center\"><img src=\"'+n+'.png \" height=\"60\" width=\"80\" /></div></td>    </tr>\n')
		f.write('</table></br></ol></body></html>\n')
		f.close()
	elif mode == "2":	# tts wav
		f.write('<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title></title></head><body>\
				<h1 align=\"center\">'+title+'</h1>\
				<ol><table border=\"2\" bordercolor=\"black\" width=\"300\" cellspacing=\"0\" cellpadding=\"5\" style=\"margin:auto\">\
				<tr>    <td>utter_ID</td>    <td>tts_audio</td>    </tr>\n')
		for w in wav:
			n = re.split(r"[\/\.]",w)[-2] 
			print(n)
			p = re.split(r"[\/\.]",w)[1]+'/'+ re.split(r"[\/\.]",w)[2]
			f.write('<tr>    <td>'+n+'</td>    <td><audio controls><source src=\"'+n+'.wav\"></audio></td>    </tr>\n')
		f.write('</table></br></ol></body></html>\n')
		f.close()
	else:
		print("error mode")

def compare(args):
	width_audio = 1200//(len(args)-1)
	pp = args[0]            #parent path  
	child_dirs = args[1:]
	nb_child = len(child_dirs)
	print(child_dirs)
	cp1 = os.path.join(pp,child_dirs[1]) #child path 2
	wav1 = glob.glob(cp1+"/*.wav")
	wav1 = sorted(wav1)
	print('parent path:',pp)	
	print('chail dirs:',child_dirs)	
	title = re.split(r"[\/]",pp)[-1]	
	f = open(pp+"/"+title+'.html','w')
	f.write('<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title></title></head><body>    \
			<h1 align=\"center\">'+title+'</h1>    \
			<ol><table border=\"2\" bordercolor=\"black\" width=\"300\" cellspacing=\"0\" cellpadding=\"5\" style=\"margin:auto\">    \
			<tr>     <td>utter_ID</td>    \n')
	for d in child_dirs:
		f.write('<td>'+d+'</td>    ')
	f.write('</tr>\n')
	for w in wav1:
		n = re.split(r"[\/\.]",w)[-2] 
		f.write('<tr><td>'+n+'</td>    \n')
		for d in child_dirs:
			f.write('<td><audio style=\"width:' + str(width_audio) +'px\"controls><source src=\"'+ d + '/' + n + '.wav' +'\"></audio></td>    \n')
	f.write('</tr></table></br></ol></body></html>\n')
	f.close()


if __name__ == "__main__":
	if len(sys.argv) == 3:
		generate_html(sys.argv[1],sys.argv[2])  #arg1 - path of result dir(example:output/21spk_mean_embedding_pretrained_4500spk_189w_r6_based_9spk10_180epoch)   ,arg2 - mode: 0(no origin audio), 1(with origin audio) 
	elif len(sys.argv) >= 4:	
		compare(sys.argv[1:])
	else:
		print('\
			usage 1: generate html for display wavs.\n\
			cmd: python html_from_wav.py dir_wav mode\n \
			--- mode 0:tts wav + alignments\n\
			--- mode 1:tts wav + origin wav + aligments\n \
			--- mode 2:tts wav \n\
			usage 2: compare 2 method of audios.\n\
			cmd: python html_from_wav.py parent_path dir1 dir2\n')

