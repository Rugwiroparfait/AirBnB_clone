# AirBnB Clone - The Console
![Airbnb clone](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240309%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240309T095225Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a6670afb98c378821ab4012424df895351e31febacf80393317499db478583ff)
Welcome to the AirBnB clone project! This project aims to build a command-line interface (CLI) that manages AirBnB objects using Python. The CLI allows you to create, retrieve, update, and delete various AirBnB objects, such as users, states, cities, places, amenities, and reviews.

## Command Interpreter

The command interpreter serves as the primary interface for managing AirBnB objects. It allows users to perform the following actions:

- Create new objects
- Retrieve objects from storage
- Perform operations on objects (e.g., count, compute stats)
- Update attributes of objects
- Destroy objects

## How to Start

To start the command interpreter, run the `console.py` script located in the project directory. Ensure that you have Python 3 installed on your system.

```
$ ./console.py
```

## How to Use

Once the command interpreter is launched, you will see the prompt `(hbnb)`. You can enter commands and interact with the AirBnB objects. Here are some available commands:

- `create`: Creates a new instance of a specified object and saves it to the JSON file.
- `show`: Prints the string representation of an instance based on the class name and ID.
- `destroy`: Deletes an instance based on the class name and ID.
- `all`: Prints string representations of all instances based on the class name.
- `update`: Updates an instance based on the class name and ID by adding or updating attributes.

## Examples

```
(hbnb) create BaseModel
```

```
(hbnb) show BaseModel 1234-1234-1234
```

```
(hbnb) destroy BaseModel 1234-1234-1234
```

```
(hbnb) all BaseModel
```

```
(hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"
```

## Authors

This project was developed by N.Rugwiro Dominique Parfait and Bugingo Alice Linzy.

## Repository

- GitHub repository: [AirBnB_clone](https://github.com/Rugwiroparfait/AirBnB_clone)

## Requirements

Ensure that your system meets the following requirements to run the project:

- Python 3.8.5 or later
- pycodestyle version 2.8 or later
- Ubuntu 20.04 LTS

## Unit Tests

All files, classes, and functions must be thoroughly tested using the `unittest` module. Run the following command to execute the unit tests:

```
$ python3 -m unittest discover tests
```

## Version History

- **0.0.1**: Initial release of the command interpreter with basic functionality.
- **1.0**: Updated version with additional classes and enhanced functionality.

Enjoy using the AirBnB clone command interpreter!
---end--
