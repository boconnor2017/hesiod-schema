# Hesiod SCHEMA
Uses [Project Hesiod](https://github.com/boconnor2017/hesiod), a Photon based approach to manage a home lab data schema and to develop necessary architectural artifacts.

## Prerequisites
None.

# Quick Start
Deploy Photon OS OVA to a physical server or desktop. Follow the steps in the [Hesiod Photon OS Quick Start](https://github.com/boconnor2017/hesiod/blob/main/photon/readme.md) readme file to prep the Photon server for VCF. 

*Recommended: run these scripts as root.*
```
cd /usr/local/
```
```
git clone https://github.com/boconnor2017/hesiod-schema
```
```
cp -r hesiod/python/ hesiod-schema/hesiod
```
```
cd hesiod-schema/
```

# Commands
Use the `hesiod-schema.py` script as follows to manage your data schema.

## Convert an O365 document to Markdown
The following command will convert a word or excel document into Markdown. This might be useful if data is stuck in O365 formats. Markdown is a lightweight language that is useful to store in code repositories (such as GitHub or GitLab) and has the benefit of having a graphical user friendly view (like the one you're reading right now) while maintaining a structure that is easy to parse or generate via Python.    

Step 1: upload your word or excel document to the `/usr/local/drop/` folder on the Photon machine.    

Step 2: run the following command:   
```
python3 hesiod-schema.py -o365 <name_of_your_o365_file.doc> <name_of_your_new_md_doc.md>  
```
