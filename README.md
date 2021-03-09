**Stage 0: **

In this stage we are going to get you started on posting messages using the Webex REST API.

Webex has the concept of spaces/rooms and you have been added to a space for this CTF with all other participants of your cohort. Your task in this stage is to:

Identify the space with all participants of your team using the name of the space and the API
Extract the id of that space
Add that id to the env.py file for the PRODUCTION_ROOM key of the config dictionary.

**Stage 1 (in stage 0): **

ACME Inc has a large footprint in Cisco Collaboration. Coming from a legacy CUCM system they are exploring the brave new world of cloud collaboration.

Their head of Collaboration, Lina, comes from a development background and had previously worked a lot with slack and slacks ability to be extended via chat commands and bots. She is especially interested in the ability to monitor and automate workflows right from within her chat client.

The account team has approached you to help them with selling the programmability side of collaboration through a few demos. While the customer has already added you to their war room the account team would prefer you to test your developments in a local test space.

You see this as a great opportunity to also sell programmability to the account team and develop a script that ...

... Creates a new space and returns you the id (You'll add that id to your env.py file in the TESTING_ROOM key)
... Adds you to that space
... Adds the account manager and account SE (the proctors of your CTF) to the space
... Sends a message to the newly created space welcoming everyone


**Stage 2: **

With your test room setup done you are ready to go develop some automations for Lina.

ACME has been increasing their usage of video conferencing. Lina would like to understand how many meetings are scheduled by herself and how many spaces she is a part of.

Your script should be able to query the Webex REST API for the following information and then send them to a space:

Find the number of meetings you/the person whos access token is running the account has scheduled (Note: You might have to create a meeting. You can go here to do so)
Find the number of messages you have send per space you are in
Find the number of spaces you are in
Share those information as formatted text into a webex space.
Once you are done with testing, you can send the message to the production space for everyone to see.
