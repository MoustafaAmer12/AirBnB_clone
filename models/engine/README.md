# Engine Package
## Description
This Package includes file storage engine, that is responsible for handling the data storage and how operations, on saved data, would take place.
## Classes
- ### FileStorage Class
This Class is responsible for storing JSON Objects into files and reloading these saved objects from the file when needed.<br>
It should be noted that objects can't be treated as normal JSON-serializable types, thus it handles the differences in string format to object format for correct data correlation.