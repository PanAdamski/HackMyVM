# Venus
![{D4111A68-ED77-4CEB-98A9-8647D3287C9D}](https://github.com/user-attachments/assets/797bf09a-764b-4c96-b66f-f9a41edb0c49)

![{B5BFD345-7FD7-4B1C-A3AA-44996F027947}](https://github.com/user-attachments/assets/6c49bef6-0b93-4e82-a66d-f832b9790dd0)

ookey. We need to find 50 flags.
![{44CE7297-8353-4C43-9876-97296D5084A9}](https://github.com/user-attachments/assets/4da83c13-ecc5-49f6-94d0-4512c4d80785)

Hello hax0r,
Welcome to the HMVLab Chapter 1: Venus!
This is a CTF for beginners where you can practice your skills with Linux and CTF
so lets start! :)
First of all, the home of each user is in /pwned/USER and in it you will find a file called mission.txt which will contain
the mission to complete to get the password of the next user.
It will also contain the flagz.txt file, which if you are registered at https://hackmyvm.eu you can enter to participate in the ranking (optional).
And for a bit of improvisation, there are secret levels and hidden flags: D
You will not have write permissions in most folders so if you need to write a script or something
use /tmp folder, keep in mind that it is frequently deleted ...

And last (and not least) some users can modify the files that are in the
folder /www, these files are accessible from http://venus.hackmyvm.eu so if you get a user
that can modify the file /www/hi.txt, you can put a message and it will be reflected in http://venus.hackmyvm.eu/hi.txt. 

If you have questions/ideas or want to comment us anything you can join
to our Discord: https://discord.gg/DxDFQrJ

Remember there are more people playing so be respectful.
Hack & Fun! 

![{A8426595-A128-40D7-B341-83AE6EE00A1D}](https://github.com/user-attachments/assets/ff032471-b512-4400-bd7a-ff5a95699401)

![{4D3E7B63-E2A2-468A-9D1F-E543283F0E23}](https://github.com/user-attachments/assets/c6965584-04ec-4fd9-9a47-1bf7a6a69e62)

# First
flag is in file `...` so we can print it using `cat ...`.
We can see "hidden" file in user directory named `.myhiddenpazz` that cointains sam random string.
Using `id` command we observate our uid is 1052 so next user should me 1051... but it failed.
My next idea was to create a list of users. I did this by using the  command below
```
cat /etc/passwd | egrep "sh|bash" |cut -d: -f1
```
and brutfore ssh using command 
```
hydra -L user_lists -P <string from .myhiddenpazz> ssh://venus.hackmyvm.eu -s 5000
```

We got userr `sophia`

![{3FB51306-D054-4E9C-ADC8-523E0721116E}](https://github.com/user-attachments/assets/e0ece9d4-cade-4ae7-a662-5c1fbcf43914)

# Second

 EN 
The user angela has saved her password in a file but she does not remember where ... she only remembers that the file was called whereismypazz.txt 
![{EE0B645E-2A67-4655-829D-8E677582F2EA}](https://github.com/user-attachments/assets/218018de-878a-496c-b0c9-177fcafa7f7c)

![{3DF09542-F48A-442C-9FE1-D59FD0D8A150}](https://github.com/user-attachments/assets/b076a403-426d-4b79-95d9-b6084a3ccf07)

Password works

# Third
![{0BD289D3-F0D3-4D6F-8D13-C2F6DDA03A88}](https://github.com/user-attachments/assets/fb5057af-ed77-4717-a355-ecf15324999f)

The password of the user emma is in line 4069 of the file findme.txt
```
cat -n findme.txt | grep 4069
```
This gave as password for next user but I back to group `www3`.
![{3E20FC46-F768-4F54-A523-B618CC965355}](https://github.com/user-attachments/assets/33c09d2d-90d5-4742-8d10-da00402fa083)

This gave as next hidden flag.

# Fourth
User mia has left her password in the file -.
![{A973CFAB-ECBB-45DB-9A11-4F2E1B785B26}](https://github.com/user-attachments/assets/dae3486c-7c2e-4bea-bfa1-5816cc476090)

```
cat ./-
```

# fifth

It seems that the user camila has left her password inside a folder called hereiam
```
find / -type d -name hereiam 2>/dev/null
```
![{C6D2C640-93C6-45BA-8F0B-1B28DEA555C4}](https://github.com/user-attachments/assets/c424b80c-95d4-4180-afe3-c7fc2e3633a3)


But also we can see intereting file

![{6DE091D3-6D03-4E74-8CF4-BA53959C1731}](https://github.com/user-attachments/assets/c1021aee-68f1-424e-a391-83826c25623e)

I will ignore this. I dont like weasting time on osint
![{0A4AB696-6954-4965-B950-AD5117E9C11F}](https://github.com/user-attachments/assets/f8b6c11c-25a3-4bb8-b84d-2ba521bc9c43)

# sixth
The user luna has left her password in a file inside the muack folder.
![{63A3EFCE-57C4-4501-9BFF-74016E8C23A3}](https://github.com/user-attachments/assets/5e860b4f-26b3-47f2-9e84-e6aad8f5f5ae)

A lot of fodlers inside
![{AD48759D-16C3-4FC2-9068-54D8CCA73EDF}](https://github.com/user-attachments/assets/4b04726d-c5de-400b-9357-9e1f0e1e209e)

I tried to find it by bruteforce
```
grep -ir a
grep -ir b
```
2nd commend works
albo you can use 
```
find / -group camila 2>/dev/null | grep -v proc
```

# Seventh
The user eleanor has left her password in a file that occupies 6969 bytes.
![{C1D520BD-7573-47C4-B649-73F94EED155E}](https://github.com/user-attachments/assets/671a1ac5-71e9-433a-8f3d-2c748fa921cc)
```
find / -type f -size 6969c 2>/dev/null
```
![{1AD5501D-4C1D-434C-AC10-AEE956F2690D}](https://github.com/user-attachments/assets/9b6b11bb-dcc8-4559-bfb6-10e578e9c092)

# eighth

The user victoria has left her password in a file in which the owner is the user violin. 

![{EA8D8862-8814-4B84-AB9F-8E46E6BDF8D9}](https://github.com/user-attachments/assets/ae2f27a5-835a-46c7-80aa-d698d0508b49)

![{103BFF03-BB4F-405C-B919-5C6A8DF3A8AE}](https://github.com/user-attachments/assets/adf25167-e487-426f-ba8f-16fd858f21e6)
```
find / -user violin 2>/dev/null | grep -v proc
```

#nineth
The user isla has left her password in a zip file.

![{2E0EF258-0B5B-402B-9D66-4F410735B5A2}](https://github.com/user-attachments/assets/187db04a-eeb4-4c81-9e38-a2409febe69b)
```
unzip passw0rd.zip
```
password froped into `/var/tmp/passw0rd/pwned/victoria/passw0rd.txt`


# tenth
The password of the user violet is in the line that begins with a9HFX (these 5 characters are not part of her password.). 

![{C29BB298-A843-43DE-9FBC-FE2441EB3CCC}](https://github.com/user-attachments/assets/787a665e-2b16-42a5-9efd-bba70a682856)
```
cat passy | grep a9HFX
```

# eleventh
The password of the user lucy is in the line that ends with 0JuAZ (these last 5 characters are not part of her password) 

![{83DE1CEC-ACA5-49C5-952C-91A7EAC7F925}](https://github.com/user-attachments/assets/02e31c97-5ad0-4987-a014-296244768837)
```
cat end | grep 0JuAZ
```

#twelfth

The password of the user elena is between the characters `fu` and `ck`. 

![{DE3C7281-49D8-4BFF-9AF5-575BF03D0549}](https://github.com/user-attachments/assets/51294d18-eb2a-434f-bc10-dcb96e8f32d5)
```
cat /pwned/lucy/file.yo | grep fu | grep ck
```

# thirteenth

The user alice has her password is in an environment variable. 

![{C0C97B64-8226-4CBD-80B1-E711F29CE4DA}](https://github.com/user-attachments/assets/1038e553-73a5-4bfb-ac66-1ea4c0ed502e)
```
env | grep PASS
```

# fourteenth

The admin has left the password of the user anna as a comment in the file passwd. 

![{A9A82EEE-F816-48FE-BC70-B048AE04AE0A}](https://github.com/user-attachments/assets/35ce2bf8-08c8-4a8d-9bbf-2779e11647da)

![{97493D33-D4D9-4B0D-8B56-22B2C9837857}](https://github.com/user-attachments/assets/4fb4a692-24b2-4333-8585-36d2806391ef)

But we are smart and I know that there is /etc/passwd-.

![alice](https://github.com/user-attachments/assets/34bfeb96-41bb-46aa-af5e-acdd4ef10779)
```
cat /etc/passwd- | grep alice
```

# fifteen
Maybe sudo can help you to be natalia.

![{8B9F4DBD-C705-46AE-9861-ADC009DE303A}](https://github.com/user-attachments/assets/47e4d82a-576f-4dc4-9dbf-9b484e3cc1a7)

![{3492DE54-22AE-458C-A40C-7DCA82CAE768}](https://github.com/user-attachments/assets/5d94f978-c692-41b1-a0af-eafbd806a115)
```
sudo -l
sudo -u natalia /bin/bash
```


# sixteenth
The password of user eva is encoded in the base64.txt file

![{8652EC74-C05E-4AD4-9D4E-79230DE70BBD}](https://github.com/user-attachments/assets/7683b299-ca89-478e-97a7-db06521f3d2f)
```
cat base64.txt | base64 -d
```

#seventeenth
The password of the clara user is found in a file modified on May 1, 1968. 

![{F5700C6B-9A32-43AB-9847-2642359AB004}](https://github.com/user-attachments/assets/c1332f47-c2dc-4218-9a06-1dcda67ced7e)

we know that the file cannot be created before January 1, 1970 so we use such a command
```
find / -type f -mtime +18615 2>/dev/null
```
![{A3C7FFFC-AFEE-477E-97CC-C50F7E31D974}](https://github.com/user-attachments/assets/73267bc8-81d8-487e-a4bd-f15f9e608a29)


# eighteen

The password of user frida is in the password-protected zip (rockyou.txt can help you) 

![{BA95E4A8-7F0E-40BA-AA77-8C5C359108B2}](https://github.com/user-attachments/assets/152aa5a3-1f08-4b96-afa5-0edc692cf421)

we need to transfer the file to our local vm
![{46576C93-F01C-4143-AE34-34025730F009}](https://github.com/user-attachments/assets/3076159c-5fc7-4693-8c38-b6eefcf2bcbd)

```
cat protected.zip | base64 -w0
```

![{B81904BD-2996-45F0-8D9A-B555AC3CBA54}](https://github.com/user-attachments/assets/51f7143c-410a-4813-99b8-d9ecacbabfda)

```
echo <base64 string> | base64 -d > protected.zip
zip2john protected.zip > hash
john hash -w=~/SHARED/lists/rockyou.tx
```

![zip](https://github.com/user-attachments/assets/8ebda042-e0f7-4e37-a21d-1c4446cb4c86)

![{BF807805-AD72-4BC4-8F39-43ABFFC37C8C}](https://github.com/user-attachments/assets/3f4c8217-64ff-418e-a826-9f0e3012ede0)

# nineteenth
The password of eliza is the only string that is repeated (unsorted) in repeated.txt. 

![{480DCC84-01AC-4D9E-A34D-5CF77DBB050A}](https://github.com/user-attachments/assets/649d422c-b65c-483a-8cda-0de65ad5d59c)

```
uniq -d repeated.txt
```

# twenty

The user iris has left me her key.

![{25028A5E-F0AE-4E64-80F8-D4854836EC88}](https://github.com/user-attachments/assets/9273f13f-ac0c-4c77-84ee-56b7dc72a688)

```
ssh iris@venus.hackmyvm.eu -p 5000 -i .iris_key
```

# twenty-first

User eloise has saved her password in a particular way. 

![{B59E9295-CBAB-46CD-AD48-AC5A7BF1E6B1}](https://github.com/user-attachments/assets/caeab1b5-723a-4c65-9c41-3bfc4cbd1854)

we can observe that the eloise file is a base64 string. When we want to decode it we see the characteristic beginning `����JFIF`.

We need to copy the entire base64 string to our local machine and execute two commands
```
cat eliose| base64 -d > pass.jpeg
open pass.jpeg
```
In the password there is no big literal `i`, there is `l`.

# twenty-second

User lucia has been creative in saving her password.

![{2054CAA3-F607-4E1C-A52A-8FA368F2BD99}](https://github.com/user-attachments/assets/c6c87ebb-ed08-44c5-a6e1-44d6d3a42cf3)

![{F6B1FD7F-71A3-4837-B69B-F6436A6D646E}](https://github.com/user-attachments/assets/8bbcc685-55aa-4677-a66a-12b099e1346f)
```
xxd -r hi
```

# twenty-third

The user isabel has left her password in a file in the /etc/xdg folder but she does not remember the name, however she has dict.txt that can help her to remember.

![{ED53CAA9-9797-4F12-B7BE-025205BFEE07}](https://github.com/user-attachments/assets/21857ba9-fb01-439d-bf42-bcf2e5017017)

I created simple bash script
```
#!/bin/bash

DIR="/etc/xdg"
DICT="/pwned/lucia/dict.txt"

while read -r arch; do
    if [[ -f "$DIR/$arch" ]]; then
        echo "'$arch' exists in $DIR."
    fi
done < "$DICT"
```
I saved it into `/tmp/Holl0w/solver.sh` and run it.
```
cd /tmp
mkdir Holl0w; cd Holl0w
nano solver.sh
bash solver.sh
```

Also we found hidden flag
```
cat dict.txt | grep '=='
```

# twenty-fifth
The password of the user freya is the only string that is not repeated in different.txt 

![{B69811F2-2765-4341-8B6D-72CF4BF0FDDA}](https://github.com/user-attachments/assets/701ce625-1f8b-4e4d-99e8-fba571c7cfad)

```
cat different.txt | uniq -c | sort -nr
```

# twenty-sixth
User alexa puts her password in a .txt file in /free every minute and then deletes it. 

![{CD94AC6C-E36E-4F0D-9F4B-2668BA0AF980}](https://github.com/user-attachments/assets/aab087a3-bd38-405b-a6c2-7d97db6babfb)

![{9B8A974B-38DF-47CC-A925-FDF45823D40B}](https://github.com/user-attachments/assets/fea47687-5a78-4be0-911b-353cfb7cada1)
```
false; while [ $? -ne 0 ]; do cat /free/* ; done 2>/dev/null
```

# twenty-seventh
The password of the user ariel is online! (HTTP)

![{F9872357-84B2-4545-B03B-4AF423E9EC46}](https://github.com/user-attachments/assets/58588aac-9925-40d8-9721-d091610f7671)
```
curl localhost
```

# twenty-eighth
Seems that ariel dont save the password for lola, but there is a temporal file.

![{A167A60F-DB1D-4671-B2C1-CB4D3AEF8D65}](https://github.com/user-attachments/assets/d69bacda-7755-4036-92c8-71f65bf7f0b9)

![{3E8105AA-16BA-4407-B8C1-19ACC7B157F7}](https://github.com/user-attachments/assets/d37c4bd7-c0c7-4578-b583-85209a7c596a)

I copied i saved passwords into my local machine to file `raw`
```
cat raw| cut -d'>' -f2 > passes
```
```
hydra -l lola -P passes ssh://venus.hackmyvm.eu:5000
```

# twenty-ninth
The user celeste has left a list of names of possible .html pages where to find her password. 

![{1D035FEB-F530-46C9-B632-B6EEDCEF829C}](https://github.com/user-attachments/assets/91867284-376d-4608-867b-f9d91a519a84)

![{5EBA073C-4F11-4CA6-AF9D-C418E515F360}](https://github.com/user-attachments/assets/19dcdcbf-b601-480b-8e83-026a0baf68e7)

Save `pages.txt` info your local machine
```
ssh -L 80:127.0.0.1:80 lola@venus.hackmyvm.eu -p 5000
```
```
ffuf -w pages.txt  -u http://127.0.0.1/FUZZ -c -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36' -mc all -fs 555 -e .html
```

# Thirty
The user celeste has access to mysql but for what?

![{154F3E82-BBAC-4194-B6A9-7C34A0D8A67F}](https://github.com/user-attachments/assets/6b96001b-8268-44fe-b328-a3c2b6c7b604)

```
mysql -u celeste -p
<paste password and enter>

![{6E747AE8-EF9A-46AB-8A1E-FF6C564C0337}](https://github.com/user-attachments/assets/f18e3817-44a1-4b35-857b-2d26588f853d)

35 haha <special hidden flag>
```
We need user `nina`
```
select * from people where uzer='nina';
```

# Thirty-first
The user kira is hidding something in http://localhost/method.php

![{0CD5B2C6-D6F2-4BDB-B95B-766BC685A2A8}](https://github.com/user-attachments/assets/cc723e8f-89cf-4f42-8c22-d05ff147a16a)

```
curl http://localhost/method.php -X PUT
```

# Thirty-second
The user veronica visits a lot http://localhost/waiting.php

![{4DD0E815-E44E-430A-9C98-E564645D54B9}](https://github.com/user-attachments/assets/8f378bc6-6e52-4c5a-9b65-36c15a4a6fe0)

```
curl http://localhost/waiting.php -A PARADISE
```


# Thirty-third
The user veronica uses a lot the password from lana, so she created an alias.

![{76EC67C2-7E8D-43A9-9F51-1A649D8724EE}](https://github.com/user-attachments/assets/c4b7a6f7-4af7-4fd8-820b-8a32b95d5cba)

```
alias
```

# Thirty-four
The user noa loves to compress her things.

![{02FE4FF0-C925-498B-91D7-6A1C2ED1836A}](https://github.com/user-attachments/assets/807f04c7-129b-4018-ac07-a85e0b1f1866)
```
tar -xvf zip.gz -C /tmp/zip
cat /var/tmp/noa/pwned/lana/zip
```

# Thirty-fifth
The password of maia is surrounded by trash 

![{7E2E382A-1BB8-4A31-B44D-7CB6F519E277}](https://github.com/user-attachments/assets/1ca4cddc-47f1-48fb-9866-d3cb5c71db2c)
```
strings trash
```
(remove \n)

# Thirty-sixth
The user gloria has forgotten the last 2 characters of her password ... They only remember that they were 2 lowercase letters. 

![{C77EEB5B-B528-4B1E-AF63-5850EDA7E146}](https://github.com/user-attachments/assets/b8c6f932-f1ed-46ef-b116-317c1e28bd9e)
```
from string import ascii_lowercase

for c1 in ascii_lowercase:
    for c2 in ascii_lowercase:
        print(f"<string from forget file>{c1}{c2}");
```
Save into `generator.py` and run `python3 generator.py > gloria_pass`

```
hydra -l gloria -P gloria_pass ssh://venus.hackmyvm.eu:5000
```
(It took a ~10 minutes)

# Thirty-seventh
User alora likes drawings, that's why she saved her password as ... 

![{FA1C1059-7C08-4A93-A86B-75FA89E63F11}](https://github.com/user-attachments/assets/7afd5ac9-65e7-4c95-a6c2-c8ebdc8513d0)

![{ABD6BE38-7AB2-47F4-ACD2-DCBD5CD4E330}](https://github.com/user-attachments/assets/759f85c4-df05-4c81-9058-c7405805e1dc)

![{E4A8875F-6D2B-4141-AE8C-809F140B485C}](https://github.com/user-attachments/assets/b231a8ef-3f1c-4d79-9860-a5c5a6ba1d60)

I asked GPT for help
```
Can you generate me qr code base na this what I will send you and tell me presents this qr code
##########################################################
##########################################################
##########################################################
##########################################################
########              ##########  ##              ########
########  ##########  ##    ##  ####  ##########  ########
########  ##      ##  ##  ##  ######  ##      ##  ########
########  ##      ##  ####  ########  ##      ##  ########
########  ##      ##  ##        ####  ##      ##  ########
########  ##########  ##        ####  ##########  ########
########              ##  ##  ##  ##              ########
########################  ####  ##########################
########    ##  ####    ####  ##  ##      ##    ##########
############    ######  ##    ##      ##          ########
########    ##    ##  ##  ##            ####  ##  ########
##############      ##  ##    ######  ##    ####  ########
############    ##      ##  ########    ##  ##  ##########
########################    ####    ##  ##  ####  ########
########              ##    ####            ##  ##########
########  ##########  ######  ##########  ####  ##########
########  ##      ##  ####  ##      ######        ########
########  ##      ##  ##    ##  ######  ##  ####  ########
########  ##      ##  ####          ##    ##  ##  ########
########  ##########  ##      ####  ##  ##################
########              ##  ##                    ##########
##########################################################
##########################################################
##########################################################
##########################################################
```
![image](https://github.com/user-attachments/assets/164769fa-945e-4ae8-bca4-2206177457a5)
GPT failed

I wrote a python code 
```
with open('qr', 'r') as img:
  lines = img.readlines()
  for l in lines:
    print(l.replace('#', chr(0x2588)), end='')
```
This code generate a readable qr code.

#Thirty-eighth
The user julie has created an iso with her password.

![{261F4379-6B6D-44B2-93ED-F7B401CB5962}](https://github.com/user-attachments/assets/ab7fb056-a47d-414c-97a8-30c5fd59f182)

On local machine
```
scp -P 5000 alora@venus.hackmyvm.eu:/pwned/alora/music.iso ./
mkdir -p /tmp/fastmount
sudo mount -o loop ./music.iso /tmp/fastmount
cd /tmp/fastmount
```
We can open this archive manualy or unzip.

# Thirty-ninth
The user irene believes that the beauty is in the difference.

![{D30E42A7-5D20-4CA9-80B7-B771281D230A}](https://github.com/user-attachments/assets/2a0bc7a4-ac8b-41d5-ac53-adc2c8ac6f4d)
```
diff 1.txt 2.txt
```

# Forty
The user adela has lent her password to irene.

![{5534DCE7-24CA-47D5-B816-51B3505E3AC8}](https://github.com/user-attachments/assets/282268f2-285a-478b-9397-f4bb02774043)
```
openssl rsautl -decrypt -inkey id_rsa.pem -in pass.enc
```

# Forty-first
User sky has saved her password to something that can be listened to.

![{774F1E42-2643-4B5B-8804-A2772E2A223C}](https://github.com/user-attachments/assets/34650de0-4ae0-403a-a0ef-24adf31a0c50)

![{866221CC-2DF4-44A2-98A5-DBCE170A6A07}](https://github.com/user-attachments/assets/dfcf6bd9-d26d-47e2-9fb6-580059ecdc96)
Paste this into cyberchef and press magic want.
(password is lowercase)

# forty-second
User sarah uses header in http://localhost/key.php

![{5B096CBE-C117-409C-A015-876772F1BA0D}](https://github.com/user-attachments/assets/d08c0d0f-4d98-42c7-8669-c13fd811ba95)

```
curl -H 'key: true' http://localhost/key.php
```

Hidden flag
```
cat .bash_history
```

# forty-third
The password of mercy is hidden in this directory.

![{84973CF1-157C-47F3-A7F9-2B2646BB1BCB}](https://github.com/user-attachments/assets/a4372129-a5c1-423e-ad5f-8f1eb8267af4)
```
cat ...
```

# forty-fourth
User mercy is always wrong with the password of paula. 

![{168B8C4C-9885-4E01-A319-D10DE84FFE28}](https://github.com/user-attachments/assets/19dcba38-35da-4fb2-9003-7f8de10c9179)
```
cat .bash_history
```

# forty-fifth
The user karla trusts me, she is part of my group of friends. 

![{951E2BB2-8C8A-4FAD-8DA5-1B7D682A30AB}](https://github.com/user-attachments/assets/c9fcd620-f1c6-4107-86cc-cc4132d809e0)


```
find / -group hidden 2>/dev/null
cat <file from output>
```

#forty-sixth
User denise has saved her password in the image.

![{640F6BA8-DC77-421E-AF00-57C629763419}](https://github.com/user-attachments/assets/cc553f75-91ec-4ecf-88ef-9d0487222177)

```
exiftool yuju.jpg
```

# forty-seventh
The user zora is screaming doas!

![{250A994A-2B1F-4ABC-9397-EA885BEC869C}](https://github.com/user-attachments/assets/3856eb8f-4ffe-4208-ad4b-fd48eda602ac)
```
doas -u zora bash
```

#forty-eighth
The user belen has left her password in venus.hmv

![{B2716B96-BD3C-4B6D-B0D3-0487C47A5275}](https://github.com/user-attachments/assets/2dd0ae60-9bad-47fe-a424-a7c7131b3a01)
```
 curl -H 'HOST: venus.hmv' http://localhost
```

# forty-ninth

It seems that belen has stolen the password of the user leona...

![{654419F5-293C-4329-B228-BC980B5FD353}](https://github.com/user-attachments/assets/28f090ee-605e-4ed9-8a86-e70fddc8d4ca)

File stolen.txt contatin hash. We need copy hash into local machine and run john
```
john leona_hash -w=~/SHARED/lists/rockyou.txt
```

#fifth
User ava plays a lot with the DNS of venus.hmv lately... 

![{3C34A282-F677-4D65-A45C-1C02E8B7803D}](https://github.com/user-attachments/assets/be56693c-8bd8-4de5-8d28-51f4df954477)

```
cat /etc/bind/*
```
password is in output

# fifth-first
The password of maria is somewhere...

![{BC54CE21-5187-4E88-AB25-C4C07F0D5762}](https://github.com/user-attachments/assets/9ef9e720-a91e-4dba-a91d-6fa6c6de5fb7)

![{745566D3-DD87-496D-8C3E-1772728A1399}](https://github.com/user-attachments/assets/09501dbf-8814-4b95-939c-b5925f42af89)

Unfortunately, at this point I will not say what to do. You have to try on your own

