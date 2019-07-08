# ![Hazel](https://hazel.gq/wp-content/uploads/2019/06/robot96.png) Technical Description - Hazel 


## Abstract
The idea behind Hazel is to become a intelligent centralized health care information service. We want it to be able to answer any health care related question with either an educated answer or direction to the right service the patient should use.  
For the prototype we decided to implement an AI personal assistant which will be integrated with one of the available personal assistants  and a website for hosting rich content pages where the 

## Personal Assistant
The personal assistant is implemented using Dialogflow, see related training files and webhooks in the dialogflow folder.  
<img src="https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Dialogflow_logo.svg/1280px-Dialogflow_logo.svg.png" width="200"/>  
The assistant was manually trained to support limited set of scenarios, links and interaction with user was splitted to HTML based responses which are used in the website integration, and to card and other special Google Assistant responses which are used in the Google Integration responses. Where more logic needed to be implemented in response we used webhooks which are hosted directly on our Dialogflow account. 

### Google Assistant Integration
For the prototype, we choose to integrate it with Google Assistant since it seems to be the most accessible and familiar.  
Using Google's Actions console we have created an Action project from our dialogflow model. After filling all the information and configuration needed for deployment we launch our test version of the Google Assistant so it can be used from any user we have attached to the test version, this way we could test our application on phones, tablets or smart-home device.

### Website Integration
The website integration is done using 'My Chatbot' Wordpress extension, the extension lets us easily implement a view which connects to dialogflow API using a shortcode within the Wordpress pages.

## Website

The website is hosted on EC2 AWS instance with route 53 static IP (52.29.18.178)
The machine is running Ubuntu 18.04  
<img src="https://www.securview.com/wp-content/uploads/2018/02/aws-logo.png" width="200"/>  
After launching the instance, Wordpress + Apache server need to be installed [see manual](https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-lamp-on-ubuntu-18-04).

<img src="https://s.w.org/style/images/about/WordPress-logotype-wmark.png" width="60"/><img src="https://httpd.apache.org/images/httpd_logo_wide_new.png" width="400"/>   

The website is using the following Wordpress plugins

 * Elementor
 * Insert Headers and Footers, and Scripts n Styles for adding custom javascripts
 * My Chatbot to integrate our dialogflow model in the website
 * Participants Database for viewing databases tables on pages
 * Really Simple SSL
 * Super Progressive Web Apps and AMP to support PWA (website as an app)
 * wpDiscuz for improving the commenting system and add rating
 * RumbleTalk Chat which enables users to chat with each other

The domain is served using Freenom and the SSL certificate is given by Let's Encrypt.

Example pages was created for number of doctors which can be redirected from the personal assistant.  

For showing the waiting-times, we created dedicated page which has view of the facilities database, with option to view/hide hospitals, and to find specific facility by location (using shortcode of Participants Database extension and javascript). The waiting times are updated using a cron job on the server that is running a python script periodically which updates the waiting time - this should be the point of interface for getting the waiting times.

## Scripts
Different scripts which were used to automate some of the tasks and to run on the servers are on the scripts folder.





