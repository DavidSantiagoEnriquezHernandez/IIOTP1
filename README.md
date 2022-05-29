<h1>I.4. Project Develop</h1>
<h2>Universidad Tenológica de Chihuahua BIS</h2>
<h5><i>David Santiago Enriquez Hernandez - TIDBIS51M - IoT Applications - 28/05/2022</i></h5>
<h4>Description</h4>
<p>This is an application developed using Python and its framework, Flask, where we have a client server-connection to see results, while using post and get methods in postman </p>



<h4>iiot_server</h4>
<p>It does the function of the sensor, getting random numbers with the randint function from 1 to 90</p>


<h4>Client</h4>
<p>In the client.py file, we import the random number as a variable call inclination, that at the same time is declared as s.getRandomNumber</p>
<ul>
  <li>Transforms data into json </li>
  <li>Works with json data to apply the method POST and the endpoints called devices </li>
  <li>Checks whether if the numbers received from the fictional sensor are greater or lesser than 15</li>
  <li> Declares a dictionary called data that will recieve the random numbers while(while loop) the server is opened</li>
 <li> Uses time library to take lectures fo the numbers as a while loop every determined period of time </li>

 </ul>

<h4>Server</h4>
<ul>
 
  <li>Establishes GET endpoint for devices.</li>
  <li>Establishes POST endpoint for devices and users.</li>
</ul>

<h4>Results</h4>
<h5>Device POST</h5>
<img src=https://github.com/DavidSantiagoEnriquezHernandez/IIOTP1/blob/master/images/Captura.PNG?raw=true/>

<h5>Device GET</h5>
<img src=https://github.com/DavidSantiagoEnriquezHernandez/IIOTP1/blob/master/images/getdevice.png?raw=true/>

<h5>User POST</h5>
<img src=https://github.com/DavidSantiagoEnriquezHernandez/IIOTP1/blob/master/images/Captura%20post.PNG?raw=true/>

<h5>Client Results</h5>
<img src=https://github.com/DavidSantiagoEnriquezHernandez/IIOTP1/blob/master/images/client1.PNG?raw=true/>

<h5>Server Results</h5>
<img src=https://github.com/DavidSantiagoEnriquezHernandez/IIOTP1/blob/master/images/sensor2.PNG?raw=true/>
