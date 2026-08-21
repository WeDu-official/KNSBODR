from tkinter import *
import os
def edit_line(file_name, line_number, new_text):
  """Edits the specified line in the given Python file.

  Args:
    file_name: The name of the Python file to edit.
    line_number: The number of the line to edit.
    new_text: The new text to write to the file.
  """

  with open(file_name, "r") as f:
    source_code = f.read()

  lines = source_code.split("\n")
  lines[line_number - 1] = new_text

  with open(file_name, "w") as f:
    f.write("\n".join(lines))
root = Tk()
root.title('PLC 1.0 kotlin')
root.geometry('300x150')
Label(root,text='write your programming language name no spaces').pack()
language_name = StringVar()
Entry(root,textvariable=language_name).pack()
Label(root,text='write the file format').pack()
format_type = StringVar()
Entry(root,textvariable=format_type).pack()
def do_it():
        try:
            os.remove(f'keys.txt')
            os.remove(f'values.txt')
        except:
            pass
        try:
            t = open(f'keys.txt', 'x')
            r = open(f'values.txt', 'x')
            t.close()
            r.close()
        except:
            pass
        os.mkdir(f'{language_name.get()}_comp')
        SI = open('PLC_things\\SI.py','r')
        SIR = open('PLC_things\\SIR.py','r')
        SOIS = open('PLC_things\\SOIS.py', 'r')
        lind = open('PLC_things\\license.txt', 'r')
        strike_lib = open('PLC_things\\strike_lib.py', 'r')
        mSI = open(f'{language_name.get()}_comp\\SI.py', 'x')
        mSIR = open(f'{language_name.get()}_comp\\SIR.py', 'x')
        mSOIS = open(f'{language_name.get()}_comp\\SOIS.py', 'x')
        mlind = open(f'{language_name.get()}_comp\\license.txt', 'x')
        mstrike_lib = open(f'{language_name.get()}_comp\\strike_lib.py', 'x')
        mSI.write(SI.read())
        mlind.write(lind.read())
        mlind.close()
        lind.close()
        mSIR.write(SIR.read())
        mSOIS.write(SOIS.read())
        mstrike_lib.write(strike_lib.read())
        mSOIS.write(SOIS.read())
        SI.close()
        mSI.close()
        SIR.close()
        mSIR.close()
        SOIS.close()
        mSOIS.close()
        strike_lib.close()
        mstrike_lib.close()
        h = language_name.get()
        op = h[0].capitalize()
        os.rename(f'{language_name.get()}_comp\\SI.py',f'{language_name.get()}_comp\\{op}I.py')
        os.rename(f'{language_name.get()}_comp\\SIR.py', f'{language_name.get()}_comp\\{op}IR.py')
        os.rename(f'{language_name.get()}_comp\\SOIS.py', f'{language_name.get()}_comp\\{op}OIS.py')
        os.rename(f'{language_name.get()}_comp\\strike_lib.py', f'{language_name.get()}_comp\\{language_name.get()}_lib.py')
        main_runnero = open('main_runner1.py','w')
        main_runnero.write(f"""from {language_name.get()}_comp import {op}IR
{op}IR.run('main.{format_type.get()}')""")
        main_runnero = open('main_runner2.py','w')
        main_runnero.write(f"""from {language_name.get()}_comp import {op}IR2
{op}IR2.run('main.{format_type.get()}')""")
        thingAPEL2 = open(f'SAPFL.py', 'w')
        thingAPEL2.write("""func_mapping = {
#write at here your first func_mapping
'~1':''
}""")
        thingAPEL2.close()
        os.rename('SAPFL.py',f'{op}APFL.py')
        oms = open(f'{language_name.get()}_comp\\{op}IR2.py', 'x')
        oms.close()
        om1 = open(f'{language_name.get()}_comp\\{op}IR.py','r')
        oms1 = open(f'{language_name.get()}_comp\\{op}IR2.py','w')
        oms1.write(om1.read())
        om1.close()
        oms1.close()
        edit_line(f'{language_name.get()}_comp\\{op}I.py',1,f'from {op}APFL import func_mapping')
        edit_line(f'{language_name.get()}_comp\\{op}IR2.py',1,f'from {op}APFL import func_mapping')
        edit_line(f'{language_name.get()}_comp\\{op}IR2.py',19,'    command = "kotlinc runned_code.kt"')
        edit_line(f'{language_name.get()}_comp\\{op}IR.py',1,f'from {op}APFL import func_mapping')
        edit_line(f'{language_name.get()}_comp\\{op}OIS.py',1,f'from {op}APFL import func_mapping')
        edit_line(f'{language_name.get()}_comp\\{language_name.get()}_lib.py',1,f'from {op}APFL import func_mapping')
        edit_line(f'{language_name.get()}_comp\\{language_name.get()}_lib.py',2,f'from {language_name.get()}_comp import {op}IR')
        edit_line(f'{language_name.get()}_comp\\{language_name.get()}_lib.py',5,f'        {op}IR.run(filepath)')
        os.remove('PLC_things\\SI.py')
        os.remove('PLC_things\\SIR.py')
        os.remove('PLC_things\\SOIS.py')
        os.remove('PLC_things\\strike_lib.py')
        os.remove('main.py')
        mainfile_format = open(f'main.{format_type.get()}','x')
        mainfile_format.close()
        os.remove('PLC_things\\license.txt')
        os.rmdir('PLC_things')
        os.remove('keys.txt')
        os.remove('values.txt')
Button(root,text='save change',command=do_it).pack()
root.mainloop()