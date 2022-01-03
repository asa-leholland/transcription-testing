# Python Project Template
Short template for python projects 


<!-- ABOUT THE PROJECT -->
## About The Project

<!-- ![{example use gif}][example-use] -->

This repository serves as a short demonstration of steps that could be taken to demonstrate the accuracy of a speech recognition service. 

**Note: The virtualbox-testing project only supports the Windows platform at the moment.**


<!-- ### Built With -->


* [Google Cloud Speech-to-Text](https://pypi.org/project/google-cloud-speech/): a Python library for converting audio to text using neural network models. More details can be found on the (Google API documentation)[https://cloud.google.com/speech-to-text].
* [JiWER](https://pypi.org/project/jiwer/): a Python library for evaluating Word Error Rate ([WER(https://en.wikipedia.org/wiki/Word_error_rate)]) in provided text 
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): a Python library for performing speech recogntion (in particular, the Google Cloud Speech API) 

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

In order to use the {name}, you must first have Python and pip installed on your system. If you need assistance installing these prerequisites, see the folowing steps:
* Python is a programming language. All of this project's code base is written in Python. Download the latest version of [Python](https://www.python.org/downloads/) and install onto your local machine.

* Pip is the package installer for Python. Once Python is installed, open your local machine's command line and use the following command to utilize Python to install Pip:
```sh
python get-pip.py -g
```

Git is a version control system. In this project, Git is used to clone (copy) the most up-to-date project files from GitHub to your local machine. Download the latest version of [git](https://git-scm.com/download/win) and install on your local machine.


### Installation

1. Open the command line on your local machine.

2. Enter the following command to use Git to clone this repository to your local machine.
```sh
git clone https://github.com/asa-leholland/virtualbox-testing.git
```
3. Enter the following command to use Pip to install this repository's dependencies.
```sh
pip install -r requirements.txt
```


<!--  -->
Harvard sentence transcripts obtained from [here](https://www.cs.columbia.edu/~hgs/audio/harvard.html).
Harvard sentence .wav files obtained from [here](https://www.voiptroubleshooter.com/open_speech/american.html).

<!-- USAGE EXAMPLES -->
## Usage

To use the {project name}, open the command line, navigate to the installation folder and run the following commands:


```sh
python3 -m venv .venv 
.\.venv\Scripts\activate
python3 transcriptionTesting.py
```

<!-- ROADMAP -->
<!-- ## Roadmap

See the [open issues](https://github.com/asa-leholland/{repo-name}/issues) for a list of proposed features (and known issues). -->



<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
 -->


<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See [LICENSE](https://github.com/asa-leholland/{repo-name}/LICENSE.txt) for more information. -->



<!-- CONTACT -->
## Contact

Asa LeHolland - asaleholland@gmail.com

Project Link: [https://github.com/asa-leholland/{repo-name}](https://github.com/asa-leholland/virtualbox-testing)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [othneildrew](https://github.com/othneildrew) for creating the [template README file](https://github.com/othneildrew/Best-README-Template) that was used as the starting point for the README for this project. 
* [David Amos](https://realpython.com/team/damos/) for his overview article with the Real Python organzition on [speech recognition and the SpeechRecognition package](https://realpython.com/python-speech-recognition/). 
* [Jie Jenn](https://www.youtube.com/c/JieJenn/about) for his Youtube video introduction to the [Google Cloud Speech-To-Text API](https://www.youtube.com/watch?v=lKra6E_tp5U). 






<!-- MARKDOWN LINKS & IMAGES
[linkedin-url]: https://www.linkedin.com/in/asa-holland-a2a0b5b7/
[example-use]: images/{filename}.gif -->
