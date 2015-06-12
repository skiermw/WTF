#!/usr/bin/env python
import sys
import json
import time
from pprint import pprint


in_filename = 'policy_model.txt'
out_filename = 'form_gen.py'

#infile = open(in_filename, 'r')

outfile = open(out_filename, 'w')

new_form = True

# header 
outfile.write('# generated from Swagger Policy model on %s \n' % time.strftime("%c"))
outfile.write(' \n')
outfile.write('from flask.ext.wtf import Form\n')
outfile.write('from wtforms.fields import BooleanField, StringField, TextField, FloatField, FormField, IntegerField, DateField, SubmitField, FieldList\n')
outfile.write('from wtforms.validators import DataRequired, InputRequired\n')
outfile.write(' \n')

form_class_template = "class {name}(Form):\n"
field_template = "\t{name} = {field}('{name}')\n"
form_field_template = "\t{name} = FormField({formname})\n"
fieldlist_template = "\t{name} = FieldList(FormField({formname}))\n"

with open(in_filename) as data_file:
    for line in data_file:
        words = line.split()
        if new_form:
            
            form_name = words[0]
            outfile.write(form_class_template.format(name=form_name))
            print form_class_template.format(name=form_name)
            new_form = False
        else:
            if line[0] == '}':      # look for end of form
                outfile.write('\n')
                print ' '
                new_form = True
            else:                # nope, it is a field on the form
                field_name = words[0]
                field_type = words[1].lstrip('(')
                field_type = field_type.rstrip(',')
                field_type = field_type.rstrip(')')
                field_type = field_type.rstrip('[')
                field_type = field_type.rstrip(']')
                
                #print 'field_type = %s' % field_type
                if field_type == 'string':
                    WTF_field = 'StringField'
                    outfile.write(field_template.format(name=field_name, field=WTF_field))
                    print field_template.format(name=field_name, field=WTF_field)
                elif field_type == 'double':
                    WTF_field = 'FloatField'
                    outfile.write(field_template.format(name=field_name, field=WTF_field))
                    print field_template.format(name=field_name, field=WTF_field)
                elif field_type == 'boolean':
                    WTF_field = 'BooleanField'
                    outfile.write(field_template.format(name=field_name, field=WTF_field))
                    print field_template.format(name=field_name, field=WTF_field)
                elif field_type == 'integer':
                    WTF_field = 'IntegerField'
                    outfile.write(field_template.format(name=field_name, field=WTF_field))
                    print field_template.format(name=field_name, field=WTF_field)
                elif  'Array' in field_type:
                    formfield_name = words[1]
                    formfield_name = formfield_name.lstrip('(Array[')
                    formfield_name = formfield_name.rstrip('])')
                    formfield_name = formfield_name[:1].upper() + formfield_name[1:]
                    formfield_name = formfield_name.split(']')[0]
                    outfile.write(fieldlist_template.format(name=field_name, formname=formfield_name))
                    print fieldlist_template.format(name=field_name, formname=formfield_name)
                else:
                    formfield_name = words[1].lstrip('(')
                    #print formfield_name
                    formfield_name = formfield_name.split(',')[0]
                    formfield_name = formfield_name[:1].upper() + formfield_name[1:]
                    outfile.write(form_field_template.format(name=field_name, formname=formfield_name))
                    print form_field_template.format(name=field_name, formname=formfield_name)

outfile.close()

                
                    
                
                    
                    
                
