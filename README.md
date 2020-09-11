# generalassemblyemr
GA team project

# Description

GeneralAsemblyEMR is a dual-purpose application made to enable medical staff with easy access to patient records, scheduling, and record information while simultaneiously offering patients access to proscription information, appointment times, and their doctor's emergency contact information. The bifurcated design of user types - doctor and patient - is joined by clerical staff who can, from an administration panel, assign doctors to patients, appointments between doctors and patients, and proscriptions to patients.

# Installation

### For non-Windows users:

```
git clone https://github.com/rahulgupta15/generalassemblyemr
cd generalassemblyemr

python3 manage.py migrate
python3 manage.py runserver

```

### For Windows users:

```
git clone https://github.com/rahulgupta15/generalassemblyemr
cd generalassemblyemr

```

From this point, each instance of the class name 'Role' located in models.py and admin.py must be changed to 'MyRole.' If such a change is not made, database migrations will not be possible.

```
python3 manage.py migrate
python3 manage.py runserver

```


# Useage

### Login Portal

If you do not already have an active account, specficy which account type you would like to create.

![Imgur Image](https://i.imgur.com/8fyC0ny.png)

![Imgur Image](https://i.imgur.com/H8PTERN.png)

![Imgur Image](https://i.imgur.com/JTMYI9O.png)

![Imgur Image](https://i.imgur.com/FWneyt8.png)

![Imgur Image](https://i.imgur.com/rP9o1hU.png)

# Credits

# License
