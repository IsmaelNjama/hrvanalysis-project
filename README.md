# [HRVSciHub](https://hrvscihub.herokuapp.com)

This project implements the most known heart rate variability analysis techniques (Frequency and Time domains as well as nonlinear parameters ) with Django using the [pyhrv](https://github.com/PGomes92/pyhrv/blob/master/README.md) tool for background heart rate analysis.

# Basic usage

After registering the users are able to:

- Add subjects to their study board

![alt Dashboard-Home](https://github.com/aserkash/hrvanalysis/blob/d249c59602c905baa0235ea248a110304cd25516/screenshots/HomeScreen.png?raw=true)

- Upload HRV marker files(supported by pyhrv) of their subjects and run the analysis

![alt Upload-files-screenshot](https://github.com/aserkash/hrvanalysis/blob/d249c59602c905baa0235ea248a110304cd25516/screenshots/UploadFile.png?raw=true)

In case you need test files you can find some [Here](https://github.com/aserkash/hrvanalysis/tree/main/sampleDataFiles)
![alt Sample-test-files](https://github.com/aserkash/hrvanalysis/blob/d249c59602c905baa0235ea248a110304cd25516/screenshots/SampleFiles.png?raw=true)

For a particular subject, access their measurements data.
![alt Sample-list](https://github.com/aserkash/hrvanalysis/blob/d249c59602c905baa0235ea248a110304cd25516/screenshots/SubjectList.png?raw=true)

Access results:
![alt Frequency-domain-results](https://github.com/aserkash/hrvanalysis/blob/d249c59602c905baa0235ea248a110304cd25516/screenshots/FrequencyResults.png?raw=true)


![alt Linear-domain-results](https://github.com/aserkash/hrvanalysis/blob/d249c59602c905baa0235ea248a110304cd25516/screenshots/LinearResults.png?raw=true)


![alt Nonlinear-results](https://github.com/aserkash/hrvanalysis/blob/d249c59602c905baa0235ea248a110304cd25516/screenshots/NonLinearResults.png?raw=true)

- Compare and export their subject data to pdf reports.

[Restful Api with DRF](https://hrvscihub.herokuapp.com/api)

# Disclaimer

This program is distributed in the hope it will be useful and provided to you "as is", but WITHOUT ANY WARRANTY, without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. This program is NOT intended for medical diagnosis. We expressly disclaim any liability whatsoever for any direct, indirect, consequential, incidental or special damages, including, without limitation, lost revenues, lost profits, losses resulting from business interruption or loss of data, regardless of the form of action or legal theory under which the liability may be asserted, even if advised of the possibility of such damages.
