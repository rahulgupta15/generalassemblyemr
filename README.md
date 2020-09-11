# GeneralAssemblyEMR

This is a team project conducted in accordance with the software engineering immersive program at General Assembley.

# Description

GeneralAsemblyEMR is a dual-purpose application made to enable medical staff with easy access to patient records, scheduling, and record information while simultaneiously offering patients access to prescription information, appointment times, and their doctor's emergency contact information. The bifurcated design of user types - doctor and patient - is joined by clerical staff who can, from an administration panel, assign doctors to patients, appointments between doctors and patients, and prescriptions to patients.

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

### Account Registration Portal

Complete a multiple-field form in order to register account. Following a succesful registration, you will immediately be redirect to the appropriate view.

![Imgur Image](https://i.imgur.com/H8PTERN.png)

### Doctor Profile View

Upon a succesful login from a 'doctor' account you will be greeted with the following view.

![Imgur Image](https://i.imgur.com/FWneyt8.png)

### Patient Profile View

Upon a succesful login from a 'patient' account you will be greeted with the following view.

![Imgur Image](https://i.imgur.com/JTMYI9O.png)

### Not Logged-in View

An attempt to access views without a succesful login will result in this view.

![Imgur Image](https://i.imgur.com/rP9o1hU.png)

# Future Enhancements 

Currently the UI and much of the functionality of the website is unimplemented or unrefined.

### Functionality - Doctor

* 'Doctor' users are currently unable to delete memos that they attach to patients profiles.
* Although the schedule functionality exists on in the administration panel, the 'doctor' user is not able to see his schedule.

### Functionality - Patient

* The 'patient' can not access his doctors files.
* 'Patient' can not see previous appointments.
* 'Patient' can not access prescriptions.
*  The API implementation of 'nearest hospital' functionality is inactive.

### Functionality - Admin

* The proscription functionality, as well as the model that mediates that functionality, is currently inaccessible.
* String overides need to be included to facilitate a more logical understanding of the objects created through the panel.

### UI

* Carosel for background images unimplemeneted
* Buttons features unimplemeneted
* Profile view renders information, but the centering is not consistent.
* Overall, the wireframe submission for the project hasn't yet been implemeneted.
* There is no navigation bar to enable easy access to views.

# Required Technologies

The required applications and frameworks are as follows:

| Requirement            | Version                                                                                                              |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `python                | 3.0 or greater                                                                                                       |
| `django`               | 3.1                                                                                                                  |
| `bootstrap`            | 4.2                                                                                                                  |

# Credits

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><img src="https://avatars1.githubusercontent.com/u/56042331?s=400&u=9fc6357e253773f8eb9c8c717d8668d3971164a4&v=4" width="100px;" alt=""/><br /><sub><b>Rahul Gupta</b></sub></a><br /><a href="https://github.com/rahulgupta15" title="Code">💻</a></td>
    <td align="center"><img src="https://avatars1.githubusercontent.com/u/63525891?s=400&v=4" width="100px;" alt=""/><br /><sub><b>Ahmed Jamal</b></sub></a><br /><a href="https://github.com/AhmedJamal93" title="Code">💻</a></td>
    <td align="center"><img src="https://i.imgur.com/AciEwUR.jpg" width="100px;" alt=""/><br /><sub><b>Noah Eror</b></sub></a><br /><a href="https://github.com/BitterHippo" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

