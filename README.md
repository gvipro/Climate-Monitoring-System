# Climate Monitoring System
Climate monitoring system created on a Raspberry Pi 4. The system uses the SenseHat sensor to measure temperature, humidity and pressure. 

The captured data is logged into a data streaming platform called "Inital Stated" to allow the user to access the desired information in case they are away from the device. The Inital State platform provides data analytics tools to allow the users to check for specific data patterns. If the climate units drop below certain level the user will receive an email notification.

The system has a web application, which provides a live video feed of the location where the system is kept. The web application has authentication mechanism developed with the use of Flask BasicAuth to prevent unauthorised user from accessing the information.

For the CSS, Bootstrap has been used.

The system will be further developed! 

