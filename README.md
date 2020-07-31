# Insight Coding Challenge

run.sh should execute the python3 script **consumer_complaints.py**

That file contains all the logic to:

- read **/input/complains.csv**
- calculate the stats the problem asks for
- and write the output to **/output/report.csv**

_____________________________________________

I decided to use a dictionary data structure (nested dictionaries to be more precise) to organize the data and minimize the number of scans over the _complains.csv_ data. Also, dictionaries are fast and efficient when the keys are strings, such as in this case.

There are two main _for_ loops:

1) Reads every line of **complains.csv** and stores only the necessary data in a 2D list called _dataset_

2) Iterates through every entry in _dataset_ and categorizes it into a dictionary which is name _output_

I probably could have achieved the same outcome with one _for_ loop but it believe two is better for the sake of clarity, while technically still being _O(n)_.

Finally, I iterate through the keys and sub-keys of a much smaller (compared to _dataset_) _output_, calculate the stats, and write to the **report.csv** file for every unique _[product, year]_ pair. 
